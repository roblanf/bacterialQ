## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_250  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 1000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_250/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_250/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_250/ref_tree.tre -l 5 -u 250 -o ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 20   
Number of taxa after pruning: 1884   
Pruned node IDs (degree): 15 (204) 1415 (35) 4 (10) 1376 (39) 1891 (164) 1163 (214) 1450 (116) 1565 (164) 222 (23) 246 (47) 293 (98) 392 (7) 1147 (15) 685 (168) 401 (21) 1127 (21) 422 (78) 499 (185) 854 (155) 1008 (120)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 20 subtree files and 100 loci files. Total number of potential alignments: 2000.  
Sub-sampling 1000 alignments from 2000 alignments.  
Remaining 1000 alignments. Deleted 12 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/subtree_update/p__Acidobacteriota_250
```
  
  Runtime: 96116.43 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_250.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| 364 | Q.PFAM |
| 299 | Q.INSECT |
| 258 | LG |
| 79 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/subtree_update/p__Acidobacteriota_250.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/subtree_update/p__Acidobacteriota_250.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/model_update/p__Acidobacteriota_250
```
  
  Runtime: 165712.02 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_250.iqtree)  
BIC of the new model: 32318914.1435  
Likelihood of the new model: -15128004.6069  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_250_1)  
Model set for next iteration: Q.PFAM,Q.INSECT,LG,Q.YEAST,p__Acidobacteriota_250_1  
![Model bubble plot](loop_1/p__Acidobacteriota_250_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_250/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_250/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile
```
  
  Runtime: 5707.84 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_250/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_250/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_250/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 638  
Normalized RF distance: 0.169  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 302.400207254  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9881162763120781  
Euclidean distance: 0.9156990314982406  
Time usage for Loop_1: 267599.04 seconds (74.33 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_250/loci/concat_testing_loci.faa -m TESTONLY -mset Q.PFAM,Q.INSECT,LG,Q.YEAST,p__Acidobacteriota_250_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_250/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/test_model/p__Acidobacteriota_250_test_concat
```
  
  Runtime: 1141.52 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_250_1+I+G4 | -5320540.681 | 10674493.340 |
| p__Acidobacteriota_250_1+F+I+G4 | -5330283.206 | 10694146.290 |
| Q.YEAST+F+I+G4 | -5343884.257 | 10721348.392 |
| Q.INSECT+F+I+G4 | -5344699.153 | 10722978.184 |
| LG+F+I+G4 | -5346246.877 | 10726073.632 |
| Q.PFAM+F+I+G4 | -5350518.263 | 10734616.404 |
| Q.PFAM+I+G4 | -5354768.768 | 10742949.514 |
| Q.PFAM+G4 | -5360787.876 | 10754978.893 |
| LG+I+G4 | -5362825.088 | 10759062.154 |
| Q.INSECT+I+G4 | -5366036.635 | 10765485.248 |
| Q.YEAST+I+G4 | -5380137.863 | 10793687.704 |
| Q.PFAM+I | -5870450.580 | 11774304.301 |
| Q.PFAM | -5928748.470 | 11890891.245 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile -l 5 -u 250 -o ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 19   
Number of taxa after pruning: 1886   
Pruned node IDs (degree): 149 (158) 152 (47) 1670 (213) 1141 (214) 1356 (35) 200 (23) 1391 (12) 1403 (164) 1566 (105) 995 (145) 226 (7) 981 (15) 519 (168) 235 (21) 961 (21) 256 (78) 333 (185) 688 (155) 842 (120)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 19 subtree files and 100 loci files. Total number of potential alignments: 1900.  
Sub-sampling 1000 alignments from 1900 alignments.  
Remaining 1000 alignments. Deleted 10 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/training_loci -m MFP -mset Q.PFAM,Q.INSECT,LG,Q.YEAST,p__Acidobacteriota_250_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/subtree_update/p__Acidobacteriota_250
```
  
  Runtime: 47955.26 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_250.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_250_1  

| Model | Count |
|-------|-------|
| 813 | p__Acidobacteriota_250_1 |
| 88 | Q.INSECT |
| 55 | LG |
| 32 | Q.PFAM |
| 12 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/subtree_update/p__Acidobacteriota_250.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/subtree_update/p__Acidobacteriota_250.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_250_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/model_update/p__Acidobacteriota_250
```
  
  Runtime: 81085.81 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_250.iqtree)  
