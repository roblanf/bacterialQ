import os
import subprocess
import json
from concurrent.futures import ThreadPoolExecutor
import time

# Define the lists of parameters
# taxa_name_list = ["p__Chloroflexota", "p__Cyanobacteriota", "p__Acidobacteriota", "p__Spirochaetota", "p__Gemmatimonadota"]
# prune_mode_list = ["upper", "split"]
# maximum_subtree_size_list = [200, 100, 50]
# num_aln_list = [1, 0.2, 0.05]
# fix_subtree_topology_list = [True, False]

taxa_name_list = ["p__Chloroflexota", "p__Cyanobacteriota"]
prune_mode_list = ["split"]
maximum_subtree_size_list = [50, 100, 150, 200]
num_aln_list = [500, 1000, 2000]
fix_subtree_topology_list = [True, False]

n_threads = 5

# Define the file paths
tree_file = "/home/tim/project/GTDB_TREE/data/r220/bac120_r220.tree"
train_loc_path = "/home/tim/project/GTDB_TREE/alignment/r220/train"
test_loc_path = "/home/tim/project/GTDB_TREE/alignment/r220/test"
model_dir = "/home/tim/project/GTDB_TREE/data/modelset_ALL.nex"
RESULT_DIR = "../Result_rona/method_test"
combined_table = "/home/tim/project/GTDB_TREE/data/r220/combined_df.csv"
FastTreeMP_path = "/home/tim/project/tool/FastTreeMP/FastTreeMP"
decorated_tree_file="/home/tim/project/GTDB_TREE/data/r220/bac120_r220_decorated.tree"
outgroup_phylum_list="/home/tim/project/GTDB_TREE/data/GTDB_stable_phyla_list.txt"
time_limit = 86400 #24hrs

log_file_path = f"{RESULT_DIR}/error_log.txt"
status_file_path = f"{RESULT_DIR}/script_status.json"

def generate_shell_script(taxa_name, prune_mode, maximum_subtree_size, num_aln, fix_subtree_topology):
    fix_subtree_topo_str = "fix_subtree_topo" if fix_subtree_topology else "free_subtree_topo"
    output_dir = f"{RESULT_DIR}/{taxa_name}/{prune_mode}/{fix_subtree_topo_str}"
    os.makedirs(output_dir, exist_ok=True)
    
    fix_subtree_topology_param = "--fix_subtree_topology" if fix_subtree_topology else ""
    
    # Construct the command string using a list of parameters
    params = [
        "python subtree_model_iteration.py",
        "--taxa_scale phylum",
        f"--taxa_name {taxa_name}",
        f"--num_aln {num_aln}",
        f"--train_loc_path {train_loc_path}",
        f"--test_loc_path {test_loc_path}",
        f"--taxa_file {combined_table}",
        f"--ref_tree {tree_file}",
        f"--model_dir {model_dir}",
        f"--output_dir {output_dir}",
        f"--FastTreeMP_path {FastTreeMP_path}",
        "--max_threads 30",
        "--tree_size_lower_lim 10",
        f"--tree_size_upper_lim {maximum_subtree_size}",
        f"--prune_mode {prune_mode}",
        "--use_outgroup",
        f"--decorated_tree {decorated_tree_file}",
        f"--outgroup_taxa_list {outgroup_phylum_list}",
        f"--time_limit {time_limit}",
        "--verbose",
        "--test_partition_test_loci",
        "--estimate_best_final_tree",
        "--final_tree_tool IQFAST",
        "--pipeline_test_settings",
        "--model_update_summary",
        "--tree_comparison_report",
        fix_subtree_topology_param
    ]

    script_content = " \\\n".join(params)
    script_dir = os.path.join(output_dir, f"{taxa_name}_{maximum_subtree_size}_{num_aln:.2f}")
    os.makedirs(script_dir, exist_ok=True)
    script_path = os.path.join(script_dir, f"run_script.sh")
    with open(script_path, "w") as script_file:
        script_file.write(script_content)
    return script_path

def run_shell_script(script_path):
    try:
        # Run the shell script and capture the output
        result = subprocess.run(["bash", script_path], check=True, capture_output=True, text=True)
        return "success", result.stdout
    except subprocess.CalledProcessError as e:
        return "error", e.output

def load_status():
    if os.path.exists(status_file_path):
        with open(status_file_path, "r") as f:
            return json.load(f)
    return {}

def save_status(status):
    with open(status_file_path, "w") as f:
        json.dump(status, f, indent=4)

def log_status(script_path, status, output, start_time):
    with open(log_file_path, "a") as log_file:
        runtime = time.time() - start_time
        log_file.write(f"Script: {script_path}\nStatus: {status}\nRuntime: {runtime:.2f} seconds\nOutput: {output}\n\n")

# Load the current status
status = load_status()

# Generate the list of shell scripts to run
shell_scripts = []
for num_aln in num_aln_list:
    for maximum_subtree_size in maximum_subtree_size_list:
        for fix_subtree_topology in fix_subtree_topology_list:
             for prune_mode in prune_mode_list:
                for taxa_name in taxa_name_list:

                    script_path = generate_shell_script(taxa_name, prune_mode, maximum_subtree_size, num_aln, fix_subtree_topology)
                    if script_path not in status:
                        status[script_path] = "not_run"
                    if status[script_path] == "not_run" or status[script_path] == "error":
                        shell_scripts.append(script_path)

# Save the initial status
save_status(status)

def run_and_update_status(script_path):
    start_time = time.time()
    status[script_path] = "running"
    save_status(status)
    result, output = run_shell_script(script_path)
    status[script_path] = result
    save_status(status)
    log_status(script_path, result, output, start_time)
    return script_path, start_time, output

def display_status(futures):
    while not all(f.done() for f in futures):
        os.system('clear')
        for i, future in enumerate(futures):
            if future.done():
                script_path, start_time, output = future.result()
                runtime = time.time() - start_time
                print(f"{script_path} {status[script_path]}")
                print(f"thread {i+1}: {runtime // 60:02}:{runtime % 60:02}")
            else:
                print(f"thread {i+1}: running")
        time.sleep(10)
    # Print the final status of all threads
    os.system('clear')
    for i, future in enumerate(futures):
        script_path, start_time, output = future.result()
        runtime = time.time() - start_time
        print(f"{script_path} {status[script_path]}")
        print(f"thread {i+1}: {runtime // 60:02}:{runtime % 60:02}")
        
# Run the shell scripts using a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=n_threads) as executor:
    futures = [executor.submit(run_and_update_status, script) for script in shell_scripts]
    display_status(futures)
