## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Gemmatimonadota_150  
  Taxa name: p__Gemmatimonadota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 150  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Gemmatimonadota_150/select_id.txt. Sampling sequences for 98 loci.  
Number of input species: 535  
Remaining 98 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Gemmatimonadota_150/select_id.txt. Sampling sequences for 19 loci.  
Number of input species: 535  
Remaining 19 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Gemmatimonadota_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 535   
Number of pruned subtrees: 7   
Number of taxa after pruning: 535   
Pruned node IDs (degree): 2 (12) 162 (43) 205 (118) 6 (132) 137 (26) 323 (89) 411 (115)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 7 subtree files and 98 loci files. Total number of potential alignments: 686.  
Obtained 685 alignments from all potential alignments.  
Remaining 685 alignments. Deleted 1 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/subtree_update/p__Gemmatimonadota_150
```
  
  Runtime: 21990.15 seconds
[Subtree update log](loop_1/subtree_update/p__Gemmatimonadota_150.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 247 | LG |
| 192 | Q.PFAM |
| 177 | Q.INSECT |
| 69 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/subtree_update/p__Gemmatimonadota_150.best_scheme.nex -te ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/subtree_update/p__Gemmatimonadota_150.treefile --model-joint GTR20+FO --init-model LG -pre ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/model_update/p__Gemmatimonadota_150
```
  
  Runtime: 39290.36 seconds
