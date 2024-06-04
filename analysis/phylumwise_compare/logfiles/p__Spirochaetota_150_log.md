## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Spirochaetota_150  
  Taxa name: p__Spirochaetota  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 150  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Spirochaetota_150/select_id.txt. Sampling sequences for 99 loci.  
Number of input species: 1308  
Remaining 99 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Spirochaetota_150/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1308  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Spirochaetota_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 1308   
Number of pruned subtrees: 32   
Number of taxa after pruning: 1296   
Pruned node IDs (degree): 8 (36) 1028 (9) 44 (6) 50 (28) 1039 (8) 78 (9) 1046 (65) 336 (57) 393 (60) 305 (32) 1114 (143) 1256 (53) 91 (9) 455 (46) 806 (10) 290 (16) 816 (25) 101 (12) 503 (16) 841 (19) 113 (14) 519 (21) 860 (6) 127 (5) 797 (9) 866 (149) 1014 (15) 284 (7) 541 (116) 656 (142) 133 (142) 274 (11)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 32 subtree files and 99 loci files. Total number of potential alignments: 3168.  
Sub-sampling 1000 alignments from 3168 alignments.  
Remaining 1000 alignments. Deleted 62 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Spirochaetota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtree_update/p__Spirochaetota_150
```
  
  Runtime: 46098.48 seconds
[Subtree update log](loop_1/subtree_update/p__Spirochaetota_150.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 324 | LG |
| 251 | Q.INSECT |
| 249 | Q.YEAST |
| 174 | Q.PFAM |
| 2 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtree_update/p__Spirochaetota_150.best_scheme.nex -te ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtree_update/p__Spirochaetota_150.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Spirochaetota_150/loop_1/model_update/p__Spirochaetota_150
```
  
  Runtime: 50872.21 seconds
