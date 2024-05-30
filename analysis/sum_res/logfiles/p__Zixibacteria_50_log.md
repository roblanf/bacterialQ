## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Zixibacteria_50  
  Taxa name: p__Zixibacteria  
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
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Zixibacteria_50/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 133  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Zixibacteria_50/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 133  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Zixibacteria_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Zixibacteria_50/loop_1/subtrees -m random
```
  
Original number of taxa: 133   
Number of pruned subtrees: 6   
Number of taxa after pruning: 128   
Pruned node IDs (degree): 3 (39) 5 (15) 92 (6) 76 (17) 27 (36) 62 (15)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Zixibacteria_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 100 loci files. Total number of potential alignments: 600.  
Obtained 594 alignments from all potential alignments.  
Remaining 594 alignments. Deleted 6 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Zixibacteria_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Zixibacteria_50/loop_1/subtree_update/p__Zixibacteria_50
```
  
  Runtime: 1157.23 seconds
[Subtree update log](loop_1/subtree_update/p__Zixibacteria_50.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 378 | LG |
| 131 | Q.INSECT |
| 43 | Q.YEAST |
| 42 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Zixibacteria_50/loop_1/subtree_update/p__Zixibacteria_50.best_scheme.nex -te ../Result/safe_phyla/p__Zixibacteria_50/loop_1/subtree_update/p__Zixibacteria_50.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Zixibacteria_50/loop_1/model_update/p__Zixibacteria_50
```
  
  Runtime: 3949.84 seconds
[Model update log](loop_1/model_update/p__Zixibacteria_50.iqtree)  
BIC of the new model: 6561589.7735  
Likelihood of the new model: -3150782.957  
Model does not meet precision requirement.  
[New model](trained_models/p__Zixibacteria_50_1)  
Model set for next iteration: LG,Q.INSECT,Q.YEAST,Q.PFAM,p__Zixibacteria_50_1  
![Model bubble plot](loop_1/p__Zixibacteria_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Zixibacteria_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Zixibacteria_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Zixibacteria_50/ref_tree.tre ../Result/safe_phyla/p__Zixibacteria_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Zixibacteria_50/loop_1/tree_update/p__Zixibacteria_50_1.treefile
```
  
  Runtime: 323.01 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Zixibacteria_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Zixibacteria_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Zixibacteria_50/loop_1/tree_update/p__Zixibacteria_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Zixibacteria_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 34  
Normalized RF distance: 0.1308  
Tree 1 branch length: 25.51771  
Tree 2 branch length: 34.104904428  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9933296639730761  
Euclidean distance: 0.6367874384242984  
Time usage for Loop_1: 5447.80 seconds (1.51 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Zixibacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.INSECT,Q.YEAST,Q.PFAM,p__Zixibacteria_50_1 -mdef ../Result/safe_phyla/p__Zixibacteria_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Zixibacteria_50/loop_1/tree_update/p__Zixibacteria_50_1.treefile -pre ../Result/safe_phyla/p__Zixibacteria_50/loop_1/test_model/p__Zixibacteria_50_test_concat
```
  
  Runtime: 94.64 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Zixibacteria_50_1+I+G4 | -539162.828 | 1080656.806 |
| p__Zixibacteria_50_1+F+I+G4 | -539485.008 | 1081468.306 |
| LG+F+I+G4 | -540995.005 | 1084488.300 |
| Q.INSECT+I+G4 | -541190.843 | 1084712.836 |
| Q.YEAST+I+G4 | -541209.559 | 1084750.269 |
| LG+I+G4 | -541291.266 | 1084913.683 |
| Q.YEAST+F+I+G4 | -541610.703 | 1085719.695 |
| Q.PFAM+I+G4 | -542055.025 | 1086441.200 |
| Q.PFAM+F+I+G4 | -541985.887 | 1086470.063 |
| LG+G4 | -542624.099 | 1087570.551 |
| Q.INSECT+F+I+G4 | -542570.704 | 1087639.697 |
| LG+I | -578765.650 | 1159853.653 |
| LG | -598095.011 | 1198503.578 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Zixibacteria_50/loop_1/tree_update/p__Zixibacteria_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Zixibacteria_50/loop_2/subtrees -m random
```
  
Original number of taxa: 133   
Number of pruned subtrees: 6   
Number of taxa after pruning: 129   
Pruned node IDs (degree): 17 (39) 19 (15) 106 (6) 90 (17) 40 (5) 44 (47)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Zixibacteria_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 100 loci files. Total number of potential alignments: 600.  
Obtained 589 alignments from all potential alignments.  
Remaining 589 alignments. Deleted 11 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Zixibacteria_50/loop_2/training_loci -m MFP -mset LG,Q.INSECT,Q.YEAST,Q.PFAM,p__Zixibacteria_50_1 -mdef ../Result/safe_phyla/p__Zixibacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Zixibacteria_50/loop_2/subtree_update/p__Zixibacteria_50
```
  
  Runtime: 1473.86 seconds
[Subtree update log](loop_2/subtree_update/p__Zixibacteria_50.iqtree)  
Best models for iteration 2:  
p__Zixibacteria_50_1  

| Model | Count |
|-------|-------|
| 536 | p__Zixibacteria_50_1 |
| 23 | LG |
| 16 | Q.PFAM |
| 12 | Q.INSECT |
| 2 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Zixibacteria_50/loop_2/subtree_update/p__Zixibacteria_50.best_scheme.nex -te ../Result/safe_phyla/p__Zixibacteria_50/loop_2/subtree_update/p__Zixibacteria_50.treefile --model-joint GTR20+FO --init-model p__Zixibacteria_50_1 -mdef ../Result/safe_phyla/p__Zixibacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Zixibacteria_50/loop_2/model_update/p__Zixibacteria_50
```
  
  Runtime: 2561.60 seconds
[Model update log](loop_2/model_update/p__Zixibacteria_50.iqtree)  
BIC of the new model: 6575686.4695  
Likelihood of the new model: -3156758.3797  
Model does not meet precision requirement.  
[New model](trained_models/p__Zixibacteria_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Zixibacteria_50_2  
![Model bubble plot](loop_2/p__Zixibacteria_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Zixibacteria_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Zixibacteria_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Zixibacteria_50/ref_tree.tre ../Result/safe_phyla/p__Zixibacteria_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Zixibacteria_50/loop_2/tree_update/p__Zixibacteria_50_2.treefile
```
  
  Runtime: 321.00 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Zixibacteria_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Zixibacteria_50/loop_1/tree_update/p__Zixibacteria_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Zixibacteria_50/loop_2/tree_update/p__Zixibacteria_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Zixibacteria_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 34.104904428  
Tree 2 branch length: 34.146928676  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998880742113492  
Euclidean distance: 0.07932135719035133  
Time usage for Loop_2: 4375.25 seconds (1.22 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Zixibacteria_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Zixibacteria_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Zixibacteria_50/loop_2/tree_update/p__Zixibacteria_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Zixibacteria_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 34  
Normalized RF distance: 0.1308  
Tree 1 branch length: 25.51771  
Tree 2 branch length: 34.146928676  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Zixibacteria_50_2):  
Pearson's correlation: 0.9933770580247294  
Euclidean distance: 0.6366614515314495  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Zixibacteria_50/loop_2/tree_update/p__Zixibacteria_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Zixibacteria_50/final_test/subtrees -m random
```
  
Original number of taxa: 133   
Number of pruned subtrees: 6   
Number of taxa after pruning: 129   
Pruned node IDs (degree): 17 (39) 19 (15) 106 (6) 90 (17) 40 (5) 44 (47)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Zixibacteria_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 19 loci files. Total number of potential alignments: 114.  
Obtained 112 alignments from all potential alignments.  
Remaining 112 alignments. Deleted 2 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Zixibacteria_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Zixibacteria_50_2 -mdef ../Result/safe_phyla/p__Zixibacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Zixibacteria_50/final_test/p__Zixibacteria_50_test_partition
```
  
  Runtime: 81.75 seconds
Best models for test data:  
p__Zixibacteria_50_2  

| Model | Count |
|-------|-------|
| 97 | p__Zixibacteria_50_2 |
| 5 | Q.INSECT |
| 4 | MTART |
| 3 | Q.YEAST |
| 2 | LG |
| 1 | Q.PFAM |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Zixibacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Zixibacteria_50_2 -mdef ../Result/safe_phyla/p__Zixibacteria_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Zixibacteria_50/loop_2/tree_update/p__Zixibacteria_50_2.treefile -pre ../Result/safe_phyla/p__Zixibacteria_50/final_test/p__Zixibacteria_50_test_concat
```
  
  Runtime: 84.12 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Zixibacteria_50_2+I+G4 | -539134.937 | 1080601.024 |
| p__Zixibacteria_50_2+F+I+G4 | -539478.979 | 1081456.248 |
| LG+F+I+G4 | -540995.005 | 1084488.300 |
| Q.INSECT+I+G4 | -541190.843 | 1084712.836 |
| Q.YEAST+I+G4 | -541209.559 | 1084750.269 |
| LG+I+G4 | -541291.266 | 1084913.683 |
| Q.YEAST+F+I+G4 | -541610.703 | 1085719.695 |
| Q.PFAM+I+G4 | -542055.025 | 1086441.200 |
| Q.PFAM+F+I+G4 | -541985.887 | 1086470.063 |
| LG+G4 | -542624.099 | 1087570.551 |
| Q.INSECT+F+I+G4 | -542570.704 | 1087639.697 |
| MTMET+F+I+G4 | -554174.864 | 1110848.018 |
| MTART+F+I+G4 | -558279.277 | 1119056.842 |
| MTMET+I+G4 | -574493.437 | 1151318.024 |
| MTART+I+G4 | -578572.535 | 1159476.221 |
| LG+I | -578765.650 | 1159853.653 |
| LG | -598095.011 | 1198503.578 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Zixibacteria_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Zixibacteria_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 10113.42 seconds (2.81 h)  
