## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_50  
  Taxa name: p__Acidobacteriota  
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
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_50/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/formal_test/p__Acidobacteriota_50/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_50/ref_tree.tre -l 5 -u 50 -o ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 69   
Number of taxa after pruning: 1820   
Pruned node IDs (degree): 1415 (35) 4 (10) 189 (30) 151 (39) 1376 (39) 18 (15) 122 (30) 222 (23) 1368 (9) 1554 (12) 1879 (13) 109 (14) 1346 (23) 1452 (17) 1730 (5) 35 (28) 62 (48) 246 (47) 1328 (19) 1568 (48) 1615 (41) 1735 (48) 1521 (32) 385 (6) 1472 (50) 1658 (47) 1704 (24) 381 (5) 392 (7) 1147 (15) 1269 (38) 1306 (22) 1839 (40) 1786 (35) 1820 (20) 297 (6) 401 (21) 1127 (21) 303 (50) 352 (29) 690 (6) 1244 (23) 500 (16) 843 (10) 965 (44) 1238 (7) 516 (5) 857 (15) 426 (40) 465 (31) 670 (14) 1012 (18) 1179 (31) 1209 (30) 701 (23) 1096 (31) 526 (38) 563 (30) 593 (40) 632 (39) 875 (37) 1084 (12) 800 (39) 912 (29) 940 (23) 1033 (44) 1076 (9) 727 (27) 753 (48)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 69 subtree files and 100 loci files. Total number of potential alignments: 6900.  
Sub-sampling 1000 alignments from 6900 alignments.  
Remaining 1000 alignments. Deleted 24 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/subtree_update/p__Acidobacteriota_50
```
  
  Runtime: 1650.09 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_50.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| 357 | Q.PFAM |
| 343 | LG |
| 243 | Q.INSECT |
| 57 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/subtree_update/p__Acidobacteriota_50.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/subtree_update/p__Acidobacteriota_50.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/model_update/p__Acidobacteriota_50
```
  
  Runtime: 11175.06 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_50.iqtree)  
BIC of the new model: 10763861.922  
Likelihood of the new model: -5091393.3227  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_50_1)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Acidobacteriota_50_1  
![Model bubble plot](loop_1/p__Acidobacteriota_50_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_50/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_50/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile
```
  
  Runtime: 7499.27 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_50/loop_1', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_50/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_50/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 646  
Normalized RF distance: 0.1711  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 300.989570228  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9825816916060758  
Euclidean distance: 1.0001305235215467  
Time usage for Loop_1: 20384.19 seconds (5.66 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_50/loci/concat_testing_loci.faa -m TESTONLY -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Acidobacteriota_50_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_50/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/test_model/p__Acidobacteriota_50_test_concat
```
  
  Runtime: 1275.24 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_50_1+I+G4 | -5324619.523 | 10682651.024 |
| p__Acidobacteriota_50_1+F+I+G4 | -5327860.646 | 10689301.170 |
| Q.YEAST+F+I+G4 | -5343736.797 | 10721053.472 |
| Q.INSECT+F+I+G4 | -5344547.414 | 10722674.706 |
| LG+F+I+G4 | -5346098.072 | 10725776.022 |
| Q.PFAM+F+I+G4 | -5350362.062 | 10734304.002 |
| Q.PFAM+I+G4 | -5354593.768 | 10742599.514 |
| Q.PFAM+G4 | -5360615.051 | 10754633.243 |
| LG+I+G4 | -5362638.364 | 10758688.706 |
| Q.INSECT+I+G4 | -5365817.321 | 10765046.620 |
| Q.YEAST+I+G4 | -5379921.609 | 10793255.196 |
| Q.PFAM+I | -5870275.648 | 11773954.437 |
| Q.PFAM | -5928572.334 | 11890538.973 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile -l 5 -u 50 -o ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 71   
Number of taxa after pruning: 1816   
Pruned node IDs (degree): 1882 (5) 152 (47) 1886 (5) 1356 (35) 1860 (23) 5 (48) 200 (23) 1346 (9) 1391 (12) 1672 (16) 1143 (15) 1822 (39) 1158 (8) 57 (37) 1093 (47) 1328 (19) 1405 (42) 1446 (48) 1568 (17) 1690 (13) 94 (22) 115 (35) 226 (7) 981 (15) 1088 (6) 1778 (45) 1084 (5) 1268 (24) 1291 (38) 1496 (47) 1542 (24) 1647 (22) 1704 (28) 1731 (48) 235 (21) 961 (21) 524 (6) 1588 (9) 334 (12) 677 (10) 799 (44) 1003 (29) 1244 (23) 1598 (50) 258 (6) 513 (5) 690 (16) 1034 (50) 1173 (11) 264 (40) 303 (31) 509 (5) 847 (18) 1185 (31) 1215 (30) 535 (23) 710 (23) 931 (31) 413 (26) 733 (30) 762 (36) 352 (36) 387 (27) 440 (38) 477 (30) 919 (12) 868 (44) 911 (9) 636 (34) 563 (27) 589 (48)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 71 subtree files and 100 loci files. Total number of potential alignments: 7100.  
Sub-sampling 1000 alignments from 7100 alignments.  
Remaining 1000 alignments. Deleted 14 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Acidobacteriota_50_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_50/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/subtree_update/p__Acidobacteriota_50
```
  
  Runtime: 2676.44 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_50.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_50_1  

| Model | Count |
|-------|-------|
| 840 | p__Acidobacteriota_50_1 |
| 80 | LG |
| 38 | Q.INSECT |
| 26 | Q.PFAM |
| 16 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/subtree_update/p__Acidobacteriota_50.best_scheme.nex -te ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/subtree_update/p__Acidobacteriota_50.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_50_1 -mdef ../Result_rona/formal_test/p__Acidobacteriota_50/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/model_update/p__Acidobacteriota_50
```
  
  Runtime: 6278.60 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_50.iqtree)  
