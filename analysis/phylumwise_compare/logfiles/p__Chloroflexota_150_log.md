## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Chloroflexota_150  
  Taxa name: p__Chloroflexota  
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
Input a single taxa file: ../Result/safe_phyla/p__Chloroflexota_150/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 2698  
## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Chloroflexota_150  
  Taxa name: p__Chloroflexota  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 150  
### Quality trimming  
## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Chloroflexota_150  
  Taxa name: p__Chloroflexota  
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
Input a single taxa file: ../Result/safe_phyla/p__Chloroflexota_150/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 2698  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Chloroflexota_150/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 2698  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Chloroflexota_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Chloroflexota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 2698   
Number of pruned subtrees: 51   
Number of taxa after pruning: 2665   
Pruned node IDs (degree): 457 (25) 797 (11) 1105 (7) 446 (5) 781 (14) 1095 (8) 1112 (146) 1257 (27) 406 (40) 776 (6) 809 (16) 825 (8) 486 (16) 833 (111) 136 (74) 681 (96) 946 (150) 212 (99) 310 (94) 1290 (45) 2459 (43) 504 (35) 538 (143) 1335 (9) 2698 (132) 2428 (32) 2665 (34) 2417 (12) 2503 (135) 2637 (29) 2270 (148) 2266 (5) 2230 (37) 2185 (46) 2128 (58) 2043 (86) 1518 (10) 2030 (14) 2017 (14) 1356 (5) 2013 (5) 1361 (127) 1487 (30) 1986 (28) 1969 (18) 1877 (93) 1535 (81) 1615 (89) 1706 (10) 1717 (41) 1757 (118)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Chloroflexota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 51 subtree files and 100 loci files. Total number of potential alignments: 5100.  
Sub-sampling 1000 alignments from 5100 alignments.  
Remaining 1000 alignments. Deleted 41 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chloroflexota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Chloroflexota_150/loop_1/subtree_update/p__Chloroflexota_150
```
  
  Runtime: 54386.67 seconds
[Subtree update log](loop_1/subtree_update/p__Chloroflexota_150.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 369 | LG |
| 345 | Q.PFAM |
| 216 | Q.INSECT |
| 70 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chloroflexota_150/loop_1/subtree_update/p__Chloroflexota_150.best_scheme.nex -te ../Result/safe_phyla/p__Chloroflexota_150/loop_1/subtree_update/p__Chloroflexota_150.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Chloroflexota_150/loop_1/model_update/p__Chloroflexota_150
```
  
  Runtime: 94838.31 seconds
