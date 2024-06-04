## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Cyanobacteriota_150  
  Taxa name: p__Cyanobacteriota  
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
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Cyanobacteriota_150/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 2177  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Cyanobacteriota_150/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 2177  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Cyanobacteriota_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 2177   
Number of pruned subtrees: 53   
Number of taxa after pruning: 2124   
Pruned node IDs (degree): 2153 (9) 2177 (17) 4 (94) 2145 (9) 98 (21) 119 (15) 702 (8) 2135 (11) 710 (40) 2123 (13) 750 (16) 1546 (133) 766 (31) 616 (80) 141 (105) 1429 (115) 1681 (75) 246 (8) 801 (7) 2118 (6) 254 (21) 808 (46) 853 (109) 964 (10) 1421 (9) 275 (124) 974 (13) 1154 (22) 610 (7) 987 (140) 1126 (27) 1176 (70) 1760 (7) 400 (6) 1413 (9) 406 (70) 475 (136) 1247 (129) 1375 (39) 2106 (7) 1773 (7) 1781 (21) 1804 (39) 1844 (13) 1858 (32) 2101 (6) 1896 (11) 1907 (5) 1912 (8) 1924 (10) 2095 (5) 1941 (125) 2065 (28)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 53 subtree files and 98 loci files. Total number of potential alignments: 5194.  
Sub-sampling 1000 alignments from 5194 alignments.  
Remaining 1000 alignments. Deleted 46 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/subtree_update/p__Cyanobacteriota_150
```
  
  Runtime: 32953.45 seconds
[Subtree update log](loop_1/subtree_update/p__Cyanobacteriota_150.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 306 | LG |
| 228 | Q.YEAST |
| 227 | Q.INSECT |
| 220 | Q.PFAM |
| 16 | MTMET |
| 3 | MTART |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/subtree_update/p__Cyanobacteriota_150.best_scheme.nex -te ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/subtree_update/p__Cyanobacteriota_150.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/model_update/p__Cyanobacteriota_150
```
  
  Runtime: 50514.72 seconds
