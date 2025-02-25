## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 3  
  Convergence threshold: 0.999  
  File prefix: Q.p__Actinomycetota  
  Taxa name: p__Actinomycetota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Actinomycetota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 11735  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Actinomycetota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Actinomycetota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Actinomycetota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Actinomycetota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Actinomycetota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/subtrees -m split
```
  
Original number of taxa: 11735   
Number of pruned subtrees: 110   
Number of taxa after pruning: 11372   
Pruned node IDs (degree): 3015 (250) 10101 (247) 8898 (245) 210 (244) 6072 (244) 2035 (243) 2727 (241) 7843 (235) 917 (233) 3447 (230) 2410 (229) 595 (222) 4394 (218) 9629 (215) 5375 (213) 11288 (213) 5059 (212) 10406 (209) 6414 (209) 7131 (209) 4675 (204) 9142 (204) 6 (200) 4138 (197) 8524 (193) 9437 (192) 1432 (191) 7339 (191) 5755 (189) 10928 (187) 1773 (175) 6704 (159) 3984 (155) 1638 (136) 7569 (126) 3676 (119) 4941 (113) 8716 (109) 6862 (107) 1191 (103) 6970 (100) 11123 (99) 10834 (95) 8288 (88) 11600 (87) 7697 (86) 2283 (83) 5988 (83) 8417 (83) 3794 (82) 3326 (81) 469 (79) 8172 (78) 1355 (75) 8077 (75) 2651 (75) 5682 (74) 10687 (68) 3883 (68) 9369 (66) 9843 (66) 5270 (65) 4613 (63) 11229 (60) 9908 (59) 1293 (59) 4336 (59) 8832 (59) 11500 (59) 858 (58) 7074 (58) 7789 (54) 3264 (54) 9966 (53) 6622 (52) 11686 (50) 6315 (49) 548 (48) 4896 (46) 10773 (44) 5334 (42) 816 (41) 8376 (41) 10347 (39) 3409 (39) 1149 (36) 10053 (35) 8253 (35) 10019 (33) 10638 (33) 2004 (32) 5599 (32) 3954 (29) 5958 (28) 2970 (27) 2385 (26) 1978 (23) 6673 (23) 10616 (22) 8502 (22) 6363 (21) 6394 (20) 5660 (20) 10385 (19) 7551 (19) 4878 (19) 2366 (18) 1961 (16) 5635 (16) 7529 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 110 subtree files and 120 loci files. Total number of potential alignments: 13200.  
Sub-sampling 2000 alignments from 13200 alignments.  
Remaining 2000 alignments. Deleted 24 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/subtree_update/Q.p__Actinomycetota
```
  
  Runtime: 66078.86 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Actinomycetota.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| Q.PFAM | 519 |
| LG | 515 |
| Q.INSECT | 400 |
| Q.PLANT | 314 |
| Q.YEAST | 233 |
| MTMET | 10 |
| MTART | 9 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/subtree_update/Q.p__Actinomycetota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/subtree_update/Q.p__Actinomycetota.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/model_update/Q.p__Actinomycetota
```
  
  Runtime: 123651.07 seconds  
[Model update log](loop_1/model_update/Q.p__Actinomycetota.iqtree)  
BIC of the new model: 47015392.29  
Likelihood of the new model: -20958512.5914  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Actinomycetota_1)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.PLANT,Q.YEAST,Q.p__Actinomycetota_1  
![Model bubble plot](loop_1/Q.p__Actinomycetota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9517423855204069  
Euclidean distance: 0.7432164632995176  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Actinomycetota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Actinomycetota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/tree_update/Q.p__Actinomycetota_1.treefile
```
  
  Runtime: 60397.64 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/tree_update/Q.p__Actinomycetota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/tree_update/Q.p__Actinomycetota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 5202  
