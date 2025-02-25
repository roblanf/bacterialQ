## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Desulfobacterota  
  Taxa name: p__Desulfobacterota  
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
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 2228  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Desulfobacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Desulfobacterota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Desulfobacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 2228   
Number of pruned subtrees: 17   
Number of taxa after pruning: 2173   
Pruned node IDs (degree): 1806 (235) 497 (225) 1266 (213) 896 (194) 2040 (171) 1602 (160) 276 (157) 129 (148) 1148 (119) 1487 (115) 724 (93) 38 (81) 818 (79) 432 (65) 1093 (54) 2 (35) 1769 (29)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 17 subtree files and 120 loci files. Total number of potential alignments: 2040.  
Sub-sampling 2000 alignments from 2040 alignments.  
Remaining 2000 alignments. Deleted 18 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/subtree_update/Q.p__Desulfobacterota
```
  
  Runtime: 141411.63 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Desulfobacterota.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 636 |
| Q.INSECT | 553 |
| LG | 336 |
| Q.PFAM | 312 |
| Q.YEAST | 159 |
| MTART | 4 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/subtree_update/Q.p__Desulfobacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/subtree_update/Q.p__Desulfobacterota.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/model_update/Q.p__Desulfobacterota
```
  
  Runtime: 489772.27 seconds  
[Model update log](loop_1/model_update/Q.p__Desulfobacterota.iqtree)  
BIC of the new model: 89498834.8939  
Likelihood of the new model: -41810264.4  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Desulfobacterota_1)  
Model set for next iteration: Q.PLANT,Q.INSECT,LG,Q.PFAM,Q.YEAST,Q.p__Desulfobacterota_1  
![Model bubble plot](loop_1/Q.p__Desulfobacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9656451794264004  
Euclidean distance: 0.5384639916917289  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/tree_update/Q.p__Desulfobacterota_1.treefile
```
  
  Runtime: 13601.79 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/tree_update/Q.p__Desulfobacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/tree_update/Q.p__Desulfobacterota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 678  
Normalized RF distance: 0.1523  
Tree 1 branch length: 279.8594  
Tree 2 branch length: 377.71723  
Time usage for Loop_1: 646823.55 seconds (179.67 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/tree_update/Q.p__Desulfobacterota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 2228   
Number of pruned subtrees: 18   
Number of taxa after pruning: 2171   
Pruned node IDs (degree): 59 (221) 544 (201) 1308 (194) 2049 (180) 744 (176) 960 (170) 1823 (157) 1676 (148) 279 (111) 403 (107) 1136 (93) 1591 (81) 1230 (79) 1510 (72) 1985 (65) 4 (54) 919 (33) 510 (29)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 18 subtree files and 120 loci files. Total number of potential alignments: 2160.  
Sub-sampling 2000 alignments from 2160 alignments.  
Remaining 2000 alignments. Deleted 17 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/training_loci -m MFP -mset Q.PLANT,Q.INSECT,LG,Q.PFAM,Q.YEAST,Q.p__Desulfobacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/subtree_update/Q.p__Desulfobacterota
```
  
  Runtime: 96390.83 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Desulfobacterota.iqtree)  
