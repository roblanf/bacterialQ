## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Margulisbacteria_50  
  Taxa name: p__Margulisbacteria  
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
Input a single taxa file: ../Result/safe_phyla/p__Margulisbacteria_50/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 87  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 4 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Margulisbacteria_50/select_id.txt. Sampling sequences for 16 loci.  
Number of input species: 87  
Remaining 16 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Margulisbacteria_50/ref_tree.tre -l 5 -u 50 -o ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/subtrees -m random
```
  
Original number of taxa: 87   
Number of pruned subtrees: 2   
Number of taxa after pruning: 86   
Pruned node IDs (degree): 5 (36) 3 (50)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 2 subtree files and 98 loci files. Total number of potential alignments: 196.  
Obtained 196 alignments from all potential alignments.  
Remaining 196 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/subtree_update/p__Margulisbacteria_50
```
  
  Runtime: 3517.15 seconds
[Subtree update log](loop_1/subtree_update/p__Margulisbacteria_50.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| 112 | Q.YEAST |
| 47 | LG |
| 19 | Q.INSECT |
| 18 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/subtree_update/p__Margulisbacteria_50.best_scheme.nex -te ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/subtree_update/p__Margulisbacteria_50.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/model_update/p__Margulisbacteria_50
```
  
  Runtime: 10318.18 seconds
[Model update log](loop_1/model_update/p__Margulisbacteria_50.iqtree)  
BIC of the new model: 5039326.0864  
Likelihood of the new model: -2438368.0649  
Model does not meet precision requirement.  
[New model](trained_models/p__Margulisbacteria_50_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,Q.PFAM,p__Margulisbacteria_50_1  
![Model bubble plot](loop_1/p__Margulisbacteria_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Margulisbacteria_50/ref_tree.tre ../Result/safe_phyla/p__Margulisbacteria_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/tree_update/p__Margulisbacteria_50_1.treefile
```
  
  Runtime: 424.93 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Margulisbacteria_50/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Margulisbacteria_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Margulisbacteria_50/loop_1/tree_update/p__Margulisbacteria_50_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Margulisbacteria_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 30  
Normalized RF distance: 0.1786  
Tree 1 branch length: 26.66691  
Tree 2 branch length: 36.292648457  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.995024798390076  
Euclidean distance: 0.5206435501930055  
Time usage for Loop_1: 14272.86 seconds (3.96 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Margulisbacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset Q.YEAST,LG,Q.INSECT,Q.PFAM,p__Margulisbacteria_50_1 -mdef ../Result/safe_phyla/p__Margulisbacteria_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/tree_update/p__Margulisbacteria_50_1.treefile -pre ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/test_model/p__Margulisbacteria_50_test_concat
```
  
  Runtime: 182.26 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Margulisbacteria_50_1+I+G4 | -392775.310 | 787050.753 |
| Q.YEAST+I+G4 | -393507.052 | 788514.236 |
| p__Margulisbacteria_50_1+F+I+G4 | -393652.360 | 788969.607 |
| Q.INSECT+I+G4 | -394221.067 | 789942.267 |
| Q.YEAST+G4 | -394254.121 | 789999.703 |
| LG+F+I+G4 | -394175.815 | 790016.517 |
| LG+I+G4 | -394413.146 | 790326.425 |
| Q.PFAM+F+I+G4 | -394491.533 | 790647.953 |
| Q.YEAST+F+I+G4 | -394569.701 | 790804.289 |
| Q.PFAM+I+G4 | -394756.716 | 791013.566 |
| Q.INSECT+F+I+G4 | -395555.299 | 792775.484 |
| Q.YEAST+I | -418843.405 | 839178.271 |
| Q.YEAST | -432175.378 | 865833.545 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Margulisbacteria_50/loop_1/tree_update/p__Margulisbacteria_50_1.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/subtrees -m random
```
  
Original number of taxa: 87   
Number of pruned subtrees: 3   
Number of taxa after pruning: 87   
Pruned node IDs (degree): 44 (36) 35 (43) 79 (8)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 98 loci files. Total number of potential alignments: 294.  
Obtained 292 alignments from all potential alignments.  
Remaining 292 alignments. Deleted 2 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,Q.PFAM,p__Margulisbacteria_50_1 -mdef ../Result/safe_phyla/p__Margulisbacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/subtree_update/p__Margulisbacteria_50
```
  
  Runtime: 2640.08 seconds
[Subtree update log](loop_2/subtree_update/p__Margulisbacteria_50.iqtree)  
Best models for iteration 2:  
p__Margulisbacteria_50_1  

| Model | Count |
|-------|-------|
| 203 | p__Margulisbacteria_50_1 |
| 37 | Q.PFAM |
| 25 | LG |
| 19 | Q.YEAST |
| 8 | Q.INSECT |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/subtree_update/p__Margulisbacteria_50.best_scheme.nex -te ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/subtree_update/p__Margulisbacteria_50.treefile --model-joint GTR20+FO --init-model p__Margulisbacteria_50_1 -mdef ../Result/safe_phyla/p__Margulisbacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/model_update/p__Margulisbacteria_50
```
  
  Runtime: 5998.85 seconds
[Model update log](loop_2/model_update/p__Margulisbacteria_50.iqtree)  
BIC of the new model: 5234941.1556  
Likelihood of the new model: -2533185.6696  
Model does not meet precision requirement.  
[New model](trained_models/p__Margulisbacteria_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Margulisbacteria_50_2  
![Model bubble plot](loop_2/p__Margulisbacteria_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Margulisbacteria_50/ref_tree.tre ../Result/safe_phyla/p__Margulisbacteria_50/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/tree_update/p__Margulisbacteria_50_2.treefile
```
  
  Runtime: 419.48 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Margulisbacteria_50/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Margulisbacteria_50/loop_1/tree_update/p__Margulisbacteria_50_1.treefile', tree2_path = '../Result/safe_phyla/p__Margulisbacteria_50/loop_2/tree_update/p__Margulisbacteria_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Margulisbacteria_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 36.292648457  
Tree 2 branch length: 36.2566928  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.99980814102464  
Euclidean distance: 0.10260743975461797  
Time usage for Loop_2: 9072.76 seconds (2.52 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Margulisbacteria_50/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Margulisbacteria_50/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Margulisbacteria_50/loop_2/tree_update/p__Margulisbacteria_50_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Margulisbacteria_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 30  
Normalized RF distance: 0.1786  
Tree 1 branch length: 26.66691  
Tree 2 branch length: 36.2566928  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (p__Margulisbacteria_50_2):  
Pearson's correlation: 0.9940823092636997  
Euclidean distance: 0.5684289890105224  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/tree_update/p__Margulisbacteria_50_2.treefile -l 5 -u 50 -o ../Result/safe_phyla/p__Margulisbacteria_50/final_test/subtrees -m random
```
  
Original number of taxa: 87   
Number of pruned subtrees: 3   
Number of taxa after pruning: 87   
Pruned node IDs (degree): 44 (36) 35 (43) 79 (8)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Margulisbacteria_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 3 subtree files and 16 loci files. Total number of potential alignments: 48.  
Obtained 48 alignments from all potential alignments.  
Remaining 48 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Margulisbacteria_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Margulisbacteria_50_2 -mdef ../Result/safe_phyla/p__Margulisbacteria_50/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Margulisbacteria_50/final_test/p__Margulisbacteria_50_test_partition
```
  
  Runtime: 9075.05 seconds
Best models for test data:  
p__Margulisbacteria_50_2  

| Model | Count |
|-------|-------|
| 36 | p__Margulisbacteria_50_2 |
| 5 | Q.PFAM |
| 3 | LG |
| 2 | Q.YEAST |
| 2 | MTART |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Margulisbacteria_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Margulisbacteria_50_2 -mdef ../Result/safe_phyla/p__Margulisbacteria_50/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Margulisbacteria_50/loop_2/tree_update/p__Margulisbacteria_50_2.treefile -pre ../Result/safe_phyla/p__Margulisbacteria_50/final_test/p__Margulisbacteria_50_test_concat
```
  
  Runtime: 538.48 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Margulisbacteria_50_2+I+G4 | -392839.120 | 787178.372 |
| Q.YEAST+I+G4 | -393507.057 | 788514.248 |
| p__Margulisbacteria_50_2+F+I+G4 | -393520.900 | 788706.687 |
| Q.INSECT+I+G4 | -394221.065 | 789942.263 |
| LG+F+I+G4 | -394175.809 | 790016.504 |
| LG+I+G4 | -394413.139 | 790326.412 |
| Q.PFAM+F+I+G4 | -394491.527 | 790647.940 |
| Q.YEAST+F+I+G4 | -394569.698 | 790804.283 |
| Q.PFAM+I+G4 | -394756.717 | 791013.567 |
| LG+G4 | -395126.949 | 791745.359 |
| Q.INSECT+F+I+G4 | -395555.296 | 792775.479 |
| MTMET+F+I+G4 | -403471.873 | 808608.632 |
| MTART+F+I+G4 | -404932.713 | 811530.313 |
| MTMET+I+G4 | -415774.043 | 833048.219 |
| MTART+I+G4 | -417637.318 | 836774.768 |
| LG+I | -418213.692 | 837918.846 |
| LG | -430662.614 | 862808.018 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Margulisbacteria_50/trained_models/trained_model.nex ../Result/safe_phyla/p__Margulisbacteria_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 33202.93 seconds (9.22 h)  