[Model update log](loop_1/model_update/p__Chloroflexota_150.iqtree)  
BIC of the new model: 20080669.4912  
Likelihood of the new model: -9469997.881  
Model does not meet precision requirement.  
[New model](trained_models/p__Chloroflexota_150_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Chloroflexota_150_1  
![Model bubble plot](loop_1/p__Chloroflexota_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Chloroflexota_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Chloroflexota_150/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Chloroflexota_150/ref_tree.tre ../Result/safe_phyla/p__Chloroflexota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Chloroflexota_150/loop_1/tree_update/p__Chloroflexota_150_1.treefile
```
  
  Runtime: 44768.48 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Chloroflexota_150/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Chloroflexota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Chloroflexota_150/loop_1/tree_update/p__Chloroflexota_150_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Chloroflexota_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 792  
Normalized RF distance: 0.1469  
Tree 1 branch length: 399.7078  
Tree 2 branch length: 505.142544114  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9899808913011889  
Euclidean distance: 0.7813550842121194  
Time usage for Loop_1: 194286.13 seconds (53.97 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Chloroflexota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Chloroflexota_150_1 -mdef ../Result/safe_phyla/p__Chloroflexota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Chloroflexota_150/loop_1/tree_update/p__Chloroflexota_150_1.treefile -pre ../Result/safe_phyla/p__Chloroflexota_150/loop_1/test_model/p__Chloroflexota_150_test_concat
```
  
  Runtime: 7085.97 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Chloroflexota_150_1+I+G4 | -8460905.478 | 16969428.021 |
| p__Chloroflexota_150_1+F+I+G4 | -8472109.774 | 16992004.310 |
| LG+F+I+G4 | -8495024.979 | 17037834.720 |
| Q.PFAM+F+I+G4 | -8501356.794 | 17050498.350 |
| Q.PFAM+I+G4 | -8506477.239 | 17060571.543 |
| Q.YEAST+F+I+G4 | -8507272.744 | 17062330.250 |
| Q.INSECT+F+I+G4 | -8513883.914 | 17075552.590 |
| LG+I+G4 | -8520554.623 | 17088726.311 |
| LG+G4 | -8526244.126 | 17100096.491 |
| Q.INSECT+I+G4 | -8536370.126 | 17120357.317 |
| Q.YEAST+I+G4 | -8556851.461 | 17161319.987 |
| LG+I | -9332484.506 | 18712577.251 |
| LG | -9385730.078 | 18819059.569 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Chloroflexota_150/loop_1/tree_update/p__Chloroflexota_150_1.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Chloroflexota_150/loop_2/subtrees -m random
```
  
Original number of taxa: 2698   
Number of pruned subtrees: 52   
Number of taxa after pruning: 2668   
Pruned node IDs (degree): 600 (8) 895 (8) 251 (6) 798 (98) 908 (5) 263 (22) 610 (39) 80 (146) 225 (27) 585 (13) 649 (150) 912 (15) 286 (9) 295 (16) 2294 (25) 5 (64) 311 (98) 409 (129) 537 (49) 1116 (5) 2318 (10) 930 (94) 1023 (94) 1125 (9) 2327 (43) 1134 (45) 2566 (132) 2263 (32) 2533 (34) 1180 (14) 2371 (135) 2505 (29) 2130 (134) 1195 (12) 2126 (5) 1208 (37) 2069 (58) 2023 (47) 1938 (86) 1413 (10) 1925 (14) 1912 (14) 1251 (121) 1371 (41) 1908 (5) 1881 (28) 1864 (18) 1772 (93) 1430 (120) 1549 (50) 1602 (131) 1732 (41)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Chloroflexota_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 52 subtree files and 100 loci files. Total number of potential alignments: 5200.  
Sub-sampling 1000 alignments from 5200 alignments.  
Remaining 1000 alignments. Deleted 40 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chloroflexota_150/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Chloroflexota_150_1 -mdef ../Result/safe_phyla/p__Chloroflexota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Chloroflexota_150/loop_2/subtree_update/p__Chloroflexota_150
```
  
  Runtime: 61944.16 seconds
[Subtree update log](loop_2/subtree_update/p__Chloroflexota_150.iqtree)  
Best models for iteration 2:  
p__Chloroflexota_150_1  

| Model | Count |
|-------|-------|
| 874 | p__Chloroflexota_150_1 |
| 52 | LG |
| 34 | Q.PFAM |
| 22 | Q.INSECT |
| 18 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chloroflexota_150/loop_2/subtree_update/p__Chloroflexota_150.best_scheme.nex -te ../Result/safe_phyla/p__Chloroflexota_150/loop_2/subtree_update/p__Chloroflexota_150.treefile --model-joint GTR20+FO --init-model p__Chloroflexota_150_1 -mdef ../Result/safe_phyla/p__Chloroflexota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Chloroflexota_150/loop_2/model_update/p__Chloroflexota_150
```
  
  Runtime: 116432.79 seconds
[Model update log](loop_2/model_update/p__Chloroflexota_150.iqtree)  
BIC of the new model: 20966843.1114  
Likelihood of the new model: -9902060.7123  
Model does not meet precision requirement.  
[New model](trained_models/p__Chloroflexota_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Chloroflexota_150_2  
![Model bubble plot](loop_2/p__Chloroflexota_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Chloroflexota_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Chloroflexota_150/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Chloroflexota_150/ref_tree.tre ../Result/safe_phyla/p__Chloroflexota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Chloroflexota_150/loop_2/tree_update/p__Chloroflexota_150_2.treefile
```
  
  Runtime: 33775.89 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Chloroflexota_150/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Chloroflexota_150/loop_1/tree_update/p__Chloroflexota_150_1.treefile', tree2_path = '../Result/safe_phyla/p__Chloroflexota_150/loop_2/tree_update/p__Chloroflexota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Chloroflexota_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0015  
Tree 1 branch length: 505.142544114  
Tree 2 branch length: 503.286042838  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997726859111473  
Euclidean distance: 0.11487311190774628  
Time usage for Loop_2: 212468.15 seconds (59.02 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Chloroflexota_150/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Chloroflexota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Chloroflexota_150/loop_2/tree_update/p__Chloroflexota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Chloroflexota_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 792  
Normalized RF distance: 0.1469  
Tree 1 branch length: 399.7078  
Tree 2 branch length: 503.286042838  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Chloroflexota_150_2):  
Pearson's correlation: 0.9900300284857706  
Euclidean distance: 0.7858002596014515  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Chloroflexota_150/loop_2/tree_update/p__Chloroflexota_150_2.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Chloroflexota_150/final_test/subtrees -m random
```
  
Original number of taxa: 2698   
Number of pruned subtrees: 52   
Number of taxa after pruning: 2668   
Pruned node IDs (degree): 649 (150) 80 (146) 2371 (135) 2130 (134) 2566 (132) 1602 (131) 409 (129) 1251 (121) 1430 (120) 798 (98) 311 (98) 930 (94) 1023 (94) 1772 (93) 1938 (86) 5 (64) 2069 (58) 1549 (50) 537 (49) 2023 (47) 1134 (45) 2327 (43) 1371 (41) 1732 (41) 610 (39) 1208 (37) 2533 (34) 2263 (32) 2505 (29) 1881 (28) 225 (27) 2294 (25) 263 (22) 1864 (18) 295 (16) 912 (15) 1180 (14) 1925 (14) 1912 (14) 585 (13) 1195 (12) 2318 (10) 1413 (10) 286 (9) 1125 (9) 600 (8) 895 (8) 251 (6) 908 (5) 1116 (5) 2126 (5) 1908 (5)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Chloroflexota_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 52 subtree files and 19 loci files. Total number of potential alignments: 988.  
Obtained 931 alignments from all potential alignments.  
Remaining 931 alignments. Deleted 57 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chloroflexota_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Chloroflexota_150_2 -mdef ../Result/safe_phyla/p__Chloroflexota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Chloroflexota_150/final_test/p__Chloroflexota_150_test_partition
```
  
  Runtime: 2176.98 seconds
Best models for test data:  
p__Chloroflexota_150_2  

| Model | Count |
|-------|-------|
| 812 | p__Chloroflexota_150_2 |
| 40 | LG |
| 28 | Q.INSECT |
| 23 | Q.YEAST |
| 23 | Q.PFAM |
| 3 | MTART |
| 2 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Chloroflexota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Chloroflexota_150_2 -mdef ../Result/safe_phyla/p__Chloroflexota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Chloroflexota_150/loop_2/tree_update/p__Chloroflexota_150_2.treefile -pre ../Result/safe_phyla/p__Chloroflexota_150/final_test/p__Chloroflexota_150_test_concat
```
  
  Runtime: 7562.57 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Chloroflexota_150_2+I+G4 | -8460703.841 | 16969024.747 |
| p__Chloroflexota_150_2+F+I+G4 | -8471251.175 | 16990287.112 |
| LG+F+I+G4 | -8495080.471 | 17037945.704 |
| Q.PFAM+F+I+G4 | -8501415.924 | 17050616.610 |
| Q.PFAM+I+G4 | -8506536.684 | 17060690.433 |
| Q.YEAST+F+I+G4 | -8507325.429 | 17062435.620 |
| Q.INSECT+F+I+G4 | -8513936.389 | 17075657.540 |
| LG+I+G4 | -8520614.497 | 17088846.059 |
| LG+G4 | -8526306.397 | 17100221.033 |
| Q.INSECT+I+G4 | -8536426.192 | 17120469.449 |
| Q.YEAST+I+G4 | -8556907.501 | 17161432.067 |
| MTMET+F+I+G4 | -8737593.657 | 17522972.076 |
| MTART+F+I+G4 | -8915827.497 | 17879439.756 |
| MTMET+I+G4 | -9096994.120 | 18241605.305 |
| MTART+I+G4 | -9280151.752 | 18607920.569 |
| LG+I | -9332540.036 | 18712688.311 |
| LG | -9385784.808 | 18819169.029 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Chloroflexota_150/trained_models/trained_model.nex ../Result/safe_phyla/p__Chloroflexota_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 424842.72 seconds (118.01 h)  