BIC of the new model: 34611380.6974  
Likelihood of the new model: -16181297.5457  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_250_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_2  
![Model bubble plot](loop_2/p__Acidobacteriota_250_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_250/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_250/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile
```
  
  Runtime: 5292.78 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_250/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_250/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 302.400207254  
Tree 2 branch length: 303.651818779  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999302630386379  
Euclidean distance: 0.07037134671525933  
Time usage for Loop_2: 134446.91 seconds (37.35 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_250/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_250/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_250/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 638  
Normalized RF distance: 0.169  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 303.651818779  
### Model comparison  
Comparison between initial best model (Q.PFAM) and final model (p__Acidobacteriota_250_2):  
Pearson's correlation: 0.9872428682399764  
Euclidean distance: 0.9550883764451356  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile -l 5 -u 250 -o ../Result_rona/formal_test/p__Acidobacteriota_250/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 19   
Number of taxa after pruning: 1886   
Pruned node IDs (degree): 149 (158) 152 (47) 1670 (213) 1141 (214) 1356 (35) 200 (23) 1391 (12) 1403 (164) 1566 (105) 995 (145) 226 (7) 981 (15) 519 (168) 235 (21) 961 (21) 256 (78) 333 (185) 688 (155) 842 (120)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_250/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 19 subtree files and 20 loci files. Total number of potential alignments: 380.  
Obtained 379 alignments from all potential alignments.  
Remaining 379 alignments. Deleted 1 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_250/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_250/final_test/p__Acidobacteriota_250_test_partition
```
  
  Runtime: 417.62 seconds
Best models for test data:  
p__Acidobacteriota_250_2  

| Model | Count |
|-------|-------|
| 302 | p__Acidobacteriota_250_2 |
| 34 | Q.INSECT |
| 23 | LG |
| 10 | Q.PFAM |
| 5 | Q.YEAST |
| 4 | MTART |
| 1 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_250/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_250/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_250/final_test/p__Acidobacteriota_250_test_concat
```
  
  Runtime: 1096.28 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_250_2+I+G4 | -5320118.975 | 10673649.928 |
| p__Acidobacteriota_250_2+F+I+G4 | -5330922.450 | 10695424.778 |
| Q.YEAST+F+I+G4 | -5343884.257 | 10721348.392 |
| Q.INSECT+F+I+G4 | -5344699.165 | 10722978.208 |
| LG+F+I+G4 | -5346246.822 | 10726073.522 |
| Q.PFAM+F+I+G4 | -5350518.243 | 10734616.364 |
| Q.PFAM+I+G4 | -5354768.766 | 10742949.510 |
| LG+I+G4 | -5362825.102 | 10759062.182 |
| Q.INSECT+I+G4 | -5366036.633 | 10765485.244 |
| LG+G4 | -5368796.563 | 10770996.267 |
| Q.YEAST+I+G4 | -5380137.863 | 10793687.704 |
| MTMET+F+I+G4 | -5505648.708 | 11044877.294 |
| MTART+F+I+G4 | -5619037.540 | 11271654.958 |
| MTMET+I+G4 | -5743775.837 | 11520963.652 |
| MTART+I+G4 | -5854852.237 | 11743116.452 |
| LG+I | -5878276.680 | 11789956.501 |
| LG | -5936787.393 | 11906969.091 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Acidobacteriota_250/trained_models/trained_model.nex ../Result_rona/formal_test/p__Acidobacteriota_250/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 404815.25 seconds (112.45 h)  
