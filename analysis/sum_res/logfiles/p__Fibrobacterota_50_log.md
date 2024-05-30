## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Fibrobacterota_50  
  Taxa name: p__Fibrobacterota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 50  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Fibrobacterota_50/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 194  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Fibrobacterota_50/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 194  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Fibrobacterota_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/subtrees -m random
```
  
Original number of taxa: 194   
Number of pruned subtrees: 8   
Number of taxa after pruning: 177   
Pruned node IDs (degree): 148 (47) 142 (5) 131 (12) 8 (14) 118 (12) 29 (28) 57 (31) 87 (28)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 8 subtree files and 98 loci files. Total number of potential alignments: 784.  
Obtained 771 alignments from all potential alignments.  
Remaining 771 alignments. Deleted 13 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/subtree_update/p__Fibrobacterota_50
```
  
  Runtime: 2612.40 seconds
[Subtree update log](loop_1/subtree_update/p__Fibrobacterota_50.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 366 | LG |
| 189 | Q.PFAM |
| 172 | Q.INSECT |
| 42 | Q.YEAST |
| 1 | MTMET |
| 1 | MTART |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/subtree_update/p__Fibrobacterota_50.best_scheme.nex -te ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/subtree_update/p__Fibrobacterota_50.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/model_update/p__Fibrobacterota_50
```
  
  Runtime: 10327.38 seconds
[Model update log](loop_1/model_update/p__Fibrobacterota_50.iqtree)  
BIC of the new model: 5707281.9722  
Likelihood of the new model: -2678378.296  
Model does not meet precision requirement.  
[New model](trained_models/p__Fibrobacterota_50_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Fibrobacterota_50_1  
![Model bubble plot](loop_1/p__Fibrobacterota_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Fibrobacterota_50/ref_tree.tre ../Result/safe_phyla/p__Fibrobacterota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/tree_update/p__Fibrobacterota_50_1.treefile
```
  
  Runtime: 1134.46 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Fibrobacterota_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Fibrobacterota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Fibrobacterota_50/loop_1/tree_update/p__Fibrobacterota_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Fibrobacterota_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 96  
Normalized RF distance: 0.2513  
Tree 1 branch length: 21.53689  
Tree 2 branch length: 29.061660588  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.988725554114228  
Euclidean distance: 0.7804753164032496  
Time usage for Loop_1: 14112.92 seconds (3.92 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Fibrobacterota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Fibrobacterota_50_1 -mdef ../Result/safe_phyla/p__Fibrobacterota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/tree_update/p__Fibrobacterota_50_1.treefile -pre ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/test_model/p__Fibrobacterota_50_test_concat
```
  
  Runtime: 422.26 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Fibrobacterota_50_1+I+G4 | -477708.986 | 958810.929 |
| p__Fibrobacterota_50_1+F+I+G4 | -477964.483 | 959488.501 |
| Q.INSECT+I+G4 | -478612.400 | 960617.757 |
| Q.YEAST+I+G4 | -478796.739 | 960986.435 |
| LG+I+G4 | -478923.873 | 961240.703 |
| LG+F+I+G4 | -478876.296 | 961312.128 |
| Q.PFAM+I+G4 | -478962.427 | 961317.811 |
| Q.PFAM+F+I+G4 | -479151.235 | 961862.006 |
| Q.YEAST+F+I+G4 | -479296.193 | 962151.922 |
| LG+G4 | -479710.937 | 962806.064 |
| Q.INSECT+F+I+G4 | -479714.995 | 962989.526 |
| LG+I | -507816.715 | 1019017.619 |
| LG | -519663.955 | 1042703.332 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Fibrobacterota_50/loop_1/tree_update/p__Fibrobacterota_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/subtrees -m random
```
  
Original number of taxa: 194   
Number of pruned subtrees: 7   
Number of taxa after pruning: 176   
Pruned node IDs (degree): 193 (47) 187 (5) 176 (12) 53 (14) 68 (11) 85 (49) 133 (38)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 7 subtree files and 98 loci files. Total number of potential alignments: 686.  
Obtained 674 alignments from all potential alignments.  
Remaining 674 alignments. Deleted 12 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Fibrobacterota_50_1 -mdef ../Result/safe_phyla/p__Fibrobacterota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/subtree_update/p__Fibrobacterota_50
```
  
  Runtime: 2944.64 seconds
[Subtree update log](loop_2/subtree_update/p__Fibrobacterota_50.iqtree)  
Best models for iteration 2:  
p__Fibrobacterota_50_1  

| Model | Count |
|-------|-------|
| 587 | p__Fibrobacterota_50_1 |
| 50 | Q.PFAM |
| 19 | LG |
| 14 | Q.INSECT |
| 4 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/subtree_update/p__Fibrobacterota_50.best_scheme.nex -te ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/subtree_update/p__Fibrobacterota_50.treefile --model-joint GTR20+FO --init-model p__Fibrobacterota_50_1 -mdef ../Result/safe_phyla/p__Fibrobacterota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/model_update/p__Fibrobacterota_50
```
  
  Runtime: 7187.51 seconds
[Model update log](loop_2/model_update/p__Fibrobacterota_50.iqtree)  
BIC of the new model: 5473175.3471  
Likelihood of the new model: -2562866.7666  
Model does not meet precision requirement.  
[New model](trained_models/p__Fibrobacterota_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Fibrobacterota_50_2  
![Model bubble plot](loop_2/p__Fibrobacterota_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Fibrobacterota_50/ref_tree.tre ../Result/safe_phyla/p__Fibrobacterota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/tree_update/p__Fibrobacterota_50_2.treefile
```
  
  Runtime: 1145.56 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Fibrobacterota_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Fibrobacterota_50/loop_1/tree_update/p__Fibrobacterota_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Fibrobacterota_50/loop_2/tree_update/p__Fibrobacterota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Fibrobacterota_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 29.061660588  
Tree 2 branch length: 29.122149159  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999856060684822  
Euclidean distance: 0.028914564877234  
Time usage for Loop_2: 11341.99 seconds (3.15 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Fibrobacterota_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Fibrobacterota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Fibrobacterota_50/loop_2/tree_update/p__Fibrobacterota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Fibrobacterota_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 96  
Normalized RF distance: 0.2513  
Tree 1 branch length: 21.53689  
Tree 2 branch length: 29.122149159  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Fibrobacterota_50_2):  
Pearson's correlation: 0.9885657371542506  
Euclidean distance: 0.7876391768440777  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/tree_update/p__Fibrobacterota_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Fibrobacterota_50/final_test/subtrees -m random
```
  
Original number of taxa: 194   
Number of pruned subtrees: 7   
Number of taxa after pruning: 176   
Pruned node IDs (degree): 193 (47) 187 (5) 176 (12) 53 (14) 68 (11) 85 (49) 133 (38)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Fibrobacterota_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 7 subtree files and 19 loci files. Total number of potential alignments: 133.  
Obtained 121 alignments from all potential alignments.  
Remaining 121 alignments. Deleted 12 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fibrobacterota_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Fibrobacterota_50_2 -mdef ../Result/safe_phyla/p__Fibrobacterota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Fibrobacterota_50/final_test/p__Fibrobacterota_50_test_partition
```
  
  Runtime: 188.69 seconds
Best models for test data:  
p__Fibrobacterota_50_2  

| Model | Count |
|-------|-------|
| 105 | p__Fibrobacterota_50_2 |
| 5 | LG |
| 3 | Q.INSECT |
| 3 | MTART |
| 2 | Q.PFAM |
| 2 | MTMET |
| 1 | Q.YEAST |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Fibrobacterota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Fibrobacterota_50_2 -mdef ../Result/safe_phyla/p__Fibrobacterota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Fibrobacterota_50/loop_2/tree_update/p__Fibrobacterota_50_2.treefile -pre ../Result/safe_phyla/p__Fibrobacterota_50/final_test/p__Fibrobacterota_50_test_concat
```
  
  Runtime: 848.30 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Fibrobacterota_50_2+I+G4 | -477713.604 | 958820.164 |
| p__Fibrobacterota_50_2+F+I+G4 | -477987.470 | 959534.476 |
| Q.INSECT+I+G4 | -478612.400 | 960617.757 |
| Q.YEAST+I+G4 | -478796.739 | 960986.435 |
| LG+I+G4 | -478923.873 | 961240.703 |
| LG+F+I+G4 | -478876.296 | 961312.128 |
| Q.PFAM+I+G4 | -478962.427 | 961317.811 |
| Q.PFAM+F+I+G4 | -479151.235 | 961862.006 |
| Q.YEAST+F+I+G4 | -479296.193 | 962151.922 |
| LG+G4 | -479710.937 | 962806.064 |
| Q.INSECT+F+I+G4 | -479714.995 | 962989.526 |
| MTMET+F+I+G4 | -491234.561 | 986028.657 |
| MTART+F+I+G4 | -497462.192 | 998483.919 |
| MTMET+I+G4 | -507492.412 | 1018377.781 |
| LG+I | -507816.715 | 1019017.620 |
| MTART+I+G4 | -514044.604 | 1031482.164 |
| LG | -519663.955 | 1042703.332 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Fibrobacterota_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Fibrobacterota_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 27025.34 seconds (7.51 h)  
