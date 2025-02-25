## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Poribacteria  
  Taxa name: p__Poribacteria  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 94  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 6 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Poribacteria/select_id.txt. Sampling sequences for 114 loci.  
Number of input species: 94  
Remaining 114 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Poribacteria  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Poribacteria -d 0.1 -o ../Result_nova/phylum_models/Q.p__Poribacteria/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Zixibacteria as the outgroup for Phylum Poribacteria
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Poribacteria/ref_tree.tre -l 15 -u 94 -o ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/subtrees -m split
```
  
Original number of taxa: 94   
Number of pruned subtrees: 1   
Number of taxa after pruning: 94   
Pruned node IDs (degree): 1 (94)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 114 loci files. Total number of potential alignments: 114.  
Obtained 114 alignments from all potential alignments.  
Remaining 114 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/subtree_update/Q.p__Poribacteria
```
  
  Runtime: 8055.06 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Poribacteria.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 75 |
| Q.PFAM | 14 |
| Q.INSECT | 13 |
| LG | 10 |
| Q.YEAST | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/subtree_update/Q.p__Poribacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/subtree_update/Q.p__Poribacteria.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/model_update/Q.p__Poribacteria
```
  
  Runtime: 14674.87 seconds  
[Model update log](loop_1/model_update/Q.p__Poribacteria.iqtree)  
BIC of the new model: 3313046.6852  
Likelihood of the new model: -1554997.2681  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Poribacteria_1)  
Model set for next iteration: Q.PLANT,Q.PFAM,Q.INSECT,LG,Q.p__Poribacteria_1  
![Model bubble plot](loop_1/Q.p__Poribacteria_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9659497491373082  
Euclidean distance: 0.5250750870537119  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Poribacteria/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Poribacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/Q.p__Poribacteria_1.treefile
```
  
  Runtime: 530.04 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/Q.p__Poribacteria_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Poribacteria/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Poribacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/Q.p__Poribacteria_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Poribacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 12  
Normalized RF distance: 0.0659  
Tree 1 branch length: 9.25482  
Tree 2 branch length: 12.55666  
Time usage for Loop_1: 23307.84 seconds (6.47 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/Q.p__Poribacteria_1.treefile -l 15 -u 94 -o ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/subtrees -m split
```
  
Original number of taxa: 94   
Number of pruned subtrees: 1   
Number of taxa after pruning: 94   
Pruned node IDs (degree): 1 (94)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 114 loci files. Total number of potential alignments: 114.  
Obtained 114 alignments from all potential alignments.  
Remaining 114 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/training_loci -m MFP -mset Q.PLANT,Q.PFAM,Q.INSECT,LG,Q.p__Poribacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Poribacteria/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/subtree_update/Q.p__Poribacteria
```
  
  Runtime: 3661.00 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Poribacteria.iqtree)  
Best models for iteration 2:  
Q.p__Poribacteria_1  

