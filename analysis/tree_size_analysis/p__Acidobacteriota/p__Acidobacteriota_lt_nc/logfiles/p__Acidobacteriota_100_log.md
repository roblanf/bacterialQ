## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_100  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: upper  
  Lower limit for subtree size: 10  
  Upper limit for subtree size: 100  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/ref_tree.tre -l 10 -u 100 -n 11 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 11   
Number of taxa after pruning: 987   
Pruned node IDs (degree): 1168 (100) 1782 (98) 293 (98) 1029 (98) 871 (95) 33 (90) 1567 (89) 1468 (87) 592 (79) 422 (78) 726 (75)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 11 subtree files and 100 loci files. Total number of potential alignments: 1100.  
Sub-sampling 1000 alignments from 1100 alignments.  
Remaining 1000 alignments. Deleted 5 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/subtree_update/p__Acidobacteriota_100
```
  
  Runtime: 56217.19 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_100.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| 487 | Q.INSECT |
| 245 | Q.PFAM |
| 161 | LG |
| 106 | Q.YEAST |
| 1 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/subtree_update/p__Acidobacteriota_100.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/subtree_update/p__Acidobacteriota_100.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/model_update/p__Acidobacteriota_100
```
  
  Runtime: 108970.61 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_100.iqtree)  
BIC of the new model: 26983135.4812  
Likelihood of the new model: -12488736.6424  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_100_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_100_1  
![Model bubble plot](loop_1/p__Acidobacteriota_100_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile
```
  
  Runtime: 13816.30 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 646  
Normalized RF distance: 0.1711  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 306.899514082  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9849736261152401  
Euclidean distance: 1.0017299615091784  
Time usage for Loop_1: 179093.98 seconds (49.75 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loci/concat_testing_loci.faa -m TESTONLY -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_100_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/trained_models/trained_model.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/test_model/p__Acidobacteriota_100
```
  
  Runtime: 4028.68 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_100_1+I+G4 | -5320918.137 | 10675248.252 |
| p__Acidobacteriota_100_1+F+I+G4 | -5330635.642 | 10694851.162 |
| Q.YEAST+F+I+G4 | -5343993.869 | 10721567.616 |
| Q.INSECT+F+I+G4 | -5344810.141 | 10723200.160 |
| LG+F+I+G4 | -5346358.543 | 10726296.964 |
| Q.PFAM+F+I+G4 | -5350628.274 | 10734836.426 |
| Q.PFAM+I+G4 | -5354874.062 | 10743160.102 |
| LG+I+G4 | -5362929.078 | 10759270.134 |
| Q.INSECT+I+G4 | -5366134.058 | 10765680.094 |
| Q.INSECT+G4 | -5372574.640 | 10778552.421 |
| Q.YEAST+I+G4 | -5380237.732 | 10793887.442 |
| Q.INSECT+I | -5893665.067 | 11820733.275 |
| Q.INSECT | -5956501.618 | 11946397.541 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile -l 10 -u 100 -n 11 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 11   
Number of taxa after pruning: 984   
Pruned node IDs (degree): 1168 (100) 52 (98) 996 (98) 864 (98) 705 (95) 1404 (90) 342 (89) 1584 (87) 256 (78) 1703 (76) 562 (75)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 11 subtree files and 100 loci files. Total number of potential alignments: 1100.  
Sub-sampling 1000 alignments from 1100 alignments.  
Remaining 1000 alignments. Deleted 4 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_100_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/subtree_update/p__Acidobacteriota_100
```
  
  Runtime: 37615.29 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_100.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_100_1  

| Model | Count |
|-------|-------|
| 864 | p__Acidobacteriota_100_1 |
| 53 | Q.INSECT |
| 36 | Q.PFAM |
| 28 | LG |
| 19 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/subtree_update/p__Acidobacteriota_100.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/subtree_update/p__Acidobacteriota_100.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_100_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/model_update/p__Acidobacteriota_100
```
  
  Runtime: 49767.43 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_100.iqtree)  
BIC of the new model: 27383455.0788  
Likelihood of the new model: -12687639.6361  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_100_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_100_2  
![Model bubble plot](loop_2/p__Acidobacteriota_100_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile
```
  
  Runtime: 6114.01 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 306.899514082  
Tree 2 branch length: 306.654890834  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999907680613472  
Euclidean distance: 0.08731001041594427  
Time usage for Loop_2: 93596.02 seconds (26.00 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/final_test', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 646  
Normalized RF distance: 0.1711  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 306.654890834  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (p__Acidobacteriota_100_2):  
Pearson's correlation: 0.983745999738515  
Euclidean distance: 1.0575409622628635  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile -l 10 -u 100 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 38   
Number of taxa after pruning: 1810   
Pruned node IDs (degree): 152 (47) 1356 (35) 1860 (23) 5 (48) 52 (98) 200 (23) 1391 (12) 1672 (16) 1143 (15) 1822 (39) 1404 (90) 1493 (74) 996 (98) 1093 (47) 1328 (19) 1568 (17) 1584 (87) 1690 (13) 981 (15) 1267 (62) 1703 (76) 1778 (45) 1168 (100) 235 (21) 961 (21) 256 (78) 501 (17) 677 (10) 799 (44) 690 (16) 705 (95) 342 (89) 430 (72) 847 (18) 864 (98) 535 (23) 562 (75) 636 (34)   
Pruning mode: random   
Pruning completed. Results saved in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/final_test/subtrees 
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 38 subtree files and 20 loci files. Total number of potential alignments: 760.  
Obtained 758 alignments from all potential alignments.  
Remaining 758 alignments. Deleted 2 alignments.  
### Final model testing  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_100_2 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/final_test/p__Acidobacteriota_100
```
  
  Runtime: 143.13 seconds
Best models for test data:  
p__Acidobacteriota_100_2  

| Model | Count |
|-------|-------|
| 635 | p__Acidobacteriota_100_2 |
| 50 | LG |
| 34 | Q.INSECT |
| 15 | MTART |
| 12 | Q.PFAM |
| 11 | Q.YEAST |
| 1 | MTMET |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/trained_models/trained_model.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_100/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 277115.36 seconds (76.98 h)  