Normalized RF distance: 0.2217  
Tree 1 branch length: 745.66234  
Tree 2 branch length: 1009.68918  
Time usage for Loop_1: 291443.92 seconds (80.96 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_1/tree_update/Q.p__Actinomycetota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/subtrees -m split
```
  
Original number of taxa: 11735   
Number of pruned subtrees: 122   
Number of taxa after pruning: 11320   
Pruned node IDs (degree): 4049 (250) 10911 (249) 6495 (249) 679 (247) 1259 (246) 2931 (244) 4650 (243) 1619 (243) 3761 (241) 8577 (241) 2555 (238) 8051 (235) 3231 (233) 4939 (231) 9871 (229) 7 (215) 4377 (213) 11457 (212) 989 (209) 7649 (209) 2307 (200) 7306 (193) 10569 (192) 7041 (192) 5270 (191) 6162 (189) 9201 (182) 5610 (175) 6773 (159) 10415 (155) 328 (149) 9058 (144) 5475 (136) 10784 (128) 5848 (127) 9667 (119) 11292 (113) 6931 (107) 7512 (100) 2837 (95) 8471 (88) 2045 (85) 8973 (85) 5169 (83) 6368 (83) 10140 (82) 9788 (81) 8380 (78) 1874 (77) 3656 (75) 8285 (75) 6089 (74) 7233 (74) 600 (72) 8817 (71) 11181 (68) 221 (66) 11668 (66) 9600 (65) 3498 (61) 476 (59) 3594 (59) 8895 (59) 10275 (58) 1970 (58) 11404 (54) 7997 (54) 534 (53) 4298 (53) 7857 (52) 2223 (50) 9419 (50) 2792 (46) 10226 (46) 10356 (45) 5800 (44) 6452 (44) 286 (43) 3178 (43) 2513 (41) 1504 (40) 925 (39) 11248 (39) 10099 (39) 3463 (36) 2272 (33) 9468 (33) 1569 (33) 4619 (32) 6006 (32) 9500 (32) 7950 (30) 9382 (29) 5975 (28) 2197 (27) 4004 (27) 4914 (26) 9539 (26) 4352 (25) 2135 (25) 6041 (25) 963 (24) 3738 (23) 4594 (23) 11159 (23) 10333 (23) 10762 (23) 7908 (23) 1199 (22) 3560 (21) 6743 (21) 1950 (21) 1548 (20) 6066 (20) 7629 (20) 7931 (19) 4895 (18) 9583 (17) 2183 (15) 3580 (15) 7498 (15) 1603 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 122 subtree files and 120 loci files. Total number of potential alignments: 14640.  
Sub-sampling 2000 alignments from 14640 alignments.  
Remaining 2000 alignments. Deleted 33 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.INSECT,Q.PLANT,Q.YEAST,Q.p__Actinomycetota_1 -mdef ../Result_nova/phylum_models/Q.p__Actinomycetota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/subtree_update/Q.p__Actinomycetota
```
  
  Runtime: 47903.42 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Actinomycetota.iqtree)  
Best models for iteration 2:  
Q.p__Actinomycetota_1  

| Model | Count |
|-------|-------|
| Q.p__Actinomycetota_1 | 1622 |
| Q.PLANT | 102 |
| LG | 97 |
| Q.PFAM | 75 |
| Q.INSECT | 59 |
| Q.YEAST | 45 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/subtree_update/Q.p__Actinomycetota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/subtree_update/Q.p__Actinomycetota.treefile --model-joint GTR20+FO --init-model Q.p__Actinomycetota_1 -mdef ../Result_nova/phylum_models/Q.p__Actinomycetota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/model_update/Q.p__Actinomycetota
```

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Actinomycetota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Actinomycetota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Actinomycetota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Actinomycetota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Actinomycetota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 34190.21 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Actinomycetota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Actinomycetota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Actinomycetota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 5212  
Normalized RF distance: 0.2221  
Tree 1 branch length: 745.66234  
Tree 2 branch length: 1011.87092  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Actinomycetota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Actinomycetota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  

### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T 20 -s ../Result_nova/phylum_models/Q.p__Actinomycetota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Actinomycetota_1,Q.p__Actinomycetota_2 -mdef ../Result_nova/phylum_models/Q.p__Actinomycetota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Actinomycetota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Actinomycetota/final_test/logfiles/reftree_best_concat_model
```
  
