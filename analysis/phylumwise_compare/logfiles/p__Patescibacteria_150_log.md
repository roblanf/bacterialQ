## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Patescibacteria_150  
  Taxa name: p__Patescibacteria  
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
Discarded 8 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Patescibacteria_150/select_id.txt. Sampling sequences for 92 loci.  
Number of input species: 4465  
Remaining 92 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 5 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Patescibacteria_150/select_id.txt. Sampling sequences for 15 loci.  
Number of input species: 4465  
Remaining 15 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Patescibacteria_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Patescibacteria_150/loop_1/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 87   
Number of taxa after pruning: 4400   
Pruned node IDs (degree): 1125 (50) 1175 (15) 979 (146) 3529 (60) 4 (112) 736 (5) 2920 (11) 3589 (10) 116 (52) 1192 (8) 2901 (19) 3486 (43) 168 (10) 742 (93) 834 (146) 2745 (10) 2754 (148) 2932 (71) 3603 (17) 722 (10) 2503 (35) 179 (70) 1202 (14) 2203 (21) 3004 (15) 3271 (62) 3621 (20) 2152 (51) 3253 (18) 3333 (28) 3360 (127) 4450 (11) 410 (85) 495 (136) 630 (93) 2130 (23) 2472 (31) 3020 (92) 3111 (143) 251 (104) 354 (57) 2121 (10) 2726 (13) 1219 (19) 2542 (44) 2585 (142) 2109 (13) 2232 (5) 2105 (5) 2237 (85) 2095 (11) 2322 (28) 2349 (123) 3826 (8) 3837 (5) 3649 (14) 2066 (29) 3663 (22) 3684 (143) 1243 (8) 1251 (44) 3847 (8) 3855 (63) 1483 (21) 1459 (25) 1505 (30) 1746 (10) 1298 (5) 1738 (8) 4101 (49) 1303 (138) 1440 (20) 1536 (66) 1601 (138) 2049 (18) 3922 (31) 3952 (150) 4426 (19) 1759 (74) 1833 (51) 1884 (104) 1987 (63) 4159 (7) 4379 (46) 4346 (34) 4169 (124) 4292 (55)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Patescibacteria_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 87 subtree files and 92 loci files. Total number of potential alignments: 8004.  
Sub-sampling 1000 alignments from 8004 alignments.  
Could not obtain the requested 1000 alignments. Keeping 960 alignments.  
Remaining 960 alignments. Deleted 140 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Patescibacteria_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Patescibacteria_150/loop_1/subtree_update/p__Patescibacteria_150
```
  
  Runtime: 105909.16 seconds
[Subtree update log](loop_1/subtree_update/p__Patescibacteria_150.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 377 | LG |
| 338 | Q.YEAST |
| 138 | Q.PFAM |
| 105 | Q.INSECT |
| 2 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Patescibacteria_150/loop_1/subtree_update/p__Patescibacteria_150.best_scheme.nex -te ../Result/safe_phyla/p__Patescibacteria_150/loop_1/subtree_update/p__Patescibacteria_150.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Patescibacteria_150/loop_1/model_update/p__Patescibacteria_150
```
  
  Runtime: 158052.52 seconds
