## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Patescibacteria_50  
  Taxa name: p__Patescibacteria  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 50  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Abstract alingment of selected taxa scale in training set:  
Running sample_alignment...  
Discarded 8 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_50/select_id.txt. Sampling sequences for 92 loci.  
Number of input species: 4465  
Remaining 92 alignments. Deleted 0 alignments.  
Abstract alingment of selected taxa scale in testing set:  
Running sample_alignment...  
Discarded 5 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_50/select_id.txt. Sampling sequences for 15 loci.  
Number of input species: 4465  
Remaining 15 alignments. Deleted 0 alignments.  
Concatenating training loci...  
Concatenating testing loci...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_50/ref_tree.tre -l 5 -u 50 -o ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 187   
Number of taxa after pruning: 4282   
Pruned node IDs (degree): 1125 (50) 181 (50) 292 (50) 3865 (50) 117 (49) 582 (49) 3187 (49) 359 (49) 3695 (49) 4101 (49) 4020 (49) 4198 (49) 2944 (48) 25 (48) 2679 (48) 3379 (48) 1649 (48) 1367 (48) 3141 (47) 3031 (47) 655 (47) 1541 (47) 1784 (47) 1079 (46) 1305 (46) 4379 (46) 1925 (46) 2153 (45) 3427 (45) 2542 (44) 1251 (44) 3486 (43) 2238 (43) 1841 (43) 3966 (43) 982 (42) 3272 (42) 2280 (42) 3744 (42) 756 (40) 504 (40) 1699 (40) 2811 (39) 871 (39) 2641 (39) 1035 (38) 2354 (38) 2503 (35) 2436 (35) 3554 (34) 946 (34) 2776 (34) 2007 (34) 4346 (34) 1603 (33) 4293 (33) 428 (32) 2472 (31) 3922 (31) 3077 (30) 1505 (30) 74 (29) 2613 (29) 543 (29) 2066 (29) 3785 (29) 3333 (28) 3114 (28) 2322 (28) 1888 (28) 2586 (26) 2849 (25) 1459 (25) 2130 (23) 846 (22) 459 (22) 3663 (22) 4325 (22) 4246 (22) 2203 (21) 262 (21) 1483 (21) 3535 (20) 3621 (20) 3313 (20) 1440 (20) 2901 (19) 2758 (19) 795 (19) 3235 (19) 1219 (19) 4426 (19) 3253 (18) 230 (18) 2419 (18) 2049 (18) 4275 (18) 3603 (17) 4073 (17) 1991 (17) 1414 (17) 1760 (16) 1175 (15) 3004 (15) 412 (15) 909 (15) 3364 (15) 1587 (15) 102 (14) 821 (14) 1202 (14) 933 (14) 640 (14) 3649 (14) 2391 (14) 3813 (14) 2726 (13) 2109 (13) 2405 (13) 1636 (13) 4089 (13) 1023 (12) 2991 (12) 2873 (12) 2920 (11) 2933 (11) 4450 (11) 923 (11) 2095 (11) 1977 (11) 3589 (10) 168 (10) 2745 (10) 722 (10) 743 (10) 835 (10) 2892 (10) 15 (10) 2121 (10) 252 (10) 709 (10) 1746 (10) 4178 (10) 2884 (9) 486 (9) 4008 (9) 4190 (9) 5 (8) 1192 (8) 3021 (8) 575 (8) 3826 (8) 1243 (8) 3847 (8) 1738 (8) 1834 (8) 1430 (8) 2040 (8) 1918 (8) 4268 (8) 480 (7) 348 (7) 3689 (7) 1778 (7) 4159 (7) 1361 (7) 1074 (6) 813 (6) 2197 (6) 3481 (6) 3106 (6) 3476 (6) 284 (6) 3471 (6) 3858 (6) 736 (5) 718 (5) 2232 (5) 2105 (5) 571 (5) 3837 (5) 344 (5) 705 (5) 701 (5) 1298 (5) 1351 (5) 1971 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Input 187 subtree files and 92 loci files. Total number of potential alignments: 17204.  
Sub-sampling 1000 alignments from 17204 alignments.  
Remaining 1000 alignments. Deleted 159 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/subtree_update/p__Patescibacteria_50
```
  
  Runtime: 4812.53 seconds
[Subtree update log](loop_1/subtree_update/p__Patescibacteria_50.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 397 | LG |
| 340 | Q.YEAST |
| 132 | Q.PFAM |
| 90 | Q.INSECT |
| 41 | Q.PLANT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/subtree_update/p__Patescibacteria_50.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/subtree_update/p__Patescibacteria_50.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/model_update/p__Patescibacteria_50
```
  
  Runtime: 28898.07 seconds
