## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_150  
  Taxa name: p__Acidobacteriota  
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
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Acidobacteriota_150/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1867  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Acidobacteriota_150/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1867  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Acidobacteriota_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 1867   
Number of pruned subtrees: 34   
Number of taxa after pruning: 1852   
Pruned node IDs (degree): 1394 (35) 4 (10) 188 (30) 17 (135) 151 (38) 1356 (38) 1429 (115) 221 (23) 1348 (9) 1855 (13) 1326 (23) 1545 (87) 1631 (74) 1706 (5) 1710 (146) 245 (45) 1308 (19) 290 (98) 1147 (101) 1247 (62) 389 (7) 1128 (14) 398 (21) 1109 (20) 419 (78) 685 (5) 845 (149) 993 (117) 497 (16) 690 (146) 835 (9) 513 (5) 521 (145) 665 (14)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 34 subtree files and 100 loci files. Total number of potential alignments: 3400.  
Sub-sampling 1000 alignments from 3400 alignments.  
Remaining 1000 alignments. Deleted 31 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/subtree_update/p__Acidobacteriota_150
```
  
  Runtime: 49805.61 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_150.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 347 | LG |
| 331 | Q.PFAM |
| 265 | Q.INSECT |
| 57 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/subtree_update/p__Acidobacteriota_150.best_scheme.nex -te ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/subtree_update/p__Acidobacteriota_150.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/model_update/p__Acidobacteriota_150
```
  
  Runtime: 62248.57 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_150.iqtree)  