BIC of the new model: 9701212.374  
Likelihood of the new model: -4577933.7987  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_50_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_50_2  
![Model bubble plot](loop_2/p__Acidobacteriota_50_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/tree_update/fasttree.log -intree ../Result_rona/formal_test/p__Acidobacteriota_50/ref_tree.tre ../Result_rona/formal_test/p__Acidobacteriota_50/loci/concat_training_loci.faa > ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile
```
  
  Runtime: 7447.95 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_50/loop_2', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_50/loop_1/tree_update/p__Acidobacteriota_50_1.treefile', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_50/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0026  
Tree 1 branch length: 300.989570228  
Tree 2 branch length: 300.422835567  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998161591786322  
Euclidean distance: 0.10306989182049899  
Time usage for Loop_2: 16465.47 seconds (4.57 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/formal_test/p__Acidobacteriota_50/final_test', params = list(tree1_path = '../Result_rona/formal_test/p__Acidobacteriota_50/ref_tree.tre', tree2_path = '../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile', root = FALSE, summary_path = '../Result_rona/formal_test/p__Acidobacteriota_50/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 642  
Normalized RF distance: 0.17  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 300.422835567  
### Model comparison  
Comparison between initial best model (Q.PFAM) and final model (p__Acidobacteriota_50_2):  
Pearson's correlation: 0.981248647324164  
Euclidean distance: 1.0338215825499728  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile -l 5 -u 50 -o ../Result_rona/formal_test/p__Acidobacteriota_50/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 70   
Number of taxa after pruning: 1817   
Pruned node IDs (degree): 1882 (5) 152 (47) 1886 (5) 1356 (35) 1860 (23) 5 (48) 200 (23) 1346 (9) 1391 (12) 1672 (16) 1143 (15) 1822 (39) 1158 (8) 57 (37) 1093 (47) 1328 (19) 1405 (42) 1446 (48) 1568 (17) 1690 (13) 94 (22) 115 (35) 226 (7) 981 (15) 1088 (6) 1778 (45) 1084 (5) 1268 (24) 1291 (38) 1496 (47) 1542 (24) 1637 (32) 1704 (28) 1731 (48) 235 (21) 961 (21) 1588 (50) 524 (6) 334 (12) 677 (10) 799 (44) 1003 (29) 1244 (23) 258 (6) 513 (5) 690 (16) 1034 (50) 1173 (11) 264 (40) 303 (31) 509 (5) 847 (18) 1185 (31) 1215 (30) 535 (23) 710 (23) 931 (31) 413 (26) 733 (30) 762 (36) 352 (36) 387 (27) 440 (38) 477 (30) 919 (12) 868 (44) 911 (9) 636 (34) 563 (27) 589 (48)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/formal_test/p__Acidobacteriota_50/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 70 subtree files and 20 loci files. Total number of potential alignments: 1400.  
Obtained 1357 alignments from all potential alignments.  
Remaining 1357 alignments. Deleted 43 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result_rona/formal_test/p__Acidobacteriota_50/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_50_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_50/trained_models/trained_model.nex -pre ../Result_rona/formal_test/p__Acidobacteriota_50/final_test/p__Acidobacteriota_50_test_partition
```
  
  Runtime: 675.74 seconds
Best models for test data:  
p__Acidobacteriota_50_2  

| Model | Count |
|-------|-------|
| 1142 | p__Acidobacteriota_50_2 |
| 90 | LG |
| 42 | Q.INSECT |
| 34 | MTART |
| 24 | Q.PFAM |
| 20 | Q.YEAST |
| 5 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result_rona/formal_test/p__Acidobacteriota_50/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_50_2 -mdef ../Result_rona/formal_test/p__Acidobacteriota_50/trained_models/trained_model.nex -te ../Result_rona/formal_test/p__Acidobacteriota_50/loop_2/tree_update/p__Acidobacteriota_50_2.treefile -pre ../Result_rona/formal_test/p__Acidobacteriota_50/final_test/p__Acidobacteriota_50_test_concat
```
  
  Runtime: 3025.68 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_50_2+I+G4 | -5324771.478 | 10682954.934 |
| p__Acidobacteriota_50_2+F+I+G4 | -5328072.870 | 10689725.618 |
| Q.YEAST+F+I+G4 | -5343684.122 | 10720948.122 |
| Q.INSECT+F+I+G4 | -5344494.091 | 10722568.060 |
| LG+F+I+G4 | -5346042.555 | 10725664.988 |
| Q.PFAM+F+I+G4 | -5350308.584 | 10734197.046 |
| Q.PFAM+I+G4 | -5354538.623 | 10742489.224 |
| LG+I+G4 | -5362581.442 | 10758574.862 |
| Q.INSECT+I+G4 | -5365771.074 | 10764954.126 |
| LG+G4 | -5368557.193 | 10770517.527 |
| Q.YEAST+I+G4 | -5379882.751 | 10793177.480 |
| MTMET+F+I+G4 | -5505417.771 | 11044415.420 |
| MTART+F+I+G4 | -5618781.498 | 11271142.874 |
| MTMET+I+G4 | -5743527.238 | 11520466.454 |
| MTART+I+G4 | -5854614.937 | 11742641.852 |
| LG+I | -5878032.488 | 11789468.117 |
| LG | -5936540.076 | 11906474.457 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/formal_test/p__Acidobacteriota_50/trained_models/trained_model.nex ../Result_rona/formal_test/p__Acidobacteriota_50/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 41978.40 seconds (11.66 h)  
