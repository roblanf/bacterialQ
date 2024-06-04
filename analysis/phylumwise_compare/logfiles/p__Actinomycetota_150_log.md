## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Actinomycetota_150  
  Taxa name: p__Actinomycetota  
  Number of training loci: 1000  
  Drop species threshold: 0.5  
  Drop locus threshold: 0.1  
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
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Actinomycetota_150/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 11558  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result/safe_phyla/p__Actinomycetota_150/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 11558  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Actinomycetota_150/ref_tree.tre -l 5 -u 150 -o ../Result/safe_phyla/p__Actinomycetota_150/loop_1/subtrees -m random
```
  
Original number of taxa: 11558   
Number of pruned subtrees: 221   
Number of taxa after pruning: 11394   
Pruned node IDs (degree): 9228 (63) 1318 (74) 1395 (114) 1508 (71) 1580 (6) 9221 (6) 7 (141) 147 (53) 1586 (7) 1866 (12) 1880 (16) 9807 (51) 1257 (58) 1594 (124) 1717 (150) 9749 (59) 9858 (33) 1897 (23) 11510 (49) 1158 (100) 5217 (42) 7564 (83) 8018 (11) 9294 (144) 9437 (40) 9684 (66) 9892 (35) 205 (54) 796 (40) 837 (57) 2553 (7) 5261 (59) 5319 (149) 7652 (51) 9215 (7) 9678 (7) 259 (140) 398 (41) 440 (14) 1151 (8) 3171 (54) 5153 (65) 7937 (75) 9479 (29) 11424 (87) 454 (79) 1116 (36) 1923 (32) 2196 (5) 2564 (72) 7441 (121) 7704 (92) 7795 (143) 9660 (19) 533 (48) 1955 (20) 2201 (82) 3696 (82) 8032 (78) 9509 (64) 9572 (89) 9930 (5) 581 (44) 897 (10) 2283 (18) 5143 (11) 5838 (27) 10220 (19) 11410 (12) 625 (54) 678 (119) 1095 (20) 1976 (6) 2851 (26) 3579 (118) 4938 (7) 5137 (7) 7423 (19) 10184 (37) 1070 (26) 2184 (10) 2302 (26) 2879 (27) 4835 (104) 5130 (8) 8113 (35) 10436 (13) 909 (125) 1033 (38) 2640 (111) 2750 (102) 2906 (7) 3233 (80) 5479 (32) 5867 (82) 8148 (88) 9941 (21) 10450 (22) 1984 (103) 2086 (99) 2913 (10) 4790 (46) 5117 (12) 6240 (21) 8236 (41) 10127 (58) 10244 (14) 10472 (32) 2330 (5) 3315 (39) 3785 (68) 5108 (10) 6192 (49) 6571 (7) 7415 (6) 8277 (83) 9963 (30) 9992 (136) 11403 (5) 2335 (73) 2407 (144) 2924 (14) 4951 (22) 4972 (137) 10426 (10) 2938 (63) 3355 (19) 4772 (19) 5515 (16) 6135 (55) 6549 (23) 6738 (106) 3001 (116) 3116 (56) 3374 (54) 4236 (59) 4487 (23) 4511 (63) 5531 (7) 5953 (15) 6845 (100) 8362 (22) 8685 (7) 10261 (69) 10329 (98) 3428 (18) 3445 (135) 3856 (29) 4296 (135) 4430 (58) 4574 (115) 4688 (85) 6271 (20) 6733 (5) 7401 (15) 8576 (109) 8692 (59) 5969 (34) 6002 (134) 6498 (52) 6585 (149) 8385 (71) 8455 (122) 9210 (6) 5540 (20) 6292 (6) 10510 (9) 3887 (126) 4012 (28) 4230 (6) 6298 (10) 10519 (63) 4041 (14) 6308 (5) 6949 (55) 7370 (32) 9204 (6) 4055 (78) 4132 (99) 5562 (74) 6313 (5) 7196 (16) 7216 (134) 7349 (22) 11393 (6) 5817 (7) 6318 (23) 7005 (56) 7060 (137) 10584 (6) 5637 (12) 8759 (7) 9003 (22) 11382 (12) 6342 (25) 6366 (133) 8766 (9) 9025 (137) 9161 (44) 5807 (10) 8775 (144) 8918 (85) 10592 (8) 10600 (43) 11324 (59) 5654 (150) 5803 (5) 11046 (8) 11054 (60) 10646 (11) 11114 (21) 10949 (98) 11135 (5) 10943 (7) 11314 (11) 11141 (119) 11259 (56) 10660 (95) 10906 (35) 10756 (137) 10892 (15)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Actinomycetota_150/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 221 subtree files and 100 loci files. Total number of potential alignments: 22100.  
Sub-sampling 1000 alignments from 22100 alignments.  
Remaining 1000 alignments. Deleted 9 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Actinomycetota_150/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result/safe_phyla/p__Actinomycetota_150/loop_1/subtree_update/p__Actinomycetota_150
```
  
  Runtime: 21137.05 seconds