[Model update log](loop_1/model_update/p__Patescibacteria_50.iqtree)  
BIC of the new model: 12249784.4639  
Likelihood of the new model: -5872939.799  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_50_1)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_50_1  
![Model bubble plot](loop_1/p__Patescibacteria_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_50/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_50/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/tree_update/p__Patescibacteria_50_1.treefile
```
  
  Runtime: 24935.04 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_50/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_50/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_50/loop_1/tree_update/p__Patescibacteria_50_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 2090  
Normalized RF distance: 0.2342  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1400.987362423  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9940411908648592  
Euclidean distance: 0.5759295628880227  
Time usage for Loop_1: 59089.69 seconds (16.41 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_50_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_50/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/tree_update/p__Patescibacteria_50_1.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/test_model/p__Patescibacteria_50_test_concat
```
  
  Runtime: 8533.90 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_50_1+I+G4 | -15065208.940 | 30207470.238 |
| p__Patescibacteria_50_1+F+I+G4 | -15079605.790 | 30236427.897 |
| Q.YEAST+I+G4 | -15109755.110 | 30296562.578 |
| LG+F+I+G4 | -15117145.300 | 30311506.917 |
| Q.PFAM+F+I+G4 | -15120505.870 | 30318228.057 |
| Q.YEAST+F+I+G4 | -15141119.610 | 30359455.537 |
| LG+I+G4 | -15142771.910 | 30362596.178 |
| Q.PFAM+I+G4 | -15143173.470 | 30363399.298 |
| LG+G4 | -15147435.080 | 30371913.888 |
| Q.INSECT+I+G4 | -15148290.990 | 30373634.338 |
| Q.INSECT+F+I+G4 | -15177690.150 | 30432596.617 |
| LG+I | -16403075.100 | 32883193.928 |
| LG | -16439074.230 | 32955183.559 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_50/loop_1/tree_update/p__Patescibacteria_50_1.treefile -l 5 -u 50 -o ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 188   
Number of taxa after pruning: 4289   
Pruned node IDs (degree): 1934 (50) 2988 (50) 3306 (50) 3759 (50) 3996 (50) 739 (50) 1073 (50) 1454 (49) 3919 (49) 813 (49) 873 (49) 1613 (48) 4314 (48) 17 (48) 4374 (48) 601 (48) 2441 (48) 2713 (48) 1408 (47) 1531 (47) 3082 (47) 4226 (47) 2552 (47) 2175 (47) 3460 (46) 113 (46) 2768 (46) 1251 (46) 2266 (46) 3198 (45) 2332 (45) 4174 (44) 1892 (43) 1745 (43) 2107 (43) 931 (43) 3129 (42) 3855 (42) 656 (42) 1673 (41) 1798 (41) 4127 (40) 3615 (39) 3039 (39) 216 (39) 329 (39) 3505 (38) 69 (38) 3400 (38) 3242 (36) 2865 (35) 3580 (34) 4094 (34) 1164 (34) 407 (33) 1198 (33) 2505 (32) 2004 (31) 1577 (30) 4423 (29) 2903 (29) 3170 (29) 1714 (28) 1381 (28) 3808 (28) 2623 (28) 2229 (28) 4055 (27) 191 (26) 3653 (25) 997 (25) 2815 (25) 2412 (25) 2689 (25) 3368 (24) 375 (23) 2965 (23) 3279 (22) 559 (22) 1230 (22) 1051 (22) 168 (21) 2839 (21) 2603 (21) 439 (20) 490 (20) 310 (20) 794 (20) 2659 (20) 3705 (19) 3562 (19) 1502 (19) 1838 (19) 540 (19) 4272 (19) 1297 (19) 471 (18) 2055 (18) 581 (18) 2089 (18) 1147 (18) 981 (17) 1867 (16) 2536 (16) 2151 (16) 3723 (15) 1350 (15) 286 (15) 3839 (15) 524 (15) 4451 (14) 3437 (14) 254 (14) 2038 (13) 3355 (13) 267 (13) 1660 (12) 3677 (12) 3896 (12) 2390 (12) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 2318 (11) 1130 (11) 3549 (10) 3696 (10) 461 (10) 1340 (10) 3450 (10) 2956 (10) 4364 (10) 3979 (10) 4294 (10) 3688 (9) 705 (9) 1789 (9) 3970 (9) 973 (9) 1122 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 1521 (8) 302 (8) 719 (8) 4166 (8) 2498 (8) 2491 (8) 2168 (8) 1140 (8) 2381 (8) 2259 (8) 4083 (7) 517 (7) 3907 (7) 2859 (7) 648 (7) 2401 (7) 1031 (7) 2760 (7) 3542 (6) 160 (6) 1862 (6) 1606 (6) 1857 (6) 108 (6) 367 (6) 697 (6) 732 (6) 862 (6) 2598 (6) 2376 (6) 402 (5) 1374 (5) 3392 (5) 64 (5) 2942 (5) 4303 (5) 2899 (5) 4290 (5) 4048 (5) 2654 (5) 2681 (5) 2312 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Input 188 subtree files and 92 loci files. Total number of potential alignments: 17296.  
Sub-sampling 1000 alignments from 17296 alignments.  
Remaining 1000 alignments. Deleted 151 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_50_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_50/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/subtree_update/p__Patescibacteria_50
```
  
  Runtime: 2063.86 seconds
[Subtree update log](loop_2/subtree_update/p__Patescibacteria_50.iqtree)  
Best models for iteration 2:  
p__Patescibacteria_50_1  

| Model | Count |
|-------|-------|
| 798 | p__Patescibacteria_50_1 |
| 73 | LG |
| 62 | Q.PFAM |
| 38 | Q.YEAST |
| 29 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/subtree_update/p__Patescibacteria_50.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/subtree_update/p__Patescibacteria_50.treefile --model-joint GTR20+FO --init-model p__Patescibacteria_50_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_50/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/model_update/p__Patescibacteria_50
```
  
  Runtime: 5976.28 seconds
[Model update log](loop_2/model_update/p__Patescibacteria_50.iqtree)  
BIC of the new model: 11980644.1117  
Likelihood of the new model: -5739547.9102  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_50_2  
![Model bubble plot](loop_2/p__Patescibacteria_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_50/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_50/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/tree_update/p__Patescibacteria_50_2.treefile
```
  
  Runtime: 14508.48 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_50/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_50/loop_1/tree_update/p__Patescibacteria_50_1.treefile', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_50/loop_2/tree_update/p__Patescibacteria_50_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 52  
Normalized RF distance: 0.0058  
Tree 1 branch length: 1400.987362423  
Tree 2 branch length: 1411.393333665  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997140613089203  
Euclidean distance: 0.12650075394716584  
Time usage for Loop_2: 22852.34 seconds (6.35 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_50/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_50/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_50/loop_2/tree_update/p__Patescibacteria_50_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2100  
Normalized RF distance: 0.2353  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1411.393333665  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Patescibacteria_50_2):  
Pearson's correlation: 0.9932041649294274  
Euclidean distance: 0.6192009653753365  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/tree_update/p__Patescibacteria_50_2.treefile -l 5 -u 50 -o ../Result_rona/formal_test/p__Patescibacteria_50/final_test/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 189   
Number of taxa after pruning: 4285   
Pruned node IDs (degree): 1934 (50) 2988 (50) 3306 (50) 3759 (50) 3996 (50) 739 (50) 1073 (50) 1454 (49) 3919 (49) 813 (49) 873 (49) 1613 (48) 4314 (48) 17 (48) 4374 (48) 587 (48) 2441 (48) 2713 (48) 1408 (47) 1531 (47) 3082 (47) 4226 (47) 2552 (47) 2350 (47) 3460 (46) 113 (46) 2768 (46) 1251 (46) 2200 (46) 3198 (45) 2266 (45) 4174 (44) 1892 (43) 1745 (43) 2107 (43) 931 (43) 3129 (42) 3855 (42) 642 (42) 1673 (41) 1798 (41) 4120 (40) 3615 (39) 3039 (39) 216 (39) 329 (39) 3505 (38) 69 (38) 3400 (38) 3242 (36) 2865 (35) 3580 (34) 4087 (34) 1164 (34) 407 (33) 1198 (33) 2505 (32) 2004 (31) 1577 (30) 4423 (29) 2903 (29) 3170 (29) 1714 (28) 1381 (28) 3808 (28) 2623 (28) 2163 (28) 4055 (27) 191 (26) 3653 (25) 997 (25) 2815 (25) 2412 (25) 2689 (25) 3368 (24) 375 (23) 2965 (23) 3279 (22) 549 (22) 1230 (22) 1051 (22) 168 (21) 2839 (21) 2603 (21) 439 (20) 490 (20) 310 (20) 794 (20) 2659 (20) 3705 (19) 3562 (19) 1502 (19) 1838 (19) 4272 (19) 1297 (19) 471 (18) 2055 (18) 2089 (18) 1147 (18) 981 (17) 1867 (16) 2536 (16) 2326 (16) 3723 (15) 1350 (15) 286 (15) 3839 (15) 524 (15) 683 (15) 4451 (14) 3437 (14) 254 (14) 571 (14) 2038 (13) 3355 (13) 267 (13) 1660 (12) 3677 (12) 3896 (12) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 2252 (11) 1130 (11) 3549 (10) 3696 (10) 461 (10) 1340 (10) 3450 (10) 2956 (10) 4364 (10) 3979 (10) 4294 (10) 3688 (9) 705 (9) 1789 (9) 3970 (9) 973 (9) 1122 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 1521 (8) 302 (8) 719 (8) 4159 (8) 541 (8) 2150 (8) 2498 (8) 2491 (8) 1140 (8) 2315 (8) 2343 (8) 2193 (8) 517 (7) 4168 (7) 3907 (7) 2859 (7) 634 (7) 2401 (7) 1031 (7) 2760 (7) 3542 (6) 160 (6) 1862 (6) 1606 (6) 1857 (6) 108 (6) 367 (6) 697 (6) 732 (6) 862 (6) 2598 (6) 2310 (6) 402 (5) 1374 (5) 3392 (5) 64 (5) 2942 (5) 4303 (5) 2899 (5) 4290 (5) 4048 (5) 2654 (5) 2681 (5) 2246 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_50/final_test/subtrees/summary  
Running sample_alignment...  
Input 189 subtree files and 15 loci files. Total number of potential alignments: 2835.  
Obtained 2528 alignments from all potential alignments.  
Remaining 2528 alignments. Deleted 307 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_50_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_50/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_50/final_test/p__Patescibacteria_50_test_partition
```
  
  Runtime: 2557.38 seconds
Best models for test data:  
p__Patescibacteria_50_2  

| Model | Count |
|-------|-------|
| 2017 | p__Patescibacteria_50_2 |
| 141 | Q.YEAST |
| 107 | Q.PFAM |
| 107 | LG |
| 51 | Q.PLANT |
| 44 | MTART |
| 34 | MTMET |
| 27 | Q.INSECT |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART,p__Patescibacteria_50_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_50/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_50/loop_2/tree_update/p__Patescibacteria_50_2.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_50/final_test/p__Patescibacteria_50_test_concat
```
  
  Runtime: 25792.55 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_50_2+I+G4 | -15069318.760 | 30215689.878 |
| p__Patescibacteria_50_2+F+I+G4 | -15083998.710 | 30245213.737 |
| Q.YEAST+I+G4 | -15110157.300 | 30297366.958 |
| LG+F+I+G4 | -15117566.930 | 30312350.177 |
| Q.PFAM+F+I+G4 | -15120922.220 | 30319060.757 |
| Q.YEAST+F+I+G4 | -15141519.250 | 30360254.817 |
| LG+I+G4 | -15143186.340 | 30363425.038 |
| Q.PFAM+I+G4 | -15143580.630 | 30364213.618 |
| LG+G4 | -15147841.910 | 30372727.548 |
| Q.INSECT+I+G4 | -15148698.060 | 30374448.478 |
| Q.INSECT+F+I+G4 | -15178091.520 | 30433399.357 |
| Q.PLANT+I+G4 | -15323604.030 | 30724260.418 |
| Q.PLANT+F+I+G4 | -15328680.090 | 30734576.497 |
| MTMET+F+I+G4 | -15477122.370 | 31031461.057 |
| MTART+F+I+G4 | -15628108.340 | 31333432.997 |
| MTMET+I+G4 | -15908327.700 | 31893707.758 |
| MTART+I+G4 | -16106833.960 | 32290720.278 |
| LG+I | -16403614.410 | 32884272.548 |
| LG | -16439615.800 | 32956266.699 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Patescibacteria_50/trained_models/trained_model.nex ../Result_rona/formal_test/p__Patescibacteria_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 119853.75 seconds (33.29 h)  
