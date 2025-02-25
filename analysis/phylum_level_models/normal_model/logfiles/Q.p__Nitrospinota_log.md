## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Nitrospinota  
  Taxa name: p__Nitrospinota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 113  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 113  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Nitrospinota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Nitrospinota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Nitrospinota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/ref_tree.tre -l 15 -u 113 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/subtrees -m split
```
  
Original number of taxa: 113   
Number of pruned subtrees: 1   
Number of taxa after pruning: 113   
Pruned node IDs (degree): 1 (113)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/subtree_update/Q.p__Nitrospinota
```
  
  Runtime: 13082.54 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Nitrospinota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 52 |
| Q.PLANT | 28 |
| Q.PFAM | 20 |
| LG | 19 |
| WAG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/subtree_update/Q.p__Nitrospinota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/subtree_update/Q.p__Nitrospinota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/model_update/Q.p__Nitrospinota
```
  
  Runtime: 21428.90 seconds  
[Model update log](loop_1/model_update/Q.p__Nitrospinota.iqtree)  
BIC of the new model: 5222506.4714  
Likelihood of the new model: -2491329.8695  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Nitrospinota_1)  
Model set for next iteration: Q.YEAST,Q.PLANT,Q.PFAM,LG,Q.p__Nitrospinota_1  
![Model bubble plot](loop_1/Q.p__Nitrospinota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9771816123424117  
Euclidean distance: 0.43476690503972343  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/Q.p__Nitrospinota_1.treefile
```
  
  Runtime: 783.91 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/Q.p__Nitrospinota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/Q.p__Nitrospinota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 24  
Normalized RF distance: 0.1081  
Tree 1 branch length: 16.46483  
Tree 2 branch length: 22.4599  
Time usage for Loop_1: 35344.31 seconds (9.82 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/Q.p__Nitrospinota_1.treefile -l 15 -u 113 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/subtrees -m split
```
  
Original number of taxa: 113   
Number of pruned subtrees: 1   
Number of taxa after pruning: 113   
Pruned node IDs (degree): 1 (113)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.PLANT,Q.PFAM,LG,Q.p__Nitrospinota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/subtree_update/Q.p__Nitrospinota
```
  
  Runtime: 10266.14 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Nitrospinota.iqtree)  
Best models for iteration 2:  
Q.p__Nitrospinota_1  

| Model | Count |
|-------|-------|
| Q.p__Nitrospinota_1 | 115 |
| LG | 2 |
| Q.PLANT | 2 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/subtree_update/Q.p__Nitrospinota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/subtree_update/Q.p__Nitrospinota.treefile --model-joint GTR20+FO --init-model Q.p__Nitrospinota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/model_update/Q.p__Nitrospinota
```
  
  Runtime: 15829.31 seconds  
[Model update log](loop_2/model_update/Q.p__Nitrospinota.iqtree)  
BIC of the new model: 5219933.6358  
Likelihood of the new model: -2490043.4517  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Nitrospinota_2)  
Model set for next iteration: LG,Q.PLANT,Q.YEAST,Q.p__Nitrospinota_2  
![Model bubble plot](loop_2/Q.p__Nitrospinota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999624774303939  
Euclidean distance: 0.01932505624886785  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/Q.p__Nitrospinota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 620.83 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 24  
Normalized RF distance: 0.1081  
Tree 1 branch length: 16.46483  
Tree 2 branch length: 22.51294  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Nitrospinota_1,Q.p__Nitrospinota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 16389.43 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Nitrospinota_1+I+R9 | -2540737.813 | 5084023.347 |
| Q.p__Nitrospinota_2+I+R9 | -2540755.318 | 5084058.357 |
| Q.p__Nitrospinota_1+F+I+R9 | -2545323.459 | 5093396.334 |
| Q.p__Nitrospinota_2+F+I+R9 | -2545538.579 | 5093826.574 |
| Q.YEAST+F+I+R9 | -2552575.021 | 5107899.458 |
| LG+F+I+R9 | -2552860.926 | 5108471.268 |
| Q.INSECT+I+R9 | -2554299.002 | 5111145.725 |
| Q.INSECT+F+I+R9 | -2554441.634 | 5111632.684 |
| Q.PFAM+F+I+R9 | -2554715.951 | 5112181.318 |
| Q.YEAST+I+R9 | -2555465.015 | 5113477.751 |
| LG+I+R9 | -2555835.162 | 5114218.045 |
| LG+I+R8 | -2555854.327 | 5114235.144 |
| LG+R9 | -2555851.701 | 5114240.508 |
| LG+R8 | -2555911.651 | 5114339.177 |
| LG+I+R7 | -2555938.609 | 5114382.477 |
| LG+R7 | -2556144.969 | 5114784.582 |
| LG+I+R6 | -2556327.370 | 5115138.768 |
| LG+R6 | -2556630.419 | 5115734.251 |
| Q.PFAM+I+R9 | -2557253.865 | 5117055.451 |
| LG+I+G4 | -2561233.248 | 5124854.985 |
| Q.PLANT+I+R9 | -2561748.015 | 5126043.751 |
| Q.PLANT+F+I+R9 | -2562673.391 | 5128096.198 |
| JTT+F+I+R9 | -2563397.925 | 5129545.266 |
| LG+G4 | -2565511.026 | 5133399.925 |
| WAG+F+I+R9 | -2566466.817 | 5135683.050 |
| JTT+I+R9 | -2567614.769 | 5137777.259 |
| WAG+I+R9 | -2569824.452 | 5142196.625 |
| CPREV+I+R9 | -2582190.010 | 5166927.741 |
| CPREV+F+I+R9 | -2583856.330 | 5170462.076 |
| MTINV+F+I+R9 | -2584286.493 | 5171322.402 |
| DCMUT+F+I+R9 | -2584956.352 | 5172662.120 |
| Q.MAMMAL+F+I+R9 | -2585963.693 | 5174676.802 |
| Q.MAMMAL+I+R9 | -2590372.203 | 5183292.127 |
| DCMUT+I+R9 | -2594678.985 | 5191905.691 |
| MTMET+F+I+R9 | -2596651.148 | 5196051.712 |
| PMB+F+I+R9 | -2602274.382 | 5207298.180 |
| Q.BIRD+F+I+R9 | -2602971.956 | 5208693.328 |
| Q.BIRD+I+R9 | -2606142.410 | 5214832.541 |
| PMB+I+R9 | -2607952.086 | 5218451.893 |
| MTVER+F+I+R9 | -2631824.959 | 5266399.334 |
| MTMET+I+R9 | -2692992.782 | 5388533.285 |
| MTINV+I+R9 | -2705533.777 | 5413615.275 |
| LG+I | -2715033.051 | 5432443.975 |
| MTVER+I+R9 | -2716549.623 | 5435646.967 |
| LG | -2794019.371 | 5590406.000 |
The inferred model Q.p__Nitrospinota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Nitrospinota_1+I+R9 | Q.YEAST+F+I+R9 |
| BIC | 5084023.347 | 5107899.458 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/Q.p__Nitrospinota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 555.53 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loop_1/tree_update/Q.p__Nitrospinota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 581.91 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
Q.YEAST model has higher likelihood than LG model, use best_existing_model model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/allloci_best_existing_model_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospinota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 21.62737  
Tree 2 branch length: 22.51294  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2607268.489 | -2621514.88 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.YEAST) and final model (Q.p__Nitrospinota_2):  
Pearson's correlation: 0.9769264138900576  
Euclidean distance: 0.439681324923459  
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
Total time usage: 79774.53 seconds (22.16 h)  
