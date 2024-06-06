## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_30  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 3500  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: upper  
  Lower limit for subtree size: 10  
  Upper limit for subtree size: 30  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/ref_tree.tre -l 10 -u 30 -n 39 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 39   
Number of taxa after pruning: 989   
Pruned node IDs (degree): 189 (30) 152 (30) 122 (30) 1209 (30) 563 (30) 432 (30) 352 (29) 912 (29) 880 (29) 35 (28) 1659 (28) 320 (28) 1097 (28) 469 (27) 633 (27) 727 (27) 1569 (25) 85 (25) 1271 (25) 1704 (24) 977 (24) 777 (24) 1416 (23) 222 (23) 1346 (23) 1593 (23) 1616 (23) 1530 (23) 1244 (23) 701 (23) 541 (23) 940 (23) 755 (23) 64 (22) 1306 (22) 598 (22) 1394 (21) 260 (21) 401 (21)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 39 subtree files and 100 loci files. Total number of potential alignments: 3900.  
Sub-sampling 3500 alignments from 3900 alignments.  
Remaining 3500 alignments. Deleted 25 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/subtree_update/p__Acidobacteriota_30
```
  
  Runtime: 19397.00 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_30.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| 1258 | Q.PFAM |
| 1182 | LG |
| 864 | Q.INSECT |
| 195 | Q.YEAST |
| 1 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/subtree_update/p__Acidobacteriota_30.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/subtree_update/p__Acidobacteriota_30.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/model_update/p__Acidobacteriota_30
```
  
  Runtime: 125506.71 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_30.iqtree)  
BIC of the new model: 33291207.7032  
Likelihood of the new model: -15600940.5145  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_30_1)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Acidobacteriota_30_1  
![Model bubble plot](loop_1/p__Acidobacteriota_30_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/tree_update/p__Acidobacteriota_30_1.treefile
```
  
  Runtime: 9894.00 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/tree_update/p__Acidobacteriota_30_1.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 636  
Normalized RF distance: 0.1684  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 301.054597036  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9792232916292116  
Euclidean distance: 1.08609271030343  
Time usage for Loop_1: 155091.09 seconds (43.08 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loci/concat_testing_loci.faa -m TESTONLY -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Acidobacteriota_30_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/trained_models/trained_model.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/tree_update/p__Acidobacteriota_30_1.treefile -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/test_model/p__Acidobacteriota_30
```
  
  Runtime: 1709.58 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_30_1+I+G4 | -5326783.074 | 10686978.126 |
| p__Acidobacteriota_30_1+F+I+G4 | -5329378.078 | 10692336.034 |
| Q.YEAST+F+I+G4 | -5343716.002 | 10721011.882 |
| Q.INSECT+F+I+G4 | -5344525.306 | 10722630.490 |
| LG+F+I+G4 | -5346074.812 | 10725729.502 |
| Q.PFAM+F+I+G4 | -5350342.866 | 10734265.610 |
| Q.PFAM+I+G4 | -5354566.831 | 10742545.640 |
| Q.PFAM+G4 | -5360589.510 | 10754582.161 |
| LG+I+G4 | -5362616.361 | 10758644.700 |
| Q.INSECT+I+G4 | -5365817.485 | 10765046.948 |
| Q.YEAST+I+G4 | -5379925.580 | 10793263.138 |
| Q.PFAM+I | -5870256.081 | 11773915.303 |
| Q.PFAM | -5928552.631 | 11890499.567 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/tree_update/p__Acidobacteriota_30_1.treefile -l 10 -u 30 -n 39 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 39   
Number of taxa after pruning: 988   
Pruned node IDs (degree): 1823 (30) 1793 (30) 1215 (30) 469 (30) 733 (30) 1003 (29) 768 (29) 1704 (28) 1497 (28) 932 (28) 1040 (28) 307 (27) 379 (27) 805 (27) 563 (27) 59 (26) 405 (26) 1447 (25) 1293 (25) 1754 (25) 1268 (24) 1542 (24) 613 (24) 1860 (23) 200 (23) 1357 (23) 1471 (23) 1407 (23) 1646 (23) 1244 (23) 535 (23) 710 (23) 447 (23) 591 (23) 94 (22) 1733 (22) 345 (22) 235 (21) 961 (21)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 39 subtree files and 100 loci files. Total number of potential alignments: 3900.  
Sub-sampling 3500 alignments from 3900 alignments.  
Remaining 3500 alignments. Deleted 25 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Acidobacteriota_30_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/subtree_update/p__Acidobacteriota_30
```
  
  Runtime: 7191.11 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_30.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_30_1  

| Model | Count |
|-------|-------|
| 3037 | p__Acidobacteriota_30_1 |
| 174 | LG |
| 137 | Q.INSECT |
| 92 | Q.PFAM |
| 60 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/subtree_update/p__Acidobacteriota_30.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/subtree_update/p__Acidobacteriota_30.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_30_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/model_update/p__Acidobacteriota_30
```
  
  Runtime: 45391.91 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_30.iqtree)  