[Model update log](loop_1/model_update/p__Patescibacteria_150.iqtree)  
BIC of the new model: 23811132.5891  
Likelihood of the new model: -11371163.1496  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_150_1)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_150_1  
![Model bubble plot](loop_1/p__Patescibacteria_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Patescibacteria_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Patescibacteria_150/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Patescibacteria_150/ref_tree.tre ../Result/safe_phyla/p__Patescibacteria_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile
```
  
  Runtime: 66365.44 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Patescibacteria_150/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Patescibacteria_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Patescibacteria_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 2078  
Normalized RF distance: 0.2329  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1434.730060389  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9907136880704035  
Euclidean distance: 0.7465817386222448  
Time usage for Loop_1: 331238.34 seconds (92.01 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Patescibacteria_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_150_1 -mdef ../Result/safe_phyla/p__Patescibacteria_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile -pre ../Result/safe_phyla/p__Patescibacteria_150/loop_1/test_model/p__Patescibacteria_150_test_concat
```
  
  Runtime: 15626.11 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_150_1+I+G4 | -15058268.350 | 30193857.915 |
| p__Patescibacteria_150_1+F+I+G4 | -15087097.710 | 30251681.167 |
| Q.YEAST+I+G4 | -15113693.680 | 30304708.575 |
| LG+F+I+G4 | -15121140.930 | 30319767.607 |
| Q.PFAM+F+I+G4 | -15124479.760 | 30326445.267 |
| Q.YEAST+F+I+G4 | -15145092.240 | 30367670.227 |
| LG+I+G4 | -15146783.240 | 30370887.695 |
| Q.PFAM+I+G4 | -15147170.620 | 30371662.455 |
| LG+G4 | -15151438.600 | 30380189.756 |
| Q.INSECT+I+G4 | -15152232.230 | 30381785.675 |
| Q.INSECT+F+I+G4 | -15181647.840 | 30440781.427 |
| LG+I | -16407326.950 | 32891966.456 |
| LG | -16443346.650 | 32963997.196 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Patescibacteria_150/loop_2/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 95   
Number of taxa after pruning: 4404   
Pruned node IDs (degree): 3558 (148) 1373 (148) 3314 (147) 12 (147) 540 (144) 3837 (142) 2411 (141) 2678 (138) 4082 (136) 867 (130) 1725 (127) 1040 (124) 3081 (116) 166 (114) 4361 (104) 3978 (104) 2194 (104) 279 (97) 4217 (93) 1520 (92) 3756 (80) 2108 (74) 3460 (70) 792 (69) 727 (63) 2297 (63) 400 (61) 1612 (60) 1196 (55) 2551 (53) 1674 (52) 4310 (52) 1934 (50) 2988 (50) 3196 (47) 1250 (46) 1892 (43) 2359 (43) 3039 (39) 3242 (36) 2865 (35) 1163 (34) 2004 (31) 2903 (29) 1851 (28) 2623 (28) 2815 (25) 996 (25) 2965 (23) 375 (23) 3279 (22) 2839 (21) 2603 (21) 490 (20) 2659 (20) 3705 (19) 1296 (19) 471 (18) 2055 (18) 2089 (18) 3723 (15) 1350 (15) 524 (15) 683 (15) 3529 (14) 2038 (13) 2182 (12) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 3549 (10) 461 (10) 1340 (10) 3305 (10) 2956 (10) 705 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 719 (8) 517 (7) 2859 (7) 2401 (7) 1030 (7) 3542 (6) 160 (6) 697 (6) 861 (6) 1878 (5) 2942 (5) 2899 (5) 2654 (5)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Patescibacteria_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 95 subtree files and 92 loci files. Total number of potential alignments: 8740.  
Sub-sampling 1000 alignments from 8740 alignments.  
Could not obtain the requested 1000 alignments. Keeping 959 alignments.  
Remaining 959 alignments. Deleted 141 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Patescibacteria_150/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_150_1 -mdef ../Result/safe_phyla/p__Patescibacteria_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Patescibacteria_150/loop_2/subtree_update/p__Patescibacteria_150
```
  
  Runtime: 50607.43 seconds
[Subtree update log](loop_2/subtree_update/p__Patescibacteria_150.iqtree)  
Best models for iteration 2:  
p__Patescibacteria_150_1  

| Model | Count |
|-------|-------|
| 730 | p__Patescibacteria_150_1 |
| 99 | LG |
| 65 | Q.PFAM |
| 36 | Q.YEAST |
| 29 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Patescibacteria_150/loop_2/subtree_update/p__Patescibacteria_150.best_scheme.nex -te ../Result/safe_phyla/p__Patescibacteria_150/loop_2/subtree_update/p__Patescibacteria_150.treefile --model-joint GTR20+FO --init-model p__Patescibacteria_150_1 -mdef ../Result/safe_phyla/p__Patescibacteria_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Patescibacteria_150/loop_2/model_update/p__Patescibacteria_150
```
  
  Runtime: 69455.58 seconds
[Model update log](loop_2/model_update/p__Patescibacteria_150.iqtree)  
BIC of the new model: 22686374.5123  
Likelihood of the new model: -10834222.0366  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_150_2  
![Model bubble plot](loop_2/p__Patescibacteria_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Patescibacteria_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Patescibacteria_150/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Patescibacteria_150/ref_tree.tre ../Result/safe_phyla/p__Patescibacteria_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile
```
  
  Runtime: 32752.35 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Patescibacteria_150/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Patescibacteria_150/loop_1/tree_update/p__Patescibacteria_150_1.treefile', tree2_path = '../Result/safe_phyla/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Patescibacteria_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 40  
Normalized RF distance: 0.0045  
Tree 1 branch length: 1434.730060389  
Tree 2 branch length: 1436.03385298  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9996866373222736  
Euclidean distance: 0.1340219495203101  
Time usage for Loop_2: 153083.23 seconds (42.52 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Patescibacteria_150/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Patescibacteria_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Patescibacteria_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2088  
Normalized RF distance: 0.234  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1436.03385298  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Patescibacteria_150_2):  
Pearson's correlation: 0.9914620542613513  
Euclidean distance: 0.7119712405114269  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Patescibacteria_150/final_test/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 95   
Number of taxa after pruning: 4404   
Pruned node IDs (degree): 3558 (148) 1373 (148) 3314 (147) 12 (147) 540 (144) 3837 (142) 2411 (141) 2678 (138) 4082 (136) 867 (130) 1725 (127) 1040 (124) 3081 (116) 166 (114) 4361 (104) 3978 (104) 2159 (104) 279 (97) 4217 (93) 1520 (92) 3756 (80) 2324 (78) 3460 (70) 792 (69) 727 (63) 2262 (63) 400 (61) 1612 (60) 1196 (55) 2551 (53) 1674 (52) 4310 (52) 1934 (50) 2988 (50) 3196 (47) 1250 (46) 1892 (43) 2107 (43) 3039 (39) 3242 (36) 2865 (35) 1163 (34) 2004 (31) 2903 (29) 1851 (28) 2623 (28) 2815 (25) 996 (25) 2965 (23) 375 (23) 3279 (22) 2839 (21) 2603 (21) 490 (20) 2659 (20) 3705 (19) 1296 (19) 471 (18) 2055 (18) 2089 (18) 3723 (15) 1350 (15) 524 (15) 683 (15) 3529 (14) 2038 (13) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 3549 (10) 461 (10) 1340 (10) 3305 (10) 2956 (10) 705 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 719 (8) 2150 (8) 517 (7) 2859 (7) 2401 (7) 1030 (7) 3542 (6) 160 (6) 697 (6) 861 (6) 1878 (5) 2942 (5) 2899 (5) 2654 (5)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Patescibacteria_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 95 subtree files and 15 loci files. Total number of potential alignments: 1425.  
Obtained 1255 alignments from all potential alignments.  
Remaining 1255 alignments. Deleted 170 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Patescibacteria_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_150_2 -mdef ../Result/safe_phyla/p__Patescibacteria_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Patescibacteria_150/final_test/p__Patescibacteria_150_test_partition
```
  
  Runtime: 1721.16 seconds
Best models for test data:  
p__Patescibacteria_150_2  

| Model | Count |
|-------|-------|
| 952 | p__Patescibacteria_150_2 |
| 95 | LG |
| 80 | Q.PFAM |
| 78 | Q.YEAST |
| 19 | MTMET |
| 18 | MTART |
| 13 | Q.INSECT |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Patescibacteria_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_150_2 -mdef ../Result/safe_phyla/p__Patescibacteria_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Patescibacteria_150/loop_2/tree_update/p__Patescibacteria_150_2.treefile -pre ../Result/safe_phyla/p__Patescibacteria_150/final_test/p__Patescibacteria_150_test_concat
```
  
  Runtime: 9148.99 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_150_2+I+G4 | -15060625.410 | 30198572.035 |
| p__Patescibacteria_150_2+F+I+G4 | -15090133.900 | 30257753.547 |
| Q.YEAST+I+G4 | -15113308.210 | 30303937.635 |
| LG+F+I+G4 | -15120987.520 | 30319460.787 |
| Q.PFAM+F+I+G4 | -15124293.860 | 30326073.467 |
| Q.YEAST+F+I+G4 | -15144861.290 | 30367208.327 |
| LG+I+G4 | -15146545.620 | 30370412.455 |
| Q.PFAM+I+G4 | -15146913.040 | 30371147.295 |
| LG+G4 | -15151185.320 | 30379683.196 |
| Q.INSECT+I+G4 | -15151913.090 | 30381147.395 |
| Q.INSECT+F+I+G4 | -15181478.680 | 30440443.107 |
| MTMET+F+I+G4 | -15480705.220 | 31038896.187 |
| MTART+F+I+G4 | -15631519.700 | 31340525.147 |
| MTMET+I+G4 | -15911765.830 | 31900852.875 |
| MTART+I+G4 | -16110260.080 | 32297841.375 |
| LG+I | -16407160.020 | 32891632.596 |
| LG | -16443179.380 | 32963662.656 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Patescibacteria_150/trained_models/trained_model.nex ../Result/safe_phyla/p__Patescibacteria_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 512227.94 seconds (142.29 h)  
