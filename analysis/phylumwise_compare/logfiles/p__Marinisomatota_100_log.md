## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Marinisomatota_100  
  Taxa name: p__Marinisomatota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 100  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Marinisomatota_100/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 275  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Marinisomatota_100/select_id.txt. Sampling sequences for 18 loci.  
Number of input species: 275  
Remaining 18 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Marinisomatota_100/ref_tree.tre -l 5 -u 100 -o ../Result/safe_phyla/p__Marinisomatota_100/loop_1/subtrees -m random
```
  
Original number of taxa: 275   
Number of pruned subtrees: 6   
Number of taxa after pruning: 275   
Pruned node IDs (degree): 49 (48) 47 (76) 231 (16) 203 (29) 99 (66) 164 (40)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Marinisomatota_100/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 100 loci files. Total number of potential alignments: 600.  
Obtained 587 alignments from all potential alignments.  
Remaining 587 alignments. Deleted 13 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Marinisomatota_100/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Marinisomatota_100/loop_1/subtree_update/p__Marinisomatota_100
```
  
  Runtime: 7795.22 seconds
[Subtree update log](loop_1/subtree_update/p__Marinisomatota_100.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 381 | Q.YEAST |
| 106 | Q.INSECT |
| 81 | LG |
| 14 | Q.PFAM |
| 4 | MTMET |
| 1 | MTART |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Marinisomatota_100/loop_1/subtree_update/p__Marinisomatota_100.best_scheme.nex -te ../Result/safe_phyla/p__Marinisomatota_100/loop_1/subtree_update/p__Marinisomatota_100.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Marinisomatota_100/loop_1/model_update/p__Marinisomatota_100
```
  
  Runtime: 31717.43 seconds
[Model update log](loop_1/model_update/p__Marinisomatota_100.iqtree)  
BIC of the new model: 10677253.5975  
Likelihood of the new model: -5068603.5436  
Model does not meet precision requirement.  
[New model](trained_models/p__Marinisomatota_100_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,p__Marinisomatota_100_1  
![Model bubble plot](loop_1/p__Marinisomatota_100_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Marinisomatota_100/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Marinisomatota_100/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Marinisomatota_100/ref_tree.tre ../Result/safe_phyla/p__Marinisomatota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Marinisomatota_100/loop_1/tree_update/p__Marinisomatota_100_1.treefile
```
  
  Runtime: 1721.77 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Marinisomatota_100/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Marinisomatota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Marinisomatota_100/loop_1/tree_update/p__Marinisomatota_100_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Marinisomatota_100/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 82  
Normalized RF distance: 0.1507  
Tree 1 branch length: 41.2724  
Tree 2 branch length: 57.993352414  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.989039654499413  
Euclidean distance: 0.7667395477357948  
Time usage for Loop_1: 41296.69 seconds (11.47 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Marinisomatota_100/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,Q.INSECT,LG,p__Marinisomatota_100_1 -mdef ../Result/safe_phyla/p__Marinisomatota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Marinisomatota_100/loop_1/tree_update/p__Marinisomatota_100_1.treefile -pre ../Result/safe_phyla/p__Marinisomatota_100/loop_1/test_model/p__Marinisomatota_100_test_concat
```
  
  Runtime: 917.01 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Marinisomatota_100_1+I+G4 | -854232.382 | 1713278.797 |
| p__Marinisomatota_100_1+F+I+G4 | -857346.954 | 1719674.548 |
| Q.YEAST+I+G4 | -857916.211 | 1720646.456 |
| LG+F+I+G4 | -859465.159 | 1723910.957 |
| Q.YEAST+G4 | -859783.912 | 1724373.089 |
| Q.INSECT+I+G4 | -860020.980 | 1724855.993 |
| Q.YEAST+F+I+G4 | -861662.455 | 1728305.548 |
| LG+I+G4 | -862257.104 | 1729328.241 |
| Q.INSECT+F+I+G4 | -862928.478 | 1730837.595 |
| Q.YEAST+I | -929283.827 | 1863372.918 |
| Q.YEAST | -954093.725 | 1912983.946 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Marinisomatota_100/loop_1/tree_update/p__Marinisomatota_100_1.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Marinisomatota_100/loop_2/subtrees -m random
```
  
Original number of taxa: 275   
Number of pruned subtrees: 6   
Number of taxa after pruning: 275   
Pruned node IDs (degree): 9 (76) 11 (48) 193 (16) 165 (29) 61 (86) 146 (20)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Marinisomatota_100/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 100 loci files. Total number of potential alignments: 600.  
Obtained 587 alignments from all potential alignments.  
Remaining 587 alignments. Deleted 13 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Marinisomatota_100/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,p__Marinisomatota_100_1 -mdef ../Result/safe_phyla/p__Marinisomatota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Marinisomatota_100/loop_2/subtree_update/p__Marinisomatota_100
```
  
  Runtime: 6774.82 seconds
[Subtree update log](loop_2/subtree_update/p__Marinisomatota_100.iqtree)  
Best models for iteration 2:  
p__Marinisomatota_100_1  

| Model | Count |
|-------|-------|
| 536 | p__Marinisomatota_100_1 |
| 26 | LG |
| 13 | Q.YEAST |
| 12 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Marinisomatota_100/loop_2/subtree_update/p__Marinisomatota_100.best_scheme.nex -te ../Result/safe_phyla/p__Marinisomatota_100/loop_2/subtree_update/p__Marinisomatota_100.treefile --model-joint GTR20+FO --init-model p__Marinisomatota_100_1 -mdef ../Result/safe_phyla/p__Marinisomatota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Marinisomatota_100/loop_2/model_update/p__Marinisomatota_100
```
  
  Runtime: 23704.10 seconds
[Model update log](loop_2/model_update/p__Marinisomatota_100.iqtree)  
BIC of the new model: 10687688.4116  
Likelihood of the new model: -5073802.6435  
Model does not meet precision requirement.  
[New model](trained_models/p__Marinisomatota_100_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Marinisomatota_100_2  
![Model bubble plot](loop_2/p__Marinisomatota_100_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Marinisomatota_100/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Marinisomatota_100/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Marinisomatota_100/ref_tree.tre ../Result/safe_phyla/p__Marinisomatota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Marinisomatota_100/loop_2/tree_update/p__Marinisomatota_100_2.treefile
```
  
  Runtime: 1750.10 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Marinisomatota_100/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Marinisomatota_100/loop_1/tree_update/p__Marinisomatota_100_1.treefile', tree2_path = '../Result/safe_phyla/p__Marinisomatota_100/loop_2/tree_update/p__Marinisomatota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Marinisomatota_100/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0074  
Tree 1 branch length: 57.993352414  
Tree 2 branch length: 57.861217785  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999579376288431  
Euclidean distance: 0.047534629039036394  
Time usage for Loop_2: 32322.56 seconds (8.98 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Marinisomatota_100/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Marinisomatota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Marinisomatota_100/loop_2/tree_update/p__Marinisomatota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Marinisomatota_100/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 86  
Normalized RF distance: 0.1581  
Tree 1 branch length: 41.2724  
Tree 2 branch length: 57.861217785  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Marinisomatota_100_2):  
Pearson's correlation: 0.9884082981259275  
Euclidean distance: 0.7886694532753606  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Marinisomatota_100/loop_2/tree_update/p__Marinisomatota_100_2.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Marinisomatota_100/final_test/subtrees -m random
```
  
Original number of taxa: 275   
Number of pruned subtrees: 6   
Number of taxa after pruning: 275   
Pruned node IDs (degree): 9 (76) 11 (48) 193 (16) 165 (29) 61 (86) 146 (20)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Marinisomatota_100/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 18 loci files. Total number of potential alignments: 108.  
Obtained 104 alignments from all potential alignments.  
Remaining 104 alignments. Deleted 4 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Marinisomatota_100/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Marinisomatota_100_2 -mdef ../Result/safe_phyla/p__Marinisomatota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Marinisomatota_100/final_test/p__Marinisomatota_100_test_partition
```
  
  Runtime: 365.38 seconds
Best models for test data:  
p__Marinisomatota_100_2  

| Model | Count |
|-------|-------|
| 92 | p__Marinisomatota_100_2 |
| 5 | LG |
| 2 | Q.YEAST |
| 2 | MTMET |
| 1 | Q.PFAM |
| 1 | Q.INSECT |
| 1 | MTART |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Marinisomatota_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Marinisomatota_100_2 -mdef ../Result/safe_phyla/p__Marinisomatota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Marinisomatota_100/loop_2/tree_update/p__Marinisomatota_100_2.treefile -pre ../Result/safe_phyla/p__Marinisomatota_100/final_test/p__Marinisomatota_100_test_concat
```
  
  Runtime: 1121.66 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Marinisomatota_100_2+I+G4 | -854281.731 | 1713377.496 |
| p__Marinisomatota_100_2+F+I+G4 | -857338.001 | 1719656.641 |
| Q.YEAST+I+G4 | -857943.404 | 1720700.841 |
| LG+F+I+G4 | -859492.162 | 1723964.962 |
| Q.INSECT+I+G4 | -860053.118 | 1724920.269 |
| Q.PFAM+F+I+G4 | -860473.531 | 1725927.701 |
| Q.YEAST+F+I+G4 | -861692.574 | 1728365.786 |
| LG+I+G4 | -862282.503 | 1729379.039 |
| Q.INSECT+F+I+G4 | -862961.146 | 1730902.931 |
| Q.PFAM+I+G4 | -863977.885 | 1732769.802 |
| LG+G4 | -864060.918 | 1732927.101 |
| MTMET+F+I+G4 | -872911.356 | 1750803.351 |
| MTART+F+I+G4 | -880272.588 | 1765525.815 |
| MTMET+I+G4 | -895673.612 | 1796161.257 |
| MTART+I+G4 | -907720.004 | 1820254.041 |
| LG+I | -929017.869 | 1862841.002 |
| LG | -952333.211 | 1909462.917 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Marinisomatota_100/trained_models/trained_model.nex ../Result/safe_phyla/p__Marinisomatota_100/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 76068.35 seconds (21.13 h)  
