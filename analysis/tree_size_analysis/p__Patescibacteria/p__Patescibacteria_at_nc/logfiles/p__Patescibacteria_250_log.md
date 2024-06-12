## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Patescibacteria_250  
  Taxa name: p__Patescibacteria  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 8 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_250/select_id.txt. Sampling sequences for 92 loci.  
Number of input species: 4465  
Remaining 92 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 5 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_250/select_id.txt. Sampling sequences for 15 loci.  
Number of input species: 4465  
Remaining 15 alignments. Deleted 0 alignments.  
Abstract alingment of selected taxa scale in training set:  
Abstract alingment of selected taxa scale in testing set:  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_250/ref_tree.tre -l 5 -u 250 -o ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 55   
Number of taxa after pruning: 4419   
Pruned node IDs (degree): 1125 (50) 1175 (15) 735 (245) 979 (146) 3529 (60) 4 (112) 2743 (177) 2920 (11) 3589 (10) 116 (52) 1192 (8) 3486 (43) 168 (10) 2502 (242) 2932 (71) 3603 (17) 722 (10) 3270 (217) 179 (70) 1202 (14) 2203 (21) 3004 (15) 3621 (20) 249 (246) 494 (229) 2152 (51) 3019 (235) 3253 (18) 4450 (11) 2130 (23) 2226 (247) 2472 (31) 2121 (10) 1219 (19) 2109 (13) 3646 (190) 2105 (5) 2095 (11) 3837 (5) 2066 (29) 1243 (8) 1251 (44) 3847 (8) 1295 (209) 3855 (63) 1504 (242) 1746 (10) 3920 (230) 2049 (18) 4426 (19) 1759 (74) 1832 (218) 4159 (7) 4166 (214) 4379 (46)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input 55 subtree files and 92 loci files. Total number of potential alignments: 5060.  
Sub-sampling 1000 alignments from 5060 alignments.  
Could not obtain the requested 1000 alignments. Keeping 981 alignments.  
Remaining 981 alignments. Deleted 119 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/subtree_update/p__Patescibacteria_250
```
  
  Runtime: 134574.73 seconds
[Subtree update log](loop_1/subtree_update/p__Patescibacteria_250.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 388 | LG |
| 332 | Q.YEAST |
| 170 | Q.PFAM |
| 91 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/subtree_update/p__Patescibacteria_250.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/subtree_update/p__Patescibacteria_250.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/model_update/p__Patescibacteria_250
```
  
  Runtime: 176919.74 seconds
