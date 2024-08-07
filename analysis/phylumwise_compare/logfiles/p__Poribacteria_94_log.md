## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Poribacteria_94  
  Taxa name: p__Poribacteria  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 94  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 6 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Poribacteria_94/select_id.txt. Sampling sequences for 94 loci.  
Number of input species: 94  
Remaining 94 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Poribacteria_94/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 94  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Poribacteria_94/ref_tree.tre -l 5 -u 94 -o ../Result/safe_phyla/p__Poribacteria_94/loop_1/subtrees -m random
```
  
Original number of taxa: 94   
Number of pruned subtrees: 1   
Number of taxa after pruning: 94   
Pruned node IDs (degree): 1 (94)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Poribacteria_94/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 94 loci files. Total number of potential alignments: 94.  
Obtained 94 alignments from all potential alignments.  
Remaining 94 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Poribacteria_94/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Poribacteria_94/loop_1/subtree_update/p__Poribacteria_94
```
  
  Runtime: 7408.16 seconds
[Subtree update log](loop_1/subtree_update/p__Poribacteria_94.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| 40 | Q.INSECT |
| 26 | Q.PFAM |
| 25 | LG |
| 3 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Poribacteria_94/loop_1/subtree_update/p__Poribacteria_94.best_scheme.nex -te ../Result/safe_phyla/p__Poribacteria_94/loop_1/subtree_update/p__Poribacteria_94.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result/safe_phyla/p__Poribacteria_94/loop_1/model_update/p__Poribacteria_94
```
  
  Runtime: 14383.80 seconds
[Model update log](loop_1/model_update/p__Poribacteria_94.iqtree)  
BIC of the new model: 2695731.8317  
Likelihood of the new model: -1262970.1142  
Model does not meet precision requirement.  
[New model](trained_models/p__Poribacteria_94_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,p__Poribacteria_94_1  
![Model bubble plot](loop_1/p__Poribacteria_94_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Poribacteria_94/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Poribacteria_94/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Poribacteria_94/ref_tree.tre ../Result/safe_phyla/p__Poribacteria_94/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Poribacteria_94/loop_1/tree_update/p__Poribacteria_94_1.treefile
```
  
  Runtime: 489.71 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Poribacteria_94/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Poribacteria_94/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Poribacteria_94/loop_1/tree_update/p__Poribacteria_94_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Poribacteria_94/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 20  
Normalized RF distance: 0.1099  
Tree 1 branch length: 9.25482  
Tree 2 branch length: 12.475917822  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9847474713399812  
Euclidean distance: 0.9076153452049852  
Time usage for Loop_1: 22325.73 seconds (6.20 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Poribacteria_94/loci/concat_testing_loci.faa -m TESTONLY -mset Q.INSECT,Q.PFAM,LG,p__Poribacteria_94_1 -mdef ../Result/safe_phyla/p__Poribacteria_94/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Poribacteria_94/loop_1/tree_update/p__Poribacteria_94_1.treefile -pre ../Result/safe_phyla/p__Poribacteria_94/loop_1/test_model/p__Poribacteria_94_test_concat
```
  
  Runtime: 454.42 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Poribacteria_94_1+I+G4 | -276075.924 | 553804.331 |
| p__Poribacteria_94_1+F+I+G4 | -276421.368 | 554663.119 |
| LG+F+I+G4 | -278014.064 | 557848.511 |
| Q.PFAM+F+I+G4 | -278247.028 | 558314.438 |
| LG+I+G4 | -278370.482 | 558393.448 |
| Q.PFAM+I+G4 | -278378.254 | 558408.992 |
| Q.INSECT+F+I+G4 | -278432.737 | 558685.857 |
| Q.INSECT+I+G4 | -278710.707 | 559073.898 |
| Q.INSECT+G4 | -278947.155 | 559537.958 |
| Q.INSECT+I | -293618.968 | 588881.582 |
| Q.INSECT | -301630.210 | 604895.231 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Poribacteria_94/loop_1/tree_update/p__Poribacteria_94_1.treefile -l 5 -u 94 -o ../Result/safe_phyla/p__Poribacteria_94/loop_2/subtrees -m random
```
  
Original number of taxa: 94   
Number of pruned subtrees: 1   
Number of taxa after pruning: 94   
Pruned node IDs (degree): 1 (94)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Poribacteria_94/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 94 loci files. Total number of potential alignments: 94.  
Obtained 94 alignments from all potential alignments.  
Remaining 94 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Poribacteria_94/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,p__Poribacteria_94_1 -mdef ../Result/safe_phyla/p__Poribacteria_94/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Poribacteria_94/loop_2/subtree_update/p__Poribacteria_94
```
  
  Runtime: 8046.23 seconds
[Subtree update log](loop_2/subtree_update/p__Poribacteria_94.iqtree)  
Best models for iteration 2:  
p__Poribacteria_94_1  

| Model | Count |
|-------|-------|
| 92 | p__Poribacteria_94_1 |
| 2 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Poribacteria_94/loop_2/subtree_update/p__Poribacteria_94.best_scheme.nex -te ../Result/safe_phyla/p__Poribacteria_94/loop_2/subtree_update/p__Poribacteria_94.treefile --model-joint GTR20+FO --init-model p__Poribacteria_94_1 -mdef ../Result/safe_phyla/p__Poribacteria_94/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Poribacteria_94/loop_2/model_update/p__Poribacteria_94
```
  
  Runtime: 14314.53 seconds
[Model update log](loop_2/model_update/p__Poribacteria_94.iqtree)  
BIC of the new model: 2695357.73  
Likelihood of the new model: -1262746.7409  
Model does not meet precision requirement.  
[New model](trained_models/p__Poribacteria_94_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Poribacteria_94_2  
![Model bubble plot](loop_2/p__Poribacteria_94_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Poribacteria_94/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Poribacteria_94/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Poribacteria_94/ref_tree.tre ../Result/safe_phyla/p__Poribacteria_94/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Poribacteria_94/loop_2/tree_update/p__Poribacteria_94_2.treefile
```
  
  Runtime: 729.42 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Poribacteria_94/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Poribacteria_94/loop_1/tree_update/p__Poribacteria_94_1.treefile', tree2_path = '../Result/safe_phyla/p__Poribacteria_94/loop_2/tree_update/p__Poribacteria_94_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Poribacteria_94/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 12.475917822  
Tree 2 branch length: 12.484163241  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999381699909586  
Euclidean distance: 0.06176461448430948  
Time usage for Loop_2: 23162.13 seconds (6.43 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Poribacteria_94/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Poribacteria_94/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Poribacteria_94/loop_2/tree_update/p__Poribacteria_94_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Poribacteria_94/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 20  
Normalized RF distance: 0.1099  
Tree 1 branch length: 9.25482  
Tree 2 branch length: 12.484163241  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (p__Poribacteria_94_2):  
Pearson's correlation: 0.9837532056741092  
Euclidean distance: 0.9413857720802765  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Poribacteria_94/loop_2/tree_update/p__Poribacteria_94_2.treefile -l 5 -u 94 -o ../Result/safe_phyla/p__Poribacteria_94/final_test/subtrees -m random
```
  
Original number of taxa: 94   
Number of pruned subtrees: 1   
Number of taxa after pruning: 94   
Pruned node IDs (degree): 1 (94)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Poribacteria_94/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 20 loci files. Total number of potential alignments: 20.  
Obtained 20 alignments from all potential alignments.  
Remaining 20 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Poribacteria_94/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Poribacteria_94_2 -mdef ../Result/safe_phyla/p__Poribacteria_94/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Poribacteria_94/final_test/p__Poribacteria_94_test_partition
```
  
  Runtime: 20612.60 seconds
Best models for test data:  
p__Poribacteria_94_2  

| Model | Count |
|-------|-------|
| 19 | p__Poribacteria_94_2 |
| 1 | Q.INSECT |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Poribacteria_94/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Poribacteria_94_2 -mdef ../Result/safe_phyla/p__Poribacteria_94/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Poribacteria_94/loop_2/tree_update/p__Poribacteria_94_2.treefile -pre ../Result/safe_phyla/p__Poribacteria_94/final_test/p__Poribacteria_94_test_concat
```
  
  Runtime: 1378.20 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Poribacteria_94_2+I+G4 | -276084.417 | 553821.317 |
| p__Poribacteria_94_2+F+I+G4 | -276426.793 | 554673.968 |
| LG+F+I+G4 | -278014.051 | 557848.485 |
| Q.PFAM+F+I+G4 | -278247.039 | 558314.461 |
| LG+I+G4 | -278370.492 | 558393.466 |
| Q.PFAM+I+G4 | -278378.251 | 558408.986 |
| Q.INSECT+F+I+G4 | -278432.773 | 558685.928 |
| Q.YEAST+F+I+G4 | -278442.001 | 558704.385 |
| LG+G4 | -278601.397 | 558846.441 |
| Q.INSECT+I+G4 | -278710.734 | 559073.951 |
| Q.YEAST+I+G4 | -279339.698 | 560331.878 |
| MTMET+F+I+G4 | -281342.687 | 564505.756 |
| MTART+F+I+G4 | -288897.151 | 579614.685 |
| LG+I | -292741.911 | 587127.470 |
| MTMET+I+G4 | -293154.145 | 587960.773 |
| LG | -300144.509 | 601923.829 |
| MTART+I+G4 | -300602.360 | 602857.204 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Poribacteria_94/trained_models/trained_model.nex ../Result/safe_phyla/p__Poribacteria_94/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 68002.87 seconds (18.89 h)  
