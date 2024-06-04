## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Chlamydiota_100  
  Taxa name: p__Chlamydiota  
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
Discarded 6 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Chlamydiota_100/select_id.txt. Sampling sequences for 94 loci.  
Number of input species: 311  
Remaining 94 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 4 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Chlamydiota_100/select_id.txt. Sampling sequences for 16 loci.  
Number of input species: 311  
Remaining 16 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Chlamydiota_100/ref_tree.tre -l 5 -u 100 -o ../Result/safe_phyla/p__Chlamydiota_100/loop_1/subtrees -m random
```
  
Original number of taxa: 311   
Number of pruned subtrees: 6   
Number of taxa after pruning: 307   
Pruned node IDs (degree): 21 (24) 23 (42) 238 (71) 193 (46) 71 (85) 155 (39)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Chlamydiota_100/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 6 subtree files and 94 loci files. Total number of potential alignments: 564.  
Obtained 557 alignments from all potential alignments.  
Remaining 557 alignments. Deleted 7 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chlamydiota_100/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Chlamydiota_100/loop_1/subtree_update/p__Chlamydiota_100
```
  
  Runtime: 9373.60 seconds
[Subtree update log](loop_1/subtree_update/p__Chlamydiota_100.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 213 | Q.YEAST |
| 191 | Q.INSECT |
| 119 | LG |
| 33 | Q.PFAM |
| 1 | MTMET |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chlamydiota_100/loop_1/subtree_update/p__Chlamydiota_100.best_scheme.nex -te ../Result/safe_phyla/p__Chlamydiota_100/loop_1/subtree_update/p__Chlamydiota_100.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Chlamydiota_100/loop_1/model_update/p__Chlamydiota_100
```
  
  Runtime: 22710.27 seconds
[Model update log](loop_1/model_update/p__Chlamydiota_100.iqtree)  
BIC of the new model: 14827532.0674  
Likelihood of the new model: -7101472.8202  
Model does not meet precision requirement.  
[New model](trained_models/p__Chlamydiota_100_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.PFAM,p__Chlamydiota_100_1  
![Model bubble plot](loop_1/p__Chlamydiota_100_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Chlamydiota_100/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Chlamydiota_100/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Chlamydiota_100/ref_tree.tre ../Result/safe_phyla/p__Chlamydiota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Chlamydiota_100/loop_1/tree_update/p__Chlamydiota_100_1.treefile
```
  
  Runtime: 983.78 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Chlamydiota_100/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Chlamydiota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Chlamydiota_100/loop_1/tree_update/p__Chlamydiota_100_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Chlamydiota_100/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 124  
Normalized RF distance: 0.2013  
Tree 1 branch length: 73.72264  
Tree 2 branch length: 104.812103475  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9944821449948326  
Euclidean distance: 0.5669532962223847  
Time usage for Loop_1: 33086.16 seconds (9.19 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Chlamydiota_100/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,Q.INSECT,LG,Q.PFAM,p__Chlamydiota_100_1 -mdef ../Result/safe_phyla/p__Chlamydiota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Chlamydiota_100/loop_1/tree_update/p__Chlamydiota_100_1.treefile -pre ../Result/safe_phyla/p__Chlamydiota_100/loop_1/test_model/p__Chlamydiota_100_test_concat
```
  
  Runtime: 319.41 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Chlamydiota_100_1+I+G4 | -1200389.553 | 2406170.541 |
| p__Chlamydiota_100_1+F+I+G4 | -1203517.887 | 2412592.164 |
| Q.YEAST+I+G4 | -1203974.289 | 2413340.013 |
| Q.INSECT+I+G4 | -1204912.815 | 2415217.065 |
| LG+F+I+G4 | -1205990.392 | 2417537.174 |
| Q.YEAST+G4 | -1206385.149 | 2418153.051 |
| Q.YEAST+F+I+G4 | -1206962.900 | 2419482.190 |
| LG+I+G4 | -1207148.136 | 2419687.707 |
| Q.PFAM+F+I+G4 | -1207150.140 | 2419856.670 |
| Q.PFAM+I+G4 | -1208549.098 | 2422489.631 |
| Q.INSECT+F+I+G4 | -1209073.616 | 2423703.622 |
| Q.YEAST+I | -1322415.913 | 2650214.579 |
| Q.YEAST | -1355154.772 | 2715683.615 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Chlamydiota_100/loop_1/tree_update/p__Chlamydiota_100_1.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Chlamydiota_100/loop_2/subtrees -m random
```
  
Original number of taxa: 311   
Number of pruned subtrees: 5   
Number of taxa after pruning: 306   
Pruned node IDs (degree): 111 (46) 158 (41) 198 (83) 4 (65) 40 (71)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Chlamydiota_100/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 94 loci files. Total number of potential alignments: 470.  
Obtained 467 alignments from all potential alignments.  
Remaining 467 alignments. Deleted 3 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chlamydiota_100/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.PFAM,p__Chlamydiota_100_1 -mdef ../Result/safe_phyla/p__Chlamydiota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Chlamydiota_100/loop_2/subtree_update/p__Chlamydiota_100
```
  
  Runtime: 8429.28 seconds
[Subtree update log](loop_2/subtree_update/p__Chlamydiota_100.iqtree)  
Best models for iteration 2:  
p__Chlamydiota_100_1  

| Model | Count |
|-------|-------|
| 378 | p__Chlamydiota_100_1 |
| 53 | Q.INSECT |
| 15 | LG |
| 11 | Q.PFAM |
| 10 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chlamydiota_100/loop_2/subtree_update/p__Chlamydiota_100.best_scheme.nex -te ../Result/safe_phyla/p__Chlamydiota_100/loop_2/subtree_update/p__Chlamydiota_100.treefile --model-joint GTR20+FO --init-model p__Chlamydiota_100_1 -mdef ../Result/safe_phyla/p__Chlamydiota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Chlamydiota_100/loop_2/model_update/p__Chlamydiota_100
```
  
  Runtime: 13186.95 seconds
[Model update log](loop_2/model_update/p__Chlamydiota_100.iqtree)  
BIC of the new model: 14595356.2744  
Likelihood of the new model: -6988553.4526  
Model does not meet precision requirement.  
[New model](trained_models/p__Chlamydiota_100_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Chlamydiota_100_2  
![Model bubble plot](loop_2/p__Chlamydiota_100_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Chlamydiota_100/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Chlamydiota_100/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Chlamydiota_100/ref_tree.tre ../Result/safe_phyla/p__Chlamydiota_100/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Chlamydiota_100/loop_2/tree_update/p__Chlamydiota_100_2.treefile
```
  
  Runtime: 781.36 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Chlamydiota_100/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Chlamydiota_100/loop_1/tree_update/p__Chlamydiota_100_1.treefile', tree2_path = '../Result/safe_phyla/p__Chlamydiota_100/loop_2/tree_update/p__Chlamydiota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Chlamydiota_100/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.013  
Tree 1 branch length: 104.812103475  
Tree 2 branch length: 105.109831013  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997882234081934  
Euclidean distance: 0.11391916737283568  
Time usage for Loop_2: 22414.31 seconds (6.23 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Chlamydiota_100/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Chlamydiota_100/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Chlamydiota_100/loop_2/tree_update/p__Chlamydiota_100_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Chlamydiota_100/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 126  
Normalized RF distance: 0.2045  
Tree 1 branch length: 73.72264  
Tree 2 branch length: 105.109831013  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Chlamydiota_100_2):  
Pearson's correlation: 0.9945097594478073  
Euclidean distance: 0.5751377654376545  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Chlamydiota_100/loop_2/tree_update/p__Chlamydiota_100_2.treefile -l 5 -u 100 -o ../Result/safe_phyla/p__Chlamydiota_100/final_test/subtrees -m random
```
  
Original number of taxa: 311   
Number of pruned subtrees: 5   
Number of taxa after pruning: 306   
Pruned node IDs (degree): 111 (46) 158 (41) 198 (83) 4 (65) 40 (71)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Chlamydiota_100/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 16 loci files. Total number of potential alignments: 80.  
Obtained 80 alignments from all potential alignments.  
Remaining 80 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Chlamydiota_100/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Chlamydiota_100_2 -mdef ../Result/safe_phyla/p__Chlamydiota_100/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Chlamydiota_100/final_test/p__Chlamydiota_100_test_partition
```
  
  Runtime: 151.34 seconds
Best models for test data:  
p__Chlamydiota_100_2  

| Model | Count |
|-------|-------|
| 71 | p__Chlamydiota_100_2 |
| 4 | Q.INSECT |
| 3 | MTMET |
| 1 | Q.YEAST |
| 1 | LG |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Chlamydiota_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Chlamydiota_100_2 -mdef ../Result/safe_phyla/p__Chlamydiota_100/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Chlamydiota_100/loop_2/tree_update/p__Chlamydiota_100_2.treefile -pre ../Result/safe_phyla/p__Chlamydiota_100/final_test/p__Chlamydiota_100_test_concat
```
  
  Runtime: 514.00 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Chlamydiota_100_2+I+G4 | -1200264.265 | 2405919.965 |
| p__Chlamydiota_100_2+F+I+G4 | -1203702.243 | 2412960.876 |
| Q.YEAST+I+G4 | -1203941.137 | 2413273.709 |
| Q.INSECT+I+G4 | -1204883.185 | 2415157.805 |
| LG+F+I+G4 | -1205961.838 | 2417480.066 |
| Q.YEAST+F+I+G4 | -1206933.111 | 2419422.612 |
| LG+I+G4 | -1207122.038 | 2419635.511 |
| Q.PFAM+F+I+G4 | -1207121.817 | 2419800.024 |
| Q.PFAM+I+G4 | -1208526.592 | 2422444.619 |
| Q.INSECT+F+I+G4 | -1209046.199 | 2423648.788 |
| LG+G4 | -1209564.559 | 2424511.871 |
| MTMET+F+I+G4 | -1232893.493 | 2471343.376 |
| MTART+F+I+G4 | -1241440.608 | 2488437.606 |
| MTMET+I+G4 | -1267940.297 | 2541272.029 |
| MTART+I+G4 | -1278639.452 | 2562670.339 |
| LG+I | -1320562.448 | 2646507.649 |
| LG | -1351712.245 | 2708798.561 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Chlamydiota_100/trained_models/trained_model.nex ../Result/safe_phyla/p__Chlamydiota_100/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 56520.42 seconds (15.70 h)  
