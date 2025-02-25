## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Omnitrophota  
  Taxa name: p__Omnitrophota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 6 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/select_id.txt. Sampling sequences for 114 loci.  
Number of input species: 585  
Remaining 114 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Omnitrophota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Omnitrophota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Omnitrophota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 118 alignments. Deleted 2 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/subtrees -m split
```
  
Original number of taxa: 585   
Number of pruned subtrees: 5   
Number of taxa after pruning: 541   
Pruned node IDs (degree): 253 (248) 62 (120) 525 (61) 2 (59) 197 (53)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 5 subtree files and 114 loci files. Total number of potential alignments: 570.  
Obtained 559 alignments from all potential alignments.  
Remaining 559 alignments. Deleted 11 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/subtree_update/Q.p__Omnitrophota
```
  
  Runtime: 57406.94 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Omnitrophota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 265 |
| LG | 138 |
| Q.PFAM | 86 |
| Q.PLANT | 68 |
| CPREV | 1 |
| JTT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/subtree_update/Q.p__Omnitrophota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/subtree_update/Q.p__Omnitrophota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/model_update/Q.p__Omnitrophota
```
  
  Runtime: 76091.94 seconds  
[Model update log](loop_1/model_update/Q.p__Omnitrophota.iqtree)  
BIC of the new model: 27194777.8593  
Likelihood of the new model: -12998931.9325  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Omnitrophota_1)  
Model set for next iteration: Q.YEAST,LG,Q.PFAM,Q.PLANT,Q.p__Omnitrophota_1  
![Model bubble plot](loop_1/Q.p__Omnitrophota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9781919959189593  
Euclidean distance: 0.4497602235128736  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/Q.p__Omnitrophota_1.treefile
```
  
  Runtime: 3153.83 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/Q.p__Omnitrophota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/Q.p__Omnitrophota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 292  
Normalized RF distance: 0.2504  
Tree 1 branch length: 127.51019  
Tree 2 branch length: 171.97622  
Time usage for Loop_1: 136839.44 seconds (38.01 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/Q.p__Omnitrophota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/subtrees -m split
```
  
Original number of taxa: 585   
Number of pruned subtrees: 6   
Number of taxa after pruning: 554   
Pruned node IDs (degree): 184 (158) 464 (122) 341 (102) 3 (60) 63 (59) 130 (53)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 6 subtree files and 114 loci files. Total number of potential alignments: 684.  
Obtained 668 alignments from all potential alignments.  
Remaining 668 alignments. Deleted 16 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.PFAM,Q.PLANT,Q.p__Omnitrophota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/subtree_update/Q.p__Omnitrophota
```
  
  Runtime: 18112.43 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Omnitrophota.iqtree)  
Best models for iteration 2:  
Q.p__Omnitrophota_1  

