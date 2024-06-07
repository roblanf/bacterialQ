## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_200  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 200  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_200/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_200/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_200/ref_tree.tre -l 5 -u 200 -o ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 23   
Number of taxa after pruning: 1884   
Pruned node IDs (degree): 1415 (35) 4 (10) 16 (174) 189 (30) 1376 (39) 1891 (164) 1450 (116) 1565 (164) 222 (23) 1368 (9) 1165 (182) 1346 (23) 246 (47) 293 (98) 392 (7) 1147 (15) 685 (168) 401 (21) 1127 (21) 422 (78) 499 (185) 854 (155) 1008 (120)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 23 subtree files and 100 loci files. Total number of potential alignments: 2300.  
Sub-sampling 1000 alignments from 2300 alignments.  
Remaining 1000 alignments. Deleted 11 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/subtree_update/p__Acidobacteriota_200
```
  
  Runtime: 85149.26 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_200.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| 346 | Q.PFAM |
| 303 | Q.INSECT |
| 271 | LG |
| 80 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/subtree_update/p__Acidobacteriota_200.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/subtree_update/p__Acidobacteriota_200.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/model_update/p__Acidobacteriota_200
```
  
  Runtime: 155005.82 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_200.iqtree)  
BIC of the new model: 28563145.049  
Likelihood of the new model: -13357505.7021  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_200_1)  
Model set for next iteration: Q.PFAM,Q.INSECT,LG,Q.YEAST,p__Acidobacteriota_200_1  
![Model bubble plot](loop_1/p__Acidobacteriota_200_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_200/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_200/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/tree_update/p__Acidobacteriota_200_1.treefile
```
  
  Runtime: 6644.71 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_200/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_200/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/tree_update/p__Acidobacteriota_200_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_200/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 640  
Normalized RF distance: 0.1695  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 304.546563245  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.988426177671865  
Euclidean distance: 0.8897733951402841  
Time usage for Loop_1: 246859.89 seconds (68.57 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_200/loci/concat_testing_loci.faa -m TESTONLY -mset Q.PFAM,Q.INSECT,LG,Q.YEAST,p__Acidobacteriota_200_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_200/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/tree_update/p__Acidobacteriota_200_1.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/test_model/p__Acidobacteriota_200_test_concat
```
  
  Runtime: 1082.45 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_200_1+I+G4 | -5320381.283 | 10674174.544 |
| p__Acidobacteriota_200_1+F+I+G4 | -5329719.187 | 10693018.252 |
| Q.YEAST+F+I+G4 | -5343930.056 | 10721439.990 |
| Q.INSECT+F+I+G4 | -5344745.955 | 10723071.788 |
| LG+F+I+G4 | -5346295.057 | 10726169.992 |
| Q.PFAM+F+I+G4 | -5350564.095 | 10734708.068 |
| Q.PFAM+I+G4 | -5354813.240 | 10743038.458 |
| Q.PFAM+G4 | -5360837.536 | 10755078.213 |
| LG+I+G4 | -5362869.462 | 10759150.902 |
| Q.INSECT+I+G4 | -5366076.503 | 10765564.984 |
| Q.YEAST+I+G4 | -5380175.926 | 10793763.830 |
| Q.PFAM+I | -5870519.685 | 11774442.511 |
| Q.PFAM | -5928820.614 | 11891035.533 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/tree_update/p__Acidobacteriota_200_1.treefile -l 5 -u 200 -o ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 22   
Number of taxa after pruning: 1886   
Pruned node IDs (degree): 149 (158) 152 (47) 1356 (35) 1671 (190) 1860 (23) 200 (23) 1346 (9) 1391 (12) 1143 (15) 1157 (190) 1403 (164) 1566 (105) 995 (145) 226 (7) 981 (15) 519 (168) 235 (21) 961 (21) 256 (78) 333 (185) 688 (155) 842 (120)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 22 subtree files and 100 loci files. Total number of potential alignments: 2200.  
Sub-sampling 1000 alignments from 2200 alignments.  
Remaining 1000 alignments. Deleted 10 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/training_loci -m MFP -mset Q.PFAM,Q.INSECT,LG,Q.YEAST,p__Acidobacteriota_200_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_200/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/subtree_update/p__Acidobacteriota_200
```
  
  Runtime: 45193.27 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_200.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_200_1  

| Model | Count |
|-------|-------|
| 823 | p__Acidobacteriota_200_1 |
| 64 | Q.INSECT |
| 59 | LG |
| 40 | Q.PFAM |
| 14 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/subtree_update/p__Acidobacteriota_200.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/subtree_update/p__Acidobacteriota_200.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_200_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_200/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/model_update/p__Acidobacteriota_200
```
  
  Runtime: 76253.55 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_200.iqtree)  