[Subtree update log](loop_1/subtree_update/p__Actinomycetota_150.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| 375 | Q.PFAM |
| 359 | LG |
| 169 | Q.INSECT |
| 93 | Q.YEAST |
| 3 | MTMET |
| 1 | MTART |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Actinomycetota_150/loop_1/subtree_update/p__Actinomycetota_150.best_scheme.nex -te ../Result/safe_phyla/p__Actinomycetota_150/loop_1/subtree_update/p__Actinomycetota_150.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre ../Result/safe_phyla/p__Actinomycetota_150/loop_1/model_update/p__Actinomycetota_150
```
  
  Runtime: 54559.91 seconds
[Model update log](loop_1/model_update/p__Actinomycetota_150.iqtree)  
BIC of the new model: 12523487.3726  
Likelihood of the new model: -5634088.7667  
Model does not meet precision requirement.  
[New model](trained_models/p__Actinomycetota_150_1)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Actinomycetota_150_1  
![Model bubble plot](loop_1/p__Actinomycetota_150_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Actinomycetota_150/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Actinomycetota_150/loop_1/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Actinomycetota_150/ref_tree.tre ../Result/safe_phyla/p__Actinomycetota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Actinomycetota_150/loop_1/tree_update/p__Actinomycetota_150_1.treefile
```
  
  Runtime: 105462.67 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Actinomycetota_150/loop_1', params = list(tree1_path = '../Result/safe_phyla/p__Actinomycetota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Actinomycetota_150/loop_1/tree_update/p__Actinomycetota_150_1.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Actinomycetota_150/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 5328  
Normalized RF distance: 0.2305  
Tree 1 branch length: 738.27635  
Tree 2 branch length: 1017.874555884  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9760751411553719  
Euclidean distance: 1.1617209322452624  
Time usage for Loop_1: 195980.71 seconds (54.44 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Actinomycetota_150/loci/concat_testing_loci.faa -m TESTONLY -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Actinomycetota_150_1 -mdef ../Result/safe_phyla/p__Actinomycetota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Actinomycetota_150/loop_1/tree_update/p__Actinomycetota_150_1.treefile -pre ../Result/safe_phyla/p__Actinomycetota_150/loop_1/test_model/p__Actinomycetota_150_test_concat
```
  
  Runtime: 171034.28 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Actinomycetota_150_1+I+G4 | -19903302.720 | 40010868.300 |
| p__Actinomycetota_150_1+F+I+G4 | -19923975.870 | 40052382.500 |
| LG+F+I+G4 | -20001085.430 | 40206601.620 |
| Q.PFAM+F+I+G4 | -20016564.270 | 40237559.300 |
| Q.YEAST+F+I+G4 | -20031630.720 | 40267692.200 |
| Q.INSECT+F+I+G4 | -20061070.900 | 40326572.560 |
| Q.PFAM+I+G4 | -20086417.150 | 40377097.160 |
| Q.PFAM+G4 | -20094502.230 | 40393258.484 |
| LG+I+G4 | -20138255.670 | 40480774.200 |
| Q.INSECT+I+G4 | -20191958.010 | 40588178.880 |
| Q.YEAST+I+G4 | -20225111.190 | 40654485.240 |
| Q.PFAM+I | -22320676.880 | 44845607.784 |
| Q.PFAM | -22399812.940 | 45003871.067 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Actinomycetota_150/loop_1/tree_update/p__Actinomycetota_150_1.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Actinomycetota_150/loop_2/subtrees -m random
```
  
Original number of taxa: 11558   
Number of pruned subtrees: 228   
Number of taxa after pruning: 11380   
Pruned node IDs (degree): 9542 (63) 9606 (35) 9640 (39) 9061 (7) 9353 (6) 9341 (12) 9359 (46) 9404 (139) 2924 (14) 5485 (23) 9015 (42) 9069 (124) 9192 (150) 6140 (7) 11507 (51) 2 (33) 10736 (58) 10798 (141) 10938 (53) 11449 (59) 35 (49) 5401 (83) 5510 (32) 6136 (5) 6325 (35) 7179 (54) 7233 (65) 1675 (27) 1721 (11) 2945 (52) 5542 (20) 6055 (82) 6319 (7) 6362 (52) 10705 (32) 10994 (144) 11137 (40) 11384 (66) 85 (7) 2918 (7) 3231 (75) 5785 (18) 6155 (79) 6233 (87) 7768 (82) 8912 (104) 10052 (17) 11178 (36) 2998 (92) 3089 (143) 3312 (122) 5563 (6) 6029 (27) 6415 (21) 7300 (118) 8906 (7) 9685 (41) 10074 (75) 11366 (19) 93 (72) 1735 (78) 3434 (27) 5569 (8) 6634 (11) 6646 (27) 10471 (54) 11215 (64) 11278 (89) 1661 (15) 6617 (18) 6673 (111) 6783 (102) 6887 (27) 8861 (46) 10153 (40) 10525 (36) 10560 (145) 3818 (6) 5382 (19) 5580 (98) 5677 (104) 5806 (15) 6606 (12) 6914 (7) 7420 (80) 8823 (39) 10047 (5) 10426 (44) 452 (24) 5821 (139) 5959 (69) 6597 (10) 6921 (10) 7855 (68) 9988 (60) 10194 (7) 416 (37) 1647 (12) 1817 (8) 3464 (32) 3826 (82) 6440 (22) 6461 (137) 8801 (23) 9953 (36) 10385 (42) 2893 (26) 3811 (6) 4199 (21) 6932 (14) 7727 (39) 9733 (7) 10202 (118) 10319 (67) 173 (21) 673 (13) 1826 (88) 3909 (44) 6946 (63) 7503 (19) 8306 (59) 9928 (26) 359 (58) 660 (14) 687 (22) 1914 (8) 4192 (8) 5063 (6) 5069 (7) 7009 (116) 7124 (56) 7522 (54) 7926 (29) 8366 (136) 8501 (57) 8786 (16) 9903 (26) 195 (30) 224 (136) 1637 (8) 3499 (25) 5359 (23) 7576 (135) 7710 (18) 8559 (146) 8704 (83) 9742 (125) 9866 (38) 483 (5) 1614 (24) 2862 (32) 3524 (20) 3955 (55) 4964 (100) 7956 (5) 488 (7) 1610 (5) 2830 (33) 4177 (16) 4387 (106) 4950 (15) 5081 (20) 495 (127) 621 (40) 2781 (50) 3547 (74) 4011 (34) 4044 (134) 5308 (52) 7962 (148) 8109 (6) 3621 (13) 5102 (17) 8282 (24) 3634 (7) 4689 (71) 5119 (9) 8117 (109) 8225 (58) 2180 (71) 2251 (7) 4234 (149) 4498 (56) 4553 (137) 4919 (32) 5128 (23) 1929 (131) 2059 (122) 2258 (59) 3642 (10) 4765 (134) 4898 (22) 5152 (11) 5162 (144) 2777 (5) 2729 (49) 3655 (13) 3667 (142) 1601 (5) 1595 (7) 722 (102) 2324 (29) 824 (13) 2590 (137) 837 (8) 2354 (144) 2497 (94) 845 (41) 886 (9) 1591 (5) 1559 (33) 898 (17) 914 (134) 1539 (21) 1049 (127) 1176 (34) 1210 (12) 1222 (19) 1518 (22) 1242 (6) 1251 (9) 1263 (17) 1280 (7) 1287 (5) 1460 (56) 1297 (7) 1304 (131) 1434 (27)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Actinomycetota_150/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 228 subtree files and 100 loci files. Total number of potential alignments: 22800.  
Sub-sampling 1000 alignments from 22800 alignments.  
Remaining 1000 alignments. Deleted 6 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Actinomycetota_150/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,p__Actinomycetota_150_1 -mdef ../Result/safe_phyla/p__Actinomycetota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Actinomycetota_150/loop_2/subtree_update/p__Actinomycetota_150
```
  
  Runtime: 33122.51 seconds
[Subtree update log](loop_2/subtree_update/p__Actinomycetota_150.iqtree)  
Best models for iteration 2:  
p__Actinomycetota_150_1  

| Model | Count |
|-------|-------|
| 834 | p__Actinomycetota_150_1 |
| 76 | LG |
| 49 | Q.PFAM |
| 27 | Q.INSECT |
| 14 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Actinomycetota_150/loop_2/subtree_update/p__Actinomycetota_150.best_scheme.nex -te ../Result/safe_phyla/p__Actinomycetota_150/loop_2/subtree_update/p__Actinomycetota_150.treefile --model-joint GTR20+FO --init-model p__Actinomycetota_150_1 -mdef ../Result/safe_phyla/p__Actinomycetota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Actinomycetota_150/loop_2/model_update/p__Actinomycetota_150
```
  
  Runtime: 48587.27 seconds
[Model update log](loop_2/model_update/p__Actinomycetota_150.iqtree)  
BIC of the new model: 11750462.3607  
Likelihood of the new model: -5281169.109  
Model does not meet precision requirement.  
[New model](trained_models/p__Actinomycetota_150_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Actinomycetota_150_2  
![Model bubble plot](loop_2/p__Actinomycetota_150_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/mnt/data/dayhoff/home/u7457359/project/GTDB/tool/FastTreeMP/FastTreeMP -trans ../Result/safe_phyla/p__Actinomycetota_150/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result/safe_phyla/p__Actinomycetota_150/loop_2/tree_update/fasttree.log -intree ../Result/safe_phyla/p__Actinomycetota_150/ref_tree.tre ../Result/safe_phyla/p__Actinomycetota_150/loci/concat_training_loci.faa > ../Result/safe_phyla/p__Actinomycetota_150/loop_2/tree_update/p__Actinomycetota_150_2.treefile
```
  
  Runtime: 73985.72 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Actinomycetota_150/loop_2', params = list(tree1_path = '../Result/safe_phyla/p__Actinomycetota_150/loop_1/tree_update/p__Actinomycetota_150_1.treefile', tree2_path = '../Result/safe_phyla/p__Actinomycetota_150/loop_2/tree_update/p__Actinomycetota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Actinomycetota_150/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 390  
Normalized RF distance: 0.0169  
Tree 1 branch length: 1017.874555884  
Tree 2 branch length: 1018.973996999  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999528769299649  
Euclidean distance: 0.16476785585931794  
Time usage for Loop_2: 156945.33 seconds (43.60 h)  
Convergence reached at iteration 2  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result/safe_phyla/p__Actinomycetota_150/final_test', params = list(tree1_path = '../Result/safe_phyla/p__Actinomycetota_150/ref_tree.tre', tree2_path = '../Result/safe_phyla/p__Actinomycetota_150/loop_2/tree_update/p__Actinomycetota_150_2.treefile', root = FALSE, summary_path = '../Result/safe_phyla/p__Actinomycetota_150/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 5314  
Normalized RF distance: 0.2299  
Tree 1 branch length: 738.27635  
Tree 2 branch length: 1018.973996999  
### Model comparison  
Comparison between initial best model (Q.PFAM) and final model (p__Actinomycetota_150_2):  
Pearson's correlation: 0.9708074835101832  
Euclidean distance: 1.28445658930121  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Final model testing of test loci in subtrees  
#### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result/safe_phyla/p__Actinomycetota_150/loop_2/tree_update/p__Actinomycetota_150_2.treefile -l 5 -u 150 -o ../Result/safe_phyla/p__Actinomycetota_150/final_test/subtrees -m random
```
  
Original number of taxa: 11558   
Number of pruned subtrees: 224   
Number of taxa after pruning: 11378   
Pruned node IDs (degree): 9192 (150) 4234 (149) 7962 (148) 8559 (146) 10560 (145) 10994 (144) 5146 (144) 2354 (144) 3089 (143) 3667 (142) 1167 (142) 10798 (141) 9404 (139) 5821 (139) 6461 (137) 4553 (137) 2590 (137) 8366 (136) 224 (136) 7576 (135) 4044 (134) 4765 (134) 1343 (134) 904 (134) 1929 (131) 495 (127) 9742 (125) 9069 (124) 3312 (122) 2059 (122) 7300 (118) 10202 (118) 7009 (116) 6673 (111) 8117 (109) 4387 (106) 8912 (104) 5677 (104) 6783 (102) 732 (102) 4964 (100) 5580 (98) 2497 (94) 2998 (92) 11278 (89) 1826 (88) 6233 (87) 5401 (83) 8704 (83) 6055 (82) 7768 (82) 3826 (82) 7420 (80) 6155 (79) 1735 (78) 3231 (75) 10074 (75) 3547 (74) 93 (72) 4689 (71) 2180 (71) 5959 (69) 7855 (68) 10319 (67) 11384 (66) 7233 (65) 11215 (64) 9542 (63) 6946 (63) 9988 (60) 11449 (59) 8306 (59) 2258 (59) 10736 (58) 359 (58) 8225 (58) 8501 (57) 7124 (56) 4498 (56) 1103 (56) 3955 (55) 7179 (54) 10471 (54) 7522 (54) 10938 (53) 2945 (52) 6362 (52) 5308 (52) 11507 (51) 2781 (50) 1556 (50) 35 (49) 2729 (49) 1509 (48) 9359 (46) 8861 (46) 10426 (44) 3909 (44) 9015 (42) 10385 (42) 9685 (41) 11137 (40) 10153 (40) 621 (40) 9640 (39) 8823 (39) 7727 (39) 9866 (38) 416 (37) 11178 (36) 10525 (36) 9953 (36) 9606 (35) 6325 (35) 4011 (34) 1476 (34) 2 (33) 2830 (33) 5510 (32) 10705 (32) 3464 (32) 2862 (32) 4919 (32) 195 (30) 7926 (29) 2324 (29) 857 (29) 1675 (27) 6029 (27) 3434 (27) 6646 (27) 6887 (27) 2893 (26) 9928 (26) 9903 (26) 3499 (25) 452 (24) 1614 (24) 8282 (24) 5485 (23) 8801 (23) 5359 (23) 5112 (23) 1037 (23) 6440 (22) 687 (22) 4898 (22) 6415 (21) 4199 (21) 173 (21) 5542 (20) 3524 (20) 5081 (20) 11366 (19) 5382 (19) 7503 (19) 5785 (18) 6617 (18) 7710 (18) 10052 (17) 5292 (17) 888 (17) 1077 (17) 8786 (16) 4177 (16) 1308 (16) 1661 (15) 5806 (15) 4950 (15) 2924 (14) 6932 (14) 660 (14) 673 (13) 3621 (13) 3655 (13) 834 (13) 9341 (12) 6606 (12) 1647 (12) 1721 (11) 6634 (11) 5136 (11) 6597 (10) 6921 (10) 3642 (10) 1332 (10) 5103 (9) 5569 (8) 1817 (8) 1914 (8) 4192 (8) 1637 (8) 847 (8) 1066 (8) 9061 (7) 6140 (7) 6319 (7) 85 (7) 2918 (7) 8906 (7) 6914 (7) 10194 (7) 9733 (7) 5069 (7) 488 (7) 3634 (7) 2251 (7) 725 (7) 1325 (7) 1160 (7) 9353 (6) 5563 (6) 3818 (6) 3811 (6) 5063 (6) 8109 (6) 6136 (5) 10047 (5) 483 (5) 7956 (5) 1610 (5) 2777 (5) 720 (5) 1059 (5)   
Pruning mode: random   
  
See detailed summary in ../Result/safe_phyla/p__Actinomycetota_150/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 224 subtree files and 20 loci files. Total number of potential alignments: 4480.  
Obtained 4386 alignments from all potential alignments.  
Remaining 4386 alignments. Deleted 94 alignments.  
#### Test model performance  
```bash
iqtree -T 50 -S ../Result/safe_phyla/p__Actinomycetota_150/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Actinomycetota_150_2 -mdef ../Result/safe_phyla/p__Actinomycetota_150/trained_models/trained_model.nex -pre ../Result/safe_phyla/p__Actinomycetota_150/final_test/p__Actinomycetota_150_test_partition
```
  
  Runtime: 6243.78 seconds
Best models for test data:  
p__Actinomycetota_150_2  

| Model | Count |
|-------|-------|
| 3659 | p__Actinomycetota_150_2 |
| 282 | LG |
| 139 | MTART |
| 125 | Q.PFAM |
| 107 | Q.YEAST |
| 63 | Q.INSECT |
| 11 | MTMET |
### Final model testing of concatenated test loci  
```bash
iqtree -T 50 -s ../Result/safe_phyla/p__Actinomycetota_150/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Actinomycetota_150_2 -mdef ../Result/safe_phyla/p__Actinomycetota_150/trained_models/trained_model.nex -te ../Result/safe_phyla/p__Actinomycetota_150/loop_2/tree_update/p__Actinomycetota_150_2.treefile -pre ../Result/safe_phyla/p__Actinomycetota_150/final_test/p__Actinomycetota_150_test_concat
```
  
  Runtime: 66613.21 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Actinomycetota_150_2+I+G4 | -19908622.240 | 40021507.340 |
| p__Actinomycetota_150_2+F+I+G4 | -19928709.230 | 40061849.220 |
| LG+F+I+G4 | -20000807.040 | 40206044.840 |
| Q.PFAM+F+I+G4 | -20016287.340 | 40237005.440 |
| Q.YEAST+F+I+G4 | -20031362.020 | 40267154.800 |
| Q.INSECT+F+I+G4 | -20060818.030 | 40326066.820 |
| Q.PFAM+I+G4 | -20086154.650 | 40376572.160 |
| LG+I+G4 | -20137986.630 | 40480236.120 |
| LG+G4 | -20146057.040 | 40496368.104 |
| Q.INSECT+I+G4 | -20191683.230 | 40587629.320 |
| Q.YEAST+I+G4 | -20224829.210 | 40653921.280 |
| MTMET+F+I+G4 | -20763017.150 | 41730465.060 |
| MTART+F+I+G4 | -21308506.890 | 42821444.540 |
| MTMET+I+G4 | -21723769.240 | 43651801.340 |
| MTART+I+G4 | -22254413.100 | 44713089.060 |
| LG+I | -22372666.280 | 44949586.584 |
| LG | -22451604.930 | 45107455.047 |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex ../Result/safe_phyla/p__Actinomycetota_150/trained_models/trained_model.nex ../Result/safe_phyla/p__Actinomycetota_150/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 606949.17 seconds (168.60 h)  
