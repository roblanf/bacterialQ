# GTDB Q-Matrix Estimation and Phylogenetic Analysis Pipeline

## Abstract

This repository contains a pipeline for estimating lineage-specific substitution models to improve the accuracy of microbial phylogenetic inference. The pipeline independently estimates optimal substitution models for each bacterial and archaeal phylum and for the deeper branches of the phylogenetic tree using an iterative approach. The program also compares the estimated models and resulting tree topologies under different constraint scenarios to assess the impact of model assumptions on phylogenetic inference.  

## Input

'run_phylum_iteration.sh' is a shell script that is used to run an iterative process of the Q matrix for a specific taxon, such as the phylum Bacteria. It launches and passes the necessary parameters to execute the iterative process.  

### Main parameters

- '--train_loc_path': The directory folder of the training site sequences (F\*\* format).  
- '--test_loc_path': The directory folder of the testing site sequences (F\*\*  format).  
- '--tree_file': Reference tree file (Newick format).  
- '--taxa_list': The taxa list file used for training.  
- '--model_dir': The NEXUS format file directory containing the initial alternative model.  
- '--max_iterate': The maximum number of iterations.  
- '--converge_thres': Threshold of person correlation coef between old and new models for stopping iteration.  
### Additional parameters

- '--max_threads': The maximum number of threads to use for IQ-TREE.  
- '--verify_on_loop': Whether or not to validate the model in each iteration.  
- '--keep_tmp': Whether to keep temporary files.  
- '--prefix': Prefix of the output path and model names.  
- '--keep_cmd_output': Whether to keep verbose command output in the log file.  
### Dictionary parameters

- --summary_dir': 'Directory for summary across all models.
- '--RESULT_DIR': Output directory.  
## Program Logic and Algorithm

### 1. Quality check

- Filter loci and species by integrity(1- gap%) of sequences under selected taxa unit, and drop the loci with lower than 30% of integrity and species with lower than 50% of integrity.
- Run Tree Shink to drop tips(speceis) with abnormal branch length. 
### 2. Initial Model Estimation (`initial_model_estimation`)

- Estimate the best-fit substitution model for each training locus using ModelFinder in IQ-TREE with the `-mset` option and the initial models specified in `--model-dir`.  
- Determine the most frequently selected model across training loci and use it as the initial model for estimating the phylum-specific substitution matrix.  
For iterative trainning of Q matrices, there are four constraint mode with different parameter abundances and explanatory power for heterogeneity.
### 3. Iterative Refinement

#### 3.1 Two step iteration

In this mode, a full iteration would be spilted into two steps:

1. Estimate the Q matrix using the training loci, using Q matrix and tree from last iteration as initial model & tree.

2. Update the tree topology using FastTree with the updated Q matrix.

After that Check the convergence (reach `max_iterate`times or person correlation coefficient of Q_new and Q_old > `converge_thres`).

##### 3.1.1 Full Constraint(fullcon)

- Estimate the Q matrix using the training loci, fixed topology from the previous iteration or the reference tree or tree from last iteration using `-te`.
- The new Q matrix was estimated under partition option `-p`, where all partitions (a locus per partition) share the same tree, but flexible on evolution speed (scalable on reletive branch length)
- Re-estimate the tree topology using FastTree with the updated Q matrix.  

##### 3.1.2 Topology Constraint(topocon)

- Estimate the Q matrix using the training loci, fixed topology from the previous iteration or the reference tree or tree from last iteration using `-te`.
 - The new Q matrix was estimated under partition option `-Q`, where all partitions (a locus per partition) share the same tree, but flexible on every branch length (This options will introduce 2(n-1) free parameters which would be unstable under large trees...)
 - Re-estimate the tree topology using FastTree with the updated Q matrix.

#### 3.2 Two step iteration

##### 3.2.1 Topology linked(topolink)

- Estimate both the Q matrix and phylogenetic tree using the training loci.
- The new Q matrix was estimated under partition option `-p`, where all partitions (a locus per partition) share the same tree, but flexible on evolution speed (scalable on reletive branch length)
##### 3.2.2 Non-constrainted(noncon)

