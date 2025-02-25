## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacteroidota  
  Taxa name: p__Bacteroidota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 30  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 14779  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacteroidota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacteroidota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Zixibacteria as the outgroup for Phylum Bacteroidota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/ref_tree.tre -l 30 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/subtrees -m split
```
  
Original number of taxa: 14779   
Number of pruned subtrees: 109   
Number of taxa after pruning: 13728   
Pruned node IDs (degree): 7146 (250) 6805 (250) 1457 (248) 12030 (248) 13731 (247) 9037 (246) 11166 (244) 949 (241) 9438 (239) 11491 (237) 4088 (236) 10086 (227) 12281 (226) 12604 (223) 7741 (221) 5540 (221) 2337 (221) 65 (216) 13178 (214) 2672 (212) 7395 (211) 3519 (208) 742 (207) 8335 (207) 10770 (200) 12914 (196) 5296 (194) 10575 (190) 6366 (188) 4973 (186) 3184 (174) 8163 (173) 4554 (172) 14237 (163) 6206 (161) 9780 (158) 1302 (156) 428 (154) 13467 (154) 3032 (152) 1883 (145) 13992 (144) 8717 (142) 9946 (140) 4836 (138) 7606 (136) 14645 (134) 280 (132) 10450 (126) 582 (125) 3398 (122) 14528 (118) 8024 (117) 3819 (117) 6553 (116) 5181 (116) 8541 (115) 2883 (114) 10969 (113) 14137 (101) 1726 (100) 3937 (100) 8876 (99) 4460 (95) 4323 (90) 11860 (84) 9304 (84) 13621 (83) 5815 (80) 14399 (80) 2028 (80) 2108 (78) 2260 (78) 11727 (78) 10345 (72) 3747 (71) 6066 (70) 13110 (69) 12829 (67) 1233 (67) 4769 (64) 8655 (63) 7961 (62) 2610 (61) 6 (60) 8982 (56) 11093 (55) 7092 (52) 12506 (52) 11957 (52) 6014 (51) 12557 (47) 4413 (45) 4044 (45) 5760 (44) 2564 (44) 4726 (44) 6162 (43) 5895 (42) 3359 (39) 11437 (38) 1199 (35) 6671 (35) 2222 (35) 10312 (33) 1850 (32) 9676 (32) 13435 (30) 5984 (30)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 109 subtree files and 120 loci files. Total number of potential alignments: 13080.  
Sub-sampling 2000 alignments from 13080 alignments.  
Remaining 2000 alignments. Deleted 5 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/subtree_update/Q.p__Bacteroidota
```
  
  Runtime: 108081.51 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacteroidota.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| Q.INSECT | 799 |
| Q.YEAST | 646 |
| LG | 266 |
| Q.PFAM | 153 |
| Q.PLANT | 132 |
| MTART | 2 |
| MTMET | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/subtree_update/Q.p__Bacteroidota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/subtree_update/Q.p__Bacteroidota.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/model_update/Q.p__Bacteroidota
```
  
  Runtime: 351927.49 seconds  
[Model update log](loop_1/model_update/Q.p__Bacteroidota.iqtree)  
BIC of the new model: 67933354.1857  
Likelihood of the new model: -30969730.6554  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacteroidota_1)  
Model set for next iteration: Q.INSECT,Q.YEAST,LG,Q.PFAM,Q.PLANT,Q.p__Bacteroidota_1  
![Model bubble plot](loop_1/Q.p__Bacteroidota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9856981077739387  
Euclidean distance: 0.3586113628373585  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/tree_update/Q.p__Bacteroidota_1.treefile
```
  
  Runtime: 108298.14 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/tree_update/Q.p__Bacteroidota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/tree_update/Q.p__Bacteroidota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 4678  
