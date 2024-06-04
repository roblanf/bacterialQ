## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Fusobacteriota_50  
  Taxa name: p__Fusobacteriota  
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
Input a single taxa file: ../Result/safe_phyla/p__Fusobacteriota_50/select_id.txt. Sampling sequences for 99 loci.  
Number of input species: 138  
Remaining 99 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Fusobacteriota_50/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 138  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Fusobacteriota_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/subtrees -m random
```
  
Original number of taxa: 138   
Number of pruned subtrees: 5   
Number of taxa after pruning: 126   
Pruned node IDs (degree): 97 (41) 86 (9) 12 (13) 25 (44) 68 (19)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 99 loci files. Total number of potential alignments: 495.  
Obtained 487 alignments from all potential alignments.  
Remaining 487 alignments. Deleted 8 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/subtree_update/p__Fusobacteriota_50
```
  
  Runtime: 2639.80 seconds
[Subtree update log](loop_1/subtree_update/p__Fusobacteriota_50.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 201 | Q.YEAST |
| 167 | LG |
| 104 | Q.INSECT |
| 13 | Q.PFAM |
| 1 | MTMET |
| 1 | MTART |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/subtree_update/p__Fusobacteriota_50.best_scheme.nex -te ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/subtree_update/p__Fusobacteriota_50.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/model_update/p__Fusobacteriota_50
```
  
  Runtime: 5361.58 seconds
[Model update log](loop_1/model_update/p__Fusobacteriota_50.iqtree)  
BIC of the new model: 3917884.4218  
Likelihood of the new model: -1823529.6469  
Model does not meet precision requirement.  
[New model](trained_models/p__Fusobacteriota_50_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,p__Fusobacteriota_50_1  
![Model bubble plot](loop_1/p__Fusobacteriota_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Fusobacteriota_50/ref_tree.tre ../Result/safe_phyla/p__Fusobacteriota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/tree_update/p__Fusobacteriota_50_1.treefile
```
  
  Runtime: 825.85 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Fusobacteriota_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Fusobacteriota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Fusobacteriota_50/loop_1/tree_update/p__Fusobacteriota_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Fusobacteriota_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 34  
Normalized RF distance: 0.1259  
Tree 1 branch length: 12.55568  
Tree 2 branch length: 21.2047582  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9686240124554106  
Euclidean distance: 1.3078750475603849  
Time usage for Loop_1: 8889.68 seconds (2.47 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Fusobacteriota_50/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,LG,Q.INSECT,p__Fusobacteriota_50_1 -mdef ../Result/safe_phyla/p__Fusobacteriota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/tree_update/p__Fusobacteriota_50_1.treefile -pre ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/test_model/p__Fusobacteriota_50_test_concat
```
  
  Runtime: 897.87 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Fusobacteriota_50_1+I+G4 | -339910.354 | 682250.832 |
| p__Fusobacteriota_50_1+F+I+G4 | -340828.340 | 684254.702 |
| LG+F+I+G4 | -341769.024 | 686136.070 |
| Q.YEAST+F+I+G4 | -342198.024 | 686994.071 |
| Q.INSECT+F+I+G4 | -342724.709 | 688047.439 |
| Q.YEAST+I+G4 | -343104.640 | 688639.403 |
| Q.YEAST+G4 | -343831.388 | 690084.061 |
| Q.INSECT+I+G4 | -343935.369 | 690300.862 |
| LG+I+G4 | -344991.518 | 692413.159 |
| Q.YEAST+I | -366680.465 | 735782.215 |
| Q.YEAST | -380754.057 | 763920.563 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Fusobacteriota_50/loop_1/tree_update/p__Fusobacteriota_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/subtrees -m random
```
  
Original number of taxa: 138   
Number of pruned subtrees: 5   
Number of taxa after pruning: 126   
Pruned node IDs (degree): 5 (41) 125 (9) 51 (13) 64 (15) 78 (48)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 99 loci files. Total number of potential alignments: 495.  
Obtained 486 alignments from all potential alignments.  
Remaining 486 alignments. Deleted 9 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,p__Fusobacteriota_50_1 -mdef ../Result/safe_phyla/p__Fusobacteriota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/subtree_update/p__Fusobacteriota_50
```
  
  Runtime: 3259.82 seconds
[Subtree update log](loop_2/subtree_update/p__Fusobacteriota_50.iqtree)  
Best models for iteration 2:  
p__Fusobacteriota_50_1  

| Model | Count |
|-------|-------|
| 446 | p__Fusobacteriota_50_1 |
| 32 | LG |
| 6 | Q.INSECT |
| 2 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/subtree_update/p__Fusobacteriota_50.best_scheme.nex -te ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/subtree_update/p__Fusobacteriota_50.treefile --model-joint GTR20+FO --init-model p__Fusobacteriota_50_1 -mdef ../Result/safe_phyla/p__Fusobacteriota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/model_update/p__Fusobacteriota_50
```
  
  Runtime: 3692.92 seconds
[Model update log](loop_2/model_update/p__Fusobacteriota_50.iqtree)  
BIC of the new model: 3911729.0701  
Likelihood of the new model: -1820307.4576  
Model does not meet precision requirement.  
[New model](trained_models/p__Fusobacteriota_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Fusobacteriota_50_2  
![Model bubble plot](loop_2/p__Fusobacteriota_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Fusobacteriota_50/ref_tree.tre ../Result/safe_phyla/p__Fusobacteriota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/tree_update/p__Fusobacteriota_50_2.treefile
```
  
  Runtime: 800.55 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Fusobacteriota_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Fusobacteriota_50/loop_1/tree_update/p__Fusobacteriota_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Fusobacteriota_50/loop_2/tree_update/p__Fusobacteriota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Fusobacteriota_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 21.2047582  
Tree 2 branch length: 21.247192266  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999844995171796  
Euclidean distance: 0.03170131730885815  
Time usage for Loop_2: 7813.32 seconds (2.17 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Fusobacteriota_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Fusobacteriota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Fusobacteriota_50/loop_2/tree_update/p__Fusobacteriota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Fusobacteriota_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 34  
Normalized RF distance: 0.1259  
Tree 1 branch length: 12.55568  
Tree 2 branch length: 21.247192266  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Fusobacteriota_50_2):  
Pearson's correlation: 0.9687523394983006  
Euclidean distance: 1.3073959100215362  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/tree_update/p__Fusobacteriota_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Fusobacteriota_50/final_test/subtrees -m random
```
  
Original number of taxa: 138   
Number of pruned subtrees: 5   
Number of taxa after pruning: 126   
Pruned node IDs (degree): 5 (41) 125 (9) 51 (13) 64 (15) 78 (48)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Fusobacteriota_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 20 loci files. Total number of potential alignments: 100.  
Obtained 97 alignments from all potential alignments.  
Remaining 97 alignments. Deleted 3 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Fusobacteriota_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Fusobacteriota_50_2 -mdef ../Result/safe_phyla/p__Fusobacteriota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Fusobacteriota_50/final_test/p__Fusobacteriota_50_test_partition
```
  
  Runtime: 241.37 seconds
Best models for test data:  
p__Fusobacteriota_50_2  

| Model | Count |
|-------|-------|
| 89 | p__Fusobacteriota_50_2 |
| 4 | MTART |
| 3 | LG |
| 1 | Q.PFAM |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Fusobacteriota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Fusobacteriota_50_2 -mdef ../Result/safe_phyla/p__Fusobacteriota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Fusobacteriota_50/loop_2/tree_update/p__Fusobacteriota_50_2.treefile -pre ../Result/safe_phyla/p__Fusobacteriota_50/final_test/p__Fusobacteriota_50_test_concat
```
  
  Runtime: 893.10 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Fusobacteriota_50_2+I+G4 | -339909.173 | 682248.470 |
| p__Fusobacteriota_50_2+F+I+G4 | -340834.838 | 684267.698 |
| LG+F+I+G4 | -341769.028 | 686136.079 |
| Q.YEAST+F+I+G4 | -342198.025 | 686994.073 |
| Q.PFAM+F+I+G4 | -342403.976 | 687405.974 |
| Q.INSECT+F+I+G4 | -342724.709 | 688047.440 |
| Q.YEAST+I+G4 | -343104.657 | 688639.437 |
| Q.INSECT+I+G4 | -343935.370 | 690300.862 |
| LG+I+G4 | -344991.522 | 692413.166 |
| LG+G4 | -345635.915 | 693693.117 |
| Q.PFAM+I+G4 | -346103.245 | 694636.613 |
| MTMET+F+I+G4 | -347857.036 | 698312.095 |
| MTART+F+I+G4 | -349390.091 | 701378.204 |
| MTMET+I+G4 | -358862.784 | 720155.690 |
| MTART+I+G4 | -362426.639 | 727283.400 |
| LG+I | -366950.530 | 736322.346 |
| LG | -380297.161 | 763006.772 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Fusobacteriota_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Fusobacteriota_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 18848.40 seconds (5.24 h)  
