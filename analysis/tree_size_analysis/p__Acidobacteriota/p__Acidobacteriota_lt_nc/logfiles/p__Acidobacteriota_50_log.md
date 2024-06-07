## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_50  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: upper  
  Lower limit for subtree size: 10  
  Upper limit for subtree size: 50  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/ref_tree.tre -l 10 -u 50 -n 22 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 22   
Number of taxa after pruning: 939   
Pruned node IDs (degree): 1472 (50) 303 (50) 62 (48) 1568 (48) 1735 (48) 753 (48) 246 (47) 1658 (47) 965 (44) 1033 (44) 1615 (41) 1839 (40) 426 (40) 593 (40) 151 (39) 1376 (39) 632 (39) 800 (39) 1269 (38) 526 (38) 875 (37) 1415 (35)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 22 subtree files and 100 loci files. Total number of potential alignments: 2200.  
Sub-sampling 2000 alignments from 2200 alignments.  
Remaining 2000 alignments. Deleted 13 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/subtree_update/p__Acidobacteriota_50
```
  
  Runtime: 25573.96 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_50.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| 711 | Q.INSECT |
| 579 | Q.PFAM |
| 541 | LG |
| 168 | Q.YEAST |
| 1 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/subtree_update/p__Acidobacteriota_50.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/subtree_update/p__Acidobacteriota_50.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/model_update/p__Acidobacteriota_50
```
  
  Runtime: 121093.45 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_50.iqtree)  
BIC of the new model: 30181590.748  
Likelihood of the new model: -14112544.1942  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_50_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_50_1  
![Model bubble plot](loop_1/p__Acidobacteriota_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile
```
  
  Runtime: 12808.06 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 644  
Normalized RF distance: 0.1706  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 301.672168238  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9815892664591441  
Euclidean distance: 1.0608055431331527  
Time usage for Loop_1: 159560.84 seconds (44.32 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loci/concat_testing_loci.faa -m TESTONLY -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_50_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/trained_models/trained_model.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/test_model/p__Acidobacteriota_50
```
  
  Runtime: 2741.85 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_50_1+I+G4 | -5323573.958 | 10680559.894 |
| p__Acidobacteriota_50_1+F+I+G4 | -5329205.678 | 10691991.234 |
| Q.YEAST+F+I+G4 | -5343850.717 | 10721281.312 |
| Q.INSECT+F+I+G4 | -5344662.479 | 10722904.836 |
| LG+F+I+G4 | -5346214.101 | 10726008.080 |
| Q.PFAM+F+I+G4 | -5350484.369 | 10734548.616 |
| Q.PFAM+I+G4 | -5354713.688 | 10742839.354 |
| LG+I+G4 | -5362764.649 | 10758941.276 |
| Q.INSECT+I+G4 | -5365953.779 | 10765319.536 |
| Q.INSECT+G4 | -5372392.198 | 10778187.537 |
| Q.YEAST+I+G4 | -5380061.551 | 10793535.080 |
| Q.INSECT+I | -5893486.601 | 11820376.343 |
| Q.INSECT | -5956321.734 | 11946037.773 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile -l 10 -u 50 -n 22 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/subtrees -m upper
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
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_50_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/subtree_update/p__Acidobacteriota_50
```
  
  Runtime: 11210.15 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_50.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_50_1  

| Model | Count |
|-------|-------|
| 1660 | p__Acidobacteriota_50_1 |
| 128 | Q.INSECT |
| 109 | LG |
| 55 | Q.PFAM |
| 48 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/subtree_update/p__Acidobacteriota_50.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/subtree_update/p__Acidobacteriota_50.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_50_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/model_update/p__Acidobacteriota_50
```
  
  Runtime: 60570.43 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_50.iqtree)  
BIC of the new model: 30951055.4322  
Likelihood of the new model: -14494495.8508  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_50_2  
![Model bubble plot](loop_2/p__Acidobacteriota_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile
```
  
  Runtime: 9740.13 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0026  
Tree 1 branch length: 301.672168238  
Tree 2 branch length: 300.897597722  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999577596895911  
Euclidean distance: 0.056690943073488015  
Time usage for Loop_2: 81631.81 seconds (22.68 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/final_test', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 644  
Normalized RF distance: 0.1706  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 300.897597722  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (p__Acidobacteriota_50_2):  
Pearson's correlation: 0.9807456150458627  
Euclidean distance: 1.0936792495335794  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile -l 10 -u 50 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/final_test/subtrees -m random
```

Number of pruned subtrees: 58   
Number of taxa after pruning: 1731   
Pruned node IDs (degree): 152 (47) 1356 (35) 1860 (23) 5 (48) 200 (23) 1391 (12) 1672 (16) 1143 (15) 1822 (39) 57 (37) 1093 (47) 1328 (19) 1405 (42) 1446 (48) 1568 (17) 1690 (13) 94 (22) 115 (35) 981 (15) 1778 (45) 1268 (24) 1291 (38) 1496 (47) 1542 (24) 1704 (28) 1731 (48) 235 (21) 961 (21) 1591 (17) 501 (17) 677 (10) 799 (44) 1003 (29) 1244 (23) 690 (16) 1034 (50) 1173 (11) 1619 (50) 264 (40) 303 (31) 405 (26) 847 (18) 1185 (31) 1215 (30) 344 (36) 379 (27) 432 (38) 469 (30) 535 (23) 710 (23) 931 (31) 733 (30) 762 (36) 919 (12) 868 (44) 636 (34) 563 (27) 589 (48)   
Pruning mode: random   
Pruning completed. Results saved in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/final_test/subtrees 

Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 58 subtree files and 20 loci files. Total number of potential alignments: 1160.  
Obtained 1151 alignments from all potential alignments.  
Remaining 1151 alignments. Deleted 9 alignments.  
### Final model testing  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_50_2 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/final_test/p__Acidobacteriota_50
```
  
  Runtime: 174.18 seconds
Best models for test data:  
p__Acidobacteriota_50_2  

| Model | Count |
|-------|-------|
| 952 | p__Acidobacteriota_50_2 |
| 76 | LG |
| 53 | Q.INSECT |
| 28 | MTART |
| 22 | Q.YEAST |
| 16 | Q.PFAM |
| 4 | MTMET |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/trained_models/trained_model.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 244310.14 seconds (67.86 h)  