Normalized RF distance: 0.1583  
Tree 1 branch length: 1192.86416  
Tree 2 branch length: 1691.55156  
Time usage for Loop_1: 649682.05 seconds (180.47 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/tree_update/Q.p__Bacteroidota_1.treefile -l 30 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/subtrees -m split
```
  
Original number of taxa: 14779   
Number of pruned subtrees: 111   
Number of taxa after pruning: 13719   
Pruned node IDs (degree): 4422 (250) 12988 (248) 9787 (246) 10088 (244) 3797 (243) 14152 (241) 3212 (240) 13517 (239) 11713 (239) 12375 (238) 9222 (237) 6851 (236) 12733 (226) 8114 (225) 730 (223) 8408 (221) 8855 (221) 4946 (221) 235 (216) 1109 (214) 1885 (212) 5940 (208) 13945 (207) 1322 (203) 10531 (203) 11178 (200) 9458 (190) 10917 (190) 13755 (188) 7464 (186) 7884 (186) 5605 (174) 10359 (173) 3 (172) 2825 (172) 6631 (172) 2657 (169) 6148 (166) 5274 (164) 2291 (163) 5437 (162) 1594 (154) 2996 (154) 2453 (144) 4144 (140) 7327 (138) 14646 (134) 450 (132) 10792 (126) 582 (125) 7761 (124) 9075 (122) 5819 (122) 14527 (120) 6410 (117) 7649 (106) 4039 (106) 2191 (101) 9655 (99) 11377 (98) 13285 (97) 6537 (95) 12002 (89) 12639 (84) 1748 (83) 2109 (82) 957 (79) 4710 (78) 4869 (78) 12298 (78) 8683 (77) 6333 (71) 3681 (70) 14436 (67) 7260 (64) 3150 (63) 11607 (63) 8775 (62) 1048 (62) 5212 (61) 176 (60) 13406 (59) 10032 (56) 11501 (55) 13235 (51) 3458 (49) 1837 (49) 3631 (49) 12147 (49) 7129 (47) 8338 (45) 6803 (45) 8628 (44) 5166 (44) 7217 (44) 3753 (43) 7175 (43) 3509 (42) 13466 (41) 11115 (39) 5780 (39) 12228 (38) 14402 (35) 4834 (35) 4286 (35) 10735 (33) 11561 (33) 7086 (32) 11951 (32) 1540 (30) 3600 (30)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 111 subtree files and 120 loci files. Total number of potential alignments: 13320.  
Sub-sampling 2000 alignments from 13320 alignments.  
Remaining 2000 alignments. Deleted 9 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/training_loci -m MFP -mset Q.INSECT,Q.YEAST,LG,Q.PFAM,Q.PLANT,Q.p__Bacteroidota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/subtree_update/Q.p__Bacteroidota
```
  
  Runtime: 86845.61 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacteroidota.iqtree)  
Best models for iteration 2:  
Q.p__Bacteroidota_1  

| Model | Count |
|-------|-------|
| Q.p__Bacteroidota_1 | 1622 |
| LG | 91 |
| Q.PFAM | 85 |
| Q.PLANT | 68 |
| Q.YEAST | 68 |
| Q.INSECT | 66 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/subtree_update/Q.p__Bacteroidota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/subtree_update/Q.p__Bacteroidota.treefile --model-joint GTR20+FO --init-model Q.p__Bacteroidota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/model_update/Q.p__Bacteroidota
```
  
  Runtime: 189458.57 seconds  
[Model update log](loop_2/model_update/Q.p__Bacteroidota.iqtree)  
BIC of the new model: 65797879.1882  
Likelihood of the new model: -30020230.1176  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacteroidota_2)  
Model set for next iteration: LG,Q.PFAM,Q.PLANT,Q.YEAST,Q.INSECT,Q.p__Bacteroidota_2  
![Model bubble plot](loop_2/Q.p__Bacteroidota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998742597705247  
Euclidean distance: 0.03534309992191385  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loop_1/tree_update/Q.p__Bacteroidota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 75219.88 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 4736  
Normalized RF distance: 0.1602  
Tree 1 branch length: 1192.86416  
Tree 2 branch length: 1694.1877  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacteroidota_1,Q.p__Bacteroidota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacteroidota/final_test/logfiles/reftree_best_concat_model
```
  
  Error:
Terminated
  
  Exit code: 143  
  Runtime: 1243388.58 seconds  
Terminated
  