BIC of the new model: 19354976.4218  
Likelihood of the new model: -9046578.2373  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_150_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_150_1  
![Model bubble plot](loop_1/p__Acidobacteriota_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Acidobacteriota_150/ref_tree.tre ../Result/safe_phyla/p__Acidobacteriota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile
```
  
  Runtime: 18265.41 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Acidobacteriota_150/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Acidobacteriota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Acidobacteriota_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 612  
Normalized RF distance: 0.1642  
Tree 1 branch length: 222.88241  
Tree 2 branch length: 301.480336567  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9885803615671033  
Euclidean distance: 0.8744888518000616  
Time usage for Loop_1: 130380.53 seconds (36.22 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Acidobacteriota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_150_1 -mdef ../Result/safe_phyla/p__Acidobacteriota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile -pre ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/test_model/p__Acidobacteriota_150_test_concat
```
  
  Runtime: 10156.13 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_150_1+I+G4 | -5294189.985 | 10621367.781 |
| p__Acidobacteriota_150_1+F+I+G4 | -5301420.259 | 10635996.229 |
| Q.YEAST+F+I+G4 | -5316700.136 | 10666555.983 |
| Q.INSECT+F+I+G4 | -5317543.280 | 10668242.271 |
| LG+F+I+G4 | -5319043.756 | 10671243.223 |
| Q.PFAM+F+I+G4 | -5323319.044 | 10679793.799 |
| Q.PFAM+I+G4 | -5327483.047 | 10687953.905 |
| LG+I+G4 | -5335441.548 | 10703870.907 |
| Q.INSECT+I+G4 | -5338677.414 | 10710342.639 |
| LG+G4 | -5341436.531 | 10715852.036 |
| Q.YEAST+I+G4 | -5352676.824 | 10738341.459 |
| LG+I | -5848370.642 | 11729720.258 |
| LG | -5906814.547 | 11846599.232 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/subtrees -m random
```
  
Original number of taxa: 1867   
Number of pruned subtrees: 35   
Number of taxa after pruning: 1858   
Pruned node IDs (degree): 1858 (5) 2 (148) 152 (46) 1862 (5) 1336 (35) 1836 (23) 199 (23) 1326 (9) 1371 (12) 1649 (16) 1123 (15) 1544 (104) 1665 (135) 1799 (38) 977 (143) 1138 (8) 1384 (88) 1471 (74) 1308 (19) 225 (7) 964 (14) 1147 (101) 1247 (62) 234 (21) 945 (20) 255 (78) 521 (5) 681 (149) 829 (117) 498 (17) 526 (146) 671 (9) 334 (7) 341 (88) 428 (71)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 35 subtree files and 100 loci files. Total number of potential alignments: 3500.  
Sub-sampling 1000 alignments from 3500 alignments.  
Remaining 1000 alignments. Deleted 27 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_150_1 -mdef ../Result/safe_phyla/p__Acidobacteriota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/subtree_update/p__Acidobacteriota_150
```
  
  Runtime: 64087.97 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_150.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_150_1  

| Model | Count |
|-------|-------|
| 801 | p__Acidobacteriota_150_1 |
| 99 | LG |
| 50 | Q.INSECT |
| 40 | Q.PFAM |
| 10 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/subtree_update/p__Acidobacteriota_150.best_scheme.nex -te ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/subtree_update/p__Acidobacteriota_150.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_150_1 -mdef ../Result/safe_phyla/p__Acidobacteriota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/model_update/p__Acidobacteriota_150
```
  
  Runtime: 117999.10 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_150.iqtree)  
BIC of the new model: 19240371.5035  
Likelihood of the new model: -9034138.5735  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_150_2  
![Model bubble plot](loop_2/p__Acidobacteriota_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Acidobacteriota_150/ref_tree.tre ../Result/safe_phyla/p__Acidobacteriota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile
```
  
  Runtime: 17734.10 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Acidobacteriota_150/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile', tree2_path = '../Result/safe_phyla/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Acidobacteriota_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0016  
Tree 1 branch length: 301.480336567  
Tree 2 branch length: 301.092671114  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997811152246331  
Euclidean distance: 0.12299656435532606  
Time usage for Loop_2: 199939.41 seconds (55.54 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Acidobacteriota_150/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Acidobacteriota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Acidobacteriota_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 614  
Normalized RF distance: 0.1647  
Tree 1 branch length: 222.88241  
Tree 2 branch length: 301.092671114  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Acidobacteriota_150_2):  
Pearson's correlation: 0.9878991497088473  
Euclidean distance: 0.9183470548761665  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Acidobacteriota_150/final_test/subtrees -m random
```
  
Original number of taxa: 1867   
Number of pruned subtrees: 35   
Number of taxa after pruning: 1858   
Pruned node IDs (degree): 1858 (5) 2 (148) 152 (46) 1862 (5) 1336 (35) 1836 (23) 199 (23) 1326 (9) 1371 (12) 1649 (16) 1123 (15) 1544 (104) 1665 (135) 1799 (38) 977 (143) 1138 (8) 1384 (88) 1471 (74) 1308 (19) 225 (7) 964 (14) 1147 (101) 1247 (62) 234 (21) 945 (20) 255 (78) 521 (5) 681 (149) 829 (117) 498 (17) 526 (146) 671 (9) 334 (7) 341 (88) 428 (71)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Acidobacteriota_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 35 subtree files and 20 loci files. Total number of potential alignments: 700.  
Obtained 682 alignments from all potential alignments.  
Remaining 682 alignments. Deleted 18 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Acidobacteriota_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_150_2 -mdef ../Result/safe_phyla/p__Acidobacteriota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Acidobacteriota_150/final_test/p__Acidobacteriota_150_test_partition
```
  
  Runtime: 1994.59 seconds
Best models for test data:  
p__Acidobacteriota_150_2  

| Model | Count |
|-------|-------|
| 558 | p__Acidobacteriota_150_2 |
| 49 | LG |
| 36 | Q.INSECT |
| 15 | MTART |
| 13 | Q.PFAM |
| 9 | Q.YEAST |
| 2 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Acidobacteriota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_150_2 -mdef ../Result/safe_phyla/p__Acidobacteriota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile -pre ../Result/safe_phyla/p__Acidobacteriota_150/final_test/p__Acidobacteriota_150_test_concat
```
  
  Runtime: 48335.95 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_150_2+I+G4 | -5294567.659 | 10622123.129 |
| p__Acidobacteriota_150_2+F+I+G4 | -5301176.605 | 10635508.921 |
| Q.YEAST+F+I+G4 | -5316757.977 | 10666671.665 |
| Q.INSECT+F+I+G4 | -5317600.302 | 10668356.315 |
| LG+F+I+G4 | -5319101.876 | 10671359.463 |
| Q.PFAM+F+I+G4 | -5323375.805 | 10679907.321 |
| Q.PFAM+I+G4 | -5327541.269 | 10688070.349 |
| LG+I+G4 | -5335501.984 | 10703991.779 |
| Q.INSECT+I+G4 | -5338727.991 | 10710443.793 |
| LG+G4 | -5341497.978 | 10715974.930 |
| Q.YEAST+I+G4 | -5352727.686 | 10738443.183 |
| MTMET+F+I+G4 | -5477656.978 | 10988469.667 |
| MTART+F+I+G4 | -5590346.606 | 11213848.923 |
| MTMET+I+G4 | -5714566.999 | 11462121.809 |
| MTART+I+G4 | -5825054.843 | 11683097.497 |
| LG+I | -5848429.664 | 11729838.302 |
| LG | -5906874.669 | 11846719.476 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Acidobacteriota_150/trained_models/trained_model.nex ../Result/safe_phyla/p__Acidobacteriota_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 391044.71 seconds (108.62 h)  
