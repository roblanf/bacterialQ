## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Patescibacteria_150  
  Taxa name: p__Patescibacteria  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 150  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Abstract alingment of selected taxa scale in training set:  
Running sample_alignment...  
Discarded 8 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_150/select_id.txt. Sampling sequences for 92 loci.  
Number of input species: 4465  
Remaining 92 alignments. Deleted 0 alignments.  
Abstract alingment of selected taxa scale in testing set:  
Running sample_alignment...  
Discarded 5 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_150/select_id.txt. Sampling sequences for 15 loci.  
Number of input species: 4465  
Remaining 15 alignments. Deleted 0 alignments.  
Concatenating training loci...  
Concatenating testing loci...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_150/ref_tree.tre -l 5 -u 150 -o ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 87   
Number of taxa after pruning: 4400   
Pruned node IDs (degree): 3952 (150) 2754 (148) 979 (146) 834 (146) 3111 (143) 3684 (143) 2585 (142) 1303 (138) 1601 (138) 495 (136) 3360 (127) 4169 (124) 2349 (123) 4 (112) 251 (104) 1884 (104) 742 (93) 630 (93) 3020 (92) 410 (85) 2237 (85) 1759 (74) 2932 (71) 179 (70) 1536 (66) 3855 (63) 1987 (63) 3271 (62) 3529 (60) 354 (57) 4292 (55) 116 (52) 2152 (51) 1833 (51) 1125 (50) 4101 (49) 4379 (46) 2542 (44) 1251 (44) 3486 (43) 2503 (35) 4346 (34) 2472 (31) 3922 (31) 1505 (30) 2066 (29) 3333 (28) 2322 (28) 1459 (25) 2130 (23) 3663 (22) 2203 (21) 1483 (21) 3621 (20) 1440 (20) 2901 (19) 1219 (19) 4426 (19) 3253 (18) 2049 (18) 3603 (17) 1175 (15) 3004 (15) 1202 (14) 3649 (14) 2726 (13) 2109 (13) 2920 (11) 4450 (11) 2095 (11) 3589 (10) 168 (10) 2745 (10) 722 (10) 2121 (10) 1746 (10) 1192 (8) 3826 (8) 1243 (8) 3847 (8) 1738 (8) 4159 (7) 736 (5) 2232 (5) 2105 (5) 3837 (5) 1298 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Input 87 subtree files and 92 loci files. Total number of potential alignments: 8004.  
Sub-sampling 1000 alignments from 8004 alignments.  
Remaining 1000 alignments. Deleted 124 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/subtree_update/p__Patescibacteria_150
```
  
  Runtime: 52670.40 seconds
[Subtree update log](loop_1/subtree_update/p__Patescibacteria_150.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 361 | Q.YEAST |
| 340 | LG |
| 181 | Q.PFAM |
| 100 | Q.INSECT |
| 17 | Q.PLANT |
| 1 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/subtree_update/p__Patescibacteria_150.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/subtree_update/p__Patescibacteria_150.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/model_update/p__Patescibacteria_150
```
  
  Runtime: 52731.27 seconds
