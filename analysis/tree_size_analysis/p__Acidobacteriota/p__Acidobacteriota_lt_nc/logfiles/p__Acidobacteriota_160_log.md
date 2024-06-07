## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_160  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 600  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: upper  
  Lower limit for subtree size: 10  
  Upper limit for subtree size: 160  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/ref_tree.tre -l 10 -u 160 -n 7 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 7   
Number of taxa after pruning: 982   
Pruned node IDs (degree): 695 (158) 854 (155) 1729 (151) 524 (147) 17 (135) 1008 (120) 1450 (116)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 7 subtree files and 100 loci files. Total number of potential alignments: 700.  
Sub-sampling 600 alignments from 700 alignments.  
Remaining 600 alignments. Deleted 3 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/subtree_update/p__Acidobacteriota_160
```
  
  Runtime: 135959.97 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_160.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| 297 | Q.INSECT |
| 153 | Q.PFAM |
| 76 | LG |
| 74 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/subtree_update/p__Acidobacteriota_160.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/subtree_update/p__Acidobacteriota_160.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/model_update/p__Acidobacteriota_160
```
  
  Runtime: 124260.82 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_160.iqtree)  
BIC of the new model: 25610214.4336  
Likelihood of the new model: -11902354.193  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_160_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_160_1  
![Model bubble plot](loop_1/p__Acidobacteriota_160_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/tree_update/p__Acidobacteriota_160_1.treefile
```
  
  Runtime: 8295.17 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/tree_update/p__Acidobacteriota_160_1.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 640  
Normalized RF distance: 0.1695  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 307.512686743  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9868056683263193  
Euclidean distance: 0.9614233188223547  
Time usage for Loop_1: 268585.62 seconds (74.61 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loci/concat_testing_loci.faa -m TESTONLY -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_160_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/trained_models/trained_model.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/tree_update/p__Acidobacteriota_160_1.treefile -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/test_model/p__Acidobacteriota_160
```
  
  Runtime: 920.15 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_160_1+I+G4 | -5319640.827 | 10672693.632 |
| p__Acidobacteriota_160_1+F+I+G4 | -5331105.803 | 10695791.484 |
| Q.YEAST+F+I+G4 | -5343858.303 | 10721296.484 |
| Q.INSECT+F+I+G4 | -5344672.985 | 10722925.848 |
| LG+F+I+G4 | -5346221.587 | 10726023.052 |
| Q.PFAM+F+I+G4 | -5350494.031 | 10734567.940 |
| Q.PFAM+I+G4 | -5354736.708 | 10742885.394 |
| LG+I+G4 | -5362785.631 | 10758983.240 |
| Q.INSECT+I+G4 | -5365983.131 | 10765378.240 |
| Q.INSECT+G4 | -5372419.844 | 10778242.829 |
| Q.YEAST+I+G4 | -5380091.631 | 10793595.240 |
| Q.INSECT+I | -5893532.209 | 11820467.559 |
| Q.INSECT | -5956369.195 | 11946132.695 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/tree_update/p__Acidobacteriota_160_1.treefile -l 10 -u 160 -n 7 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 7   
Number of taxa after pruning: 976   
Pruned node IDs (degree): 149 (158) 529 (158) 688 (155) 995 (145) 1688 (135) 842 (120) 1566 (105)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 7 subtree files and 100 loci files. Total number of potential alignments: 700.  
Sub-sampling 600 alignments from 700 alignments.  
Remaining 600 alignments. Deleted 2 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_160_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/subtree_update/p__Acidobacteriota_160
```
  
  Runtime: 32532.78 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_160.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_160_1  

| Model | Count |
|-------|-------|
| 504 | p__Acidobacteriota_160_1 |
| 39 | Q.INSECT |
| 26 | LG |
| 25 | Q.PFAM |
| 6 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/subtree_update/p__Acidobacteriota_160.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/subtree_update/p__Acidobacteriota_160.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_160_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/model_update/p__Acidobacteriota_160
```
  
  Runtime: 130860.61 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_160.iqtree)  
BIC of the new model: 25735951.4021  
Likelihood of the new model: -11975408.1623  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_160_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_160_2  
![Model bubble plot](loop_2/p__Acidobacteriota_160_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/tree_update/p__Acidobacteriota_160_2.treefile
```
  
  Runtime: 8805.27 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_1/tree_update/p__Acidobacteriota_160_1.treefile', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/tree_update/p__Acidobacteriota_160_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0016  
Tree 1 branch length: 307.512686743  
Tree 2 branch length: 306.639984093  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997692467965094  
Euclidean distance: 0.12987764564477802  
Time usage for Loop_2: 172238.09 seconds (47.84 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/final_test', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/tree_update/p__Acidobacteriota_160_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 642  
Normalized RF distance: 0.17  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 306.639984093  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (p__Acidobacteriota_160_2):  
Pearson's correlation: 0.9852701346710809  
Euclidean distance: 1.0327526380180734  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/loop_2/tree_update/p__Acidobacteriota_160_2.treefile -l 10 -u 160 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 27   
Number of taxa after pruning: 1845   
Pruned node IDs (degree): 149 (158) 152 (47) 1356 (35) 1860 (23) 200 (23) 1391 (12) 1672 (16) 1143 (15) 1566 (105) 1688 (135) 1822 (39) 995 (145) 1404 (90) 1493 (74) 1328 (19) 981 (15) 1167 (101) 1267 (62) 235 (21) 961 (21) 256 (78) 529 (158) 688 (155) 842 (120) 501 (17) 342 (89) 430 (72)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 27 subtree files and 20 loci files. Total number of potential alignments: 540.  
Obtained 540 alignments from all potential alignments.  
Remaining 540 alignments. Deleted 0 alignments.  
### Final model testing  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_160_2 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/final_test/p__Acidobacteriota_160
```
  
  Runtime: 1244.29 seconds
Best models for test data:  
p__Acidobacteriota_160_2  

| Model | Count |
|-------|-------|
| 454 | p__Acidobacteriota_160_2 |
| 30 | Q.INSECT |
| 27 | LG |
| 13 | Q.PFAM |
| 8 | MTART |
| 7 | Q.YEAST |
| 1 | MTMET |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/trained_models/trained_model.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_160/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 443233.81 seconds (123.12 h)  
