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
  Pruning mode: random  
  Lower limit for subtree size: 5  
  Upper limit for subtree size: 100  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_100/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_100/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_100/ref_tree.tre -l 5 -u 100 -o ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 45   
Number of taxa after pruning: 1859   
Pruned node IDs (degree): 1415 (35) 4 (10) 189 (30) 151 (39) 1376 (39) 18 (15) 33 (90) 122 (30) 222 (23) 1368 (9) 1554 (12) 1879 (13) 1346 (23) 1452 (17) 1468 (87) 1567 (89) 1655 (74) 1730 (5) 246 (47) 1328 (19) 1735 (48) 1782 (98) 293 (98) 1267 (62) 1168 (100) 392 (7) 1147 (15) 401 (21) 1127 (21) 422 (78) 690 (6) 500 (16) 843 (10) 965 (44) 516 (5) 857 (15) 871 (95) 670 (14) 1012 (18) 1029 (98) 525 (68) 592 (79) 701 (23) 726 (75) 800 (39)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 45 subtree files and 100 loci files. Total number of potential alignments: 4500.  
Sub-sampling 1000 alignments from 4500 alignments.  
Remaining 1000 alignments. Deleted 21 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/subtree_update/p__Acidobacteriota_100
```
  
  Runtime: 12217.68 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_100.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| 336 | LG |
| 326 | Q.PFAM |
| 261 | Q.INSECT |
| 77 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/subtree_update/p__Acidobacteriota_100.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/subtree_update/p__Acidobacteriota_100.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/model_update/p__Acidobacteriota_100
```
  
  Runtime: 18273.81 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_100.iqtree)  
BIC of the new model: 15153515.4842  
Likelihood of the new model: -7122198.3688  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_100_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_100_1  
![Model bubble plot](loop_1/p__Acidobacteriota_100_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_100/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_100/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile
```
  
  Runtime: 6271.94 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_100/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_100/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_100/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 640  
Normalized RF distance: 0.1695  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 301.849785559  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9886181905893321  
Euclidean distance: 0.858962076819  
Time usage for Loop_1: 36842.79 seconds (10.23 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_100_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_100/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/test_model/p__Acidobacteriota_100_test_concat
```
  
  Runtime: 1663.54 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_100_1+I+G4 | -5322568.129 | 10678548.236 |
| p__Acidobacteriota_100_1+F+I+G4 | -5328339.251 | 10690258.380 |
| Q.YEAST+F+I+G4 | -5343939.209 | 10721458.296 |
| Q.INSECT+F+I+G4 | -5344752.302 | 10723084.482 |
| LG+F+I+G4 | -5346301.291 | 10726182.460 |
| Q.PFAM+F+I+G4 | -5350569.543 | 10734718.964 |
| Q.PFAM+I+G4 | -5354805.522 | 10743023.022 |
| LG+I+G4 | -5362861.022 | 10759134.022 |
| Q.INSECT+I+G4 | -5366059.787 | 10765531.552 |
| LG+G4 | -5368835.298 | 10771073.737 |
| Q.YEAST+I+G4 | -5380165.459 | 10793742.896 |
| LG+I | -5878301.827 | 11790006.795 |
| LG | -5936812.976 | 11907020.257 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile -l 5 -u 100 -o ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 45   
Number of taxa after pruning: 1857   
Pruned node IDs (degree): 1882 (5) 152 (47) 1886 (5) 1356 (35) 1860 (23) 5 (48) 52 (98) 200 (23) 1346 (9) 1391 (12) 1672 (16) 1143 (15) 1822 (39) 1158 (8) 1404 (90) 1493 (74) 996 (98) 1093 (47) 1328 (19) 1568 (17) 1584 (87) 1690 (13) 226 (7) 981 (15) 1267 (62) 1703 (76) 1778 (45) 1168 (100) 235 (21) 961 (21) 256 (78) 524 (6) 501 (17) 677 (10) 799 (44) 335 (7) 690 (16) 705 (95) 342 (89) 430 (72) 847 (18) 864 (98) 535 (23) 562 (75) 636 (34)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 45 subtree files and 100 loci files. Total number of potential alignments: 4500.  
Sub-sampling 1000 alignments from 4500 alignments.  
Remaining 1000 alignments. Deleted 24 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,p__Acidobacteriota_100_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_100/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/subtree_update/p__Acidobacteriota_100
```
  
  Runtime: 26261.20 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_100.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_100_1  

| Model | Count |
|-------|-------|
| 816 | p__Acidobacteriota_100_1 |
| 85 | LG |
| 53 | Q.INSECT |
| 29 | Q.PFAM |
| 17 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/subtree_update/p__Acidobacteriota_100.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/subtree_update/p__Acidobacteriota_100.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_100_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_100/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/model_update/p__Acidobacteriota_100
```
  
  Runtime: 53616.13 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_100.iqtree)  