| Model | Count |
|-------|-------|
| Q.p__Poribacteria_1 | 107 |
| Q.PFAM | 3 |
| Q.PLANT | 2 |
| Q.INSECT | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/subtree_update/Q.p__Poribacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/subtree_update/Q.p__Poribacteria.treefile --model-joint GTR20+FO --init-model Q.p__Poribacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Poribacteria/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/model_update/Q.p__Poribacteria
```
  
  Runtime: 14853.20 seconds  
[Model update log](loop_2/model_update/Q.p__Poribacteria.iqtree)  
BIC of the new model: 3311866.26  
Likelihood of the new model: -1554407.0555  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Poribacteria_2)  
Model set for next iteration: Q.PFAM,Q.PLANT,Q.INSECT,Q.p__Poribacteria_2  
![Model bubble plot](loop_2/Q.p__Poribacteria_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998903246177223  
Euclidean distance: 0.029827982210027883  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Poribacteria/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/Q.p__Poribacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Poribacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 453.48 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Poribacteria', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Poribacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Poribacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Poribacteria/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 12  
Normalized RF distance: 0.0659  
Tree 1 branch length: 9.25482  
Tree 2 branch length: 12.53659  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Poribacteria/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Poribacteria/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Poribacteria/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Poribacteria_1,Q.p__Poribacteria_2 -mdef ../Result_nova/phylum_models/Q.p__Poribacteria/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Poribacteria/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 14811.35 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Poribacteria_2+I+R7 | -1598207.637 | 3198507.070 |
| Q.p__Poribacteria_2+R7 | -1598223.980 | 3198529.192 |
| Q.p__Poribacteria_1+I+R7 | -1598219.834 | 3198531.464 |
| Q.p__Poribacteria_1+R7 | -1598236.669 | 3198554.570 |
| Q.p__Poribacteria_2+F+I+R7 | -1599978.081 | 3202248.686 |
| Q.p__Poribacteria_2+F+R7 | -1599994.273 | 3202270.506 |
| Q.p__Poribacteria_1+F+I+R7 | -1600005.662 | 3202303.848 |
| Q.p__Poribacteria_1+F+R7 | -1600022.268 | 3202326.496 |
| JTT+F+I+R7 | -1608866.902 | 3220026.328 |
| JTT+F+R7 | -1608875.391 | 3220032.742 |
| LG+F+I+R7 | -1610052.771 | 3222398.066 |
| LG+F+R7 | -1610061.831 | 3222405.622 |
| Q.PLANT+F+I+R7 | -1610134.391 | 3222561.306 |
| Q.PLANT+F+R7 | -1610155.213 | 3222592.386 |
| Q.PFAM+F+I+R7 | -1610994.799 | 3224282.122 |
| Q.PFAM+F+R7 | -1611006.336 | 3224294.632 |
| Q.INSECT+F+I+R7 | -1611536.600 | 3225365.724 |
| Q.YEAST+F+I+R7 | -1611540.295 | 3225373.114 |
| Q.INSECT+F+R7 | -1611549.342 | 3225380.644 |
| Q.YEAST+F+R7 | -1611550.618 | 3225383.196 |
| JTT+I+R7 | -1611673.108 | 3225438.012 |
| JTT+R7 | -1611685.083 | 3225451.398 |
| Q.PLANT+I+R7 | -1612015.065 | 3226121.926 |
| Q.PLANT+R7 | -1612039.067 | 3226159.366 |
| Q.PFAM+I+R7 | -1612220.661 | 3226533.118 |
| Q.PFAM+R7 | -1612230.752 | 3226542.736 |
| LG+I+R7 | -1612449.634 | 3226991.064 |
| LG+R7 | -1612458.807 | 3226998.846 |
| LG+R8 | -1612449.512 | 3227001.385 |
| LG+I+R8 | -1612446.457 | 3227005.840 |
| LG+I+R6 | -1612516.097 | 3227102.861 |
| LG+R6 | -1612609.317 | 3227278.736 |
| WAG+F+R7 | -1613706.197 | 3229694.354 |
| WAG+F+I+R7 | -1613701.016 | 3229694.556 |
| Q.INSECT+I+R7 | -1614255.743 | 3230603.282 |
| Q.INSECT+R7 | -1614271.311 | 3230623.854 |
| LG+I+G4 | -1615586.187 | 3233147.959 |
| LG+G4 | -1617117.629 | 3236200.279 |
| Q.YEAST+I+R7 | -1617460.392 | 3237012.580 |
| Q.YEAST+R7 | -1617472.290 | 3237025.812 |
| WAG+I+R7 | -1617885.668 | 3237863.132 |
| WAG+R7 | -1617893.088 | 3237867.408 |
| CPREV+F+I+R7 | -1618523.149 | 3239338.822 |
| CPREV+F+R7 | -1618535.632 | 3239353.224 |
| Q.MAMMAL+F+I+R7 | -1619298.350 | 3240889.224 |
| Q.MAMMAL+F+R7 | -1619336.772 | 3240955.504 |
| CPREV+I+R7 | -1621405.320 | 3244902.436 |
| CPREV+R7 | -1621416.408 | 3244914.048 |
| Q.MAMMAL+I+R7 | -1621769.638 | 3245631.072 |
| Q.MAMMAL+R7 | -1621798.805 | 3245678.842 |
| MTINV+F+I+R7 | -1625164.099 | 3252620.722 |
| MTINV+F+R7 | -1625181.233 | 3252644.426 |
| DCMUT+F+I+R7 | -1627068.191 | 3256428.906 |
| DCMUT+F+R7 | -1627083.164 | 3256448.288 |
| Q.BIRD+F+I+R7 | -1627752.865 | 3257798.254 |
| Q.BIRD+F+R7 | -1627803.471 | 3257888.902 |
| MTMET+F+I+R7 | -1628709.127 | 3259710.778 |
| MTMET+F+R7 | -1628748.999 | 3259779.958 |
| Q.BIRD+I+R7 | -1629600.256 | 3261292.308 |
| Q.BIRD+R7 | -1629643.002 | 3261367.236 |
| DCMUT+I+R7 | -1635771.683 | 3273635.162 |
| DCMUT+R7 | -1635791.025 | 3273663.282 |
| PMB+F+R7 | -1638722.972 | 3279727.904 |
| PMB+F+I+R7 | -1638718.107 | 3279728.738 |
| MTVER+F+I+R7 | -1642841.525 | 3287975.574 |
| MTVER+F+R7 | -1642898.792 | 3288079.544 |
| PMB+I+R7 | -1643777.556 | 3289646.908 |
| PMB+R7 | -1643783.207 | 3289647.646 |
| LG+I | -1694083.259 | 3390131.539 |
| MTMET+I+R7 | -1696514.310 | 3395120.416 |
| MTMET+R7 | -1696560.356 | 3395201.944 |
| MTVER+I+R7 | -1700177.768 | 3402447.332 |
| MTVER+R7 | -1700239.739 | 3402560.710 |
| MTINV+I+R7 | -1712758.432 | 3427608.660 |
| MTINV+R7 | -1712792.856 | 3427666.944 |
| LG | -1737426.419 | 3476807.294 |
The inferred model Q.p__Poribacteria_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Poribacteria_2+I+R7 | JTT+F+I+R7 |
| BIC | 3198507.07 | 3220026.328 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/allloci_best_existing_model_tree.log -intree ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/Q.p__Poribacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Poribacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 478.85 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Poribacteria/loop_1/tree_update/Q.p__Poribacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Poribacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 461.21 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than JTT model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Poribacteria/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Poribacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Poribacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Poribacteria/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.022  
Tree 1 branch length: 11.90923  
Tree 2 branch length: 12.53659  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1688929.156 | -1702435.876 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (JTT) and final model (Q.p__Poribacteria_2):  
Pearson's correlation: 0.9554114480399718  
Euclidean distance: 0.6383642375742963  
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
Total time usage: 58217.59 seconds (16.17 h)  