Best models for iteration 2:  
Q.p__Desulfobacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Desulfobacterota_1 | 1537 |
| Q.PLANT | 217 |
| Q.INSECT | 98 |
| LG | 72 |
| Q.PFAM | 52 |
| Q.YEAST | 24 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/subtree_update/Q.p__Desulfobacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/subtree_update/Q.p__Desulfobacterota.treefile --model-joint GTR20+FO --init-model Q.p__Desulfobacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/model_update/Q.p__Desulfobacterota
```
  
  Runtime: 230124.60 seconds  
[Model update log](loop_2/model_update/Q.p__Desulfobacterota.iqtree)  
BIC of the new model: 84532250.2571  
Likelihood of the new model: -39495853.9757  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Desulfobacterota_2)  
Model set for next iteration: Q.PLANT,Q.INSECT,LG,Q.PFAM,Q.p__Desulfobacterota_2  
![Model bubble plot](loop_2/Q.p__Desulfobacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999420727470675  
Euclidean distance: 0.022576109257791847  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/tree_update/Q.p__Desulfobacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 11859.01 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 674  
Normalized RF distance: 0.1514  
Tree 1 branch length: 279.8594  
Tree 2 branch length: 378.13672  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Desulfobacterota_1,Q.p__Desulfobacterota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 546590.04 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Desulfobacterota_1+I+R9 | -43615252.370 | 87277976.837 |
| Q.p__Desulfobacterota_2+I+R9 | -43617132.750 | 87281737.597 |
| Q.p__Desulfobacterota_1+F+I+R9 | -43709381.390 | 87466436.660 |
| Q.p__Desulfobacterota_2+F+I+R9 | -43712673.770 | 87473021.420 |
| LG+F+I+R9 | -43810011.230 | 87667696.340 |
| Q.YEAST+F+I+R9 | -43824838.070 | 87697350.020 |
| Q.PFAM+I+R9 | -43828168.290 | 87703808.677 |
| Q.PFAM+F+I+R9 | -43834699.660 | 87717073.200 |
| LG+I+R9 | -43854830.970 | 87757134.037 |
| Q.INSECT+F+I+R9 | -43855102.700 | 87757879.280 |
| LG+R9 | -43859646.260 | 87766753.997 |
| LG+I+R8 | -43876376.450 | 87800203.757 |
| Q.INSECT+I+R9 | -43876926.210 | 87801324.517 |
| LG+R8 | -43883041.830 | 87813523.897 |
| LG+I+R7 | -43905675.760 | 87858781.136 |
| LG+R7 | -43914759.060 | 87876937.116 |
| LG+I+R6 | -43957175.620 | 87961759.616 |
| Q.YEAST+I+R9 | -43959253.410 | 87965978.917 |
| LG+R6 | -43968875.050 | 87985147.856 |
| JTT+F+I+R9 | -44035625.420 | 88118924.720 |
| Q.PLANT+I+R9 | -44040048.260 | 88127568.617 |
| JTT+I+R9 | -44053114.430 | 88153700.957 |
| WAG+F+I+R9 | -44055369.330 | 88158412.540 |
| Q.PLANT+F+I+R9 | -44058764.230 | 88165202.340 |
| WAG+I+R9 | -44097314.150 | 88242100.397 |
| LG+I+G4 | -44202461.690 | 88452236.175 |
| LG+G4 | -44247595.600 | 88542493.375 |
| CPREV+I+R9 | -44410144.080 | 88867760.257 |
| CPREV+F+I+R9 | -44420051.310 | 88887776.500 |
| DCMUT+F+I+R9 | -44468943.870 | 88985561.620 |
| Q.MAMMAL+I+R9 | -44474994.510 | 88997461.117 |
| Q.MAMMAL+F+I+R9 | -44526438.150 | 89100550.180 |
| MTINV+F+I+R9 | -44546439.410 | 89140552.700 |
| DCMUT+I+R9 | -44591828.200 | 89231128.497 |
| PMB+F+I+R9 | -44696222.700 | 89440119.280 |
| PMB+I+R9 | -44722351.340 | 89492174.777 |
| Q.BIRD+I+R9 | -44828614.940 | 89704701.977 |
| MTMET+F+I+R9 | -44848053.720 | 89743781.320 |
| Q.BIRD+F+I+R9 | -44880620.140 | 89808914.160 |
| MTVER+F+I+R9 | -45564825.600 | 91177325.080 |
| MTMET+I+R9 | -46637156.040 | 93321784.177 |
| MTINV+I+R9 | -46780137.680 | 93607747.457 |
| MTVER+I+R9 | -47072228.240 | 94191928.577 |
| LG+I | -48567815.960 | 97182934.095 |
| LG | -49013272.380 | 98073836.314 |
The inferred model Q.p__Desulfobacterota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Desulfobacterota_1+I+R9 | LG+F+I+R9 |
| BIC | 87277976.837 | 87667696.34 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loop_1/tree_update/Q.p__Desulfobacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 13255.97 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 98  
Normalized RF distance: 0.022  
Tree 1 branch length: 358.67618  
Tree 2 branch length: 378.13672  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -43659701.148 | -43894295.902 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Desulfobacterota_2):  
Pearson's correlation: 0.971965439740559  
Euclidean distance: 0.5294114052644101  
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
Total time usage: 1546277.05 seconds (429.52 h)  
