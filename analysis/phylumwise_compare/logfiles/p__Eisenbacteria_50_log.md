## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Eisenbacteria_50  
  Taxa name: p__Eisenbacteria  
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
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Eisenbacteria_50/select_id.txt. Sampling sequences for 99 loci.  
Number of input species: 50  
Remaining 99 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Eisenbacteria_50/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 50  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Eisenbacteria_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/subtrees -m random
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 99 loci files. Total number of potential alignments: 99.  
Obtained 99 alignments from all potential alignments.  
Remaining 99 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/subtree_update/p__Eisenbacteria_50
```
  
  Runtime: 3235.02 seconds
[Subtree update log](loop_1/subtree_update/p__Eisenbacteria_50.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 40 | LG |
| 36 | Q.PFAM |
| 18 | Q.INSECT |
| 5 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/subtree_update/p__Eisenbacteria_50.best_scheme.nex -te ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/subtree_update/p__Eisenbacteria_50.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/model_update/p__Eisenbacteria_50
```
  
  Runtime: 14678.42 seconds
[Model update log](loop_1/model_update/p__Eisenbacteria_50.iqtree)  
BIC of the new model: 2695499.2856  
Likelihood of the new model: -1302392.314  
Model does not meet precision requirement.  
[New model](trained_models/p__Eisenbacteria_50_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Eisenbacteria_50_1  
![Model bubble plot](loop_1/p__Eisenbacteria_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Eisenbacteria_50/ref_tree.tre ../Result/safe_phyla/p__Eisenbacteria_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/tree_update/p__Eisenbacteria_50_1.treefile
```
  
  Runtime: 441.06 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Eisenbacteria_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Eisenbacteria_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Eisenbacteria_50/loop_1/tree_update/p__Eisenbacteria_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Eisenbacteria_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 18  
Normalized RF distance: 0.1915  
Tree 1 branch length: 11.90697  
Tree 2 branch length: 15.524826354  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9834307729645009  
Euclidean distance: 1.1930913076069118  
Time usage for Loop_1: 18367.57 seconds (5.10 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Eisenbacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Eisenbacteria_50_1 -mdef ../Result/safe_phyla/p__Eisenbacteria_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/tree_update/p__Eisenbacteria_50_1.treefile -pre ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/test_model/p__Eisenbacteria_50_test_concat
```
  
  Runtime: 448.69 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Eisenbacteria_50_1+I+G4 | -245748.181 | 492371.207 |
| p__Eisenbacteria_50_1+F+I+G4 | -245977.723 | 492998.190 |
| LG+F+I+G4 | -246540.038 | 494122.819 |
| Q.PFAM+F+I+G4 | -246777.457 | 494597.658 |
| Q.YEAST+F+I+G4 | -246810.766 | 494664.275 |
| Q.INSECT+F+I+G4 | -247183.581 | 495409.906 |
| Q.PFAM+I+G4 | -248196.421 | 497267.685 |
| LG+I+G4 | -248684.905 | 498244.655 |
| LG+G4 | -249095.730 | 499057.468 |
| Q.INSECT+I+G4 | -250243.384 | 501361.613 |
| Q.YEAST+I+G4 | -250966.468 | 502807.781 |
| LG+I | -259318.832 | 519503.672 |
| LG | -269324.015 | 539505.200 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Eisenbacteria_50/loop_1/tree_update/p__Eisenbacteria_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/subtrees -m random
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 99 loci files. Total number of potential alignments: 99.  
Obtained 99 alignments from all potential alignments.  
Remaining 99 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Eisenbacteria_50_1 -mdef ../Result/safe_phyla/p__Eisenbacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/subtree_update/p__Eisenbacteria_50
```
  
  Runtime: 2694.03 seconds
[Subtree update log](loop_2/subtree_update/p__Eisenbacteria_50.iqtree)  
Best models for iteration 2:  
p__Eisenbacteria_50_1  

| Model | Count |
|-------|-------|
| 84 | p__Eisenbacteria_50_1 |
| 8 | LG |
| 5 | Q.INSECT |
| 2 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/subtree_update/p__Eisenbacteria_50.best_scheme.nex -te ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/subtree_update/p__Eisenbacteria_50.treefile --model-joint GTR20+FO --init-model p__Eisenbacteria_50_1 -mdef ../Result/safe_phyla/p__Eisenbacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/model_update/p__Eisenbacteria_50
```
  
  Runtime: 6391.57 seconds
[Model update log](loop_2/model_update/p__Eisenbacteria_50.iqtree)  
BIC of the new model: 2695258.7514  
Likelihood of the new model: -1302199.0162  
Model does not meet precision requirement.  
[New model](trained_models/p__Eisenbacteria_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Eisenbacteria_50_2  
![Model bubble plot](loop_2/p__Eisenbacteria_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Eisenbacteria_50/ref_tree.tre ../Result/safe_phyla/p__Eisenbacteria_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/tree_update/p__Eisenbacteria_50_2.treefile
```
  
  Runtime: 440.75 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Eisenbacteria_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Eisenbacteria_50/loop_1/tree_update/p__Eisenbacteria_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Eisenbacteria_50/loop_2/tree_update/p__Eisenbacteria_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Eisenbacteria_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 15.524826354  
Tree 2 branch length: 15.537096343  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999915504913149  
Euclidean distance: 0.024632141411657617  
Time usage for Loop_2: 9538.97 seconds (2.65 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Eisenbacteria_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Eisenbacteria_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Eisenbacteria_50/loop_2/tree_update/p__Eisenbacteria_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Eisenbacteria_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 18  
Normalized RF distance: 0.1915  
Tree 1 branch length: 11.90697  
Tree 2 branch length: 15.537096343  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Eisenbacteria_50_2):  
Pearson's correlation: 0.9834656966204003  
Euclidean distance: 1.1966526559748052  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/tree_update/p__Eisenbacteria_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Eisenbacteria_50/final_test/subtrees -m random
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Eisenbacteria_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 20 loci files. Total number of potential alignments: 20.  
Obtained 20 alignments from all potential alignments.  
Remaining 20 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Eisenbacteria_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Eisenbacteria_50_2 -mdef ../Result/safe_phyla/p__Eisenbacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Eisenbacteria_50/final_test/p__Eisenbacteria_50_test_partition
```
  
  Runtime: 14304.35 seconds
Best models for test data:  
p__Eisenbacteria_50_2  

| Model | Count |
|-------|-------|
| 18 | p__Eisenbacteria_50_2 |
| 1 | Q.INSECT |
| 1 | LG |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Eisenbacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Eisenbacteria_50_2 -mdef ../Result/safe_phyla/p__Eisenbacteria_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Eisenbacteria_50/loop_2/tree_update/p__Eisenbacteria_50_2.treefile -pre ../Result/safe_phyla/p__Eisenbacteria_50/final_test/p__Eisenbacteria_50_test_concat
```
  
  Runtime: 186.10 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Eisenbacteria_50_2+I+G4 | -245748.839 | 492372.523 |
| p__Eisenbacteria_50_2+F+I+G4 | -245981.454 | 493005.652 |
| LG+F+I+G4 | -246540.038 | 494122.819 |
| Q.PFAM+F+I+G4 | -246777.457 | 494597.658 |
| Q.YEAST+F+I+G4 | -246810.766 | 494664.275 |
| Q.INSECT+F+I+G4 | -247183.581 | 495409.905 |
| Q.PFAM+I+G4 | -248196.421 | 497267.685 |
| LG+I+G4 | -248684.905 | 498244.654 |
| LG+G4 | -249095.730 | 499057.468 |
| Q.INSECT+I+G4 | -250243.384 | 501361.613 |
| Q.YEAST+I+G4 | -250966.468 | 502807.781 |
| MTMET+F+I+G4 | -254360.198 | 509763.140 |
| MTART+F+I+G4 | -257272.600 | 515587.943 |
| LG+I | -259318.832 | 519503.672 |
| LG | -269324.015 | 539505.200 |
| MTMET+I+G4 | -270324.736 | 541524.317 |
| MTART+I+G4 | -272319.257 | 545513.357 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Eisenbacteria_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Eisenbacteria_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 42910.27 seconds (11.92 h)  
