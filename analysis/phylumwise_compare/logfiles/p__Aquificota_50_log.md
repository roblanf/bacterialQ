## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Aquificota_50  
  Taxa name: p__Aquificota  
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
Input a single taxa file: ../Result/safe_phyla/p__Aquificota_50/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 132  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Aquificota_50/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 132  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Aquificota_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Aquificota_50/loop_1/subtrees -m random
```
  
Original number of taxa: 132   
Number of pruned subtrees: 6   
Number of taxa after pruning: 131   
Pruned node IDs (degree): 63 (7) 69 (41) 132 (24) 59 (5) 7 (24) 30 (30)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Aquificota_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 98 loci files. Total number of potential alignments: 588.  
Obtained 563 alignments from all potential alignments.  
Remaining 563 alignments. Deleted 25 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Aquificota_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Aquificota_50/loop_1/subtree_update/p__Aquificota_50
```
  
  Runtime: 929.98 seconds
[Subtree update log](loop_1/subtree_update/p__Aquificota_50.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 329 | LG |
| 165 | Q.YEAST |
| 65 | Q.INSECT |
| 2 | Q.PFAM |
| 2 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Aquificota_50/loop_1/subtree_update/p__Aquificota_50.best_scheme.nex -te ../Result/safe_phyla/p__Aquificota_50/loop_1/subtree_update/p__Aquificota_50.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Aquificota_50/loop_1/model_update/p__Aquificota_50
```
  
  Runtime: 3627.98 seconds
[Model update log](loop_1/model_update/p__Aquificota_50.iqtree)  
BIC of the new model: 4711382.1732  
Likelihood of the new model: -2223920.4346  
Model does not meet precision requirement.  
[New model](trained_models/p__Aquificota_50_1)  
Model set for next iteration: LG,Q.YEAST,Q.INSECT,p__Aquificota_50_1  
![Model bubble plot](loop_1/p__Aquificota_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Aquificota_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Aquificota_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Aquificota_50/ref_tree.tre ../Result/safe_phyla/p__Aquificota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Aquificota_50/loop_1/tree_update/p__Aquificota_50_1.treefile
```
  
  Runtime: 275.63 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Aquificota_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Aquificota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Aquificota_50/loop_1/tree_update/p__Aquificota_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Aquificota_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.0853  
Tree 1 branch length: 16.16049  
Tree 2 branch length: 24.457831707  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9667594849278972  
Euclidean distance: 1.3809659478867882  
Time usage for Loop_1: 4851.89 seconds (1.35 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Aquificota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.YEAST,Q.INSECT,p__Aquificota_50_1 -mdef ../Result/safe_phyla/p__Aquificota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Aquificota_50/loop_1/tree_update/p__Aquificota_50_1.treefile -pre ../Result/safe_phyla/p__Aquificota_50/loop_1/test_model/p__Aquificota_50_test_concat
```
  
  Runtime: 118.71 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Aquificota_50_1+I+G4 | -410390.223 | 823104.527 |
| p__Aquificota_50_1+F+I+G4 | -411113.535 | 824719.051 |
| LG+F+I+G4 | -412478.356 | 827448.692 |
| Q.YEAST+F+I+G4 | -413527.723 | 829547.427 |
| Q.INSECT+F+I+G4 | -414288.529 | 831069.038 |
| Q.YEAST+I+G4 | -414382.236 | 831088.554 |
| LG+I+G4 | -415079.933 | 832483.948 |
| Q.INSECT+I+G4 | -415111.919 | 832547.920 |
| LG+G4 | -415897.956 | 834111.157 |
| LG+I | -439875.819 | 882066.883 |
| LG | -454603.819 | 911514.045 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Aquificota_50/loop_1/tree_update/p__Aquificota_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Aquificota_50/loop_2/subtrees -m random
```
  
Original number of taxa: 132   
Number of pruned subtrees: 6   
Number of taxa after pruning: 131   
Pruned node IDs (degree): 85 (7) 91 (41) 131 (24) 81 (5) 29 (24) 52 (30)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Aquificota_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 98 loci files. Total number of potential alignments: 588.  
Obtained 563 alignments from all potential alignments.  
Remaining 563 alignments. Deleted 25 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Aquificota_50/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.INSECT,p__Aquificota_50_1 -mdef ../Result/safe_phyla/p__Aquificota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Aquificota_50/loop_2/subtree_update/p__Aquificota_50
```
  
  Runtime: 837.06 seconds
[Subtree update log](loop_2/subtree_update/p__Aquificota_50.iqtree)  
Best models for iteration 2:  
p__Aquificota_50_1  

| Model | Count |
|-------|-------|
| 520 | p__Aquificota_50_1 |
| 21 | LG |
| 16 | Q.YEAST |
| 6 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Aquificota_50/loop_2/subtree_update/p__Aquificota_50.best_scheme.nex -te ../Result/safe_phyla/p__Aquificota_50/loop_2/subtree_update/p__Aquificota_50.treefile --model-joint GTR20+FO --init-model p__Aquificota_50_1 -mdef ../Result/safe_phyla/p__Aquificota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Aquificota_50/loop_2/model_update/p__Aquificota_50
```
  
  Runtime: 2795.50 seconds
[Model update log](loop_2/model_update/p__Aquificota_50.iqtree)  
BIC of the new model: 4710705.4553  
Likelihood of the new model: -2223327.5751  
Model does not meet precision requirement.  
[New model](trained_models/p__Aquificota_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Aquificota_50_2  
![Model bubble plot](loop_2/p__Aquificota_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Aquificota_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Aquificota_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Aquificota_50/ref_tree.tre ../Result/safe_phyla/p__Aquificota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Aquificota_50/loop_2/tree_update/p__Aquificota_50_2.treefile
```
  
  Runtime: 276.79 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Aquificota_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Aquificota_50/loop_1/tree_update/p__Aquificota_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Aquificota_50/loop_2/tree_update/p__Aquificota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Aquificota_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 24.457831707  
Tree 2 branch length: 24.530773323  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998791521866066  
Euclidean distance: 0.08457290439506537  
Time usage for Loop_2: 3927.32 seconds (1.09 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Aquificota_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Aquificota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Aquificota_50/loop_2/tree_update/p__Aquificota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Aquificota_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.0853  
Tree 1 branch length: 16.16049  
Tree 2 branch length: 24.530773323  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Aquificota_50_2):  
Pearson's correlation: 0.9648713466948813  
Euclidean distance: 1.4219469962093019  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Aquificota_50/loop_2/tree_update/p__Aquificota_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Aquificota_50/final_test/subtrees -m random
```
  
Original number of taxa: 132   
Number of pruned subtrees: 6   
Number of taxa after pruning: 131   
Pruned node IDs (degree): 85 (7) 91 (41) 131 (24) 81 (5) 29 (24) 52 (30)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Aquificota_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 20 loci files. Total number of potential alignments: 120.  
Obtained 115 alignments from all potential alignments.  
Remaining 115 alignments. Deleted 5 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Aquificota_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Aquificota_50_2 -mdef ../Result/safe_phyla/p__Aquificota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Aquificota_50/final_test/p__Aquificota_50_test_partition
```
  
  Runtime: 80.54 seconds
Best models for test data:  
p__Aquificota_50_2  

| Model | Count |
|-------|-------|
| 103 | p__Aquificota_50_2 |
| 6 | MTART |
| 3 | Q.YEAST |
| 2 | Q.PFAM |
| 1 | LG |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Aquificota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Aquificota_50_2 -mdef ../Result/safe_phyla/p__Aquificota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Aquificota_50/loop_2/tree_update/p__Aquificota_50_2.treefile -pre ../Result/safe_phyla/p__Aquificota_50/final_test/p__Aquificota_50_test_concat
```
  
  Runtime: 159.24 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Aquificota_50_2+I+G4 | -410426.561 | 823177.203 |
| p__Aquificota_50_2+F+I+G4 | -411154.889 | 824801.758 |
| LG+F+I+G4 | -412478.356 | 827448.692 |
| Q.YEAST+F+I+G4 | -413527.723 | 829547.427 |
| Q.PFAM+F+I+G4 | -413574.769 | 829641.519 |
| Q.INSECT+F+I+G4 | -414288.529 | 831069.038 |
| Q.YEAST+I+G4 | -414382.236 | 831088.554 |
| LG+I+G4 | -415079.933 | 832483.948 |
| Q.INSECT+I+G4 | -415111.919 | 832547.920 |
| LG+G4 | -415897.956 | 834111.157 |
| Q.PFAM+I+G4 | -416588.915 | 835501.910 |
| MTMET+F+I+G4 | -423497.535 | 849487.049 |
| MTART+F+I+G4 | -426009.942 | 854511.865 |
| LG+I | -439875.819 | 882066.883 |
| MTMET+I+G4 | -441686.788 | 885697.657 |
| MTART+I+G4 | -446611.444 | 895546.969 |
| LG | -454603.819 | 911514.045 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Aquificota_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Aquificota_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 9163.61 seconds (2.55 h)  
