import os
import time

def scan_and_rename_files(folders):
    for folder in folders:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                if 'final_model_verify.log' in files:
                    for file in files:
                        if file.startswith('test_best_concat_model.'):
                            old_path = os.path.join(root, file)
                            new_file = file.replace('test_', 'testset_', 1)
                            new_path = os.path.join(root, new_file)
                            os.rename(old_path, new_path)
                            print(f'Renamed {old_path} to {new_path}')

def check_folders(folders):
    for folder in folders:
        if os.path.exists(folder):
            print(f'Folder {folder} exists.')
            for root, dirs, files in os.walk(folder):
                test_files = [f for f in files if f.startswith('test_best_concat_model.')]
                if test_files:
                    print(f'Found files in {root}: {test_files}')
                else:
                    print(f'No test_best_concat_model files found in {root}')
        else:
            print(f'Folder {folder} does not exist.')

def main(folders):
    check_folders(folders)  # Initial check before entering the loop
    while True:
        scan_and_rename_files(folders)
        time.sleep(60)

if __name__ == "__main__":
    folders_to_monitor = [
        '../Result_rona/method_test/p__Chloroflexota/fix_subtree_topo/p__Chloroflexota_50_1000/final_test/logfiles',
        '../Result_rona/method_test/p__Cyanobacteriota/fix_subtree_topo/p__Cyanobacteriota_50_1000/final_test/logfiles',
        '../Result_rona/method_test/p__Chloroflexota/free_subtree_topo/p__Chloroflexota_50_1000/final_test/logfiles',
        '../Result_rona/method_test/p__Cyanobacteriota/free_subtree_topo/p__Cyanobacteriota_50_1000/final_test/logfiles',
        '../Result_rona/method_test/p__Chloroflexota/fix_subtree_topo/p__Chloroflexota_100_1000/final_test/logfiles'
    ]
    main(folders_to_monitor)
