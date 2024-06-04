## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Caldisericota_49  
  Taxa name: p__Caldisericota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 49  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Caldisericota_49/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 49  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Caldisericota_49/select_id.txt. Sampling sequences for 18 loci.  
Number of input species: 49  
Remaining 18 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Caldisericota_49/ref_tree.tre -l 5 -u 49 -o ../Result/safe_phyla/p__Caldisericota_49/loop_1/subtrees -m random
```
  
Original number of taxa: 49   
Number of pruned subtrees: 1   
Number of taxa after pruning: 49   
Pruned node IDs (degree): 1 (49)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Caldisericota_49/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 98 loci files. Total number of potential alignments: 98.  
Obtained 98 alignments from all potential alignments.  
Remaining 98 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Caldisericota_49/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Caldisericota_49/loop_1/subtree_update/p__Caldisericota_49
```
  
  Runtime: 1308.84 seconds
[Subtree update log](loop_1/subtree_update/p__Caldisericota_49.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 59 | Q.YEAST |
| 23 | LG |
| 14 | Q.INSECT |
| 2 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Caldisericota_49/loop_1/subtree_update/p__Caldisericota_49.best_scheme.nex -te ../Result/safe_phyla/p__Caldisericota_49/loop_1/subtree_update/p__Caldisericota_49.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Caldisericota_49/loop_1/model_update/p__Caldisericota_49
```
  
  Runtime: 3751.06 seconds
[Model update log](loop_1/model_update/p__Caldisericota_49.iqtree)  
BIC of the new model: 2162032.6592  
Likelihood of the new model: -1038136.5009  
Model does not meet precision requirement.  
[New model](trained_models/p__Caldisericota_49_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,p__Caldisericota_49_1  
![Model bubble plot](loop_1/p__Caldisericota_49_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Caldisericota_49/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Caldisericota_49/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Caldisericota_49/ref_tree.tre ../Result/safe_phyla/p__Caldisericota_49/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Caldisericota_49/loop_1/tree_update/p__Caldisericota_49_1.treefile
```
  
  Runtime: 98.19 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Caldisericota_49/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Caldisericota_49/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Caldisericota_49/loop_1/tree_update/p__Caldisericota_49_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Caldisericota_49/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0652  
Tree 1 branch length: 9.6693  
Tree 2 branch length: 12.581759875  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9932573889204186  
Euclidean distance: 0.624722819920663  
Time usage for Loop_1: 5166.39 seconds (1.44 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Caldisericota_49/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,LG,Q.INSECT,p__Caldisericota_49_1 -mdef ../Result/safe_phyla/p__Caldisericota_49/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Caldisericota_49/loop_1/tree_update/p__Caldisericota_49_1.treefile -pre ../Result/safe_phyla/p__Caldisericota_49/loop_1/test_model/p__Caldisericota_49_test_concat
```
  
  Runtime: 40.23 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Caldisericota_49_1+I+G4 | -190744.100 | 382331.940 |
| p__Caldisericota_49_1+F+I+G4 | -191109.486 | 383227.979 |
| LG+F+I+G4 | -191355.194 | 383719.397 |
| Q.YEAST+I+G4 | -191635.917 | 384115.573 |
| Q.YEAST+G4 | -191761.503 | 384358.048 |
| Q.YEAST+F+I+G4 | -191744.751 | 384498.511 |
| Q.INSECT+I+G4 | -191978.424 | 384800.587 |
| LG+I+G4 | -191988.452 | 384820.644 |
| Q.INSECT+F+I+G4 | -192051.289 | 385111.587 |
| Q.YEAST+I | -198547.763 | 397930.566 |
| Q.YEAST | -202739.378 | 406305.100 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Caldisericota_49/loop_1/tree_update/p__Caldisericota_49_1.treefile -l 5 -u 49 -o ../Result/safe_phyla/p__Caldisericota_49/loop_2/subtrees -m random
```
  
Original number of taxa: 49   
Number of pruned subtrees: 1   
Number of taxa after pruning: 49   
Pruned node IDs (degree): 1 (49)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Caldisericota_49/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 98 loci files. Total number of potential alignments: 98.  
Obtained 98 alignments from all potential alignments.  
Remaining 98 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Caldisericota_49/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,p__Caldisericota_49_1 -mdef ../Result/safe_phyla/p__Caldisericota_49/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Caldisericota_49/loop_2/subtree_update/p__Caldisericota_49
```
  
  Runtime: 956.70 seconds
[Subtree update log](loop_2/subtree_update/p__Caldisericota_49.iqtree)  
Best models for iteration 2:  
p__Caldisericota_49_1  

| Model | Count |
|-------|-------|
| 91 | p__Caldisericota_49_1 |
| 4 | LG |
| 3 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Caldisericota_49/loop_2/subtree_update/p__Caldisericota_49.best_scheme.nex -te ../Result/safe_phyla/p__Caldisericota_49/loop_2/subtree_update/p__Caldisericota_49.treefile --model-joint GTR20+FO --init-model p__Caldisericota_49_1 -mdef ../Result/safe_phyla/p__Caldisericota_49/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Caldisericota_49/loop_2/model_update/p__Caldisericota_49
```
  
  Runtime: 3285.11 seconds
[Model update log](loop_2/model_update/p__Caldisericota_49.iqtree)  
BIC of the new model: 2161988.507  
Likelihood of the new model: -1038051.8646  
Model does not meet precision requirement.  
[New model](trained_models/p__Caldisericota_49_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Caldisericota_49_2  
![Model bubble plot](loop_2/p__Caldisericota_49_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Caldisericota_49/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Caldisericota_49/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Caldisericota_49/ref_tree.tre ../Result/safe_phyla/p__Caldisericota_49/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Caldisericota_49/loop_2/tree_update/p__Caldisericota_49_2.treefile
```
  
  Runtime: 122.47 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Caldisericota_49/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Caldisericota_49/loop_1/tree_update/p__Caldisericota_49_1.treefile', tree2_path = '../Result/safe_phyla/p__Caldisericota_49/loop_2/tree_update/p__Caldisericota_49_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Caldisericota_49/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 12.581759875  
Tree 2 branch length: 12.596124051  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999823265909306  
Euclidean distance: 0.1005261018161065  
Time usage for Loop_2: 4372.40 seconds (1.21 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Caldisericota_49/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Caldisericota_49/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Caldisericota_49/loop_2/tree_update/p__Caldisericota_49_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Caldisericota_49/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0652  
Tree 1 branch length: 9.6693  
Tree 2 branch length: 12.596124051  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Caldisericota_49_2):  
Pearson's correlation: 0.9926825901950416  
Euclidean distance: 0.6466040616539511  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Caldisericota_49/loop_2/tree_update/p__Caldisericota_49_2.treefile -l 5 -u 49 -o ../Result/safe_phyla/p__Caldisericota_49/final_test/subtrees -m random
```
  
Original number of taxa: 49   
Number of pruned subtrees: 1   
Number of taxa after pruning: 49   
Pruned node IDs (degree): 1 (49)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Caldisericota_49/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 18 loci files. Total number of potential alignments: 18.  
Obtained 18 alignments from all potential alignments.  
Remaining 18 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Caldisericota_49/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Caldisericota_49_2 -mdef ../Result/safe_phyla/p__Caldisericota_49/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Caldisericota_49/final_test/p__Caldisericota_49_test_partition
```
  
  Runtime: 1516.36 seconds
Best models for test data:  
p__Caldisericota_49_2  

| Model | Count |
|-------|-------|
| 17 | p__Caldisericota_49_2 |
| 1 | Q.YEAST |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Caldisericota_49/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Caldisericota_49_2 -mdef ../Result/safe_phyla/p__Caldisericota_49/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Caldisericota_49/loop_2/tree_update/p__Caldisericota_49_2.treefile -pre ../Result/safe_phyla/p__Caldisericota_49/final_test/p__Caldisericota_49_test_concat
```
  
  Runtime: 62.83 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Caldisericota_49_2+I+G4 | -190741.109 | 382325.958 |
| p__Caldisericota_49_2+F+I+G4 | -191109.093 | 383227.193 |
| LG+F+I+G4 | -191355.188 | 383719.383 |
| Q.PFAM+F+I+G4 | -191507.749 | 384024.506 |
| Q.YEAST+I+G4 | -191635.906 | 384115.551 |
| Q.YEAST+F+I+G4 | -191744.749 | 384498.506 |
| Q.INSECT+I+G4 | -191978.427 | 384800.594 |
| LG+I+G4 | -191988.466 | 384820.672 |
| LG+G4 | -192124.378 | 385083.798 |
| Q.INSECT+F+I+G4 | -192051.291 | 385111.590 |
| Q.PFAM+I+G4 | -192325.586 | 385494.912 |
| MTMET+F+I+G4 | -194248.761 | 389506.529 |
| MTART+F+I+G4 | -196320.187 | 393649.382 |
| LG+I | -198244.738 | 397324.518 |
| MTMET+I+G4 | -201146.918 | 403137.576 |
| LG | -202082.720 | 404991.783 |
| MTART+I+G4 | -203907.392 | 408658.525 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Caldisericota_49/trained_models/trained_model.nex ../Result/safe_phyla/p__Caldisericota_49/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 11181.74 seconds (3.11 h)  
