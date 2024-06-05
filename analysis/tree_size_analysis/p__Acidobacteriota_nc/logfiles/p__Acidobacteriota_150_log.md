## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_150  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
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
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_150/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_150/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_150/ref_tree.tre -l 5 -u 150 -o ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 35   
Number of taxa after pruning: 1876   
Pruned node IDs (degree): 1415 (35) 4 (10) 189 (30) 17 (135) 151 (39) 1376 (39) 1450 (116) 222 (23) 1368 (9) 1879 (13) 1346 (23) 1567 (89) 1655 (74) 1730 (5) 1734 (146) 246 (47) 1328 (19) 293 (98) 1167 (101) 1267 (62) 392 (7) 1147 (15) 401 (21) 1127 (21) 422 (78) 690 (6) 1008 (120) 500 (16) 696 (148) 843 (10) 855 (111) 965 (44) 516 (5) 524 (147) 670 (14)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 35 subtree files and 100 loci files. Total number of potential alignments: 3500.  
Sub-sampling 1000 alignments from 3500 alignments.  
Remaining 1000 alignments. Deleted 22 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/subtree_update/p__Acidobacteriota_150
```
  
  Runtime: 21045.43 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_150.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 349 | LG |
| 320 | Q.PFAM |
| 256 | Q.INSECT |
| 75 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/subtree_update/p__Acidobacteriota_150.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/subtree_update/p__Acidobacteriota_150.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/model_update/p__Acidobacteriota_150
```
  
  Runtime: 73702.05 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_150.iqtree)  
BIC of the new model: 18901913.3098  
Likelihood of the new model: -8840252.63  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_150_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_150_1  
![Model bubble plot](loop_1/p__Acidobacteriota_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_150/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_150/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile
```
  
  Runtime: 14334.94 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_150/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_150/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 634  
Normalized RF distance: 0.1679  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 302.294789417  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9885916722516558  
Euclidean distance: 0.8854949031020427  
Time usage for Loop_1: 109216.34 seconds (30.34 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_150_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_150/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/test_model/p__Acidobacteriota_150
```
  
  Runtime: 47405.21 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_150_1+I+G4 | -5321786.508 | 10676984.994 |
| p__Acidobacteriota_150_1+F+I+G4 | -5328089.803 | 10689759.484 |
| Q.YEAST+F+I+G4 | -5343671.739 | 10720923.356 |
| Q.INSECT+F+I+G4 | -5344490.312 | 10722560.502 |
| LG+F+I+G4 | -5346033.636 | 10725647.150 |
| Q.PFAM+F+I+G4 | -5350304.527 | 10734188.932 |
| Q.PFAM+I+G4 | -5354537.716 | 10742487.410 |
| LG+I+G4 | -5362587.132 | 10758586.242 |
| Q.INSECT+I+G4 | -5365788.278 | 10764988.534 |
| LG+G4 | -5368558.909 | 10770520.959 |
| Q.YEAST+I+G4 | -5379887.091 | 10793186.160 |
| LG+I | -5878060.599 | 11789524.339 |
| LG | -5936569.503 | 11906533.311 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile -l 5 -u 150 -o ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 36   
Number of taxa after pruning: 1882   
Pruned node IDs (degree): 1882 (5) 2 (148) 152 (47) 1886 (5) 1356 (35) 1860 (23) 200 (23) 1346 (9) 1391 (12) 1672 (16) 1143 (15) 1566 (105) 1688 (135) 1822 (39) 995 (145) 1158 (8) 1404 (90) 1493 (74) 1328 (19) 226 (7) 981 (15) 1167 (101) 1267 (62) 235 (21) 961 (21) 256 (78) 524 (6) 842 (120) 501 (17) 530 (148) 677 (10) 689 (111) 799 (44) 335 (7) 342 (89) 430 (72)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 36 subtree files and 100 loci files. Total number of potential alignments: 3600.  
Sub-sampling 1000 alignments from 3600 alignments.  
Remaining 1000 alignments. Deleted 29 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_150_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_150/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/subtree_update/p__Acidobacteriota_150
```
  
  Runtime: 39091.64 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_150.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_150_1  

| Model | Count |
|-------|-------|
| 803 | p__Acidobacteriota_150_1 |
| 79 | LG |
| 62 | Q.INSECT |
| 41 | Q.PFAM |
| 15 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/subtree_update/p__Acidobacteriota_150.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/subtree_update/p__Acidobacteriota_150.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_150_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_150/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/model_update/p__Acidobacteriota_150
```
  
  Runtime: 33157.40 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_150.iqtree)  
BIC of the new model: 19298160.7249  
Likelihood of the new model: -9059170.9304  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_150_2  
![Model bubble plot](loop_2/p__Acidobacteriota_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_150/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_150/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile
```
  
  Runtime: 6817.08 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_150/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_150/loop_1/tree_update/p__Acidobacteriota_150_1.treefile', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 14  
Normalized RF distance: 0.0037  
Tree 1 branch length: 302.294789417  
Tree 2 branch length: 303.353271877  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997883467157125  
Euclidean distance: 0.11251761672114628  
Time usage for Loop_2: 79175.27 seconds (21.99 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_150/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_150/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 630  
Normalized RF distance: 0.1668  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 303.353271877  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Acidobacteriota_150_2):  
Pearson's correlation: 0.9878896913270551  
Euclidean distance: 0.9037528260790488  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile -l 5 -u 150 -o ../Result_rona/formal_test/p__Acidobacteriota_150/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 36   
Number of taxa after pruning: 1882   
Pruned node IDs (degree): 1882 (5) 2 (148) 152 (47) 1886 (5) 1356 (35) 1860 (23) 200 (23) 1346 (9) 1391 (12) 1672 (16) 1143 (15) 1566 (105) 1688 (135) 1822 (39) 995 (145) 1158 (8) 1404 (90) 1493 (74) 1328 (19) 226 (7) 981 (15) 1167 (101) 1267 (62) 235 (21) 961 (21) 256 (78) 524 (6) 842 (120) 501 (17) 530 (148) 677 (10) 689 (111) 799 (44) 335 (7) 342 (89) 430 (72)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 36 subtree files and 20 loci files. Total number of potential alignments: 720.  
Obtained 704 alignments from all potential alignments.  
Remaining 704 alignments. Deleted 16 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_150_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_150/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_150/final_test/p__Acidobacteriota_150
```
  
  Runtime: 548.82 seconds
Best models for test data:  
p__Acidobacteriota_150_2  

| Model | Count |
|-------|-------|
| 578 | p__Acidobacteriota_150_2 |
| 51 | LG |
| 37 | Q.INSECT |
| 14 | MTART |
| 13 | Q.PFAM |
| 9 | Q.YEAST |
| 2 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_150_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_150/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_150/loop_2/tree_update/p__Acidobacteriota_150_2.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_150/final_test/p__Acidobacteriota_150_test_concat
```
  
  Runtime: 1612.33 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_150_2+I+G4 | -5320747.348 | 10674906.674 |
| p__Acidobacteriota_150_2+F+I+G4 | -5329855.674 | 10693291.226 |
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
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Acidobacteriota_150/trained_models/trained_model.nex ../Result_rona/formal_test/p__Acidobacteriota_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 378139.43 seconds (50.52 h)  
