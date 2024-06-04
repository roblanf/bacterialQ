## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Synergistota_100  
  Taxa name: p__Synergistota  
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
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Synergistota_100/select_id.txt. Sampling sequences for 99 loci.  
Number of input species: 208  
Remaining 99 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Synergistota_100/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 208  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Synergistota_100/ref_tree.tre -l 5 -u 100 -o ../Result/safe_phyla/p__Synergistota_100/loop_1/subtrees -m random
```
  
Original number of taxa: 208   
Number of pruned subtrees: 3   
Number of taxa after pruning: 208   
Pruned node IDs (degree): 81 (99) 8 (95) 179 (14)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Synergistota_100/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 99 loci files. Total number of potential alignments: 297.  
Obtained 297 alignments from all potential alignments.  
Remaining 297 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Synergistota_100/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Synergistota_100/loop_1/subtree_update/p__Synergistota_100
```
  
  Runtime: 10304.43 seconds
[Subtree update log](loop_1/subtree_update/p__Synergistota_100.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| 110 | Q.INSECT |
| 91 | LG |
| 76 | Q.PFAM |
| 20 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Synergistota_100/loop_1/subtree_update/p__Synergistota_100.best_scheme.nex -te ../Result/safe_phyla/p__Synergistota_100/loop_1/subtree_update/p__Synergistota_100.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result/safe_phyla/p__Synergistota_100/loop_1/model_update/p__Synergistota_100
```
  
  Runtime: 14424.29 seconds
[Model update log](loop_1/model_update/p__Synergistota_100.iqtree)  
BIC of the new model: 7837463.4043  
Likelihood of the new model: -3706604.3884  
Model does not meet precision requirement.  
[New model](trained_models/p__Synergistota_100_1)  
Model set for next iteration: Q.INSECT,LG,Q.PFAM,Q.YEAST,p__Synergistota_100_1  
![Model bubble plot](loop_1/p__Synergistota_100_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Synergistota_100/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Synergistota_100/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Synergistota_100/ref_tree.tre ../Result/safe_phyla/p__Synergistota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Synergistota_100/loop_1/tree_update/p__Synergistota_100_1.treefile
```
  
  Runtime: 501.48 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Synergistota_100/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Synergistota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Synergistota_100/loop_1/tree_update/p__Synergistota_100_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Synergistota_100/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 38  
Normalized RF distance: 0.0927  
Tree 1 branch length: 27.96226  
Tree 2 branch length: 40.775740871  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9911561081457321  
Euclidean distance: 0.7311295394839379  
Time usage for Loop_1: 25242.93 seconds (7.01 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Synergistota_100/loci/concat_testing_loci.faa -m TESTONLY -mset Q.INSECT,LG,Q.PFAM,Q.YEAST,p__Synergistota_100_1 -mdef ../Result/safe_phyla/p__Synergistota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Synergistota_100/loop_1/tree_update/p__Synergistota_100_1.treefile -pre ../Result/safe_phyla/p__Synergistota_100/loop_1/test_model/p__Synergistota_100_test_concat
```
  
  Runtime: 185.05 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Synergistota_100_1+I+G4 | -692653.897 | 1388946.237 |
| p__Synergistota_100_1+F+I+G4 | -694251.619 | 1392308.258 |
| LG+F+I+G4 | -696313.739 | 1396432.499 |
| Q.INSECT+I+G4 | -696800.919 | 1397240.280 |
| Q.YEAST+F+I+G4 | -696924.464 | 1397653.949 |
| Q.PFAM+F+I+G4 | -697014.977 | 1397834.975 |
| Q.INSECT+F+I+G4 | -697186.427 | 1398177.874 |
| Q.PFAM+I+G4 | -697673.362 | 1398985.165 |
| LG+I+G4 | -697721.134 | 1399080.710 |
| Q.YEAST+I+G4 | -697911.939 | 1399462.321 |
| Q.INSECT+G4 | -698155.706 | 1399941.087 |
| Q.INSECT+I | -757165.396 | 1517960.466 |
| Q.INSECT | -776647.994 | 1556916.894 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Synergistota_100/loop_1/tree_update/p__Synergistota_100_1.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Synergistota_100/loop_2/subtrees -m random
```
  
Original number of taxa: 208   
Number of pruned subtrees: 3   
Number of taxa after pruning: 208   
Pruned node IDs (degree): 76 (99) 3 (95) 174 (14)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Synergistota_100/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 99 loci files. Total number of potential alignments: 297.  
Obtained 297 alignments from all potential alignments.  
Remaining 297 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Synergistota_100/loop_2/training_loci -m MFP -mset Q.INSECT,LG,Q.PFAM,Q.YEAST,p__Synergistota_100_1 -mdef ../Result/safe_phyla/p__Synergistota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Synergistota_100/loop_2/subtree_update/p__Synergistota_100
```
  
  Runtime: 8874.14 seconds
[Subtree update log](loop_2/subtree_update/p__Synergistota_100.iqtree)  
Best models for iteration 2:  
p__Synergistota_100_1  

| Model | Count |
|-------|-------|
| 268 | p__Synergistota_100_1 |
| 13 | LG |
| 7 | Q.PFAM |
| 7 | Q.INSECT |
| 2 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Synergistota_100/loop_2/subtree_update/p__Synergistota_100.best_scheme.nex -te ../Result/safe_phyla/p__Synergistota_100/loop_2/subtree_update/p__Synergistota_100.treefile --model-joint GTR20+FO --init-model p__Synergistota_100_1 -mdef ../Result/safe_phyla/p__Synergistota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Synergistota_100/loop_2/model_update/p__Synergistota_100
```
  
  Runtime: 12883.24 seconds
[Model update log](loop_2/model_update/p__Synergistota_100.iqtree)  
BIC of the new model: 7836763.9339  
Likelihood of the new model: -3706127.8207  
Model does not meet precision requirement.  
[New model](trained_models/p__Synergistota_100_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Synergistota_100_2  
![Model bubble plot](loop_2/p__Synergistota_100_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Synergistota_100/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Synergistota_100/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Synergistota_100/ref_tree.tre ../Result/safe_phyla/p__Synergistota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Synergistota_100/loop_2/tree_update/p__Synergistota_100_2.treefile
```
  
  Runtime: 501.60 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Synergistota_100/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Synergistota_100/loop_1/tree_update/p__Synergistota_100_1.treefile', tree2_path = '../Result/safe_phyla/p__Synergistota_100/loop_2/tree_update/p__Synergistota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Synergistota_100/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 40.775740871  
Tree 2 branch length: 40.823511275  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999869307173403  
Euclidean distance: 0.029628292481126955  
Time usage for Loop_2: 22276.75 seconds (6.19 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Synergistota_100/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Synergistota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Synergistota_100/loop_2/tree_update/p__Synergistota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Synergistota_100/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 38  
Normalized RF distance: 0.0927  
Tree 1 branch length: 27.96226  
Tree 2 branch length: 40.823511275  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (p__Synergistota_100_2):  
Pearson's correlation: 0.9907802221766167  
Euclidean distance: 0.7495226287580503  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Synergistota_100/loop_2/tree_update/p__Synergistota_100_2.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Synergistota_100/final_test/subtrees -m random
```
  
Original number of taxa: 208   
Number of pruned subtrees: 3   
Number of taxa after pruning: 208   
Pruned node IDs (degree): 76 (99) 3 (95) 174 (14)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Synergistota_100/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 19 loci files. Total number of potential alignments: 57.  
Obtained 57 alignments from all potential alignments.  
Remaining 57 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Synergistota_100/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Synergistota_100_2 -mdef ../Result/safe_phyla/p__Synergistota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Synergistota_100/final_test/p__Synergistota_100_test_partition
```
  
  Runtime: 215.03 seconds
Best models for test data:  
p__Synergistota_100_2  

| Model | Count |
|-------|-------|
| 53 | p__Synergistota_100_2 |
| 2 | Q.INSECT |
| 1 | Q.PFAM |
| 1 | LG |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Synergistota_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Synergistota_100_2 -mdef ../Result/safe_phyla/p__Synergistota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Synergistota_100/loop_2/tree_update/p__Synergistota_100_2.treefile -pre ../Result/safe_phyla/p__Synergistota_100/final_test/p__Synergistota_100_test_concat
```
  
  Runtime: 248.14 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Synergistota_100_2+I+G4 | -692669.074 | 1388976.590 |
| p__Synergistota_100_2+F+I+G4 | -694250.332 | 1392305.684 |
| LG+F+I+G4 | -696313.734 | 1396432.489 |
| Q.INSECT+I+G4 | -696800.923 | 1397240.288 |
| Q.YEAST+F+I+G4 | -696924.464 | 1397653.949 |
| Q.PFAM+F+I+G4 | -697014.976 | 1397834.974 |
| Q.INSECT+F+I+G4 | -697186.428 | 1398177.878 |
| Q.PFAM+I+G4 | -697673.361 | 1398985.165 |
| LG+I+G4 | -697721.136 | 1399080.713 |
| Q.YEAST+I+G4 | -697911.940 | 1399462.321 |
| LG+G4 | -698964.136 | 1401557.945 |
| MTMET+F+I+G4 | -710492.016 | 1424789.053 |
| MTART+F+I+G4 | -723117.323 | 1450039.667 |
| MTMET+I+G4 | -737865.464 | 1479369.370 |
| MTART+I+G4 | -750604.477 | 1504847.396 |
| LG+I | -755883.818 | 1515397.309 |
| LG | -774068.051 | 1551757.008 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Synergistota_100/trained_models/trained_model.nex ../Result/safe_phyla/p__Synergistota_100/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 48200.58 seconds (13.39 h)  