[Model update log](loop_1/model_update/p__Cyanobacteriota_150.iqtree)  
BIC of the new model: 11636281.9395  
Likelihood of the new model: -5349854.6039  
Model does not meet precision requirement.  
[New model](trained_models/p__Cyanobacteriota_150_1)  
Model set for next iteration: LG,Q.YEAST,Q.INSECT,Q.PFAM,p__Cyanobacteriota_150_1  
![Model bubble plot](loop_1/p__Cyanobacteriota_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Cyanobacteriota_150/ref_tree.tre ../Result/safe_phyla/p__Cyanobacteriota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/tree_update/p__Cyanobacteriota_150_1.treefile
```
  
  Runtime: 9948.72 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Cyanobacteriota_150/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Cyanobacteriota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/tree_update/p__Cyanobacteriota_150_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Cyanobacteriota_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 1108  
Normalized RF distance: 0.2548  
Tree 1 branch length: 147.21093  
Tree 2 branch length: 206.631395431  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9888773604231023  
Euclidean distance: 0.7720091849064349  
Time usage for Loop_1: 93451.90 seconds (25.96 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Cyanobacteriota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.YEAST,Q.INSECT,Q.PFAM,p__Cyanobacteriota_150_1 -mdef ../Result/safe_phyla/p__Cyanobacteriota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/tree_update/p__Cyanobacteriota_150_1.treefile -pre ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/test_model/p__Cyanobacteriota_150_test_concat
```
  
  Runtime: 4901.51 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Cyanobacteriota_150_1+I+G4 | -4133192.669 | 8304851.971 |
| p__Cyanobacteriota_150_1+F+I+G4 | -4138777.306 | 8316189.145 |
| Q.YEAST+I+G4 | -4147363.815 | 8333194.263 |
| Q.INSECT+I+G4 | -4147951.393 | 8334369.419 |
| LG+I+G4 | -4157319.242 | 8353105.117 |
| LG+F+I+G4 | -4157707.719 | 8354049.971 |
| Q.PFAM+I+G4 | -4159985.536 | 8358437.705 |
| Q.PFAM+F+I+G4 | -4161834.841 | 8362304.215 |
| Q.YEAST+F+I+G4 | -4162500.967 | 8363636.467 |
| Q.INSECT+F+I+G4 | -4163783.575 | 8366201.683 |
| LG+G4 | -4164147.843 | 8366753.483 |
| LG+I | -4603420.854 | 9245299.505 |
| LG | -4672885.555 | 9384220.070 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/tree_update/p__Cyanobacteriota_150_1.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/subtrees -m random
```
  
Original number of taxa: 2177   
Number of pruned subtrees: 49   
Number of taxa after pruning: 2131   
Pruned node IDs (degree): 2168 (9) 2176 (17) 19 (94) 2160 (9) 113 (21) 699 (15) 717 (8) 2150 (11) 725 (40) 2138 (13) 765 (16) 1561 (133) 781 (31) 614 (80) 139 (105) 1696 (75) 244 (8) 814 (110) 923 (53) 976 (11) 2133 (6) 470 (145) 987 (104) 464 (7) 1369 (10) 1545 (13) 1361 (9) 1380 (27) 1406 (140) 2126 (6) 256 (83) 338 (123) 1094 (22) 1779 (10) 1116 (70) 2118 (9) 1353 (9) 1187 (129) 1315 (39) 1793 (21) 2079 (40) 1817 (13) 1830 (32) 2074 (6) 1870 (20) 2068 (6) 1891 (6) 1898 (19) 1920 (148)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 49 subtree files and 98 loci files. Total number of potential alignments: 4802.  
Sub-sampling 1000 alignments from 4802 alignments.  
Remaining 1000 alignments. Deleted 26 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.INSECT,Q.PFAM,p__Cyanobacteriota_150_1 -mdef ../Result/safe_phyla/p__Cyanobacteriota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/subtree_update/p__Cyanobacteriota_150
```
  
  Runtime: 33010.15 seconds
[Subtree update log](loop_2/subtree_update/p__Cyanobacteriota_150.iqtree)  
Best models for iteration 2:  
p__Cyanobacteriota_150_1  

| Model | Count |
|-------|-------|
| 777 | p__Cyanobacteriota_150_1 |
| 79 | Q.PFAM |
| 53 | Q.YEAST |
| 49 | LG |
| 42 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/subtree_update/p__Cyanobacteriota_150.best_scheme.nex -te ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/subtree_update/p__Cyanobacteriota_150.treefile --model-joint GTR20+FO --init-model p__Cyanobacteriota_150_1 -mdef ../Result/safe_phyla/p__Cyanobacteriota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/model_update/p__Cyanobacteriota_150
```
  
  Runtime: 51367.34 seconds
[Model update log](loop_2/model_update/p__Cyanobacteriota_150.iqtree)  
BIC of the new model: 10919045.6023  
Likelihood of the new model: -4969111.0266  
Model does not meet precision requirement.  
[New model](trained_models/p__Cyanobacteriota_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Cyanobacteriota_150_2  
![Model bubble plot](loop_2/p__Cyanobacteriota_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Cyanobacteriota_150/ref_tree.tre ../Result/safe_phyla/p__Cyanobacteriota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/tree_update/p__Cyanobacteriota_150_2.treefile
```
  
  Runtime: 10085.35 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Cyanobacteriota_150/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Cyanobacteriota_150/loop_1/tree_update/p__Cyanobacteriota_150_1.treefile', tree2_path = '../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/tree_update/p__Cyanobacteriota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Cyanobacteriota_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 78  
Normalized RF distance: 0.0179  
Tree 1 branch length: 206.631395431  
Tree 2 branch length: 207.11432516  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9996893360180792  
Euclidean distance: 0.139297651956135  
Time usage for Loop_2: 94518.53 seconds (26.26 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Cyanobacteriota_150/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Cyanobacteriota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/tree_update/p__Cyanobacteriota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Cyanobacteriota_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 1112  
Normalized RF distance: 0.2557  
Tree 1 branch length: 147.21093  
Tree 2 branch length: 207.11432516  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Cyanobacteriota_150_2):  
Pearson's correlation: 0.9883454056011945  
Euclidean distance: 0.8021446072949787  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/tree_update/p__Cyanobacteriota_150_2.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Cyanobacteriota_150/final_test/subtrees -m random
```
  
Original number of taxa: 2177   
Number of pruned subtrees: 49   
Number of taxa after pruning: 2131   
Pruned node IDs (degree): 2168 (9) 2176 (17) 19 (94) 2160 (9) 113 (21) 699 (15) 717 (8) 2150 (11) 725 (40) 2138 (13) 765 (16) 1561 (133) 781 (31) 614 (80) 139 (105) 1696 (75) 244 (8) 814 (110) 923 (53) 976 (11) 2133 (6) 470 (145) 987 (104) 464 (7) 1369 (10) 1545 (13) 1361 (9) 1380 (27) 1406 (140) 2126 (6) 256 (83) 338 (123) 1094 (22) 1779 (10) 1116 (70) 2118 (9) 1353 (9) 1187 (129) 1315 (39) 1793 (21) 2079 (40) 1817 (13) 1830 (32) 2074 (6) 1870 (20) 2068 (6) 1891 (6) 1898 (19) 1920 (148)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Cyanobacteriota_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 49 subtree files and 20 loci files. Total number of potential alignments: 980.  
Obtained 965 alignments from all potential alignments.  
Remaining 965 alignments. Deleted 15 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cyanobacteriota_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Cyanobacteriota_150_2 -mdef ../Result/safe_phyla/p__Cyanobacteriota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Cyanobacteriota_150/final_test/p__Cyanobacteriota_150_test_partition
```
  
  Runtime: 1495.42 seconds
Best models for test data:  
p__Cyanobacteriota_150_2  

| Model | Count |
|-------|-------|
| 764 | p__Cyanobacteriota_150_2 |
| 83 | Q.YEAST |
| 34 | Q.PFAM |
| 32 | MTART |
| 23 | Q.INSECT |
| 23 | LG |
| 6 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Cyanobacteriota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Cyanobacteriota_150_2 -mdef ../Result/safe_phyla/p__Cyanobacteriota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Cyanobacteriota_150/loop_2/tree_update/p__Cyanobacteriota_150_2.treefile -pre ../Result/safe_phyla/p__Cyanobacteriota_150/final_test/p__Cyanobacteriota_150_test_concat
```
  
  Runtime: 6432.46 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Cyanobacteriota_150_2+I+G4 | -4134164.138 | 8306794.909 |
| p__Cyanobacteriota_150_2+F+I+G4 | -4138934.595 | 8316503.723 |
| Q.YEAST+I+G4 | -4147260.845 | 8332988.323 |
| Q.INSECT+I+G4 | -4147855.400 | 8334177.433 |
| LG+I+G4 | -4157204.070 | 8352874.773 |
| LG+F+I+G4 | -4157586.247 | 8353807.027 |
| Q.PFAM+I+G4 | -4159873.061 | 8358212.755 |
| Q.PFAM+F+I+G4 | -4161724.766 | 8362084.065 |
| Q.YEAST+F+I+G4 | -4162389.776 | 8363414.085 |
| Q.INSECT+F+I+G4 | -4163667.902 | 8365970.337 |
| LG+G4 | -4164044.694 | 8366547.185 |
| MTMET+F+I+G4 | -4234251.791 | 8507138.115 |
| MTART+F+I+G4 | -4298075.826 | 8634786.185 |
| MTMET+I+G4 | -4351369.562 | 8741205.757 |
| MTART+I+G4 | -4430580.405 | 8899627.443 |
| LG+I | -4603307.046 | 9245071.889 |
| LG | -4672770.719 | 9383990.398 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Cyanobacteriota_150/trained_models/trained_model.nex ../Result/safe_phyla/p__Cyanobacteriota_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 201105.90 seconds (55.86 h)  
