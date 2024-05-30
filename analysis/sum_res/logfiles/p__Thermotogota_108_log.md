## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Thermotogota_108  
  Taxa name: p__Thermotogota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 108  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Thermotogota_108/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 108  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Thermotogota_108/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 108  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Thermotogota_108/ref_tree.tre -l 5 -u 108 -o ../Result/safe_phyla/p__Thermotogota_108/loop_1/subtrees -m random
```
  
Original number of taxa: 108   
Number of pruned subtrees: 1   
Number of taxa after pruning: 108   
Pruned node IDs (degree): 1 (108)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Thermotogota_108/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 98 loci files. Total number of potential alignments: 98.  
Obtained 98 alignments from all potential alignments.  
Remaining 98 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Thermotogota_108/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Thermotogota_108/loop_1/subtree_update/p__Thermotogota_108
```
  
  Runtime: 14940.44 seconds
[Subtree update log](loop_1/subtree_update/p__Thermotogota_108.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 46 | Q.YEAST |
| 35 | LG |
| 14 | Q.INSECT |
| 3 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Thermotogota_108/loop_1/subtree_update/p__Thermotogota_108.best_scheme.nex -te ../Result/safe_phyla/p__Thermotogota_108/loop_1/subtree_update/p__Thermotogota_108.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Thermotogota_108/loop_1/model_update/p__Thermotogota_108
```
  
  Runtime: 15195.29 seconds
[Model update log](loop_1/model_update/p__Thermotogota_108.iqtree)  
BIC of the new model: 4563888.6187  
Likelihood of the new model: -2176345.6166  
Model does not meet precision requirement.  
[New model](trained_models/p__Thermotogota_108_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,p__Thermotogota_108_1  
![Model bubble plot](loop_1/p__Thermotogota_108_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Thermotogota_108/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Thermotogota_108/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Thermotogota_108/ref_tree.tre ../Result/safe_phyla/p__Thermotogota_108/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Thermotogota_108/loop_1/tree_update/p__Thermotogota_108_1.treefile
```
  
  Runtime: 246.89 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Thermotogota_108/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Thermotogota_108/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Thermotogota_108/loop_1/tree_update/p__Thermotogota_108_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Thermotogota_108/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0381  
Tree 1 branch length: 16.91519  
Tree 2 branch length: 25.417440601  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.987342550510659  
Euclidean distance: 0.850661785477436  
Time usage for Loop_1: 30391.45 seconds (8.44 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Thermotogota_108/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,LG,Q.INSECT,p__Thermotogota_108_1 -mdef ../Result/safe_phyla/p__Thermotogota_108/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Thermotogota_108/loop_1/tree_update/p__Thermotogota_108_1.treefile -pre ../Result/safe_phyla/p__Thermotogota_108/loop_1/test_model/p__Thermotogota_108_test_concat
```
  
  Runtime: 64.87 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Thermotogota_108_1+I+G4 | -433055.727 | 868011.368 |
| p__Thermotogota_108_1+F+I+G4 | -434935.970 | 871939.753 |
| LG+F+I+G4 | -435440.123 | 872948.059 |
| Q.YEAST+I+G4 | -436307.362 | 874514.638 |
| Q.YEAST+F+I+G4 | -436419.470 | 874906.754 |
| Q.INSECT+I+G4 | -436986.392 | 875872.698 |
| Q.YEAST+G4 | -437031.760 | 875954.598 |
| Q.INSECT+F+I+G4 | -437222.438 | 876512.691 |
| LG+I+G4 | -437618.073 | 877136.060 |
| Q.YEAST+I | -464831.305 | 931553.687 |
| Q.YEAST | -478597.448 | 959077.136 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Thermotogota_108/loop_1/tree_update/p__Thermotogota_108_1.treefile -l 5 -u 108 -o ../Result/safe_phyla/p__Thermotogota_108/loop_2/subtrees -m random
```
  
Original number of taxa: 108   
Number of pruned subtrees: 1   
Number of taxa after pruning: 108   
Pruned node IDs (degree): 1 (108)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Thermotogota_108/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 98 loci files. Total number of potential alignments: 98.  
Obtained 98 alignments from all potential alignments.  
Remaining 98 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Thermotogota_108/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,p__Thermotogota_108_1 -mdef ../Result/safe_phyla/p__Thermotogota_108/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Thermotogota_108/loop_2/subtree_update/p__Thermotogota_108
```
  
  Runtime: 5387.13 seconds
[Subtree update log](loop_2/subtree_update/p__Thermotogota_108.iqtree)  
Best models for iteration 2:  
p__Thermotogota_108_1  

| Model | Count |
|-------|-------|
| 95 | p__Thermotogota_108_1 |
| 3 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Thermotogota_108/loop_2/subtree_update/p__Thermotogota_108.best_scheme.nex -te ../Result/safe_phyla/p__Thermotogota_108/loop_2/subtree_update/p__Thermotogota_108.treefile --model-joint GTR20+FO --init-model p__Thermotogota_108_1 -mdef ../Result/safe_phyla/p__Thermotogota_108/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Thermotogota_108/loop_2/model_update/p__Thermotogota_108
```
  
  Runtime: 15159.57 seconds
[Model update log](loop_2/model_update/p__Thermotogota_108.iqtree)  
BIC of the new model: 4563689.1614  
Likelihood of the new model: -2176063.5968  
Model does not meet precision requirement.  
[New model](trained_models/p__Thermotogota_108_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Thermotogota_108_2  
![Model bubble plot](loop_2/p__Thermotogota_108_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Thermotogota_108/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Thermotogota_108/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Thermotogota_108/ref_tree.tre ../Result/safe_phyla/p__Thermotogota_108/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Thermotogota_108/loop_2/tree_update/p__Thermotogota_108_2.treefile
```
  
  Runtime: 245.72 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Thermotogota_108/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Thermotogota_108/loop_1/tree_update/p__Thermotogota_108_1.treefile', tree2_path = '../Result/safe_phyla/p__Thermotogota_108/loop_2/tree_update/p__Thermotogota_108_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Thermotogota_108/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 25.417440601  
Tree 2 branch length: 25.464851372  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999897259465743  
Euclidean distance: 0.027043537544713  
Time usage for Loop_2: 20800.49 seconds (5.78 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Thermotogota_108/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Thermotogota_108/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Thermotogota_108/loop_2/tree_update/p__Thermotogota_108_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Thermotogota_108/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0381  
Tree 1 branch length: 16.91519  
Tree 2 branch length: 25.464851372  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Thermotogota_108_2):  
Pearson's correlation: 0.9873083271666434  
Euclidean distance: 0.8549636674368292  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Thermotogota_108/loop_2/tree_update/p__Thermotogota_108_2.treefile -l 5 -u 108 -o ../Result/safe_phyla/p__Thermotogota_108/final_test/subtrees -m random
```
  
Original number of taxa: 108   
Number of pruned subtrees: 1   
Number of taxa after pruning: 108   
Pruned node IDs (degree): 1 (108)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Thermotogota_108/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 20 loci files. Total number of potential alignments: 20.  
Obtained 20 alignments from all potential alignments.  
Remaining 20 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Thermotogota_108/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Thermotogota_108_2 -mdef ../Result/safe_phyla/p__Thermotogota_108/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Thermotogota_108/final_test/p__Thermotogota_108_test_partition
```
  
  Runtime: 4646.70 seconds
Best models for test data:  
p__Thermotogota_108_2  

| Model | Count |
|-------|-------|
| 20 | p__Thermotogota_108_2 |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Thermotogota_108/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Thermotogota_108_2 -mdef ../Result/safe_phyla/p__Thermotogota_108/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Thermotogota_108/loop_2/tree_update/p__Thermotogota_108_2.treefile -pre ../Result/safe_phyla/p__Thermotogota_108/final_test/p__Thermotogota_108_test_concat
```
  
  Runtime: 85.18 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Thermotogota_108_2+I+G4 | -433064.227 | 868028.368 |
| p__Thermotogota_108_2+F+I+G4 | -434979.204 | 872026.221 |
| LG+F+I+G4 | -435440.120 | 872948.053 |
| Q.YEAST+I+G4 | -436307.358 | 874514.630 |
| Q.PFAM+F+I+G4 | -436319.664 | 874707.142 |
| Q.YEAST+F+I+G4 | -436419.476 | 874906.766 |
| Q.INSECT+I+G4 | -436986.393 | 875872.700 |
| Q.INSECT+F+I+G4 | -437222.439 | 876512.691 |
| LG+I+G4 | -437618.076 | 877136.066 |
| LG+G4 | -438354.472 | 878600.022 |
| Q.PFAM+I+G4 | -438987.746 | 879875.406 |
| MTMET+F+I+G4 | -443386.932 | 888841.677 |
| MTART+F+I+G4 | -446357.176 | 894782.166 |
| MTMET+I+G4 | -458190.925 | 918281.765 |
| MTART+I+G4 | -463403.716 | 928707.346 |
| LG+I | -463913.489 | 929718.055 |
| LG | -476801.672 | 955485.584 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Thermotogota_108/trained_models/trained_model.nex ../Result/safe_phyla/p__Thermotogota_108/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 56014.05 seconds (15.56 h)  
