## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Bipolaricaulota_106  
  Taxa name: p__Bipolaricaulota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 106  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 12 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Bipolaricaulota_106/select_id.txt. Sampling sequences for 88 loci.  
Number of input species: 106  
Remaining 88 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Bipolaricaulota_106/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 106  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Bipolaricaulota_106/ref_tree.tre -l 5 -u 106 -o ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/subtrees -m random
```
  
Original number of taxa: 106   
Number of pruned subtrees: 1   
Number of taxa after pruning: 106   
Pruned node IDs (degree): 1 (106)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 88 loci files. Total number of potential alignments: 88.  
Obtained 88 alignments from all potential alignments.  
Remaining 88 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/subtree_update/p__Bipolaricaulota_106
```
  
  Runtime: 9100.63 seconds
[Subtree update log](loop_1/subtree_update/p__Bipolaricaulota_106.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 45 | LG |
| 28 | Q.PFAM |
| 9 | Q.INSECT |
| 6 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/subtree_update/p__Bipolaricaulota_106.best_scheme.nex -te ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/subtree_update/p__Bipolaricaulota_106.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/model_update/p__Bipolaricaulota_106
```
  
  Runtime: 21498.58 seconds
[Model update log](loop_1/model_update/p__Bipolaricaulota_106.iqtree)  
BIC of the new model: 3598228.6557  
Likelihood of the new model: -1714241.9646  
Model does not meet precision requirement.  
[New model](trained_models/p__Bipolaricaulota_106_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Bipolaricaulota_106_1  
![Model bubble plot](loop_1/p__Bipolaricaulota_106_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Bipolaricaulota_106/ref_tree.tre ../Result/safe_phyla/p__Bipolaricaulota_106/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/tree_update/p__Bipolaricaulota_106_1.treefile
```
  
  Runtime: 460.35 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Bipolaricaulota_106/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Bipolaricaulota_106/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/tree_update/p__Bipolaricaulota_106_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Bipolaricaulota_106/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 24  
Normalized RF distance: 0.1165  
Tree 1 branch length: 16.0359  
Tree 2 branch length: 20.769402594  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9865481250593969  
Euclidean distance: 1.0056828223373346  
Time usage for Loop_1: 31068.17 seconds (8.63 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Bipolaricaulota_106/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Bipolaricaulota_106_1 -mdef ../Result/safe_phyla/p__Bipolaricaulota_106/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/tree_update/p__Bipolaricaulota_106_1.treefile -pre ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/test_model/p__Bipolaricaulota_106_test_concat
```
  
  Runtime: 1033.96 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Bipolaricaulota_106_1+I+G4 | -364614.182 | 731087.244 |
| p__Bipolaricaulota_106_1+F+I+G4 | -365335.122 | 732696.512 |
| LG+F+I+G4 | -366399.967 | 734826.203 |
| Q.PFAM+F+I+G4 | -366568.714 | 735163.696 |
| Q.YEAST+F+I+G4 | -367202.661 | 736431.590 |
| Q.PFAM+I+G4 | -367780.376 | 737419.633 |
| Q.INSECT+F+I+G4 | -367917.889 | 737862.047 |
| LG+I+G4 | -368367.281 | 738593.443 |
| LG+G4 | -368920.020 | 739690.112 |
| Q.INSECT+I+G4 | -370433.316 | 742725.513 |
| Q.YEAST+I+G4 | -371330.002 | 744518.884 |
| LG+I | -389123.509 | 780097.088 |
| LG | -400553.411 | 802948.084 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/tree_update/p__Bipolaricaulota_106_1.treefile -l 5 -u 106 -o ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/subtrees -m random
```
  
Original number of taxa: 106   
Number of pruned subtrees: 1   
Number of taxa after pruning: 106   
Pruned node IDs (degree): 1 (106)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 88 loci files. Total number of potential alignments: 88.  
Obtained 88 alignments from all potential alignments.  
Remaining 88 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Bipolaricaulota_106_1 -mdef ../Result/safe_phyla/p__Bipolaricaulota_106/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/subtree_update/p__Bipolaricaulota_106
```
  
  Runtime: 8518.51 seconds
[Subtree update log](loop_2/subtree_update/p__Bipolaricaulota_106.iqtree)  
Best models for iteration 2:  
p__Bipolaricaulota_106_1  

| Model | Count |
|-------|-------|
| 81 | p__Bipolaricaulota_106_1 |
| 4 | LG |
| 3 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/subtree_update/p__Bipolaricaulota_106.best_scheme.nex -te ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/subtree_update/p__Bipolaricaulota_106.treefile --model-joint GTR20+FO --init-model p__Bipolaricaulota_106_1 -mdef ../Result/safe_phyla/p__Bipolaricaulota_106/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/model_update/p__Bipolaricaulota_106
```
  
  Runtime: 15184.12 seconds
[Model update log](loop_2/model_update/p__Bipolaricaulota_106.iqtree)  
BIC of the new model: 3597663.5172  
Likelihood of the new model: -1714113.7368  
Model does not meet precision requirement.  
[New model](trained_models/p__Bipolaricaulota_106_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Bipolaricaulota_106_2  
![Model bubble plot](loop_2/p__Bipolaricaulota_106_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Bipolaricaulota_106/ref_tree.tre ../Result/safe_phyla/p__Bipolaricaulota_106/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/tree_update/p__Bipolaricaulota_106_2.treefile
```
  
  Runtime: 419.12 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Bipolaricaulota_106/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Bipolaricaulota_106/loop_1/tree_update/p__Bipolaricaulota_106_1.treefile', tree2_path = '../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/tree_update/p__Bipolaricaulota_106_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Bipolaricaulota_106/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 20.769402594  
Tree 2 branch length: 20.775098159  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999813637433751  
Euclidean distance: 0.11733537893521946  
Time usage for Loop_2: 24130.13 seconds (6.70 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Bipolaricaulota_106/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Bipolaricaulota_106/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/tree_update/p__Bipolaricaulota_106_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Bipolaricaulota_106/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 24  
Normalized RF distance: 0.1165  
Tree 1 branch length: 16.0359  
Tree 2 branch length: 20.775098159  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Bipolaricaulota_106_2):  
Pearson's correlation: 0.9845103079278659  
Euclidean distance: 1.0870905496134682  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/tree_update/p__Bipolaricaulota_106_2.treefile -l 5 -u 106 -o ../Result/safe_phyla/p__Bipolaricaulota_106/final_test/subtrees -m random
```
  
Original number of taxa: 106   
Number of pruned subtrees: 1   
Number of taxa after pruning: 106   
Pruned node IDs (degree): 1 (106)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Bipolaricaulota_106/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 19 loci files. Total number of potential alignments: 19.  
Obtained 19 alignments from all potential alignments.  
Remaining 19 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Bipolaricaulota_106/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Bipolaricaulota_106_2 -mdef ../Result/safe_phyla/p__Bipolaricaulota_106/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Bipolaricaulota_106/final_test/p__Bipolaricaulota_106_test_partition
```
  
  Runtime: 11287.05 seconds
Best models for test data:  
p__Bipolaricaulota_106_2  

| Model | Count |
|-------|-------|
| 18 | p__Bipolaricaulota_106_2 |
| 1 | Q.YEAST |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Bipolaricaulota_106/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Bipolaricaulota_106_2 -mdef ../Result/safe_phyla/p__Bipolaricaulota_106/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Bipolaricaulota_106/loop_2/tree_update/p__Bipolaricaulota_106_2.treefile -pre ../Result/safe_phyla/p__Bipolaricaulota_106/final_test/p__Bipolaricaulota_106_test_concat
```
  
  Runtime: 658.69 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Bipolaricaulota_106_2+I+G4 | -364613.269 | 731085.419 |
| p__Bipolaricaulota_106_2+F+I+G4 | -365354.558 | 732735.385 |
| LG+F+I+G4 | -366399.967 | 734826.203 |
| Q.PFAM+F+I+G4 | -366568.714 | 735163.696 |
| Q.YEAST+F+I+G4 | -367202.661 | 736431.590 |
| Q.PFAM+I+G4 | -367780.376 | 737419.633 |
| Q.INSECT+F+I+G4 | -367917.889 | 737862.047 |
| LG+I+G4 | -368367.281 | 738593.443 |
| LG+G4 | -368920.020 | 739690.112 |
| Q.INSECT+I+G4 | -370433.316 | 742725.513 |
| Q.YEAST+I+G4 | -371330.002 | 744518.884 |
| MTMET+F+I+G4 | -375185.172 | 752396.612 |
| MTART+F+I+G4 | -384884.407 | 771795.082 |
| LG+I | -389123.509 | 780097.088 |
| MTMET+I+G4 | -396357.631 | 794574.143 |
| LG | -400553.411 | 802948.084 |
| MTART+I+G4 | -405712.448 | 813283.777 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Bipolaricaulota_106/trained_models/trained_model.nex ../Result/safe_phyla/p__Bipolaricaulota_106/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 68235.54 seconds (18.95 h)  