| Model | Count |
|-------|-------|
| Q.p__Omnitrophota_1 | 568 |
| Q.PFAM | 46 |
| LG | 34 |
| Q.YEAST | 12 |
| Q.PLANT | 8 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/subtree_update/Q.p__Omnitrophota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/subtree_update/Q.p__Omnitrophota.treefile --model-joint GTR20+FO --init-model Q.p__Omnitrophota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/model_update/Q.p__Omnitrophota
```
  
  Runtime: 34995.06 seconds  
[Model update log](loop_2/model_update/Q.p__Omnitrophota.iqtree)  
BIC of the new model: 27937751.5916  
Likelihood of the new model: -13348499.6917  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Omnitrophota_2)  
Model set for next iteration: Q.PFAM,LG,Q.YEAST,Q.p__Omnitrophota_2  
![Model bubble plot](loop_2/Q.p__Omnitrophota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999388721803488  
Euclidean distance: 0.02908711134989772  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/Q.p__Omnitrophota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 2330.51 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 294  
Normalized RF distance: 0.2521  
Tree 1 branch length: 127.51019  
Tree 2 branch length: 173.03258  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Omnitrophota_1,Q.p__Omnitrophota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 106535.38 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Omnitrophota_1+I+R9 | -14174479.580 | 28361463.393 |
| Q.p__Omnitrophota_2+I+R9 | -14175916.590 | 28364337.413 |
| Q.p__Omnitrophota_1+F+I+R9 | -14211924.120 | 28436553.132 |
| Q.p__Omnitrophota_2+F+I+R9 | -14214394.270 | 28441493.432 |
| Q.YEAST+F+I+R9 | -14232382.660 | 28477470.212 |
| LG+F+I+R9 | -14240056.800 | 28492818.492 |
| Q.YEAST+I+R9 | -14245290.230 | 28503084.693 |
| Q.PFAM+F+I+R9 | -14245811.820 | 28504328.532 |
| LG+I+R9 | -14251343.620 | 28515191.473 |
| Q.INSECT+I+R9 | -14251567.020 | 28515638.273 |
| LG+R9 | -14253268.680 | 28519031.032 |
| Q.PFAM+I+R9 | -14253832.430 | 28520169.093 |
| LG+I+R8 | -14255665.450 | 28523814.011 |
| Q.INSECT+F+I+R9 | -14256337.090 | 28525379.072 |
| LG+R8 | -14258442.240 | 28529357.030 |
| LG+I+R7 | -14262816.430 | 28538094.849 |
| LG+R7 | -14266685.190 | 28545821.808 |
| LG+I+R6 | -14274833.570 | 28562108.007 |
| LG+R6 | -14280320.850 | 28573072.006 |
| Q.PLANT+I+R9 | -14317465.530 | 28647435.293 |
| JTT+F+I+R9 | -14325117.450 | 28662939.792 |
| Q.PLANT+F+I+R9 | -14329014.510 | 28670733.912 |
| LG+I+G4 | -14340055.330 | 28692456.478 |
| WAG+F+I+R9 | -14341092.760 | 28694890.412 |
| JTT+I+R9 | -14350095.700 | 28712695.633 |
| WAG+I+R9 | -14350438.430 | 28713381.093 |
| LG+G4 | -14364628.180 | 28741591.617 |
| CPREV+I+R9 | -14406722.570 | 28825949.373 |
| MTINV+F+I+R9 | -14426769.190 | 28866243.272 |
| CPREV+F+I+R9 | -14451907.000 | 28916518.892 |
| DCMUT+F+I+R9 | -14456075.150 | 28924855.192 |
| Q.MAMMAL+F+I+R9 | -14457372.200 | 28927449.292 |
| Q.MAMMAL+I+R9 | -14475735.940 | 28963976.113 |
| DCMUT+I+R9 | -14504524.780 | 29021553.793 |
| PMB+F+I+R9 | -14512065.670 | 29036836.232 |
| MTMET+F+I+R9 | -14514428.040 | 29041560.972 |
| PMB+I+R9 | -14516492.350 | 29045488.933 |
| Q.BIRD+F+I+R9 | -14549677.150 | 29112059.192 |
| Q.BIRD+I+R9 | -14567159.460 | 29146823.153 |
| MTVER+F+I+R9 | -14752253.260 | 29517211.412 |
| MTMET+I+R9 | -15089459.850 | 30191423.933 |
| MTINV+I+R9 | -15138586.490 | 30289677.213 |
| MTVER+I+R9 | -15244524.710 | 30501553.653 |
| LG+I | -15577947.650 | 31168230.557 |
| LG | -15820614.620 | 31653553.936 |
The inferred model Q.p__Omnitrophota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Omnitrophota_1+I+R9 | Q.YEAST+F+I+R9 |
| BIC | 28361463.393 | 28477470.212 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/Q.p__Omnitrophota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 2784.44 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loop_1/tree_update/Q.p__Omnitrophota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 2957.06 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
Q.YEAST model has higher likelihood than LG model, use best_existing_model model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/allloci_best_existing_model_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Omnitrophota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 26  
Normalized RF distance: 0.0223  
Tree 1 branch length: 164.61158  
Tree 2 branch length: 173.03258  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -14245291.244 | -14313849.076 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.YEAST) and final model (Q.p__Omnitrophota_2):  
Pearson's correlation: 0.9780965460482903  
Euclidean distance: 0.4588247534710284  
![Best existing model bubble plot](final_test/best_existing_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Pairwise tree distance comparison  
![Heatmap of RF distance of trees:](estimated_tree/RF_heatmap.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_heatmap.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 305033.92 seconds (84.73 h)  
