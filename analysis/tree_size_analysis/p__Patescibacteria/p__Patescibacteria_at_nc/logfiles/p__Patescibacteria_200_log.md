## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Patescibacteria_200  
  Taxa name: p__Patescibacteria  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
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
Discarded 8 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_200/select_id.txt. Sampling sequences for 92 loci.  
Number of input species: 4465  
Remaining 92 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 5 loci based on the loci filter.  
Input a single taxa file: ../Result_rona/formal_test/p__Patescibacteria_200/select_id.txt. Sampling sequences for 15 loci.  
Number of input species: 4465  
Remaining 15 alignments. Deleted 0 alignments.  
Abstract alingment of selected taxa scale in training set:  
Abstract alingment of selected taxa scale in testing set:  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_200/ref_tree.tre -l 5 -u 200 -o ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 71   
Number of taxa after pruning: 4404   
Pruned node IDs (degree): 1125 (50) 1175 (15) 979 (146) 3529 (60) 4 (112) 736 (5) 2743 (177) 2920 (11) 3589 (10) 116 (52) 1192 (8) 3486 (43) 168 (10) 742 (93) 834 (146) 2932 (71) 3603 (17) 722 (10) 2503 (35) 179 (70) 1202 (14) 2203 (21) 3004 (15) 3271 (62) 3332 (155) 3621 (20) 2152 (51) 2539 (200) 3253 (18) 4450 (11) 250 (161) 410 (85) 495 (136) 630 (93) 2130 (23) 2472 (31) 3020 (92) 3111 (143) 2121 (10) 1219 (19) 2109 (13) 2232 (5) 3646 (190) 2105 (5) 2237 (85) 2321 (151) 2095 (11) 3837 (5) 2066 (29) 1243 (8) 1251 (44) 3847 (8) 3855 (63) 1296 (188) 1483 (21) 1505 (30) 1746 (10) 1738 (8) 3921 (181) 4101 (49) 1536 (66) 1601 (138) 2049 (18) 4426 (19) 1759 (74) 1833 (51) 1883 (167) 4159 (7) 4379 (46) 4168 (179) 4346 (34)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input 71 subtree files and 92 loci files. Total number of potential alignments: 6532.  
Sub-sampling 1000 alignments from 6532 alignments.  
Could not obtain the requested 1000 alignments. Keeping 971 alignments.  
Remaining 971 alignments. Deleted 129 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/subtree_update/p__Patescibacteria_200
```
  
  Runtime: 63107.80 seconds
[Subtree update log](loop_1/subtree_update/p__Patescibacteria_200.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 383 | LG |
| 324 | Q.YEAST |
| 162 | Q.PFAM |
| 102 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/subtree_update/p__Patescibacteria_200.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/subtree_update/p__Patescibacteria_200.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/model_update/p__Patescibacteria_200
```
  
  Runtime: 190230.12 seconds