[Model update log](loop_1/model_update/p__Spirochaetota_150.iqtree)  
BIC of the new model: 16243497.291  
Likelihood of the new model: -7644739.1606  
Model does not meet precision requirement.  
[New model](trained_models/p__Spirochaetota_150_1)  
Model set for next iteration: LG,Q.INSECT,Q.YEAST,Q.PFAM,p__Spirochaetota_150_1  
![Model bubble plot](loop_1/p__Spirochaetota_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Spirochaetota_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Spirochaetota_150/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Spirochaetota_150/ref_tree.tre ../Result/safe_phyla/p__Spirochaetota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Spirochaetota_150/loop_1/tree_update/p__Spirochaetota_150_1.treefile
```
  
  Runtime: 6082.46 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Spirochaetota_150/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Spirochaetota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Spirochaetota_150/loop_1/tree_update/p__Spirochaetota_150_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Spirochaetota_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 442  
Normalized RF distance: 0.1693  
Tree 1 branch length: 177.19801  
Tree 2 branch length: 242.187717111  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9935090617884137  
Euclidean distance: 0.6115831114855889  
Time usage for Loop_1: 103119.24 seconds (28.64 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Spirochaetota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.INSECT,Q.YEAST,Q.PFAM,p__Spirochaetota_150_1 -mdef ../Result/safe_phyla/p__Spirochaetota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Spirochaetota_150/loop_1/tree_update/p__Spirochaetota_150_1.treefile -pre ../Result/safe_phyla/p__Spirochaetota_150/loop_1/test_model/p__Spirochaetota_150_test_concat
```
  
  Runtime: 6050.02 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Spirochaetota_150_1+I+G4 | -4027009.205 | 8077126.668 |
| p__Spirochaetota_150_1+F+I+G4 | -4031327.852 | 8085931.861 |
| Q.YEAST+I+G4 | -4036212.861 | 8095533.980 |
| LG+F+I+G4 | -4037056.654 | 8097389.465 |
| Q.INSECT+I+G4 | -4038425.656 | 8099959.570 |
| Q.PFAM+F+I+G4 | -4039556.425 | 8102389.007 |
| LG+I+G4 | -4040235.398 | 8103579.054 |
| Q.PFAM+I+G4 | -4040769.454 | 8104647.166 |
| Q.YEAST+F+I+G4 | -4040689.246 | 8104654.649 |
| LG+G4 | -4044837.447 | 8112774.315 |
| Q.INSECT+F+I+G4 | -4046889.562 | 8117055.281 |
| LG+I | -4414300.129 | 8851699.679 |
| LG | -4457396.095 | 8937882.774 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Spirochaetota_150/loop_1/tree_update/p__Spirochaetota_150_1.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Spirochaetota_150/loop_2/subtrees -m random
```
  
Original number of taxa: 1308   
Number of pruned subtrees: 32   
Number of taxa after pruning: 1279   
Pruned node IDs (degree): 203 (36) 1223 (9) 239 (6) 245 (32) 1215 (9) 1236 (8) 1243 (62) 916 (57) 973 (32) 2 (143) 144 (53) 1205 (11) 1194 (12) 282 (60) 1007 (10) 1185 (10) 343 (46) 694 (10) 1022 (5) 1179 (7) 391 (16) 707 (43) 1028 (142) 1169 (11) 407 (5) 750 (130) 879 (35) 689 (5) 683 (7) 675 (9) 419 (116) 534 (142)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Spirochaetota_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 32 subtree files and 99 loci files. Total number of potential alignments: 3168.  
Sub-sampling 1000 alignments from 3168 alignments.  
Remaining 1000 alignments. Deleted 61 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Spirochaetota_150/loop_2/training_loci -m MFP -mset LG,Q.INSECT,Q.YEAST,Q.PFAM,p__Spirochaetota_150_1 -mdef ../Result/safe_phyla/p__Spirochaetota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Spirochaetota_150/loop_2/subtree_update/p__Spirochaetota_150
```
  
  Runtime: 35055.70 seconds
[Subtree update log](loop_2/subtree_update/p__Spirochaetota_150.iqtree)  
Best models for iteration 2:  
p__Spirochaetota_150_1  

| Model | Count |
|-------|-------|
| 730 | p__Spirochaetota_150_1 |
| 81 | Q.YEAST |
| 77 | LG |
| 60 | Q.PFAM |
| 52 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Spirochaetota_150/loop_2/subtree_update/p__Spirochaetota_150.best_scheme.nex -te ../Result/safe_phyla/p__Spirochaetota_150/loop_2/subtree_update/p__Spirochaetota_150.treefile --model-joint GTR20+FO --init-model p__Spirochaetota_150_1 -mdef ../Result/safe_phyla/p__Spirochaetota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Spirochaetota_150/loop_2/model_update/p__Spirochaetota_150
```
  
## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Spirochaetota_150  
  Taxa name: p__Spirochaetota  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 150  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Spirochaetota_150/select_id.txt. Sampling sequences for 99 loci.  
Number of input species: 1308  
Remaining 99 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Spirochaetota_150/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1308  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Spirochaetota_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 1308   
Number of pruned subtrees: 32   
Number of taxa after pruning: 1296   
Pruned node IDs (degree): 8 (36) 1028 (9) 44 (6) 50 (28) 1039 (8) 78 (9) 1046 (65) 336 (57) 393 (60) 305 (32) 1114 (143) 1256 (53) 91 (9) 455 (46) 806 (10) 290 (16) 816 (25) 101 (12) 503 (16) 841 (19) 113 (14) 519 (21) 860 (6) 127 (5) 797 (9) 866 (149) 1014 (15) 284 (7) 541 (116) 656 (142) 133 (142) 274 (11)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 32 subtree files and 99 loci files. Total number of potential alignments: 3168.  
Sub-sampling 1000 alignments from 3168 alignments.  
Remaining 1000 alignments. Deleted 63 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Spirochaetota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtree_update/p__Spirochaetota_150
```
  
  Error:
Checkpoint (../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtree_update/p__Spirochaetota_150.ckp.gz) indicates that a previous run successfully finished
Use `-redo` option if you really want to redo the analysis and overwrite all output files.
Use `--redo-tree` option if you want to restore ModelFinder and only redo tree search.
Use `--undo` option if you want to continue previous run when changing/adding options.
  Exit code: 2
  Runtime: 0.58 seconds
Checkpoint (../Result/safe_phyla/p__Spirochaetota_150/loop_1/subtree_update/p__Spirochaetota_150.ckp.gz) indicates that a previous run successfully finished
Use `-redo` option if you really want to redo the analysis and overwrite all output files.
Use `--redo-tree` option if you want to restore ModelFinder and only redo tree search.
Use `--undo` option if you want to continue previous run when changing/adding options.
  
  Runtime: 50084.95 seconds
[Model update log](loop_2/model_update/p__Spirochaetota_150.iqtree)  
BIC of the new model: 15435795.7646  
Likelihood of the new model: -7260042.5998  
Model does not meet precision requirement.  
[New model](trained_models/p__Spirochaetota_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Spirochaetota_150_2  
![Model bubble plot](loop_2/p__Spirochaetota_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Spirochaetota_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Spirochaetota_150/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Spirochaetota_150/ref_tree.tre ../Result/safe_phyla/p__Spirochaetota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Spirochaetota_150/loop_2/tree_update/p__Spirochaetota_150_2.treefile
```
  
  Runtime: 6084.50 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Spirochaetota_150/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Spirochaetota_150/loop_1/tree_update/p__Spirochaetota_150_1.treefile', tree2_path = '../Result/safe_phyla/p__Spirochaetota_150/loop_2/tree_update/p__Spirochaetota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Spirochaetota_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0023  
Tree 1 branch length: 242.187717111  
Tree 2 branch length: 243.255074852  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997157285888755  
Euclidean distance: 0.12718895969109906  
Time usage for Loop_2: 91318.22 seconds (25.37 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Spirochaetota_150/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Spirochaetota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Spirochaetota_150/loop_2/tree_update/p__Spirochaetota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Spirochaetota_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 440  
Normalized RF distance: 0.1686  
Tree 1 branch length: 177.19801  
Tree 2 branch length: 243.255074852  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Spirochaetota_150_2):  
Pearson's correlation: 0.9929815253633487  
Euclidean distance: 0.6264167371737628  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Spirochaetota_150/loop_2/tree_update/p__Spirochaetota_150_2.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Spirochaetota_150/final_test/subtrees -m random
```
  
Original number of taxa: 1308   
Number of pruned subtrees: 32   
Number of taxa after pruning: 1279   
Pruned node IDs (degree): 203 (36) 1223 (9) 239 (6) 245 (32) 1215 (9) 1236 (8) 1243 (62) 916 (57) 973 (32) 2 (143) 144 (53) 1205 (11) 1194 (12) 282 (60) 1007 (10) 1185 (10) 343 (46) 694 (10) 1022 (5) 1179 (7) 391 (16) 707 (43) 1028 (142) 1169 (11) 407 (5) 750 (130) 879 (35) 689 (5) 683 (7) 675 (9) 419 (116) 534 (142)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Spirochaetota_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 32 subtree files and 20 loci files. Total number of potential alignments: 640.  
Obtained 602 alignments from all potential alignments.  
Remaining 602 alignments. Deleted 38 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Spirochaetota_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Spirochaetota_150_2 -mdef ../Result/safe_phyla/p__Spirochaetota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Spirochaetota_150/final_test/p__Spirochaetota_150_test_partition
```
  
  Runtime: 1074.41 seconds
Best models for test data:  
p__Spirochaetota_150_2  

| Model | Count |
|-------|-------|
| 438 | p__Spirochaetota_150_2 |
| 49 | Q.YEAST |
| 43 | LG |
| 38 | Q.PFAM |
| 13 | Q.INSECT |
| 13 | MTART |
| 8 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Spirochaetota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Spirochaetota_150_2 -mdef ../Result/safe_phyla/p__Spirochaetota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Spirochaetota_150/loop_2/tree_update/p__Spirochaetota_150_2.treefile -pre ../Result/safe_phyla/p__Spirochaetota_150/final_test/p__Spirochaetota_150_test_concat
```
  
  Runtime: 4027.49 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Spirochaetota_150_2+I+G4 | -4027213.782 | 8077535.822 |
| p__Spirochaetota_150_2+F+I+G4 | -4032346.974 | 8087970.105 |
| Q.YEAST+I+G4 | -4036467.404 | 8096043.066 |
| LG+F+I+G4 | -4037309.711 | 8097895.579 |
| Q.INSECT+I+G4 | -4038678.928 | 8100466.114 |
| Q.PFAM+F+I+G4 | -4039810.479 | 8102897.115 |
| LG+I+G4 | -4040488.755 | 8104085.768 |
| Q.PFAM+I+G4 | -4041022.555 | 8105153.368 |
| Q.YEAST+F+I+G4 | -4040944.438 | 8105165.033 |
| LG+G4 | -4045093.098 | 8113285.617 |
| Q.INSECT+F+I+G4 | -4047142.927 | 8117562.011 |
| MTMET+F+I+G4 | -4147630.912 | 8318537.981 |
| MTART+F+I+G4 | -4204204.923 | 8431686.003 |
| MTMET+I+G4 | -4279347.117 | 8581802.492 |
| MTART+I+G4 | -4337962.399 | 8699033.056 |
| LG+I | -4414537.108 | 8852173.637 |
| LG | -4457635.589 | 8938361.762 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Spirochaetota_150/trained_models/trained_model.nex ../Result/safe_phyla/p__Spirochaetota_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 205796.18 seconds (57.17 h)  