- Estimate both the Q matrix and phylogenetic tree using the training loci.
- The new Q matrix was estimated under partition option `-S`, where all partitions (a locus per partition) have their individual tree estimation.

### 4. Model Testing and Comparison

- Compare the estimated Q matrices directly using correlation coefficients and matrix norms (`PCA_Q.R`).  
- Infer phylogenetic trees on the testing set using the trained Q matrices and previous best-fit empirical models, and compare the resulting tree topologies using various tree distance metrics (`Q_convert.py`).  
- Perform partitioned analysis on the testing set using IQ-TREE, allowing each locus to have its own substitution model and evolutionary rate, and assess the relative fit of the different models using model fit metrics.  

### 5. Visualization (Todo)

- Perform PCA on the estimated Q matrices and equilibrium frequencies to visualize differences between constraint scenarios, sampling strategies, and phyla (`PCA_Q.R`).  
- Plot branch lengths, equilibrium frequency deviations, and other metrics against measures of phylogenetic information to assess the impact of constraint settings and sampling strategies on the relationships between metrics and phylogenetic information.  

## Output

The program generates the following output files:  

- `iqtree_result.csv`: Summary statistics for each iteration, including parameter settings, likelihood scores, tree statistics and time usage.  
- `log.txt`: Detailed log of the program execution.   
- `prefix_reference.tree`: Extracted subtree from GTDB-TK reference tree based on the taxa list.  
- `pruned_integrity_table.csv`: Summary of the integrity(1 - gap%) across all loci and species for current taxa unit.
- `select_id.txt`: Under single tree method, the list of taxa ramdomly selected.
- `select_loci.txt`: Filtered list of loci, with average integrity across current taxa unit higher than 30%.
- `species_statistic.png`: A histogram of the distribution of inregrity and empty(100% gap) frequency across all speceis for current taxa unit.
- `loci_statistic.png`: A scatter plot shows number of sites and propotion of informative sites for every loci selected.

### estimate/

#### initial/

- `models.txt`: List count of best-performed models across all single training locus compared among initial models.  
- log files for IQ-TREE  

#### loop_n/

- `Q_diff_bubble.png`: Bubble plot of the difference between the current and previous subsititution model.  
- `Q_bubble.png`: Bubble plot of the new estimated subsititution model.  
- `tree_comparison.html`: Summary of the difference of tree topology for iteration n. (For two step iteration only) 
- log files for IQ-TREE and FastTree

### final_verification/

- `models.txt`: List count of best-performed models across all single training locus compared among best initial model and trained models.  
- log files for IQ-TREE  

### trained_models

- IQ-TREE format model file for every iertation.
- `trained_models.nex`: NEXUS file containing the trained substitution models.  
- `PCA_F.png`: PCA plot of the stationary frequencies among trained and initial models.  
- `PCA_Q.png`: PCA plot of the Q matrices among trained and initial models. 

### ../summary/
- `all_iteration_summary.csv`: Summary statistics for all iterations across all runs, with additional information on the prefix and iteration number.  
- `best_trained_models.nex`: NEXUS file containing the best-trained substitution models across all runs.  

## TODO List

- [x] Develop quality check for alignments  
  - [x] Using treeshink to delete abnormal long branches  
  - [x] Delete loci and species with high gap ratio  
- [ ] Complete subtree method to utilize more data  
  - [x] Implement a better subtree pruning method to replace `get_subtree()`  
  - [ ] Make a new launcher for subtree method  
  - [ ] Develop visualization tool for multi-tree outputs   
- [x] Implement other topology constraint scenario in the iterative refinement step  
- [x] Improve model and tree comparison between iterations  
  - [x] Add tree comparison inner each loop  
  - [x] Add model comparison inner each loop  
  - [x] Visualize model parameter changes between iterations using bubble plots  
- [ ] Enhance code readability and documentation  
  - [ ] Add inline comments explaining key steps  
  - [ ] Update the README with more detailed environment and usage instructions  
