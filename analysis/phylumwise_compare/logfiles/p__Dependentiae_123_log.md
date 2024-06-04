## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Dependentiae_123  
  Taxa name: p__Dependentiae  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 123  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 14 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Dependentiae_123/select_id.txt. Sampling sequences for 86 loci.  
Number of input species: 123  
Remaining 86 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 4 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Dependentiae_123/select_id.txt. Sampling sequences for 16 loci.  
Number of input species: 123  
Remaining 16 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Dependentiae_123/ref_tree.tre -l 5 -u 123 -o ../Result/safe_phyla/p__Dependentiae_123/loop_1/subtrees -m random
```
  
Original number of taxa: 123   
Number of pruned subtrees: 1   
Number of taxa after pruning: 123   
Pruned node IDs (degree): 1 (123)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Dependentiae_123/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 86 loci files. Total number of potential alignments: 86.  
Obtained 86 alignments from all potential alignments.  
Remaining 86 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Dependentiae_123/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Dependentiae_123/loop_1/subtree_update/p__Dependentiae_123
```
  
  Runtime: 25392.03 seconds
[Subtree update log](loop_1/subtree_update/p__Dependentiae_123.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 43 | Q.YEAST |
| 16 | Q.INSECT |
| 16 | LG |
| 11 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Dependentiae_123/loop_1/subtree_update/p__Dependentiae_123.best_scheme.nex -te ../Result/safe_phyla/p__Dependentiae_123/loop_1/subtree_update/p__Dependentiae_123.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Dependentiae_123/loop_1/model_update/p__Dependentiae_123
```
  
  Runtime: 36592.26 seconds
[Model update log](loop_1/model_update/p__Dependentiae_123.iqtree)  
BIC of the new model: 6055187.8127  
Likelihood of the new model: -2929318.9993  
Model does not meet precision requirement.  
[New model](trained_models/p__Dependentiae_123_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.PFAM,p__Dependentiae_123_1  
![Model bubble plot](loop_1/p__Dependentiae_123_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Dependentiae_123/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Dependentiae_123/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Dependentiae_123/ref_tree.tre ../Result/safe_phyla/p__Dependentiae_123/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Dependentiae_123/loop_1/tree_update/p__Dependentiae_123_1.treefile
```
  
  Runtime: 668.55 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Dependentiae_123/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Dependentiae_123/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Dependentiae_123/loop_1/tree_update/p__Dependentiae_123_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Dependentiae_123/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 54  
Normalized RF distance: 0.225  
Tree 1 branch length: 37.04804  
Tree 2 branch length: 50.473629733  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9917013960708948  
Euclidean distance: 0.6683362782071379  
Time usage for Loop_1: 62696.41 seconds (17.42 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Dependentiae_123/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,Q.INSECT,LG,Q.PFAM,p__Dependentiae_123_1 -mdef ../Result/safe_phyla/p__Dependentiae_123/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Dependentiae_123/loop_1/tree_update/p__Dependentiae_123_1.treefile -pre ../Result/safe_phyla/p__Dependentiae_123/loop_1/test_model/p__Dependentiae_123_test_concat
```
  
  Runtime: 535.39 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Dependentiae_123_1+I+G4 | -604149.849 | 1210433.922 |
| Q.YEAST+I+G4 | -605883.198 | 1213900.619 |
| LG+F+I+G4 | -606849.841 | 1215999.416 |
| Q.INSECT+I+G4 | -607053.675 | 1216241.572 |
| Q.YEAST+G4 | -607087.228 | 1216299.968 |
| p__Dependentiae_123_1+F+I+G4 | -607001.244 | 1216302.222 |
| Q.YEAST+F+I+G4 | -607338.760 | 1216977.253 |
| Q.PFAM+F+I+G4 | -607375.650 | 1217051.034 |
| LG+I+G4 | -607697.813 | 1217529.848 |
| Q.PFAM+I+G4 | -608194.605 | 1218523.433 |
| Q.INSECT+F+I+G4 | -608852.649 | 1220005.032 |
| Q.YEAST+I | -654724.467 | 1311574.446 |
| Q.YEAST | -674347.173 | 1350811.147 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Dependentiae_123/loop_1/tree_update/p__Dependentiae_123_1.treefile -l 5 -u 123 -o ../Result/safe_phyla/p__Dependentiae_123/loop_2/subtrees -m random
```
  
Original number of taxa: 123   
Number of pruned subtrees: 1   
Number of taxa after pruning: 123   
Pruned node IDs (degree): 1 (123)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Dependentiae_123/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 86 loci files. Total number of potential alignments: 86.  
Obtained 86 alignments from all potential alignments.  
Remaining 86 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Dependentiae_123/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.PFAM,p__Dependentiae_123_1 -mdef ../Result/safe_phyla/p__Dependentiae_123/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Dependentiae_123/loop_2/subtree_update/p__Dependentiae_123
```
  
  Runtime: 28481.52 seconds
[Subtree update log](loop_2/subtree_update/p__Dependentiae_123.iqtree)  
Best models for iteration 2:  
p__Dependentiae_123_1  

| Model | Count |
|-------|-------|
| 71 | p__Dependentiae_123_1 |
| 6 | Q.INSECT |
| 5 | LG |
| 3 | Q.PFAM |
| 1 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Dependentiae_123/loop_2/subtree_update/p__Dependentiae_123.best_scheme.nex -te ../Result/safe_phyla/p__Dependentiae_123/loop_2/subtree_update/p__Dependentiae_123.treefile --model-joint GTR20+FO --init-model p__Dependentiae_123_1 -mdef ../Result/safe_phyla/p__Dependentiae_123/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Dependentiae_123/loop_2/model_update/p__Dependentiae_123
```
  
  Runtime: 43097.45 seconds
[Model update log](loop_2/model_update/p__Dependentiae_123.iqtree)  
BIC of the new model: 6054628.6482  
Likelihood of the new model: -2928890.5468  
Model does not meet precision requirement.  
[New model](trained_models/p__Dependentiae_123_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Dependentiae_123_2  
![Model bubble plot](loop_2/p__Dependentiae_123_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Dependentiae_123/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Dependentiae_123/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Dependentiae_123/ref_tree.tre ../Result/safe_phyla/p__Dependentiae_123/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Dependentiae_123/loop_2/tree_update/p__Dependentiae_123_2.treefile
```
  
  Runtime: 991.97 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Dependentiae_123/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Dependentiae_123/loop_1/tree_update/p__Dependentiae_123_1.treefile', tree2_path = '../Result/safe_phyla/p__Dependentiae_123/loop_2/tree_update/p__Dependentiae_123_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Dependentiae_123/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 50.473629733  
Tree 2 branch length: 50.594621668  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998681674073701  
Euclidean distance: 0.0947000983857552  
Time usage for Loop_2: 72612.91 seconds (20.17 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Dependentiae_123/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Dependentiae_123/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Dependentiae_123/loop_2/tree_update/p__Dependentiae_123_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Dependentiae_123/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 54  
Normalized RF distance: 0.225  
Tree 1 branch length: 37.04804  
Tree 2 branch length: 50.594621668  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Dependentiae_123_2):  
Pearson's correlation: 0.990606969495406  
Euclidean distance: 0.7158650199717461  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Dependentiae_123/loop_2/tree_update/p__Dependentiae_123_2.treefile -l 5 -u 123 -o ../Result/safe_phyla/p__Dependentiae_123/final_test/subtrees -m random
```
  
Original number of taxa: 123   
Number of pruned subtrees: 1   
Number of taxa after pruning: 123   
Pruned node IDs (degree): 1 (123)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Dependentiae_123/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 16 loci files. Total number of potential alignments: 16.  
Obtained 16 alignments from all potential alignments.  
Remaining 16 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Dependentiae_123/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Dependentiae_123_2 -mdef ../Result/safe_phyla/p__Dependentiae_123/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Dependentiae_123/final_test/p__Dependentiae_123_test_partition
```
  
  Runtime: 23841.74 seconds
Best models for test data:  
p__Dependentiae_123_2  

| Model | Count |
|-------|-------|
| 12 | p__Dependentiae_123_2 |
| 1 | Q.YEAST |
| 1 | Q.INSECT |
| 1 | MTMET |
| 1 | LG |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Dependentiae_123/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Dependentiae_123_2 -mdef ../Result/safe_phyla/p__Dependentiae_123/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Dependentiae_123/loop_2/tree_update/p__Dependentiae_123_2.treefile -pre ../Result/safe_phyla/p__Dependentiae_123/final_test/p__Dependentiae_123_test_concat
```
  
  Runtime: 236.15 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Dependentiae_123_2+I+G4 | -604170.300 | 1210474.824 |
| Q.YEAST+I+G4 | -605883.201 | 1213900.624 |
| LG+F+I+G4 | -606849.839 | 1215999.411 |
| Q.INSECT+I+G4 | -607053.669 | 1216241.561 |
| p__Dependentiae_123_2+F+I+G4 | -607134.258 | 1216568.250 |
| Q.YEAST+F+I+G4 | -607338.759 | 1216977.252 |
| Q.PFAM+F+I+G4 | -607375.641 | 1217051.016 |
| LG+I+G4 | -607697.811 | 1217529.845 |
| Q.PFAM+I+G4 | -608194.606 | 1218523.435 |
| LG+G4 | -608830.397 | 1219786.307 |
| Q.INSECT+F+I+G4 | -608852.654 | 1220005.042 |
| MTMET+F+I+G4 | -619411.704 | 1241123.141 |
| MTART+F+I+G4 | -622103.038 | 1246505.809 |
| MTMET+I+G4 | -637410.986 | 1276956.195 |
| MTART+I+G4 | -640453.561 | 1283041.344 |
| LG+I | -653844.930 | 1309815.372 |
| LG | -672559.213 | 1347235.226 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Dependentiae_123/trained_models/trained_model.nex ../Result/safe_phyla/p__Dependentiae_123/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 160020.96 seconds (44.45 h)  
