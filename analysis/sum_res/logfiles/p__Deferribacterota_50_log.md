## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Deferribacterota_50  
  Taxa name: p__Deferribacterota  
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
Input a single taxa file: ../Result/safe_phyla/p__Deferribacterota_50/select_id.txt. Sampling sequences for 99 loci.  
Number of input species: 50  
Remaining 99 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Deferribacterota_50/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 50  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Deferribacterota_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Deferribacterota_50/loop_1/subtrees -m random
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Deferribacterota_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 99 loci files. Total number of potential alignments: 99.  
Obtained 99 alignments from all potential alignments.  
Remaining 99 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deferribacterota_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Deferribacterota_50/loop_1/subtree_update/p__Deferribacterota_50
```
  
  Runtime: 4187.22 seconds
[Subtree update log](loop_1/subtree_update/p__Deferribacterota_50.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 58 | Q.YEAST |
| 25 | Q.INSECT |
| 14 | LG |
| 2 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deferribacterota_50/loop_1/subtree_update/p__Deferribacterota_50.best_scheme.nex -te ../Result/safe_phyla/p__Deferribacterota_50/loop_1/subtree_update/p__Deferribacterota_50.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Deferribacterota_50/loop_1/model_update/p__Deferribacterota_50
```
  
  Runtime: 9078.82 seconds
