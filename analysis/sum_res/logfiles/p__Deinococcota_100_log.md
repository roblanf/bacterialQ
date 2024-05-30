## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Deinococcota_100  
  Taxa name: p__Deinococcota  
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
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Deinococcota_100/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 211  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Deinococcota_100/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 211  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Deinococcota_100/ref_tree.tre -l 5 -u 100 -o ../Result/safe_phyla/p__Deinococcota_100/loop_1/subtrees -m random
```
  
Original number of taxa: 211   
Number of pruned subtrees: 3   
Number of taxa after pruning: 211   
Pruned node IDs (degree): 97 (43) 2 (74) 4 (94)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Deinococcota_100/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 98 loci files. Total number of potential alignments: 294.  
Obtained 294 alignments from all potential alignments.  
Remaining 294 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deinococcota_100/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Deinococcota_100/loop_1/subtree_update/p__Deinococcota_100
```
  
  Runtime: 11655.50 seconds
[Subtree update log](loop_1/subtree_update/p__Deinococcota_100.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| 93 | Q.PFAM |
| 93 | LG |
| 76 | Q.INSECT |
| 32 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deinococcota_100/loop_1/subtree_update/p__Deinococcota_100.best_scheme.nex -te ../Result/safe_phyla/p__Deinococcota_100/loop_1/subtree_update/p__Deinococcota_100.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre ../Result/safe_phyla/p__Deinococcota_100/loop_1/model_update/p__Deinococcota_100
```
  
  Runtime: 23005.73 seconds
[Model update log](loop_1/model_update/p__Deinococcota_100.iqtree)  
BIC of the new model: 5929671.4844  
Likelihood of the new model: -2740975.4387  
Model does not meet precision requirement.  
[New model](trained_models/p__Deinococcota_100_1)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Deinococcota_100_1  
![Model bubble plot](loop_1/p__Deinococcota_100_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Deinococcota_100/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Deinococcota_100/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Deinococcota_100/ref_tree.tre ../Result/safe_phyla/p__Deinococcota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Deinococcota_100/loop_1/tree_update/p__Deinococcota_100_1.treefile
```
  
  Runtime: 1244.28 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Deinococcota_100/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Deinococcota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Deinococcota_100/loop_1/tree_update/p__Deinococcota_100_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Deinococcota_100/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 30  
Normalized RF distance: 0.0721  
Tree 1 branch length: 19.29548  
Tree 2 branch length: 25.896411863  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9804441743426249  
Euclidean distance: 1.178795052723117  
Time usage for Loop_1: 35959.59 seconds (9.99 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Deinococcota_100/loci/concat_testing_loci.faa -m TESTONLY -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Deinococcota_100_1 -mdef ../Result/safe_phyla/p__Deinococcota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Deinococcota_100/loop_1/tree_update/p__Deinococcota_100_1.treefile -pre ../Result/safe_phyla/p__Deinococcota_100/loop_1/test_model/p__Deinococcota_100_test_concat
```
  
  Runtime: 670.86 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Deinococcota_100_1+I+G4 | -508188.099 | 1020067.243 |
| p__Deinococcota_100_1+F+I+G4 | -509166.304 | 1022190.233 |
| LG+F+I+G4 | -511405.338 | 1026668.300 |
| Q.PFAM+F+I+G4 | -511805.591 | 1027468.806 |
| Q.YEAST+F+I+G4 | -512006.464 | 1027870.553 |
| Q.INSECT+F+I+G4 | -512467.545 | 1028792.714 |
| Q.PFAM+I+G4 | -513679.989 | 1031051.023 |
| Q.PFAM+G4 | -514710.131 | 1033102.540 |
| LG+I+G4 | -514891.253 | 1033473.551 |
| Q.INSECT+I+G4 | -516917.589 | 1037526.224 |
| Q.YEAST+I+G4 | -518239.124 | 1040169.293 |
| Q.PFAM+I | -552025.889 | 1107734.056 |
| Q.PFAM | -569397.600 | 1142468.711 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Deinococcota_100/loop_1/tree_update/p__Deinococcota_100_1.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Deinococcota_100/loop_2/subtrees -m random
```
  
Original number of taxa: 211   
Number of pruned subtrees: 3   
Number of taxa after pruning: 211   
Pruned node IDs (degree): 96 (43) 3 (94) 210 (74)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Deinococcota_100/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 98 loci files. Total number of potential alignments: 294.  
Obtained 294 alignments from all potential alignments.  
Remaining 294 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deinococcota_100/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Deinococcota_100_1 -mdef ../Result/safe_phyla/p__Deinococcota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Deinococcota_100/loop_2/subtree_update/p__Deinococcota_100
```
  
  Runtime: 10465.01 seconds
[Subtree update log](loop_2/subtree_update/p__Deinococcota_100.iqtree)  
Best models for iteration 2:  
p__Deinococcota_100_1  

| Model | Count |
|-------|-------|
| 263 | p__Deinococcota_100_1 |
| 13 | Q.INSECT |
| 11 | LG |
| 7 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deinococcota_100/loop_2/subtree_update/p__Deinococcota_100.best_scheme.nex -te ../Result/safe_phyla/p__Deinococcota_100/loop_2/subtree_update/p__Deinococcota_100.treefile --model-joint GTR20+FO --init-model p__Deinococcota_100_1 -mdef ../Result/safe_phyla/p__Deinococcota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Deinococcota_100/loop_2/model_update/p__Deinococcota_100
```
  
  Runtime: 20739.16 seconds
[Model update log](loop_2/model_update/p__Deinococcota_100.iqtree)  
BIC of the new model: 5928256.9592  
Likelihood of the new model: -2740193.2718  
Model does not meet precision requirement.  
[New model](trained_models/p__Deinococcota_100_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Deinococcota_100_2  
![Model bubble plot](loop_2/p__Deinococcota_100_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Deinococcota_100/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Deinococcota_100/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Deinococcota_100/ref_tree.tre ../Result/safe_phyla/p__Deinococcota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Deinococcota_100/loop_2/tree_update/p__Deinococcota_100_2.treefile
```
  
  Runtime: 1211.87 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Deinococcota_100/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Deinococcota_100/loop_1/tree_update/p__Deinococcota_100_1.treefile', tree2_path = '../Result/safe_phyla/p__Deinococcota_100/loop_2/tree_update/p__Deinococcota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Deinococcota_100/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 25.896411863  
Tree 2 branch length: 25.944092042  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999291101077052  
Euclidean distance: 0.08214438869860617  
Time usage for Loop_2: 32469.20 seconds (9.02 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Deinococcota_100/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Deinococcota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Deinococcota_100/loop_2/tree_update/p__Deinococcota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Deinococcota_100/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 30  
Normalized RF distance: 0.0721  
Tree 1 branch length: 19.29548  
Tree 2 branch length: 25.944092042  
### Model comparison  
Comparison between initial best model (Q.PFAM) and final model (p__Deinococcota_100_2):  
Pearson's correlation: 0.9788349298695869  
Euclidean distance: 1.241820918254587  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Deinococcota_100/loop_2/tree_update/p__Deinococcota_100_2.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Deinococcota_100/final_test/subtrees -m random
```
  
Original number of taxa: 211   
Number of pruned subtrees: 3   
Number of taxa after pruning: 211   
Pruned node IDs (degree): 96 (43) 3 (94) 210 (74)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Deinococcota_100/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 19 loci files. Total number of potential alignments: 57.  
Obtained 57 alignments from all potential alignments.  
Remaining 57 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deinococcota_100/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Deinococcota_100_2 -mdef ../Result/safe_phyla/p__Deinococcota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Deinococcota_100/final_test/p__Deinococcota_100_test_partition
```
  
  Runtime: 421.69 seconds
Best models for test data:  
p__Deinococcota_100_2  

| Model | Count |
|-------|-------|
| 52 | p__Deinococcota_100_2 |
| 4 | LG |
| 1 | Q.YEAST |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Deinococcota_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Deinococcota_100_2 -mdef ../Result/safe_phyla/p__Deinococcota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Deinococcota_100/loop_2/tree_update/p__Deinococcota_100_2.treefile -pre ../Result/safe_phyla/p__Deinococcota_100/final_test/p__Deinococcota_100_test_concat
```
  
  Runtime: 1079.97 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Deinococcota_100_2+I+G4 | -508216.185 | 1020123.415 |
| p__Deinococcota_100_2+F+I+G4 | -509225.937 | 1022309.498 |
| LG+F+I+G4 | -511405.336 | 1026668.296 |
| Q.PFAM+F+I+G4 | -511805.589 | 1027468.804 |
| Q.YEAST+F+I+G4 | -512006.469 | 1027870.562 |
| Q.INSECT+F+I+G4 | -512467.543 | 1028792.711 |
| Q.PFAM+I+G4 | -513679.993 | 1031051.031 |
| LG+I+G4 | -514891.240 | 1033473.526 |
| LG+G4 | -515943.679 | 1035569.636 |
| Q.INSECT+I+G4 | -516917.589 | 1037526.223 |
| Q.YEAST+I+G4 | -518239.122 | 1040169.290 |
| MTMET+F+I+G4 | -529987.337 | 1063832.299 |
| MTART+F+I+G4 | -541898.060 | 1087653.745 |
| LG+I | -553175.997 | 1110034.272 |
| MTMET+I+G4 | -558584.174 | 1120859.394 |
| MTART+I+G4 | -570078.291 | 1143847.628 |
| LG | -570696.241 | 1145065.994 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Deinococcota_100/trained_models/trained_model.nex ../Result/safe_phyla/p__Deinococcota_100/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 70677.12 seconds (19.63 h)  
