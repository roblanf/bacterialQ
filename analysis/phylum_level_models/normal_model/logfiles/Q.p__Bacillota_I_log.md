## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_I  
  Taxa name: p__Bacillota_I  
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
Discarded 3 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/select_id.txt. Sampling sequences for 117 loci.  
Number of input species: 2899  
Remaining 117 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_I  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_I -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Fusobacteriota as the outgroup for Phylum Bacillota_I
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/subtrees -m split
```
  
Original number of taxa: 2899   
Number of pruned subtrees: 28   
Number of taxa after pruning: 2798   
Pruned node IDs (degree): 2159 (234) 922 (221) 1690 (217) 104 (190) 2587 (177) 510 (177) 1388 (157) 1267 (122) 5 (100) 831 (91) 1920 (90) 2397 (89) 2499 (89) 423 (88) 2079 (81) 1552 (78) 2824 (76) 293 (75) 1201 (66) 762 (66) 2763 (60) 1142 (55) 371 (48) 1647 (44) 2049 (30) 2019 (29) 736 (25) 714 (23)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 28 subtree files and 117 loci files. Total number of potential alignments: 3276.  
Sub-sampling 2000 alignments from 3276 alignments.  
Remaining 2000 alignments. Deleted 90 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/subtree_update/Q.p__Bacillota_I
```
  
  Runtime: 138672.29 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_I.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 1088 |
| LG | 509 |
| Q.PFAM | 211 |
| Q.INSECT | 182 |
| Q.PLANT | 5 |
| MTART | 4 |
| MTMET | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/subtree_update/Q.p__Bacillota_I.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/subtree_update/Q.p__Bacillota_I.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/model_update/Q.p__Bacillota_I
```
  
  Runtime: 312064.63 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_I.iqtree)  
BIC of the new model: 74192437.0232  
Likelihood of the new model: -34807035.9398  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_I_1)  
Model set for next iteration: Q.YEAST,LG,Q.PFAM,Q.INSECT,Q.p__Bacillota_I_1  
![Model bubble plot](loop_1/Q.p__Bacillota_I_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9714248218721069  
Euclidean distance: 0.5041590421972985  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/tree_update/Q.p__Bacillota_I_1.treefile
```
  
  Runtime: 17466.54 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/tree_update/Q.p__Bacillota_I_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/tree_update/Q.p__Bacillota_I_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 868  