[Model update log](loop_1/model_update/p__Patescibacteria_200.iqtree)  
BIC of the new model: 29625204.2891  
Likelihood of the new model: -14133179.6831  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_200_1)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_200_1  
![Model bubble plot](loop_1/p__Patescibacteria_200_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_200/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_200/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/tree_update/p__Patescibacteria_200_1.treefile
```
  
  Runtime: 35766.22 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_200/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_200/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_200/loop_1/tree_update/p__Patescibacteria_200_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_200/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 2086  
Normalized RF distance: 0.2338  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1427.967175338  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9896204262939782  
Euclidean distance: 0.7913412424932338  
Time usage for Loop_1: 289553.56 seconds (80.43 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_200/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_200_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_200/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/tree_update/p__Patescibacteria_200_1.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/test_model/p__Patescibacteria_200_test_concat
```
  
  Runtime: 19833.97 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_200_1+I+G4 | -15056270.460 | 30189862.135 |
| p__Patescibacteria_200_1+F+I+G4 | -15090164.500 | 30257814.747 |
| Q.YEAST+I+G4 | -15113258.160 | 30303837.535 |
| LG+F+I+G4 | -15120838.190 | 30319162.127 |
| Q.PFAM+F+I+G4 | -15124165.360 | 30325816.467 |
| Q.YEAST+F+I+G4 | -15144762.810 | 30367011.367 |
| LG+I+G4 | -15146429.670 | 30370180.555 |
| Q.PFAM+I+G4 | -15146828.320 | 30370977.855 |
| LG+G4 | -15151077.520 | 30379467.596 |
| Q.INSECT+I+G4 | -15151838.620 | 30380998.455 |
| Q.INSECT+F+I+G4 | -15181365.790 | 30440217.327 |
| LG+I | -16406940.210 | 32891192.976 |
| LG | -16442958.390 | 32963220.676 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_200/loop_1/tree_update/p__Patescibacteria_200_1.treefile -l 5 -u 200 -o ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 76   
Number of taxa after pruning: 4408   
Pruned node IDs (degree): 3078 (200) 2410 (194) 515 (190) 2652 (188) 1673 (179) 2181 (179) 3547 (177) 860 (161) 1039 (158) 3304 (157) 1373 (148) 12 (147) 3837 (142) 4082 (136) 166 (114) 4361 (104) 3978 (104) 279 (97) 4217 (93) 1520 (92) 3756 (80) 2108 (74) 3460 (70) 792 (69) 727 (63) 400 (61) 1612 (60) 1196 (55) 4310 (52) 1934 (50) 2988 (50) 1250 (46) 1892 (43) 2359 (43) 3039 (39) 2865 (35) 2004 (31) 2903 (29) 1851 (28) 2623 (28) 2965 (23) 375 (23) 3279 (22) 2839 (21) 2603 (21) 490 (20) 1296 (19) 471 (18) 2055 (18) 2089 (18) 3723 (15) 1350 (15) 3529 (14) 2038 (13) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 461 (10) 1340 (10) 2956 (10) 705 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 719 (8) 2859 (7) 2401 (7) 1030 (7) 3542 (6) 160 (6) 1878 (5) 2942 (5) 2899 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input 76 subtree files and 92 loci files. Total number of potential alignments: 6992.  
Sub-sampling 1000 alignments from 6992 alignments.  
Could not obtain the requested 1000 alignments. Keeping 978 alignments.  
Remaining 978 alignments. Deleted 122 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PFAM,Q.INSECT,p__Patescibacteria_200_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_200/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/subtree_update/p__Patescibacteria_200
```
  
  Runtime: 64324.52 seconds
[Subtree update log](loop_2/subtree_update/p__Patescibacteria_200.iqtree)  
Best models for iteration 2:  
p__Patescibacteria_200_1  

| Model | Count |
|-------|-------|
| 745 | p__Patescibacteria_200_1 |
| 115 | LG |
| 58 | Q.PFAM |
| 30 | Q.YEAST |
| 30 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/subtree_update/p__Patescibacteria_200.best_scheme.nex -te ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/subtree_update/p__Patescibacteria_200.treefile --model-joint GTR20+FO --init-model p__Patescibacteria_200_1 -mdef ../Result_rona/formal_test/p__Patescibacteria_200/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/model_update/p__Patescibacteria_200
```
  
  Runtime: 151671.76 seconds
[Model update log](loop_2/model_update/p__Patescibacteria_200.iqtree)  
BIC of the new model: 27967619.1494  
Likelihood of the new model: -13338861.9131  
Model does not meet precision requirement.  
[New model](trained_models/p__Patescibacteria_200_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_200_2  
![Model bubble plot](loop_2/p__Patescibacteria_200_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Patescibacteria_200/ref_tree.tre ../Result_rona/formal_test/p__Patescibacteria_200/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/tree_update/p__Patescibacteria_200_2.treefile
```
  
  Runtime: 33327.40 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_200/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_200/loop_1/tree_update/p__Patescibacteria_200_1.treefile', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_200/loop_2/tree_update/p__Patescibacteria_200_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_200/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 48  
Normalized RF distance: 0.0054  
Tree 1 branch length: 1427.967175338  
Tree 2 branch length: 1427.990666829  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9992184160266804  
Euclidean distance: 0.21429126911150825  
Time usage for Loop_2: 249469.91 seconds (69.30 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Patescibacteria_200/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Patescibacteria_200/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Patescibacteria_200/loop_2/tree_update/p__Patescibacteria_200_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Patescibacteria_200/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2088  
Normalized RF distance: 0.234  
Tree 1 branch length: 1135.26331  
Tree 2 branch length: 1427.990666829  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Patescibacteria_200_2):  
Pearson's correlation: 0.9865999863297882  
Euclidean distance: 0.9020365481507199  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/tree_update/p__Patescibacteria_200_2.treefile -l 5 -u 200 -o ../Result_rona/formal_test/p__Patescibacteria_200/final_test/subtrees -m random
```
  
Original number of taxa: 4465   
Number of pruned subtrees: 76   
Number of taxa after pruning: 4408   
Pruned node IDs (degree): 3078 (200) 2410 (194) 515 (190) 2652 (188) 1673 (179) 2181 (179) 3547 (177) 860 (161) 1039 (158) 3304 (157) 1373 (148) 12 (147) 3837 (142) 4082 (136) 166 (114) 4361 (104) 3978 (104) 279 (97) 4217 (93) 1520 (92) 3756 (80) 2108 (74) 3460 (70) 792 (69) 727 (63) 400 (61) 1612 (60) 1196 (55) 4310 (52) 1934 (50) 2988 (50) 1250 (46) 1892 (43) 2359 (43) 3039 (39) 2865 (35) 2004 (31) 2903 (29) 1851 (28) 2623 (28) 2965 (23) 375 (23) 3279 (22) 2839 (21) 2603 (21) 490 (20) 1296 (19) 471 (18) 2055 (18) 2089 (18) 3723 (15) 1350 (15) 3529 (14) 2038 (13) 1984 (11) 1882 (11) 1319 (11) 2946 (11) 2932 (11) 461 (10) 1340 (10) 2956 (10) 705 (9) 1996 (8) 3737 (8) 1365 (8) 3746 (8) 719 (8) 2859 (7) 2401 (7) 1030 (7) 3542 (6) 160 (6) 1878 (5) 2942 (5) 2899 (5)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Patescibacteria_200/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input 76 subtree files and 15 loci files. Total number of potential alignments: 1140.  
Obtained 1015 alignments from all potential alignments.  
Remaining 1015 alignments. Deleted 125 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Patescibacteria_200/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_200_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_200/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Patescibacteria_200/final_test/p__Patescibacteria_200_test_partition
```
  
  Runtime: 2032.03 seconds
Best models for test data:  
p__Patescibacteria_200_2  

| Model | Count |
|-------|-------|
| 713 | p__Patescibacteria_200_2 |
| 114 | LG |
| 80 | Q.YEAST |
| 66 | Q.PFAM |
| 18 | MTMET |
| 12 | Q.INSECT |
| 12 | MTART |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Patescibacteria_200/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Patescibacteria_200_2 -mdef ../Result_rona/formal_test/p__Patescibacteria_200/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Patescibacteria_200/loop_2/tree_update/p__Patescibacteria_200_2.treefile -pre ../Result_rona/formal_test/p__Patescibacteria_200/final_test/p__Patescibacteria_200_test_concat
```
  
  Runtime: 63201.08 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Patescibacteria_200_2+I+G4 | -15055385.320 | 30188091.855 |
| p__Patescibacteria_200_2+F+I+G4 | -15087138.180 | 30251762.107 |
| Q.YEAST+I+G4 | -15113574.630 | 30304470.475 |
| LG+F+I+G4 | -15121024.340 | 30319534.427 |
| Q.PFAM+F+I+G4 | -15124367.750 | 30326221.247 |
| Q.YEAST+F+I+G4 | -15145001.590 | 30367488.927 |
| LG+I+G4 | -15146680.010 | 30370681.235 |
| Q.PFAM+I+G4 | -15147082.350 | 30371485.915 |
| LG+G4 | -15151337.330 | 30379987.216 |
| Q.INSECT+I+G4 | -15152113.160 | 30381547.535 |
| Q.INSECT+F+I+G4 | -15181543.830 | 30440573.407 |
| MTMET+F+I+G4 | -15480742.440 | 31038970.627 |
| MTART+F+I+G4 | -15631800.040 | 31341085.827 |
| MTMET+I+G4 | -15912019.340 | 31901359.895 |
| MTART+I+G4 | -16110689.430 | 32298700.075 |
| LG+I | -16407128.170 | 32891568.896 |
| LG | -16443146.190 | 32963596.276 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Patescibacteria_200/trained_models/trained_model.nex ../Result_rona/formal_test/p__Patescibacteria_200/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 624697.01 seconds (173.53 h)  
