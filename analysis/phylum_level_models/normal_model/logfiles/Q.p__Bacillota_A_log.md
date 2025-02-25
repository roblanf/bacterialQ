## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_A  
  Taxa name: p__Bacillota_A  
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
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 14788  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_A  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_A -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota_A
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/ref_tree.tre -l 30 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/subtrees -m split
```
  
Original number of taxa: 14788   
Number of pruned subtrees: 112   
Number of taxa after pruning: 13922   
Pruned node IDs (degree): 3752 (248) 5333 (248) 6035 (246) 10121 (246) 1984 (238) 6464 (235) 2229 (231) 13062 (231) 8761 (231) 1257 (230) 7274 (229) 6782 (229) 9326 (227) 7864 (226) 8221 (223) 140 (221) 12494 (219) 11550 (219) 3268 (210) 10513 (209) 14200 (206) 868 (206) 13783 (205) 4792 (205) 2961 (204) 5581 (203) 8569 (191) 10941 (186) 7010 (165) 1610 (164) 3487 (163) 4252 (163) 7516 (162) 9143 (162) 706 (161) 9706 (161) 4474 (161) 9955 (154) 4634 (154) 11359 (149) 13368 (146) 14458 (145) 14602 (144) 2682 (141) 2542 (140) 11992 (137) 2822 (137) 5785 (136) 12360 (134) 8089 (133) 1073 (130) 4126 (127) 7740 (125) 11238 (122) 1836 (116) 525 (115) 5921 (115) 5179 (115) 12712 (115) 5062 (100) 11827 (100) 1512 (99) 8444 (99) 10843 (99) 12842 (98) 13687 (97) 3649 (97) 9614 (93) 9867 (88) 12203 (87) 6351 (87) 12979 (84) 6698 (83) 9059 (79) 14056 (78) 10437 (77) 13294 (73) 8991 (69) 12291 (68) 14134 (67) 3164 (66) 641 (62) 10723 (61) 12141 (59) 4996 (59) 11181 (57) 7174 (56) 412 (56) 11768 (56) 13514 (55) 1773 (53) 360 (53) 2460 (49) 1202 (49) 11126 (48) 4007 (46) 42 (45) 4415 (45) 95 (42) 7234 (41) 4085 (40) 5294 (40) 13624 (39) 9552 (39) 4 (38) 467 (38) 13584 (38) 3229 (38) 13989 (38) 11926 (37) 10810 (32) 4052 (31)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 112 subtree files and 120 loci files. Total number of potential alignments: 13440.  
Sub-sampling 2000 alignments from 13440 alignments.  
Remaining 2000 alignments. Deleted 18 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/subtree_update/Q.p__Bacillota_A
```
  
  Runtime: 141516.81 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_A.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 589 |
| Q.YEAST | 541 |
| Q.INSECT | 488 |
| Q.PFAM | 257 |
| Q.PLANT | 123 |
| MTART | 1 |
| MTMET | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/subtree_update/Q.p__Bacillota_A.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/subtree_update/Q.p__Bacillota_A.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/model_update/Q.p__Bacillota_A
```
  
  Runtime: 300641.00 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_A.iqtree)  
BIC of the new model: 74705427.303  
Likelihood of the new model: -34540658.8806  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_A_1)  
Model set for next iteration: LG,Q.YEAST,Q.INSECT,Q.PFAM,Q.PLANT,Q.p__Bacillota_A_1  
![Model bubble plot](loop_1/Q.p__Bacillota_A_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9782715603759611  
Euclidean distance: 0.4296444099122883  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/tree_update/Q.p__Bacillota_A_1.treefile
```
  
  Runtime: 102635.88 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/tree_update/Q.p__Bacillota_A_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/tree_update/Q.p__Bacillota_A_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 4136  
Normalized RF distance: 0.1399  
Tree 1 branch length: 1407.7998  
Tree 2 branch length: 1986.6405  
Time usage for Loop_1: 618922.36 seconds (171.92 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/tree_update/Q.p__Bacillota_A_1.treefile -l 30 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/subtrees -m split
```
  
Original number of taxa: 14788   
Number of pruned subtrees: 113   
Number of taxa after pruning: 13903   
Pruned node IDs (degree): 5290 (248) 6855 (248) 11548 (247) 7370 (246) 10836 (246) 2917 (245) 9132 (242) 6008 (236) 8087 (235) 3673 (231) 1623 (231) 8861 (231) 14395 (231) 9887 (231) 8405 (229) 13668 (228) 9632 (223) 6268 (223) 12040 (219) 4806 (210) 6490 (210) 12517 (209) 935 (206) 2210 (205) 583 (205) 5666 (205) 3978 (204) 2677 (203) 4602 (203) 12876 (184) 10271 (174) 3267 (164) 5117 (163) 10648 (162) 1918 (161) 11211 (161) 8646 (158) 11373 (155) 1200 (151) 13392 (149) 131 (146) 7830 (143) 4324 (142) 4183 (141) 4465 (137) 7120 (136) 1350 (135) 9500 (133) 2080 (131) 13895 (131) 2551 (127) 11830 (127) 13271 (122) 1507 (116) 3493 (116) 7256 (115) 14025 (115) 6701 (115) 13560 (109) 13059 (101) 12332 (100) 3169 (99) 5020 (98) 487 (97) 11119 (93) 10460 (89) 14206 (87) 10562 (85) 14706 (83) 8321 (83) 5929 (79) 10185 (79) 14625 (76) 57 (73) 10117 (69) 14139 (68) 869 (67) 3913 (66) 9373 (64) 1854 (61) 7757 (59) 5870 (59) 13214 (57) 14322 (56) 12258 (56) 277 (55) 3430 (53) 12759 (52) 820 (49) 2414 (49) 7974 (48) 13159 (48) 5545 (46) 8819 (43) 2470 (42) 12476 (42) 8022 (40) 5625 (40) 6816 (40) 385 (39) 424 (39) 11081 (39) 7677 (38) 347 (38) 7618 (38) 2513 (37) 12431 (37) 9436 (37) 12725 (35) 11971 (32) 12843 (32) 3642 (31) 5590 (31)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 113 subtree files and 120 loci files. Total number of potential alignments: 13560.  
Sub-sampling 2000 alignments from 13560 alignments.  
Remaining 2000 alignments. Deleted 16 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.INSECT,Q.PFAM,Q.PLANT,Q.p__Bacillota_A_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/subtree_update/Q.p__Bacillota_A
```
  
  Runtime: 91718.57 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_A.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_A_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_A_1 | 1609 |
| Q.PFAM | 113 |
| LG | 104 |
| Q.INSECT | 74 |
| Q.YEAST | 61 |
| Q.PLANT | 39 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/subtree_update/Q.p__Bacillota_A.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/subtree_update/Q.p__Bacillota_A.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_A_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/model_update/Q.p__Bacillota_A
```
  
  Runtime: 207674.66 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_A.iqtree)  
BIC of the new model: 73342711.6674  
Likelihood of the new model: -33883058.464  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_A_2)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.YEAST,Q.p__Bacillota_A_2  
![Model bubble plot](loop_2/Q.p__Bacillota_A_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997069513128496  
Euclidean distance: 0.04915166046567824  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loop_1/tree_update/Q.p__Bacillota_A_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 72940.70 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 4174  
Normalized RF distance: 0.1411  
Tree 1 branch length: 1407.7998  
Tree 2 branch length: 1985.82769  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_A_1,Q.p__Bacillota_A_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_A/final_test/logfiles/reftree_best_concat_model
```
  
  Error:
Killed
  
  Exit code: 137  
  Runtime: 92707.28 seconds  
Killed
  
