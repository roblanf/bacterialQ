## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Cloacimonadota_50  
  Taxa name: p__Cloacimonadota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 50  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Cloacimonadota_50/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 143  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Cloacimonadota_50/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 143  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Cloacimonadota_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/subtrees -m random
```
  
Original number of taxa: 143   
Number of pruned subtrees: 6   
Number of taxa after pruning: 130   
Pruned node IDs (degree): 18 (21) 21 (6) 26 (45) 135 (6) 80 (20) 99 (32)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 98 loci files. Total number of potential alignments: 588.  
Obtained 577 alignments from all potential alignments.  
Remaining 577 alignments. Deleted 11 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/subtree_update/p__Cloacimonadota_50
```
  
  Runtime: 2820.26 seconds
[Subtree update log](loop_1/subtree_update/p__Cloacimonadota_50.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 230 | Q.YEAST |
| 173 | LG |
| 152 | Q.INSECT |
| 22 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/subtree_update/p__Cloacimonadota_50.best_scheme.nex -te ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/subtree_update/p__Cloacimonadota_50.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/model_update/p__Cloacimonadota_50
```
  
  Runtime: 11584.61 seconds
[Model update log](loop_1/model_update/p__Cloacimonadota_50.iqtree)  
BIC of the new model: 5883963.9011  
Likelihood of the new model: -2811481.2761  
Model does not meet precision requirement.  
[New model](trained_models/p__Cloacimonadota_50_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,p__Cloacimonadota_50_1  
![Model bubble plot](loop_1/p__Cloacimonadota_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Cloacimonadota_50/ref_tree.tre ../Result/safe_phyla/p__Cloacimonadota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/tree_update/p__Cloacimonadota_50_1.treefile
```
  
  Runtime: 669.80 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Cloacimonadota_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Cloacimonadota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Cloacimonadota_50/loop_1/tree_update/p__Cloacimonadota_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Cloacimonadota_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 32  
Normalized RF distance: 0.1143  
Tree 1 branch length: 22.18114  
Tree 2 branch length: 31.737379768  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.982566680963641  
Euclidean distance: 0.9690818132048994  
Time usage for Loop_1: 15124.26 seconds (4.20 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Cloacimonadota_50/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,LG,Q.INSECT,p__Cloacimonadota_50_1 -mdef ../Result/safe_phyla/p__Cloacimonadota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/tree_update/p__Cloacimonadota_50_1.treefile -pre ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/test_model/p__Cloacimonadota_50_test_concat
```
  
  Runtime: 763.86 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Cloacimonadota_50_1+I+G4 | -530004.730 | 1062527.950 |
| p__Cloacimonadota_50_1+F+I+G4 | -530629.968 | 1063946.325 |
| Q.YEAST+I+G4 | -531818.623 | 1066155.736 |
| Q.INSECT+I+G4 | -532330.193 | 1067178.878 |
| LG+F+I+G4 | -532327.987 | 1067342.364 |
| Q.YEAST+G4 | -532817.895 | 1068145.445 |
| Q.YEAST+F+I+G4 | -533122.403 | 1068931.196 |
| Q.INSECT+F+I+G4 | -533503.529 | 1069693.448 |
| LG+I+G4 | -533773.796 | 1070066.083 |
| Q.YEAST+I | -573119.651 | 1148748.955 |
| Q.YEAST | -590823.927 | 1184148.671 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Cloacimonadota_50/loop_1/tree_update/p__Cloacimonadota_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/subtrees -m random
```
  
Original number of taxa: 143   
Number of pruned subtrees: 5   
Number of taxa after pruning: 129   
Pruned node IDs (degree): 142 (21) 4 (50) 118 (6) 63 (20) 82 (32)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 98 loci files. Total number of potential alignments: 490.  
Obtained 482 alignments from all potential alignments.  
Remaining 482 alignments. Deleted 8 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,p__Cloacimonadota_50_1 -mdef ../Result/safe_phyla/p__Cloacimonadota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/subtree_update/p__Cloacimonadota_50
```
  
  Runtime: 3006.65 seconds
[Subtree update log](loop_2/subtree_update/p__Cloacimonadota_50.iqtree)  
Best models for iteration 2:  
p__Cloacimonadota_50_1  

| Model | Count |
|-------|-------|
| 411 | p__Cloacimonadota_50_1 |
| 37 | LG |
| 25 | Q.INSECT |
| 9 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/subtree_update/p__Cloacimonadota_50.best_scheme.nex -te ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/subtree_update/p__Cloacimonadota_50.treefile --model-joint GTR20+FO --init-model p__Cloacimonadota_50_1 -mdef ../Result/safe_phyla/p__Cloacimonadota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/model_update/p__Cloacimonadota_50
```
  
  Runtime: 10912.96 seconds
[Model update log](loop_2/model_update/p__Cloacimonadota_50.iqtree)  
BIC of the new model: 5662047.8992  
Likelihood of the new model: -2702032.2125  
Model does not meet precision requirement.  
[New model](trained_models/p__Cloacimonadota_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Cloacimonadota_50_2  
![Model bubble plot](loop_2/p__Cloacimonadota_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Cloacimonadota_50/ref_tree.tre ../Result/safe_phyla/p__Cloacimonadota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/tree_update/p__Cloacimonadota_50_2.treefile
```
  
  Runtime: 669.44 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Cloacimonadota_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Cloacimonadota_50/loop_1/tree_update/p__Cloacimonadota_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Cloacimonadota_50/loop_2/tree_update/p__Cloacimonadota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Cloacimonadota_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 31.737379768  
Tree 2 branch length: 31.785002697  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999321644320015  
Euclidean distance: 0.06066694406548989  
Time usage for Loop_2: 14635.49 seconds (4.07 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Cloacimonadota_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Cloacimonadota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Cloacimonadota_50/loop_2/tree_update/p__Cloacimonadota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Cloacimonadota_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 32  
Normalized RF distance: 0.1143  
Tree 1 branch length: 22.18114  
Tree 2 branch length: 31.785002697  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Cloacimonadota_50_2):  
Pearson's correlation: 0.9831314076532583  
Euclidean distance: 0.953665196227485  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/tree_update/p__Cloacimonadota_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Cloacimonadota_50/final_test/subtrees -m random
```
  
Original number of taxa: 143   
Number of pruned subtrees: 5   
Number of taxa after pruning: 129   
Pruned node IDs (degree): 142 (21) 4 (50) 118 (6) 63 (20) 82 (32)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Cloacimonadota_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 20 loci files. Total number of potential alignments: 100.  
Obtained 97 alignments from all potential alignments.  
Remaining 97 alignments. Deleted 3 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Cloacimonadota_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Cloacimonadota_50_2 -mdef ../Result/safe_phyla/p__Cloacimonadota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Cloacimonadota_50/final_test/p__Cloacimonadota_50_test_partition
```
  
  Runtime: 187.43 seconds
Best models for test data:  
p__Cloacimonadota_50_2  

| Model | Count |
|-------|-------|
| 79 | p__Cloacimonadota_50_2 |
| 7 | Q.INSECT |
| 4 | MTART |
| 4 | LG |
| 2 | Q.YEAST |
| 1 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Cloacimonadota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Cloacimonadota_50_2 -mdef ../Result/safe_phyla/p__Cloacimonadota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Cloacimonadota_50/loop_2/tree_update/p__Cloacimonadota_50_2.treefile -pre ../Result/safe_phyla/p__Cloacimonadota_50/final_test/p__Cloacimonadota_50_test_concat
```
  
  Runtime: 582.96 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Cloacimonadota_50_2+I+G4 | -529963.322 | 1062445.135 |
| p__Cloacimonadota_50_2+F+I+G4 | -530656.881 | 1064000.152 |
| Q.YEAST+I+G4 | -531818.613 | 1066155.717 |
| Q.INSECT+I+G4 | -532330.192 | 1067178.874 |
| LG+F+I+G4 | -532327.993 | 1067342.376 |
| Q.PFAM+F+I+G4 | -533092.509 | 1068871.408 |
| Q.YEAST+F+I+G4 | -533122.403 | 1068931.197 |
| Q.INSECT+F+I+G4 | -533503.535 | 1069693.461 |
| LG+I+G4 | -533773.797 | 1070066.084 |
| LG+G4 | -534809.604 | 1072128.861 |
| Q.PFAM+I+G4 | -535023.489 | 1072565.468 |
| MTMET+F+I+G4 | -543201.691 | 1089089.772 |
| MTART+F+I+G4 | -546763.296 | 1096212.982 |
| MTMET+I+G4 | -558147.806 | 1118814.103 |
| MTART+I+G4 | -563233.340 | 1128985.170 |
| LG+I | -572592.220 | 1147694.094 |
| LG | -589246.895 | 1180994.608 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Cloacimonadota_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Cloacimonadota_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 31324.81 seconds (8.70 h)  
