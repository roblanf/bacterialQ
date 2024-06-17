## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Patescibacteria_100  
  Taxa name: p__Patescibacteria  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 100  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Abstract alingment of selected taxa scale in training set:  
Running sample_alignment...  
Discarded 8 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_100/select_id.txt. Sampling sequences for 92 loci.  
Number of input species: 4465  
Remaining 92 alignments. Deleted 0 alignments.  
Abstract alingment of selected taxa scale in testing set:  
Running sample_alignment...  
Discarded 5 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_100/select_id.txt. Sampling sequences for 15 loci.  
Number of input species: 4465  
Remaining 15 alignments. Deleted 0 alignments.  
Concatenating training loci...  
Concatenating testing loci...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_100/ref_tree.tre -l 5 -u 100 -o ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 116   
Number of taxa after pruning: 4390   
Pruned node IDs (degree): 3686 (100) 3378 (99) 1602 (98) 4171 (98) 261 (94) 742 (93) 630 (93) 1885 (93) 3020 (92) 1034 (91) 13 (90) 1350 (90) 496 (87) 410 (85) 2237 (85) 867 (80) 2809 (76) 3113 (75) 1759 (74) 2932 (71) 179 (70) 2612 (68) 2404 (68) 1536 (66) 3855 (63) 1987 (63) 3271 (62) 3529 (60) 354 (57) 3962 (57) 4018 (56) 980 (55) 2350 (55) 4292 (55) 2757 (53) 116 (52) 2152 (51) 1833 (51) 1125 (50) 582 (49) 3187 (49) 4101 (49) 2679 (48) 1305 (46) 4379 (46) 2542 (44) 1251 (44) 3486 (43) 1699 (40) 2503 (35) 946 (34) 4346 (34) 2472 (31) 3922 (31) 1505 (30) 2066 (29) 3785 (29) 3333 (28) 2322 (28) 2586 (26) 1459 (25) 2130 (23) 846 (22) 3663 (22) 2203 (21) 1483 (21) 3621 (20) 1440 (20) 2901 (19) 3235 (19) 1219 (19) 4426 (19) 3253 (18) 2049 (18) 4275 (18) 3603 (17) 4073 (17) 1175 (15) 3004 (15) 3364 (15) 102 (14) 1202 (14) 3649 (14) 3813 (14) 2726 (13) 2109 (13) 4089 (13) 2920 (11) 4450 (11) 2095 (11) 1977 (11) 3589 (10) 168 (10) 2745 (10) 722 (10) 835 (10) 2892 (10) 2121 (10) 252 (10) 1746 (10) 2884 (9) 5 (8) 1192 (8) 3826 (8) 1243 (8) 3847 (8) 1738 (8) 4268 (8) 4159 (7) 3481 (6) 3476 (6) 736 (5) 2232 (5) 2105 (5) 3837 (5) 1298 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Input 116 subtree files and 92 loci files. Total number of potential alignments: 10672.  
Sub-sampling 1000 alignments from 10672 alignments.  
Remaining 1000 alignments. Deleted 134 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/subtree_update/p__Patescibacteria_100
```
  
  Runtime: 22631.34 seconds
[Subtree update log](loop_1/subtree_update/p__Patescibacteria_100.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 397 | LG |
| 361 | Q.YEAST |
| 133 | Q.PFAM |
| 76 | Q.INSECT |
| 32 | Q.PLANT |
| 1 | MTART |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/subtree_update/p__Patescibacteria_100.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/subtree_update/p__Patescibacteria_100.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/model_update/p__Patescibacteria_100
```
  
  Runtime: 48406.67 seconds