BIC of the new model: 32546704.8414  
Likelihood of the new model: -15225343.9553  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_30_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_30_2  
![Model bubble plot](loop_2/p__Acidobacteriota_30_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/tree_update/p__Acidobacteriota_30_2.treefile
```
  
  Runtime: 15698.12 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_1/tree_update/p__Acidobacteriota_30_1.treefile', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/tree_update/p__Acidobacteriota_30_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0011  
Tree 1 branch length: 301.054597036  
Tree 2 branch length: 301.81844298  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999017548969373  
Euclidean distance: 0.075198282477454  
Time usage for Loop_2: 68479.17 seconds (19.02 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/final_test', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/tree_update/p__Acidobacteriota_30_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 636  
Normalized RF distance: 0.1684  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 301.81844298  
### Model comparison  
Comparison between initial best model (Q.PFAM) and final model (p__Acidobacteriota_30_2):  
Pearson's correlation: 0.9778132259748387  
Euclidean distance: 1.1229074680929587  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/loop_2/tree_update/p__Acidobacteriota_30_2.treefile -l 10 -u 30 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 81   
Number of taxa after pruning: 1630   
Pruned node IDs (degree): 1860 (23) 161 (19) 179 (20) 200 (23) 1357 (23) 1379 (12) 1391 (12) 1672 (16) 6 (12) 1143 (15) 1823 (30) 19 (16) 34 (17) 1328 (19) 1568 (17) 1690 (13) 94 (22) 981 (15) 1447 (25) 1471 (23) 59 (26) 84 (10) 116 (20) 135 (15) 1095 (13) 1268 (24) 1407 (23) 1429 (18) 1542 (24) 1704 (28) 1779 (15) 1793 (30) 235 (21) 961 (21) 1108 (17) 1124 (16) 1497 (28) 1524 (19) 1646 (23) 1293 (25) 1733 (22) 1754 (25) 501 (17) 677 (10) 1003 (29) 1244 (23) 690 (16) 1173 (11) 1621 (12) 1072 (12) 1592 (17) 1608 (14) 307 (27) 405 (26) 847 (18) 1215 (30) 379 (27) 469 (30) 535 (23) 710 (23) 805 (27) 1186 (21) 1206 (10) 345 (22) 366 (14) 433 (15) 447 (23) 733 (30) 932 (28) 1040 (28) 268 (19) 286 (12) 919 (12) 768 (29) 563 (27) 637 (14) 650 (20) 878 (12) 889 (20) 591 (23) 613 (24)   
Pruning mode: random   
Pruning completed. Results saved in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/final_test/subtrees 
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...
Input 81 subtree files and 20 loci files. Total number of potential alignments: 1620.
Obtained 1605 alignments from all potential alignments.
Remaining 1605 alignments. Deleted 15 alignments.
### Final model testing  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_30_2 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/final_test/p__Acidobacteriota_30
```
  
  Runtime: 234.70 seconds
Best models for test data:  
p__Acidobacteriota_30_2  

| Model | Count |
|-------|-------|
| 1353 | p__Acidobacteriota_30_2 |
| 92 | LG |
| 49 | MTART |
| 46 | Q.YEAST |
| 41 | Q.INSECT |
| 18 | Q.PFAM |
| 6 | MTMET |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/trained_models/trained_model.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_30/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 225801.56 seconds (62.72 h)  