BIC of the new model: 29563522.578  
Likelihood of the new model: -13814755.5814  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_200_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_200_2  
![Model bubble plot](loop_2/p__Acidobacteriota_200_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_200/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_200/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/tree_update/p__Acidobacteriota_200_2.treefile
```
  
  Runtime: 6481.58 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_200/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_200/loop_1/tree_update/p__Acidobacteriota_200_1.treefile', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/tree_update/p__Acidobacteriota_200_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_200/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0011  
Tree 1 branch length: 304.546563245  
Tree 2 branch length: 304.314682936  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998863922198149  
Euclidean distance: 0.08802916588021359  
Time usage for Loop_2: 127988.17 seconds (35.55 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_200/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_200/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/tree_update/p__Acidobacteriota_200_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_200/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 644  
Normalized RF distance: 0.1706  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 304.314682936  
### Model comparison  
Comparison between initial best model (Q.PFAM) and final model (p__Acidobacteriota_200_2):  
Pearson's correlation: 0.987312569937251  
Euclidean distance: 0.937942968485253  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/tree_update/p__Acidobacteriota_200_2.treefile -l 5 -u 200 -o ../Result_rona/formal_test/p__Acidobacteriota_200/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 22   
Number of taxa after pruning: 1886   
Pruned node IDs (degree): 149 (158) 152 (47) 1356 (35) 1671 (190) 1860 (23) 200 (23) 1346 (9) 1391 (12) 1143 (15) 1157 (190) 1403 (164) 1566 (105) 995 (145) 226 (7) 981 (15) 519 (168) 235 (21) 961 (21) 256 (78) 333 (185) 688 (155) 842 (120)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_200/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 22 subtree files and 20 loci files. Total number of potential alignments: 440.  
Obtained 437 alignments from all potential alignments.  
Remaining 437 alignments. Deleted 3 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_200/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_200_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_200/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_200/final_test/p__Acidobacteriota_200_test_partition
```
  
  Runtime: 555.11 seconds
Best models for test data:  
p__Acidobacteriota_200_2  

| Model | Count |
|-------|-------|
| 356 | p__Acidobacteriota_200_2 |
| 37 | Q.INSECT |
| 20 | LG |
| 10 | Q.PFAM |
| 7 | Q.YEAST |
| 6 | MTART |
| 1 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_200/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_200_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_200/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_200/loop_2/tree_update/p__Acidobacteriota_200_2.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_200/final_test/p__Acidobacteriota_200_test_concat
```
  
  Runtime: 1534.12 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_200_2+I+G4 | -5320747.348 | 10674906.674 |
| p__Acidobacteriota_200_2+F+I+G4 | -5329855.674 | 10693291.226 |
| Q.YEAST+F+I+G4 | -5343972.975 | 10721525.828 |
| Q.INSECT+F+I+G4 | -5344790.572 | 10723161.022 |
| LG+F+I+G4 | -5346338.863 | 10726257.604 |
| Q.PFAM+F+I+G4 | -5350607.851 | 10734795.580 |
| Q.PFAM+I+G4 | -5354856.346 | 10743124.670 |
| LG+I+G4 | -5362911.155 | 10759234.288 |
| Q.INSECT+I+G4 | -5366117.582 | 10765647.142 |
| LG+G4 | -5368888.807 | 10771180.755 |
| Q.YEAST+I+G4 | -5380218.605 | 10793849.188 |
| MTMET+F+I+G4 | -5505725.668 | 11045031.214 |
| MTART+F+I+G4 | -5619085.492 | 11271750.862 |
| MTMET+I+G4 | -5743877.785 | 11521167.548 |
| MTART+I+G4 | -5854942.823 | 11743297.624 |
| LG+I | -5878396.397 | 11790195.935 |
| LG | -5936910.251 | 11907214.807 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Acidobacteriota_200/trained_models/trained_model.nex ../Result_rona/formal_test/p__Acidobacteriota_200/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 378139.43 seconds (105.04 h)  