[Model update log](loop_1/model_update/p__Deferribacterota_50.iqtree)  
BIC of the new model: 2096348.4721  
Likelihood of the new model: -1000094.6541  
Model does not meet precision requirement.  
[New model](trained_models/p__Deferribacterota_50_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,p__Deferribacterota_50_1  
![Model bubble plot](loop_1/p__Deferribacterota_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Deferribacterota_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Deferribacterota_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Deferribacterota_50/ref_tree.tre ../Result/safe_phyla/p__Deferribacterota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Deferribacterota_50/loop_1/tree_update/p__Deferribacterota_50_1.treefile
```
  
  Runtime: 234.46 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Deferribacterota_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Deferribacterota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Deferribacterota_50/loop_1/tree_update/p__Deferribacterota_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Deferribacterota_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0426  
Tree 1 branch length: 7.46515  
Tree 2 branch length: 11.511121177  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9923279461239514  
Euclidean distance: 0.6478508712558799  
Time usage for Loop_1: 13509.18 seconds (3.75 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Deferribacterota_50/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,Q.INSECT,LG,p__Deferribacterota_50_1 -mdef ../Result/safe_phyla/p__Deferribacterota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Deferribacterota_50/loop_1/tree_update/p__Deferribacterota_50_1.treefile -pre ../Result/safe_phyla/p__Deferribacterota_50/loop_1/test_model/p__Deferribacterota_50_test_concat
```
  
  Runtime: 304.57 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Deferribacterota_50_1+I+G4 | -190227.401 | 381329.647 |
| p__Deferribacterota_50_1+F+I+G4 | -190498.317 | 382039.378 |
| LG+F+I+G4 | -190930.248 | 382903.239 |
| Q.YEAST+I+G4 | -191054.006 | 382982.857 |
| Q.YEAST+F+I+G4 | -191034.806 | 383112.355 |
| Q.INSECT+I+G4 | -191272.696 | 383420.235 |
| Q.YEAST+G4 | -191282.554 | 383431.116 |
| Q.INSECT+F+I+G4 | -191234.628 | 383511.999 |
| LG+I+G4 | -191722.768 | 384320.380 |
| Q.YEAST+I | -199277.392 | 399420.792 |
| Q.YEAST | -206917.308 | 414691.786 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Deferribacterota_50/loop_1/tree_update/p__Deferribacterota_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Deferribacterota_50/loop_2/subtrees -m random
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Deferribacterota_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 99 loci files. Total number of potential alignments: 99.  
Obtained 99 alignments from all potential alignments.  
Remaining 99 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deferribacterota_50/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,p__Deferribacterota_50_1 -mdef ../Result/safe_phyla/p__Deferribacterota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Deferribacterota_50/loop_2/subtree_update/p__Deferribacterota_50
```
  
  Runtime: 2580.36 seconds
[Subtree update log](loop_2/subtree_update/p__Deferribacterota_50.iqtree)  
Best models for iteration 2:  
p__Deferribacterota_50_1  

| Model | Count |
|-------|-------|
| 96 | p__Deferribacterota_50_1 |
| 1 | Q.YEAST |
| 1 | Q.INSECT |
| 1 | LG |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deferribacterota_50/loop_2/subtree_update/p__Deferribacterota_50.best_scheme.nex -te ../Result/safe_phyla/p__Deferribacterota_50/loop_2/subtree_update/p__Deferribacterota_50.treefile --model-joint GTR20+FO --init-model p__Deferribacterota_50_1 -mdef ../Result/safe_phyla/p__Deferribacterota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Deferribacterota_50/loop_2/model_update/p__Deferribacterota_50
```
  
  Runtime: 6360.08 seconds
[Model update log](loop_2/model_update/p__Deferribacterota_50.iqtree)  
BIC of the new model: 2096207.252  
Likelihood of the new model: -1000071.0069  
Model does not meet precision requirement.  
[New model](trained_models/p__Deferribacterota_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Deferribacterota_50_2  
![Model bubble plot](loop_2/p__Deferribacterota_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Deferribacterota_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Deferribacterota_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Deferribacterota_50/ref_tree.tre ../Result/safe_phyla/p__Deferribacterota_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Deferribacterota_50/loop_2/tree_update/p__Deferribacterota_50_2.treefile
```
  
  Runtime: 200.53 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Deferribacterota_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Deferribacterota_50/loop_1/tree_update/p__Deferribacterota_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Deferribacterota_50/loop_2/tree_update/p__Deferribacterota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Deferribacterota_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 11.511121177  
Tree 2 branch length: 11.50259093  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999937145691965  
Euclidean distance: 0.05944216266050882  
Time usage for Loop_2: 9179.86 seconds (2.55 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Deferribacterota_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Deferribacterota_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Deferribacterota_50/loop_2/tree_update/p__Deferribacterota_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Deferribacterota_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0426  
Tree 1 branch length: 7.46515  
Tree 2 branch length: 11.50259093  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Deferribacterota_50_2):  
Pearson's correlation: 0.992171160209493  
Euclidean distance: 0.6557627870186502  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Deferribacterota_50/loop_2/tree_update/p__Deferribacterota_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Deferribacterota_50/final_test/subtrees -m random
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Deferribacterota_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 20 loci files. Total number of potential alignments: 20.  
Obtained 20 alignments from all potential alignments.  
Remaining 20 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Deferribacterota_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Deferribacterota_50_2 -mdef ../Result/safe_phyla/p__Deferribacterota_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Deferribacterota_50/final_test/p__Deferribacterota_50_test_partition
```
  
  Runtime: 7040.58 seconds
Best models for test data:  
p__Deferribacterota_50_2  

| Model | Count |
|-------|-------|
| 19 | p__Deferribacterota_50_2 |
| 1 | MTART |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Deferribacterota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Deferribacterota_50_2 -mdef ../Result/safe_phyla/p__Deferribacterota_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Deferribacterota_50/loop_2/tree_update/p__Deferribacterota_50_2.treefile -pre ../Result/safe_phyla/p__Deferribacterota_50/final_test/p__Deferribacterota_50_test_concat
```
  
  Runtime: 664.16 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Deferribacterota_50_2+I+G4 | -190224.370 | 381323.585 |
| p__Deferribacterota_50_2+F+I+G4 | -190485.903 | 382014.550 |
| LG+F+I+G4 | -190930.232 | 382903.207 |
| Q.YEAST+I+G4 | -191054.004 | 382982.852 |
| Q.YEAST+F+I+G4 | -191034.819 | 383112.382 |
| Q.INSECT+I+G4 | -191272.732 | 383420.308 |
| Q.PFAM+F+I+G4 | -191214.743 | 383472.230 |
| Q.INSECT+F+I+G4 | -191234.669 | 383512.082 |
| LG+I+G4 | -191722.776 | 384320.396 |
| LG+G4 | -191939.687 | 384745.381 |
| Q.PFAM+I+G4 | -192125.247 | 385125.339 |
| MTMET+F+I+G4 | -194550.004 | 390142.752 |
| MTART+F+I+G4 | -195248.709 | 391540.161 |
| LG+I | -199318.907 | 399503.822 |
| MTMET+I+G4 | -200763.600 | 402402.045 |
| MTART+I+G4 | -201736.280 | 404347.404 |
| LG | -206520.756 | 413898.682 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Deferribacterota_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Deferribacterota_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 30781.09 seconds (8.55 h)  