[Model update log](loop_1/model_update/p__Patescibacteria_250.iqtree)  
BIC of the new model: 39061699.0607  
Likelihood of the new model: -18607833.2833  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_250_1)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_250_1  
![Model bubble plot](loop_1/p__Patescibacteria_250_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_250/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_250/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/tree_update/p__Patescibacteria_250_1.treefile
```
  
  Runtime: 15817.43 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_250/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_250/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_250/loop_1/tree_update/p__Patescibacteria_250_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_250/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 2080  
Normalized RF distance: 0.2331  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1425.119712395  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9880507851277308  
Euclidean distance: 0.8588500740203086  
Time usage for Loop_1: 327515.15 seconds (90.98 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_250/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_250_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_250/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/tree_update/p__Patescibacteria_250_1.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/test_model/p__Patescibacteria_250_test_concat
```
  
  Runtime: 4151.78 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_250_1+I+G4 | -15054892.020 | 30187105.255 |
| p__Patescibacteria_250_1+F+I+G4 | -15092969.050 | 30263423.847 |
| Q.YEAST+I+G4 | -15113122.880 | 30303566.975 |
| LG+F+I+G4 | -15120757.460 | 30319000.667 |
| Q.PFAM+F+I+G4 | -15124063.390 | 30325612.527 |
| Q.YEAST+F+I+G4 | -15144651.610 | 30366788.967 |
| LG+I+G4 | -15146350.530 | 30370022.275 |
| Q.PFAM+I+G4 | -15146718.490 | 30370758.195 |
| LG+G4 | -15150997.830 | 30379308.216 |
| Q.INSECT+I+G4 | -15151709.900 | 30380741.015 |
| Q.INSECT+F+I+G4 | -15181242.090 | 30439969.927 |
| LG+I | -16406740.900 | 32890794.356 |
| LG | -16442757.910 | 32962819.716 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_250/loop_1/tree_update/p__Patescibacteria_250_1.treefile -l 5 -u 250 -o ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 58   
Number of taxa after pruning: 4412   
Pruned node IDs (degree): 2091 (248) 3072 (247) 97 (246) 2775 (243) 885 (240) 1518 (230) 342 (229) 3919 (216) 3678 (215) 1764 (214) 2398 (212) 1242 (190) 3450 (179) 4274 (177) 739 (147) 622 (104) 17 (80) 3377 (74) 1454 (63) 1127 (61) 2339 (60) 571 (52) 2661 (50) 2726 (50) 1977 (46) 2619 (43) 3628 (43) 4134 (35) 3042 (31) 4172 (29) 3892 (28) 4234 (23) 3019 (22) 1217 (20) 2023 (19) 1198 (18) 3324 (18) 3358 (18) 4450 (15) 2077 (15) 4256 (13) 2711 (11) 2609 (11) 2046 (11) 4215 (11) 4201 (11) 1188 (10) 2067 (10) 4225 (10) 1432 (9) 725 (8) 7 (8) 1446 (8) 4268 (7) 3670 (7) 1757 (7) 4211 (5) 4168 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input 58 subtree files and 92 loci files. Total number of potential alignments: 5336.  
Sub-sampling 1000 alignments from 5336 alignments.  
Could not obtain the requested 1000 alignments. Keeping 993 alignments.  
Remaining 993 alignments. Deleted 107 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_250_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_250/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/subtree_update/p__Patescibacteria_250
```
  
  Runtime: 221847.19 seconds
[Subtree update log](loop_2/subtree_update/p__Patescibacteria_250.iqtree)  
Best models for iteration 2:  
p__Patescibacteria_250_1  

| Model | Count |
|-------|-------|
| 714 | p__Patescibacteria_250_1 |
| 125 | LG |
| 76 | Q.PFAM |
| 40 | Q.YEAST |
| 38 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/subtree_update/p__Patescibacteria_250.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/subtree_update/p__Patescibacteria_250.treefile --model-joint GTR20+FO --init-model p__Patescibacteria_250_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_250/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/model_update/p__Patescibacteria_250
```
  
  Runtime: 120283.97 seconds
[Model update log](loop_2/model_update/p__Patescibacteria_250.iqtree)  
BIC of the new model: 36651883.7623  
Likelihood of the new model: -17443242.9778  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_250_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_250_2  
![Model bubble plot](loop_2/p__Patescibacteria_250_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_250/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_250/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/tree_update/p__Patescibacteria_250_2.treefile
```
  
  Runtime: 13590.44 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_250/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_250/loop_1/tree_update/p__Patescibacteria_250_1.treefile', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_250/loop_2/tree_update/p__Patescibacteria_250_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_250/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 36  
Normalized RF distance: 0.004  
Tree 1 branch length: 1425.119712395  
Tree 2 branch length: 1440.98182411  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9996866793463004  
Euclidean distance: 0.1375623961143901  
Time usage for Loop_2: 355820.72 seconds (98.84 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_250/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_250/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_250/loop_2/tree_update/p__Patescibacteria_250_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_250/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2086  
Normalized RF distance: 0.2338  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1440.98182411  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Patescibacteria_250_2):  
Pearson's correlation: 0.9860679188587262  
Euclidean distance: 0.9310066437211734  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/tree_update/p__Patescibacteria_250_2.treefile -l 5 -u 250 -o ../Result_rona/formal_test/p__Patescibacteria_250/final_test/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 58   
Number of taxa after pruning: 4412   
Pruned node IDs (degree): 1364 (248) 2345 (247) 3836 (246) 2048 (243) 158 (240) 791 (230) 4081 (229) 3192 (216) 2951 (215) 1037 (214) 1671 (212) 515 (190) 2723 (179) 3547 (177) 12 (147) 4361 (104) 3756 (80) 2650 (74) 727 (63) 400 (61) 1612 (60) 4310 (52) 1934 (50) 1999 (50) 1250 (46) 1892 (43) 2901 (43) 3407 (35) 2315 (31) 3445 (29) 3165 (28) 3507 (23) 2292 (22) 490 (20) 1296 (19) 471 (18) 2597 (18) 2631 (18) 3723 (15) 1350 (15) 3529 (13) 1984 (11) 1882 (11) 1319 (11) 3488 (11) 3474 (11) 461 (10) 1340 (10) 3498 (10) 705 (9) 3737 (8) 3746 (8) 719 (8) 3541 (7) 2943 (7) 1030 (7) 3484 (5) 3441 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_250/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input 58 subtree files and 15 loci files. Total number of potential alignments: 870.  
Obtained 775 alignments from all potential alignments.  
Remaining 775 alignments. Deleted 95 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_250/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_250_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_250/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_250/final_test/p__Patescibacteria_250_test_partition
```
  
  Runtime: 1195.73 seconds
Best models for test data:  
p__Patescibacteria_250_2  

| Model | Count |
|-------|-------|
| 561 | p__Patescibacteria_250_2 |
| 83 | LG |
| 62 | Q.YEAST |
| 43 | Q.PFAM |
| 14 | MTMET |
| 7 | Q.INSECT |
| 5 | MTART |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_250/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_250_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_250/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_250/loop_2/tree_update/p__Patescibacteria_250_2.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_250/final_test/p__Patescibacteria_250_test_concat
```
  
  Runtime: 4965.84 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_250_2+I+G4 | -15054566.410 | 30186454.035 |
| p__Patescibacteria_250_2+F+I+G4 | -15092186.940 | 30261859.627 |
| Q.YEAST+I+G4 | -15113298.380 | 30303917.975 |
| LG+F+I+G4 | -15120824.590 | 30319134.927 |
| Q.PFAM+F+I+G4 | -15124152.510 | 30325790.767 |
| Q.YEAST+F+I+G4 | -15144761.180 | 30367008.107 |
| LG+I+G4 | -15146475.280 | 30370271.775 |
| Q.PFAM+I+G4 | -15146849.720 | 30371020.655 |
| LG+G4 | -15151125.410 | 30379563.376 |
| Q.INSECT+I+G4 | -15151851.210 | 30381023.635 |
| Q.INSECT+F+I+G4 | -15181293.360 | 30440072.467 |
| MTMET+F+I+G4 | -15480445.860 | 31038377.467 |
| MTART+F+I+G4 | -15631512.670 | 31340511.087 |
| MTMET+I+G4 | -15911559.500 | 31900440.215 |
| MTART+I+G4 | -16110251.840 | 32297824.895 |
| LG+I | -16406835.630 | 32890983.816 |
| LG | -16442852.830 | 32963009.556 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Patescibacteria_250/trained_models/trained_model.nex ../Result_rona/formal_test/p__Patescibacteria_250/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 694119.78 seconds (192.81 h)  