[Model update log](loop_1/model_update/p__Gemmatimonadota_150.iqtree)  
BIC of the new model: 18243746.8269  
Likelihood of the new model: -8560228.6634  
Model does not meet precision requirement.  
[New model](trained_models/p__Gemmatimonadota_150_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Gemmatimonadota_150_1  
![Model bubble plot](loop_1/p__Gemmatimonadota_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Gemmatimonadota_150/ref_tree.tre ../Result/safe_phyla/p__Gemmatimonadota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/tree_update/p__Gemmatimonadota_150_1.treefile
```
  
  Runtime: 1690.38 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Gemmatimonadota_150/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Gemmatimonadota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/tree_update/p__Gemmatimonadota_150_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Gemmatimonadota_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 132  
Normalized RF distance: 0.1241  
Tree 1 branch length: 66.39753  
Tree 2 branch length: 89.552852075  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.976829754016255  
Euclidean distance: 1.375313542067387  
Time usage for Loop_1: 63039.06 seconds (17.51 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Gemmatimonadota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Gemmatimonadota_150_1 -mdef ../Result/safe_phyla/p__Gemmatimonadota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/tree_update/p__Gemmatimonadota_150_1.treefile -pre ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/test_model/p__Gemmatimonadota_150_test_concat
```
  
  Runtime: 1059.14 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Gemmatimonadota_150_1+I+G4 | -1493673.616 | 2996764.975 |
| p__Gemmatimonadota_150_1+F+I+G4 | -1497680.402 | 3004945.935 |
| LG+F+I+G4 | -1501666.999 | 3012919.129 |
| Q.PFAM+F+I+G4 | -1502687.924 | 3014960.979 |
| Q.YEAST+F+I+G4 | -1503296.406 | 3016177.943 |
| Q.INSECT+F+I+G4 | -1504621.266 | 3018827.663 |
| Q.PFAM+I+G4 | -1511601.328 | 3032620.399 |
| LG+I+G4 | -1516400.136 | 3042218.015 |
| LG+G4 | -1519388.495 | 3048185.923 |
| Q.INSECT+I+G4 | -1522555.058 | 3054527.859 |
| Q.YEAST+I+G4 | -1527533.618 | 3064484.979 |
| LG+I | -1657139.692 | 3323688.317 |
| LG | -1696349.395 | 3402098.914 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/tree_update/p__Gemmatimonadota_150_1.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/subtrees -m random
```
  
Original number of taxa: 535   
Number of pruned subtrees: 9   
Number of taxa after pruning: 535   
Pruned node IDs (degree): 6 (12) 166 (43) 10 (14) 23 (144) 209 (118) 511 (19) 482 (30) 329 (39) 367 (116)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 9 subtree files and 98 loci files. Total number of potential alignments: 882.  
Obtained 882 alignments from all potential alignments.  
Remaining 882 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Gemmatimonadota_150_1 -mdef ../Result/safe_phyla/p__Gemmatimonadota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/subtree_update/p__Gemmatimonadota_150
```
  
  Runtime: 17928.36 seconds
[Subtree update log](loop_2/subtree_update/p__Gemmatimonadota_150.iqtree)  
Best models for iteration 2:  
p__Gemmatimonadota_150_1  

| Model | Count |
|-------|-------|
| 727 | p__Gemmatimonadota_150_1 |
| 89 | LG |
| 44 | Q.INSECT |
| 19 | Q.PFAM |
| 3 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/subtree_update/p__Gemmatimonadota_150.best_scheme.nex -te ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/subtree_update/p__Gemmatimonadota_150.treefile --model-joint GTR20+FO --init-model p__Gemmatimonadota_150_1 -mdef ../Result/safe_phyla/p__Gemmatimonadota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/model_update/p__Gemmatimonadota_150
```
  
  Runtime: 33245.70 seconds
[Model update log](loop_2/model_update/p__Gemmatimonadota_150.iqtree)  
BIC of the new model: 18616838.9253  
Likelihood of the new model: -8737429.5263  
Model does not meet precision requirement.  
[New model](trained_models/p__Gemmatimonadota_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Gemmatimonadota_150_2  
![Model bubble plot](loop_2/p__Gemmatimonadota_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Gemmatimonadota_150/ref_tree.tre ../Result/safe_phyla/p__Gemmatimonadota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/tree_update/p__Gemmatimonadota_150_2.treefile
```
  
  Runtime: 1693.26 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Gemmatimonadota_150/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Gemmatimonadota_150/loop_1/tree_update/p__Gemmatimonadota_150_1.treefile', tree2_path = '../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/tree_update/p__Gemmatimonadota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Gemmatimonadota_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0019  
Tree 1 branch length: 89.552852075  
Tree 2 branch length: 89.491718449  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998476690776432  
Euclidean distance: 0.10320874117378318  
Time usage for Loop_2: 52911.40 seconds (14.70 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Gemmatimonadota_150/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Gemmatimonadota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/tree_update/p__Gemmatimonadota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Gemmatimonadota_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 134  
Normalized RF distance: 0.1259  
Tree 1 branch length: 66.39753  
Tree 2 branch length: 89.491718449  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Gemmatimonadota_150_2):  
Pearson's correlation: 0.9768484282738953  
Euclidean distance: 1.3620712654666476  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/tree_update/p__Gemmatimonadota_150_2.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Gemmatimonadota_150/final_test/subtrees -m random
```
  
Original number of taxa: 535   
Number of pruned subtrees: 9   
Number of taxa after pruning: 535   
Pruned node IDs (degree): 6 (12) 166 (43) 10 (14) 23 (144) 209 (118) 511 (19) 482 (30) 329 (39) 367 (116)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Gemmatimonadota_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 9 subtree files and 19 loci files. Total number of potential alignments: 171.  
Obtained 171 alignments from all potential alignments.  
Remaining 171 alignments. Deleted 0 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Gemmatimonadota_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Gemmatimonadota_150_2 -mdef ../Result/safe_phyla/p__Gemmatimonadota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Gemmatimonadota_150/final_test/p__Gemmatimonadota_150_test_partition
```
  
  Runtime: 289.50 seconds
Best models for test data:  
p__Gemmatimonadota_150_2  

| Model | Count |
|-------|-------|
| 148 | p__Gemmatimonadota_150_2 |
| 8 | LG |
| 6 | Q.PFAM |
| 5 | Q.INSECT |
| 4 | MTART |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Gemmatimonadota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Gemmatimonadota_150_2 -mdef ../Result/safe_phyla/p__Gemmatimonadota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Gemmatimonadota_150/loop_2/tree_update/p__Gemmatimonadota_150_2.treefile -pre ../Result/safe_phyla/p__Gemmatimonadota_150/final_test/p__Gemmatimonadota_150_test_concat
```
  
  Runtime: 1324.35 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Gemmatimonadota_150_2+I+G4 | -1493783.990 | 2996985.723 |
| p__Gemmatimonadota_150_2+F+I+G4 | -1497444.550 | 3004474.231 |
| LG+F+I+G4 | -1501674.494 | 3012934.119 |
| Q.PFAM+F+I+G4 | -1502696.343 | 3014977.817 |
| Q.YEAST+F+I+G4 | -1503306.206 | 3016197.543 |
| Q.INSECT+F+I+G4 | -1504631.855 | 3018848.841 |
| Q.PFAM+I+G4 | -1511609.245 | 3032636.233 |
| LG+I+G4 | -1516408.324 | 3042234.391 |
| LG+G4 | -1519395.902 | 3048200.737 |
| Q.INSECT+I+G4 | -1522565.666 | 3054549.075 |
| Q.YEAST+I+G4 | -1527543.617 | 3064504.977 |
| MTMET+F+I+G4 | -1556544.817 | 3122674.765 |
| MTART+F+I+G4 | -1594938.198 | 3199461.527 |
| MTMET+I+G4 | -1645161.148 | 3299740.039 |
| LG+I | -1657152.085 | 3323713.103 |
| MTART+I+G4 | -1678873.448 | 3367164.639 |
| LG | -1696361.771 | 3402123.666 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Gemmatimonadota_150/trained_models/trained_model.nex ../Result/safe_phyla/p__Gemmatimonadota_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 118708.56 seconds (32.97 h)  