[Model update log](loop_1/model_update/p__Patescibacteria_150.iqtree)  
BIC of the new model: 26186316.6336  
Likelihood of the new model: -12514654.7464  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_150_1)  
Model set for next iteration: Q.YEAST,LG,Q.PFAM,Q.INSECT,p__Patescibacteria_150_1  
![Model bubble plot](loop_1/p__Patescibacteria_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_150/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_150/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile
```
  
  Runtime: 18732.52 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_150/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_150/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 2092  
Normalized RF distance: 0.2344  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1410.674845321  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.994578621958267  
Euclidean distance: 0.5566050488197827  
Time usage for Loop_1: 124453.57 seconds (34.57 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_150/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,LG,Q.PFAM,Q.INSECT,p__Patescibacteria_150_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_150/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/test_model/p__Patescibacteria_150_test_concat
```
  
  Runtime: 13282.25 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_150_1+I+G4 | -15057702.680 | 30192457.718 |
| p__Patescibacteria_150_1+F+I+G4 | -15087990.740 | 30253197.797 |
| Q.YEAST+I+G4 | -15110197.540 | 30297447.438 |
| Q.YEAST+G4 | -15114825.560 | 30306694.848 |
| LG+F+I+G4 | -15117885.090 | 30312986.497 |
| Q.PFAM+F+I+G4 | -15121197.490 | 30319611.297 |
| Q.YEAST+F+I+G4 | -15141751.950 | 30360720.217 |
| LG+I+G4 | -15143415.800 | 30363883.958 |
| Q.PFAM+I+G4 | -15143781.620 | 30364615.598 |
| Q.INSECT+I+G4 | -15148784.590 | 30374621.538 |
| Q.INSECT+F+I+G4 | -15178368.470 | 30433953.257 |
| Q.YEAST+I | -16456581.210 | 32990206.148 |
| Q.YEAST | -16492749.210 | 33062533.519 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile -l 5 -u 150 -o ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 95   
Number of taxa after pruning: 4403   
Pruned node IDs (degree): 3558 (148) 1373 (148) 3314 (147) 12 (147) 540 (144) 3837 (142) 2411 (141) 2678 (138) 4082 (136) 867 (130) 1725 (127) 1040 (124) 3081 (116) 166 (114) 4361 (104) 3978 (104) 2159 (104) 279 (97) 4217 (93) 1520 (92) 3756 (80) 2324 (78) 3460 (70) 792 (69) 727 (63) 2262 (63) 400 (61) 1612 (60) 1196 (55) 2551 (53) 1674 (52) 4310 (52) 1934 (50) 2988 (50) 3196 (47) 1250 (46) 1892 (43) 2107 (43) 3039 (39) 3242 (36) 2865 (35) 1163 (34) 2004 (31) 2903 (29) 1851 (28) 2623 (28) 2815 (25) 996 (25) 2965 (23) 375 (23) 3279 (22) 2839 (21) 2603 (21) 490 (20) 2659 (20) 3705 (19) 1296 (19) 471 (18) 2055 (18) 2089 (18) 3723 (15) 1350 (15) 524 (15) 683 (15) 3529 (14) 2038 (13) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 3549 (10) 461 (10) 1340 (10) 3305 (10) 2956 (10) 705 (9) 1996 (8) 1365 (8) 3746 (8) 719 (8) 2150 (8) 3738 (7) 517 (7) 2859 (7) 2401 (7) 1030 (7) 3542 (6) 160 (6) 697 (6) 861 (6) 1878 (5) 2942 (5) 2899 (5) 2654 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Input 95 subtree files and 92 loci files. Total number of potential alignments: 8740.  
Sub-sampling 1000 alignments from 8740 alignments.  
Remaining 1000 alignments. Deleted 120 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.PFAM,Q.INSECT,p__Patescibacteria_150_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_150/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/subtree_update/p__Patescibacteria_150
```
  
  Runtime: 14158.77 seconds
[Subtree update log](loop_2/subtree_update/p__Patescibacteria_150.iqtree)  
Best models for iteration 2:  
p__Patescibacteria_150_1  

| Model | Count |
|-------|-------|
| 783 | p__Patescibacteria_150_1 |
| 103 | LG |
| 48 | Q.PFAM |
| 41 | Q.YEAST |
| 25 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/subtree_update/p__Patescibacteria_150.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/subtree_update/p__Patescibacteria_150.treefile --model-joint GTR20+FO --init-model p__Patescibacteria_150_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_150/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/model_update/p__Patescibacteria_150
```
  
  Runtime: 20932.10 seconds
[Model update log](loop_2/model_update/p__Patescibacteria_150.iqtree)  
BIC of the new model: 23904753.8739  
Likelihood of the new model: -11427818.1869  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_150_2  
![Model bubble plot](loop_2/p__Patescibacteria_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_150/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_150/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile
```
  
  Runtime: 11066.13 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_150/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 44  
Normalized RF distance: 0.0049  
Tree 1 branch length: 1410.674845321  
Tree 2 branch length: 1421.650020385  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999756884222773  
Euclidean distance: 0.11735179831476904  
Time usage for Loop_2: 46282.11 seconds (12.86 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_150/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_150/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2086  
Normalized RF distance: 0.2338  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1421.650020385  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Patescibacteria_150_2):  
Pearson's correlation: 0.9940433282868423  
Euclidean distance: 0.5851757854149744  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile -l 5 -u 150 -o ../Result_rona/formal_test/p__Patescibacteria_150/final_test/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 95   
Number of taxa after pruning: 4404   
Pruned node IDs (degree): 4285 (148) 2100 (148) 4041 (147) 739 (147) 1267 (144) 98 (142) 3138 (141) 3405 (138) 343 (136) 1594 (130) 2452 (127) 1767 (124) 3889 (116) 893 (114) 622 (104) 239 (104) 2886 (104) 1006 (97) 478 (93) 2247 (92) 17 (80) 3051 (78) 4187 (70) 1519 (69) 1454 (63) 2989 (63) 1127 (61) 2339 (60) 1923 (55) 3278 (53) 2401 (52) 571 (52) 2661 (50) 3715 (50) 3841 (49) 1977 (46) 2619 (43) 2834 (43) 3766 (39) 3592 (35) 3807 (34) 1890 (34) 2731 (31) 3630 (29) 2578 (28) 3350 (28) 3542 (25) 1723 (25) 3692 (23) 1102 (23) 4006 (22) 3566 (21) 3330 (21) 1217 (20) 3386 (20) 4432 (19) 2023 (19) 1198 (18) 2782 (18) 2816 (18) 4450 (15) 2077 (15) 1251 (15) 1410 (15) 4256 (14) 2765 (13) 2711 (11) 2609 (11) 2046 (11) 3673 (11) 3659 (11) 4276 (10) 1188 (10) 2067 (10) 4032 (10) 3683 (10) 1432 (9) 2723 (8) 725 (8) 2092 (8) 7 (8) 1446 (8) 2877 (8) 1244 (7) 3586 (7) 3128 (7) 1757 (7) 4269 (6) 887 (6) 1424 (6) 1588 (6) 2605 (5) 3669 (5) 3626 (5) 3381 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_150/final_test/subtrees/summary  
Running sample_alignment...  
Input 95 subtree files and 15 loci files. Total number of potential alignments: 1425.  
Obtained 1279 alignments from all potential alignments.  
Remaining 1279 alignments. Deleted 146 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_150_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_150/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_150/final_test/p__Patescibacteria_150_test_partition
```
  
  Runtime: 647.43 seconds
Best models for test data:  
p__Patescibacteria_150_2  

| Model | Count |
|-------|-------|
| 956 | p__Patescibacteria_150_2 |
| 106 | LG |
| 79 | Q.PFAM |
| 74 | Q.YEAST |
| 20 | MTMET |
| 18 | Q.PLANT |
| 16 | MTART |
| 10 | Q.INSECT |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_150_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_150/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_150/final_test/p__Patescibacteria_150_test_concat
```
  
  Runtime: 3015.42 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_150_2+I+G4 | -15056899.720 | 30190851.798 |
| p__Patescibacteria_150_2+F+I+G4 | -15085944.560 | 30249105.437 |
| Q.YEAST+I+G4 | -15110311.320 | 30297674.998 |
| LG+F+I+G4 | -15117986.600 | 30313189.517 |
| Q.PFAM+F+I+G4 | -15121278.640 | 30319773.597 |
| Q.YEAST+F+I+G4 | -15141855.810 | 30360927.937 |
| LG+I+G4 | -15143525.910 | 30364104.178 |
| Q.PFAM+I+G4 | -15143879.760 | 30364811.878 |
| LG+G4 | -15148165.140 | 30373374.008 |
| Q.INSECT+I+G4 | -15148902.650 | 30374857.658 |
| Q.INSECT+F+I+G4 | -15178464.560 | 30434145.437 |
| Q.PLANT+I+G4 | -15323930.840 | 30724914.038 |
| Q.PLANT+F+I+G4 | -15329086.710 | 30735389.737 |
| MTMET+F+I+G4 | -15477640.400 | 31032497.117 |
| MTART+F+I+G4 | -15628468.030 | 31334152.377 |
| MTMET+I+G4 | -15908500.430 | 31894053.218 |
| MTART+I+G4 | -16106930.040 | 32290912.438 |
| LG+I | -16403907.030 | 32884857.788 |
| LG | -16439911.690 | 32956858.479 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Patescibacteria_150/trained_models/trained_model.nex ../Result_rona/formal_test/p__Patescibacteria_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 188359.89 seconds (52.32 h)  
