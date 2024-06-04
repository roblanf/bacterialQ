## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Krumholzibacteriota_93  
  Taxa name: p__Krumholzibacteriota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 93  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Krumholzibacteriota_93/select_id.txt. Sampling sequences for 99 loci.  
Number of input species: 93  
Remaining 99 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Krumholzibacteriota_93/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 93  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Krumholzibacteriota_93/ref_tree.tre -l 5 -u 93 -o ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/subtrees -m random
```
  
Original number of taxa: 93   
Number of pruned subtrees: 1   
Number of taxa after pruning: 93   
Pruned node IDs (degree): 1 (93)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 99 loci files. Total number of potential alignments: 99.  
Obtained 99 alignments from all potential alignments.  
Remaining 99 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/subtree_update/p__Krumholzibacteriota_93
```
  
  Runtime: 4099.15 seconds
[Subtree update log](loop_1/subtree_update/p__Krumholzibacteriota_93.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 36 | LG |
| 33 | Q.PFAM |
| 22 | Q.INSECT |
| 8 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/subtree_update/p__Krumholzibacteriota_93.best_scheme.nex -te ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/subtree_update/p__Krumholzibacteriota_93.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/model_update/p__Krumholzibacteriota_93
```
  
  Runtime: 8781.27 seconds
[Model update log](loop_1/model_update/p__Krumholzibacteriota_93.iqtree)  
BIC of the new model: 4154032.0462  
Likelihood of the new model: -1991027.5001  
Model does not meet precision requirement.  
[New model](trained_models/p__Krumholzibacteriota_93_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Krumholzibacteriota_93_1  
![Model bubble plot](loop_1/p__Krumholzibacteriota_93_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Krumholzibacteriota_93/ref_tree.tre ../Result/safe_phyla/p__Krumholzibacteriota_93/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/tree_update/p__Krumholzibacteriota_93_1.treefile
```
  
  Runtime: 203.70 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/tree_update/p__Krumholzibacteriota_93_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 16  
Normalized RF distance: 0.0889  
Tree 1 branch length: 16.45173  
Tree 2 branch length: 21.699476187  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9864858614274711  
Euclidean distance: 1.0429733482294745  
Time usage for Loop_1: 13092.64 seconds (3.64 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Krumholzibacteriota_93/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Krumholzibacteriota_93_1 -mdef ../Result/safe_phyla/p__Krumholzibacteriota_93/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/tree_update/p__Krumholzibacteriota_93_1.treefile -pre ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/test_model/p__Krumholzibacteriota_93_test_concat
```
  
  Runtime: 82.54 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Krumholzibacteriota_93_1+I+G4 | -342410.834 | 686449.075 |
| p__Krumholzibacteriota_93_1+F+I+G4 | -342951.454 | 687697.453 |
| LG+F+I+G4 | -343573.752 | 688942.051 |
| Q.PFAM+F+I+G4 | -343882.598 | 689559.742 |
| Q.YEAST+F+I+G4 | -344008.521 | 689811.589 |
| Q.INSECT+F+I+G4 | -344543.305 | 690881.155 |
| Q.PFAM+I+G4 | -344714.511 | 691056.429 |
| LG+I+G4 | -345120.138 | 691867.683 |
| LG+G4 | -345725.324 | 693069.258 |
| Q.INSECT+I+G4 | -346464.336 | 694556.078 |
| Q.YEAST+I+G4 | -347078.969 | 695785.345 |
| LG+I | -364741.683 | 731101.977 |
| LG | -376523.204 | 754656.221 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/tree_update/p__Krumholzibacteriota_93_1.treefile -l 5 -u 93 -o ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/subtrees -m random
```
  
Original number of taxa: 93   
Number of pruned subtrees: 1   
Number of taxa after pruning: 93   
Pruned node IDs (degree): 1 (93)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 99 loci files. Total number of potential alignments: 99.  
Obtained 99 alignments from all potential alignments.  
Remaining 99 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Krumholzibacteriota_93_1 -mdef ../Result/safe_phyla/p__Krumholzibacteriota_93/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/subtree_update/p__Krumholzibacteriota_93
```
  
  Runtime: 4138.83 seconds
[Subtree update log](loop_2/subtree_update/p__Krumholzibacteriota_93.iqtree)  
Best models for iteration 2:  
p__Krumholzibacteriota_93_1  

| Model | Count |
|-------|-------|
| 79 | p__Krumholzibacteriota_93_1 |
| 10 | Q.INSECT |
| 4 | LG |
| 3 | Q.YEAST |
| 3 | Q.PFAM |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/subtree_update/p__Krumholzibacteriota_93.best_scheme.nex -te ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/subtree_update/p__Krumholzibacteriota_93.treefile --model-joint GTR20+FO --init-model p__Krumholzibacteriota_93_1 -mdef ../Result/safe_phyla/p__Krumholzibacteriota_93/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/model_update/p__Krumholzibacteriota_93
```
  
  Runtime: 8747.06 seconds
[Model update log](loop_2/model_update/p__Krumholzibacteriota_93.iqtree)  
BIC of the new model: 4153542.7239  
Likelihood of the new model: -1990741.1071  
Model does not meet precision requirement.  
[New model](trained_models/p__Krumholzibacteriota_93_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Krumholzibacteriota_93_2  
![Model bubble plot](loop_2/p__Krumholzibacteriota_93_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Krumholzibacteriota_93/ref_tree.tre ../Result/safe_phyla/p__Krumholzibacteriota_93/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/tree_update/p__Krumholzibacteriota_93_2.treefile
```
  
  Runtime: 203.14 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/loop_1/tree_update/p__Krumholzibacteriota_93_1.treefile', tree2_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/tree_update/p__Krumholzibacteriota_93_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 21.699476187  
Tree 2 branch length: 21.698709694  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997067151431979  
Euclidean distance: 0.14200901789768677  
Time usage for Loop_2: 13097.26 seconds (3.64 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Krumholzibacteriota_93/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/tree_update/p__Krumholzibacteriota_93_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Krumholzibacteriota_93/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 16  
Normalized RF distance: 0.0889  
Tree 1 branch length: 16.45173  
Tree 2 branch length: 21.698709694  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Krumholzibacteriota_93_2):  
Pearson's correlation: 0.9851466055042908  
Euclidean distance: 1.1017504327517786  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/tree_update/p__Krumholzibacteriota_93_2.treefile -l 5 -u 93 -o ../Result/safe_phyla/p__Krumholzibacteriota_93/final_test/subtrees -m random
```
  
Original number of taxa: 93   
Number of pruned subtrees: 1   
Number of taxa after pruning: 93   
Pruned node IDs (degree): 1 (93)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Krumholzibacteriota_93/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 1 subtree files and 19 loci files. Total number of potential alignments: 19.  
Obtained 19 alignments from all potential alignments.  
Remaining 19 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Krumholzibacteriota_93/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Krumholzibacteriota_93_2 -mdef ../Result/safe_phyla/p__Krumholzibacteriota_93/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Krumholzibacteriota_93/final_test/p__Krumholzibacteriota_93_test_partition
```
  
  Runtime: 3243.83 seconds
Best models for test data:  
p__Krumholzibacteriota_93_2  

| Model | Count |
|-------|-------|
| 16 | p__Krumholzibacteriota_93_2 |
| 2 | LG |
| 1 | Q.INSECT |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Krumholzibacteriota_93/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Krumholzibacteriota_93_2 -mdef ../Result/safe_phyla/p__Krumholzibacteriota_93/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Krumholzibacteriota_93/loop_2/tree_update/p__Krumholzibacteriota_93_2.treefile -pre ../Result/safe_phyla/p__Krumholzibacteriota_93/final_test/p__Krumholzibacteriota_93_test_concat
```
  
  Runtime: 134.24 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Krumholzibacteriota_93_2+I+G4 | -342401.492 | 686430.390 |
| p__Krumholzibacteriota_93_2+F+I+G4 | -342938.786 | 687672.118 |
| LG+F+I+G4 | -343573.752 | 688942.051 |
| Q.PFAM+F+I+G4 | -343882.598 | 689559.742 |
| Q.YEAST+F+I+G4 | -344008.521 | 689811.589 |
| Q.INSECT+F+I+G4 | -344543.305 | 690881.155 |
| Q.PFAM+I+G4 | -344714.511 | 691056.429 |
| LG+I+G4 | -345120.138 | 691867.683 |
| LG+G4 | -345725.324 | 693069.258 |
| Q.INSECT+I+G4 | -346464.336 | 694556.078 |
| Q.YEAST+I+G4 | -347078.969 | 695785.345 |
| MTMET+F+I+G4 | -353792.070 | 709378.687 |
| MTART+F+I+G4 | -359526.965 | 720848.475 |
| LG+I | -364741.683 | 731101.977 |
| MTMET+I+G4 | -372152.036 | 745931.480 |
| LG | -376523.204 | 754656.221 |
| MTART+I+G4 | -376836.408 | 755300.223 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Krumholzibacteriota_93/trained_models/trained_model.nex ../Result/safe_phyla/p__Krumholzibacteriota_93/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 29674.54 seconds (8.24 h)  