BIC of the new model: 15133524.9673  
Likelihood of the new model: -7098266.1311  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_100_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_100_2  
![Model bubble plot](loop_2/p__Acidobacteriota_100_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_100/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_100/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile
```
  
  Runtime: 16147.78 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_100/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_100/loop_1/tree_update/p__Acidobacteriota_100_1.treefile', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_100/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0026  
Tree 1 branch length: 301.849785559  
Tree 2 branch length: 301.793671685  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998900061707728  
Euclidean distance: 0.08124738636637711  
Time usage for Loop_2: 96173.25 seconds (26.71 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_100/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_100/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_100/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 642  
Normalized RF distance: 0.17  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 301.793671685  
### Model comparison  
Comparison between initial best model (LG) and final model (p__Acidobacteriota_100_2):  
Pearson's correlation: 0.9880263201752274  
Euclidean distance: 0.8832960787880692  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile -l 5 -u 100 -o ../Result_rona/formal_test/p__Acidobacteriota_100/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 45   
Number of taxa after pruning: 1857   
Pruned node IDs (degree): 1882 (5) 152 (47) 1886 (5) 1356 (35) 1860 (23) 5 (48) 52 (98) 200 (23) 1346 (9) 1391 (12) 1672 (16) 1143 (15) 1822 (39) 1158 (8) 1404 (90) 1493 (74) 996 (98) 1093 (47) 1328 (19) 1568 (17) 1584 (87) 1690 (13) 226 (7) 981 (15) 1267 (62) 1703 (76) 1778 (45) 1168 (100) 235 (21) 961 (21) 256 (78) 524 (6) 501 (17) 677 (10) 799 (44) 335 (7) 690 (16) 705 (95) 342 (89) 430 (72) 847 (18) 864 (98) 535 (23) 562 (75) 636 (34)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_100/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 45 subtree files and 20 loci files. Total number of potential alignments: 900.  
Obtained 882 alignments from all potential alignments.  
Remaining 882 alignments. Deleted 18 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_100/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_100_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_100/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_100/final_test/p__Acidobacteriota_100_test_partition
```
  
  Runtime: 2340.41 seconds
Best models for test data:  
p__Acidobacteriota_100_2  

| Model | Count |
|-------|-------|
| 719 | p__Acidobacteriota_100_2 |
| 69 | LG |
| 48 | Q.INSECT |
| 20 | MTART |
| 14 | Q.PFAM |
| 10 | Q.YEAST |
| 2 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_100/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_100_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_100/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_100/loop_2/tree_update/p__Acidobacteriota_100_2.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_100/final_test/p__Acidobacteriota_100_test_concat
```
  
  Runtime: 81142.67 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_100_2+I+G4 | -5322217.209 | 10677846.396 |
| p__Acidobacteriota_100_2+F+I+G4 | -5327699.175 | 10688978.228 |
| Q.YEAST+F+I+G4 | -5343816.544 | 10721212.966 |
| Q.INSECT+F+I+G4 | -5344633.678 | 10722847.234 |
| LG+F+I+G4 | -5346181.800 | 10725943.478 |
| Q.PFAM+F+I+G4 | -5350450.205 | 10734480.288 |
| Q.PFAM+I+G4 | -5354676.132 | 10742764.242 |
| LG+I+G4 | -5362726.494 | 10758864.966 |
| Q.INSECT+I+G4 | -5365917.379 | 10765246.736 |
| LG+G4 | -5368699.303 | 10770801.747 |
| Q.YEAST+I+G4 | -5380022.636 | 10793457.250 |
| MTMET+F+I+G4 | -5505558.803 | 11044697.484 |
| MTART+F+I+G4 | -5618905.664 | 11271391.206 |
| MTMET+I+G4 | -5743677.219 | 11520766.416 |
| MTART+I+G4 | -5854740.377 | 11742892.732 |
| LG+I | -5878199.644 | 11789802.429 |
| LG | -5936710.938 | 11906816.181 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Acidobacteriota_100/trained_models/trained_model.nex ../Result_rona/formal_test/p__Acidobacteriota_100/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 218450.47 seconds (60.68 h)  