Normalized RF distance: 0.1498  
Tree 1 branch length: 393.41662  
Tree 2 branch length: 573.58778  
Time usage for Loop_1: 470631.18 seconds (130.73 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/tree_update/Q.p__Bacillota_I_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/subtrees -m split
```
  
Original number of taxa: 2899   
Number of pruned subtrees: 28   
Number of taxa after pruning: 2837   
Pruned node IDs (degree): 2622 (248) 954 (235) 486 (233) 78 (190) 1323 (179) 2184 (177) 1912 (157) 1791 (122) 267 (104) 2531 (91) 1223 (89) 1501 (89) 728 (88) 2097 (88) 874 (81) 1648 (76) 7 (71) 2390 (71) 1725 (66) 2462 (66) 375 (63) 1589 (60) 440 (47) 2360 (31) 1188 (30) 843 (29) 815 (28) 2869 (28)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 28 subtree files and 117 loci files. Total number of potential alignments: 3276.  
Sub-sampling 2000 alignments from 3276 alignments.  
Remaining 2000 alignments. Deleted 86 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.PFAM,Q.INSECT,Q.p__Bacillota_I_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/subtree_update/Q.p__Bacillota_I
```
  
  Runtime: 69864.69 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_I.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_I_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_I_1 | 1581 |
| LG | 150 |
| Q.YEAST | 142 |
| Q.INSECT | 93 |
| Q.PFAM | 34 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/subtree_update/Q.p__Bacillota_I.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/subtree_update/Q.p__Bacillota_I.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_I_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/model_update/Q.p__Bacillota_I
```
  
  Runtime: 253035.79 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_I.iqtree)  
BIC of the new model: 73820540.1493  
Likelihood of the new model: -34639274.6291  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_I_2)  
Model set for next iteration: LG,Q.YEAST,Q.INSECT,Q.p__Bacillota_I_2  
![Model bubble plot](loop_2/Q.p__Bacillota_I_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998345951332516  
Euclidean distance: 0.03868266092702621  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/tree_update/Q.p__Bacillota_I_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 15850.33 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 868  
Normalized RF distance: 0.1498  
Tree 1 branch length: 393.41662  
Tree 2 branch length: 574.88765  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_I_1,Q.p__Bacillota_I_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 353838.18 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bacillota_I_1+I+R9 | -57327909.570 | 114717325.428 |
| Q.p__Bacillota_I_2+I+R9 | -57331014.650 | 114723535.588 |
| Q.p__Bacillota_I_1+F+I+R9 | -57623145.130 | 115307997.618 |
| Q.p__Bacillota_I_2+F+I+R9 | -57628332.260 | 115318371.878 |
| Q.PFAM+F+I+R9 | -57670090.690 | 115401888.738 |
| LG+F+I+R9 | -57677723.990 | 115417155.338 |
| Q.YEAST+I+R9 | -57744546.750 | 115550599.788 |
| Q.YEAST+F+I+R9 | -57795809.680 | 115653326.718 |
| WAG+F+I+R9 | -57846356.810 | 115754420.978 |
| Q.INSECT+I+R9 | -57954063.330 | 115969632.948 |
| Q.INSECT+F+I+R9 | -57959910.210 | 115981527.778 |
| LG+I+R9 | -57997044.050 | 116055594.388 |
| LG+R9 | -58002558.770 | 116066613.245 |
| LG+I+R8 | -58023230.060 | 116107945.242 |
| LG+R8 | -58030177.790 | 116121830.120 |
| LG+I+R7 | -58061569.980 | 116184603.917 |
| Q.PFAM+I+R9 | -58063314.600 | 116188135.488 |
| LG+R7 | -58071477.200 | 116204407.774 |
| LG+I+R6 | -58121844.820 | 116305132.432 |
| LG+R6 | -58135685.020 | 116332802.249 |
| WAG+I+R9 | -58171914.030 | 116405334.348 |
| PMB+F+I+R9 | -58197083.450 | 116455874.258 |
| JTT+F+I+R9 | -58316955.950 | 116695619.258 |
| CPREV+F+I+R9 | -58376656.160 | 116815019.678 |
| LG+I+G4 | -58412598.840 | 116886545.228 |
| CPREV+I+R9 | -58415631.230 | 116892768.748 |
| LG+G4 | -58455985.330 | 116973307.625 |
| DCMUT+F+I+R9 | -58573356.680 | 117208420.718 |
| MTINV+F+I+R9 | -58587570.100 | 117236847.558 |
| PMB+I+R9 | -58646488.750 | 117354483.788 |
| JTT+I+R9 | -58717904.630 | 117497315.548 |
| Q.PLANT+F+I+R9 | -58759652.380 | 117581012.118 |
| DCMUT+I+R9 | -58935045.680 | 117931597.648 |
| Q.PLANT+I+R9 | -58973431.650 | 118008369.588 |
| MTMET+F+I+R9 | -59170051.540 | 118401810.438 |
| Q.MAMMAL+F+I+R9 | -59278051.140 | 118617809.638 |
| Q.MAMMAL+I+R9 | -59759659.550 | 119580825.388 |
| Q.BIRD+F+I+R9 | -59967356.850 | 119996421.058 |
| MTINV+I+R9 | -60325080.500 | 120711667.288 |
| Q.BIRD+I+R9 | -60403662.820 | 120868831.928 |
| MTMET+I+R9 | -60462344.700 | 120986195.688 |
| MTVER+F+I+R9 | -60507746.550 | 121077200.458 |
| MTVER+I+R9 | -61596552.100 | 123254610.488 |
| LG+I | -63419409.550 | 126900156.065 |
| LG | -63760939.730 | 127583205.843 |
The inferred model Q.p__Bacillota_I_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bacillota_I_1+I+R9 | LG+F+I+R9 |
| BIC | 114717325.428 | 115417155.338 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loop_1/tree_update/Q.p__Bacillota_I_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 17758.28 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_I/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 108  
Normalized RF distance: 0.0186  
Tree 1 branch length: 530.18377  
Tree 2 branch length: 574.88765  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -57454426.932 | -58123600.179 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bacillota_I_2):  
Pearson's correlation: 0.9446776238054029  
Euclidean distance: 0.7059363698222278  
![Initial best model bubble plot](final_test/best_existing_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Pairwise tree distance comparison  
![Heatmap of RF distance of trees:](estimated_tree/RF_heatmap.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_heatmap.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 1183639.03 seconds (328.79 h)  