[Model update log](loop_1/model_update/p__Patescibacteria_100.iqtree)  
BIC of the new model: 20008873.5758  
Likelihood of the new model: -9581856.0636  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_100_1)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_100_1  
![Model bubble plot](loop_1/p__Patescibacteria_100_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_100/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_100/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/tree_update/p__Patescibacteria_100_1.treefile
```
  
  Runtime: 18248.72 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_100/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_100/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_100/loop_1/tree_update/p__Patescibacteria_100_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_100/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 2078  
Normalized RF distance: 0.2329  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1413.951895367  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9930425226109719  
Euclidean distance: 0.6335589162788786  
Time usage for Loop_1: 89613.88 seconds (24.89 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_100_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_100/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/tree_update/p__Patescibacteria_100_1.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/test_model/p__Patescibacteria_100_test_concat
```
  
  Runtime: 24728.00 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_100_1+I+G4 | -15057829.540 | 30192711.438 |
| p__Patescibacteria_100_1+F+I+G4 | -15081807.390 | 30240831.097 |
| Q.YEAST+I+G4 | -15109825.820 | 30296703.998 |
| LG+F+I+G4 | -15117414.120 | 30312044.557 |
| Q.PFAM+F+I+G4 | -15120743.610 | 30318703.537 |
| Q.YEAST+F+I+G4 | -15141316.430 | 30359849.177 |
| LG+I+G4 | -15142961.600 | 30362975.558 |
| Q.PFAM+I+G4 | -15143344.380 | 30363741.118 |
| LG+G4 | -15147611.760 | 30372267.248 |
| Q.INSECT+I+G4 | -15148413.840 | 30373880.038 |
| Q.INSECT+F+I+G4 | -15177955.470 | 30433127.257 |
| LG+I | -16403405.620 | 32883854.968 |
| LG | -16439407.740 | 32955850.579 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_100/loop_1/tree_update/p__Patescibacteria_100_1.treefile -l 5 -u 100 -o ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 125   
Number of taxa after pruning: 4399   
Pruned node IDs (degree): 584 (100) 1042 (98) 279 (97) 3988 (94) 4217 (93) 2160 (93) 1520 (92) 68 (91) 4362 (90) 2680 (89) 4083 (85) 3756 (80) 188 (80) 2324 (78) 3613 (76) 3838 (76) 1380 (75) 2447 (73) 1787 (71) 3126 (71) 3460 (70) 792 (69) 3393 (68) 3913 (66) 727 (63) 2262 (63) 400 (61) 1612 (60) 869 (57) 925 (56) 3339 (55) 14 (55) 1196 (55) 3561 (53) 2551 (53) 4310 (52) 4167 (51) 1934 (50) 2988 (50) 1454 (49) 3196 (47) 2768 (46) 1250 (46) 3082 (45) 1892 (43) 1745 (43) 2107 (43) 1673 (41) 3039 (39) 3242 (36) 2865 (35) 2413 (35) 1163 (34) 2519 (33) 2004 (31) 2903 (29) 1714 (28) 2623 (28) 2815 (25) 996 (25) 3315 (24) 2965 (23) 375 (23) 3279 (22) 549 (22) 168 (21) 2839 (21) 2603 (21) 490 (20) 2659 (20) 3705 (19) 1502 (19) 1296 (19) 471 (18) 2055 (18) 2089 (18) 1146 (18) 980 (17) 1867 (16) 3723 (15) 1350 (15) 524 (15) 683 (15) 3529 (14) 4451 (14) 571 (14) 2038 (13) 267 (13) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 2252 (11) 3549 (10) 3696 (10) 461 (10) 1340 (10) 3305 (10) 2956 (10) 3979 (10) 3688 (9) 705 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 719 (8) 541 (8) 2150 (8) 1139 (8) 517 (7) 2859 (7) 2401 (7) 1030 (7) 3542 (6) 160 (6) 1862 (6) 1857 (6) 697 (6) 861 (6) 1374 (5) 2942 (5) 2899 (5) 2654 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Input 125 subtree files and 92 loci files. Total number of potential alignments: 11500.  
Sub-sampling 1000 alignments from 11500 alignments.  
Remaining 1000 alignments. Deleted 113 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_100_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_100/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/subtree_update/p__Patescibacteria_100
```
  
  Runtime: 12661.20 seconds
[Subtree update log](loop_2/subtree_update/p__Patescibacteria_100.iqtree)  
Best models for iteration 2:  
p__Patescibacteria_100_1  

| Model | Count |
|-------|-------|
| 782 | p__Patescibacteria_100_1 |
| 83 | LG |
| 63 | Q.PFAM |
| 41 | Q.YEAST |
| 31 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/subtree_update/p__Patescibacteria_100.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/subtree_update/p__Patescibacteria_100.treefile --model-joint GTR20+FO --init-model p__Patescibacteria_100_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_100/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/model_update/p__Patescibacteria_100
```
  
  Runtime: 22283.90 seconds
[Model update log](loop_2/model_update/p__Patescibacteria_100.iqtree)  
BIC of the new model: 18170290.6087  
Likelihood of the new model: -8697895.7273  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_100_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_100_2  
![Model bubble plot](loop_2/p__Patescibacteria_100_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_100/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_100/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/tree_update/p__Patescibacteria_100_2.treefile
```
  
  Runtime: 13840.42 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_100/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_100/loop_1/tree_update/p__Patescibacteria_100_1.treefile', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_100/loop_2/tree_update/p__Patescibacteria_100_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_100/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.0025  
Tree 1 branch length: 1413.951895367  
Tree 2 branch length: 1418.430773574  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9996037722633488  
Euclidean distance: 0.15100898874765115  
Time usage for Loop_2: 48922.51 seconds (13.59 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_100/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_100/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_100/loop_2/tree_update/p__Patescibacteria_100_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_100/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2080  
Normalized RF distance: 0.2331  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1418.430773574  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Patescibacteria_100_2):  
Pearson's correlation: 0.9918583899462312  
Euclidean distance: 0.691385598780871  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/tree_update/p__Patescibacteria_100_2.treefile -l 5 -u 100 -o ../Result_rona/formal_test/p__Patescibacteria_100/final_test/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 125   
Number of taxa after pruning: 4399   
Pruned node IDs (degree): 584 (100) 1042 (98) 279 (97) 3988 (94) 4217 (93) 2195 (93) 1520 (92) 68 (91) 4362 (90) 2680 (89) 4083 (85) 3756 (80) 188 (80) 3613 (76) 3838 (76) 1380 (75) 2108 (74) 2447 (73) 1787 (71) 3126 (71) 3460 (70) 792 (69) 3393 (68) 3913 (66) 727 (63) 2297 (63) 400 (61) 1612 (60) 869 (57) 925 (56) 3339 (55) 14 (55) 1196 (55) 3561 (53) 2551 (53) 4310 (52) 4167 (51) 1934 (50) 2988 (50) 1454 (49) 3196 (47) 2768 (46) 1250 (46) 3082 (45) 1892 (43) 1745 (43) 2359 (43) 1673 (41) 3039 (39) 3242 (36) 2865 (35) 2413 (35) 1163 (34) 2519 (33) 2004 (31) 2903 (29) 1714 (28) 2623 (28) 2815 (25) 996 (25) 3315 (24) 2965 (23) 375 (23) 3279 (22) 549 (22) 168 (21) 2839 (21) 2603 (21) 490 (20) 2659 (20) 3705 (19) 1502 (19) 1296 (19) 471 (18) 2055 (18) 2089 (18) 1146 (18) 980 (17) 1867 (16) 3723 (15) 1350 (15) 524 (15) 683 (15) 3529 (14) 4451 (14) 571 (14) 2038 (13) 267 (13) 2182 (12) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 2287 (11) 3549 (10) 3696 (10) 461 (10) 1340 (10) 3305 (10) 2956 (10) 3979 (10) 3688 (9) 705 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 719 (8) 541 (8) 1139 (8) 517 (7) 2859 (7) 2401 (7) 1030 (7) 3542 (6) 160 (6) 1862 (6) 1857 (6) 697 (6) 861 (6) 1374 (5) 2942 (5) 2899 (5) 2654 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_100/final_test/subtrees/summary  
Running sample_alignment...  
Input 125 subtree files and 15 loci files. Total number of potential alignments: 1875.  
Obtained 1689 alignments from all potential alignments.  
Remaining 1689 alignments. Deleted 186 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_100/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_100_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_100/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_100/final_test/p__Patescibacteria_100_test_partition
```
  
  Runtime: 887.23 seconds
Best models for test data:  
p__Patescibacteria_100_2  

| Model | Count |
|-------|-------|
| 1281 | p__Patescibacteria_100_2 |
| 120 | LG |
| 98 | Q.YEAST |
| 95 | Q.PFAM |
| 29 | MTMET |
| 24 | Q.PLANT |
| 24 | MTART |
| 18 | Q.INSECT |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_100_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_100/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_100/loop_2/tree_update/p__Patescibacteria_100_2.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_100/final_test/p__Patescibacteria_100_test_concat
```
  
  Runtime: 3421.47 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_100_2+I+G4 | -15059348.140 | 30195748.638 |
| p__Patescibacteria_100_2+F+I+G4 | -15082343.930 | 30241904.177 |
| Q.YEAST+I+G4 | -15109712.330 | 30296477.018 |
| LG+F+I+G4 | -15117171.480 | 30311559.277 |
| Q.PFAM+F+I+G4 | -15120520.690 | 30318257.697 |
| Q.YEAST+F+I+G4 | -15141121.320 | 30359458.957 |
| LG+I+G4 | -15142773.920 | 30362600.198 |
| Q.PFAM+I+G4 | -15143168.140 | 30363388.638 |
| LG+G4 | -15147430.140 | 30371904.008 |
| Q.INSECT+I+G4 | -15148266.940 | 30373586.238 |
| Q.INSECT+F+I+G4 | -15177716.730 | 30432649.777 |
| Q.PLANT+I+G4 | -15323180.090 | 30723412.538 |
| Q.PLANT+F+I+G4 | -15328276.650 | 30733769.617 |
| MTMET+F+I+G4 | -15476688.850 | 31030594.017 |
| MTART+F+I+G4 | -15627732.800 | 31332681.917 |
| MTMET+I+G4 | -15907825.170 | 31892702.698 |
| MTART+I+G4 | -16106420.580 | 32289893.518 |
| LG+I | -16403158.110 | 32883359.948 |
| LG | -16439157.790 | 32955350.679 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Patescibacteria_100/trained_models/trained_model.nex ../Result_rona/formal_test/p__Patescibacteria_100/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 168242.84 seconds (46.73 h)  
