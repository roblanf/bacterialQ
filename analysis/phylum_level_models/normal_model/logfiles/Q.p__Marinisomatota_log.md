## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Marinisomatota  
  Taxa name: p__Marinisomatota  
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
Discarded 2 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Marinisomatota/select_id.txt. Sampling sequences for 118 loci.  
Number of input species: 275  
Remaining 118 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Marinisomatota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Marinisomatota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Marinisomatota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Zixibacteria as the outgroup for Phylum Marinisomatota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Marinisomatota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/subtrees -m split
```
  
Original number of taxa: 275   
Number of pruned subtrees: 2   
Number of taxa after pruning: 266   
Pruned node IDs (degree): 47 (222) 4 (44)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 2 subtree files and 118 loci files. Total number of potential alignments: 236.  
Obtained 236 alignments from all potential alignments.  
Remaining 236 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/subtree_update/Q.p__Marinisomatota
```
  
  Runtime: 50747.12 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Marinisomatota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 146 |
| Q.INSECT | 40 |
| LG | 38 |
| Q.PFAM | 8 |
| Q.PLANT | 4 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/subtree_update/Q.p__Marinisomatota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/subtree_update/Q.p__Marinisomatota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/model_update/Q.p__Marinisomatota
```
  
  Runtime: 52910.44 seconds  
[Model update log](loop_1/model_update/Q.p__Marinisomatota.iqtree)  
BIC of the new model: 11469400.3899  
Likelihood of the new model: -5453786.6325  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Marinisomatota_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.p__Marinisomatota_1  
![Model bubble plot](loop_1/Q.p__Marinisomatota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9758958893031495  
Euclidean distance: 0.4849583380504352  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Marinisomatota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Marinisomatota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/tree_update/Q.p__Marinisomatota_1.treefile
```
  
  Runtime: 1606.22 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/tree_update/Q.p__Marinisomatota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/tree_update/Q.p__Marinisomatota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 84  
Normalized RF distance: 0.1544  
Tree 1 branch length: 41.2724  
Tree 2 branch length: 57.23271  
Time usage for Loop_1: 105339.65 seconds (29.26 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/tree_update/Q.p__Marinisomatota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/subtrees -m split
```
  
Original number of taxa: 275   
Number of pruned subtrees: 2   
Number of taxa after pruning: 267   
Pruned node IDs (degree): 5 (223) 227 (44)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 2 subtree files and 118 loci files. Total number of potential alignments: 236.  
Obtained 236 alignments from all potential alignments.  
Remaining 236 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.p__Marinisomatota_1 -mdef ../Result_nova/phylum_models/Q.p__Marinisomatota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/subtree_update/Q.p__Marinisomatota
```
  
  Runtime: 26803.26 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Marinisomatota.iqtree)  
Best models for iteration 2:  
Q.p__Marinisomatota_1  

| Model | Count |
|-------|-------|
| Q.p__Marinisomatota_1 | 208 |
| LG | 15 |
| Q.YEAST | 7 |
| Q.INSECT | 6 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/subtree_update/Q.p__Marinisomatota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/subtree_update/Q.p__Marinisomatota.treefile --model-joint GTR20+FO --init-model Q.p__Marinisomatota_1 -mdef ../Result_nova/phylum_models/Q.p__Marinisomatota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/model_update/Q.p__Marinisomatota
```
  
  Runtime: 52065.13 seconds  
[Model update log](loop_2/model_update/Q.p__Marinisomatota.iqtree)  
BIC of the new model: 11527024.6406  
Likelihood of the new model: -5481830.3075  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Marinisomatota_2)  
Model set for next iteration: LG,Q.YEAST,Q.INSECT,Q.p__Marinisomatota_2  
![Model bubble plot](loop_2/Q.p__Marinisomatota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999711737965742  
Euclidean distance: 0.019991701592285475  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/tree_update/Q.p__Marinisomatota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Marinisomatota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 1230.18 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Marinisomatota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 82  
Normalized RF distance: 0.1507  
Tree 1 branch length: 41.2724  
Tree 2 branch length: 57.32393  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (Q.p__Marinisomatota_2):  
Pearson's correlation: 0.9756650438339592  
Euclidean distance: 0.4926913344121154  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Marinisomatota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Marinisomatota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Marinisomatota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Marinisomatota_1,Q.p__Marinisomatota_2 -mdef ../Result_nova/phylum_models/Q.p__Marinisomatota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Marinisomatota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 22269.61 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Marinisomatota_1+I+R8 | -5743823.841 | 11493607.552 |
| Q.p__Marinisomatota_2+I+R8 | -5743854.275 | 11493668.420 |
| Q.YEAST+I+R8 | -5772097.606 | 11550155.082 |
| Q.p__Marinisomatota_1+F+I+R8 | -5774787.983 | 11555737.327 |
| Q.p__Marinisomatota_2+F+I+R8 | -5775401.389 | 11556964.139 |
| LG+F+I+R8 | -5778001.513 | 11562164.387 |
| Q.PFAM+F+I+R8 | -5782533.738 | 11571228.837 |
| Q.INSECT+I+R8 | -5786112.740 | 11578185.350 |
| Q.YEAST+F+I+R8 | -5790618.005 | 11587397.371 |
| Q.INSECT+F+I+R8 | -5798724.952 | 11603611.265 |
| WAG+F+I+R8 | -5799043.829 | 11604249.019 |
| LG+I+R8 | -5800781.759 | 11607523.388 |
| LG+R8 | -5801340.828 | 11608630.922 |
| LG+I+R7 | -5802083.516 | 11610105.693 |
| LG+R7 | -5802893.334 | 11611714.724 |
| LG+I+R6 | -5804352.039 | 11614621.529 |
| LG+R6 | -5806467.847 | 11618842.541 |
| LG+I+R5 | -5809528.654 | 11624953.550 |
| Q.PFAM+I+R8 | -5811641.484 | 11629242.838 |
| LG+R5 | -5813273.851 | 11632433.339 |
| JTT+F+I+R8 | -5814851.201 | 11635863.763 |
| Q.PLANT+F+I+R8 | -5818070.763 | 11642302.887 |
| LG+I+G4 | -5822233.683 | 11650289.375 |
| Q.PLANT+I+R8 | -5828581.611 | 11663123.092 |
| CPREV+F+I+R8 | -5829848.242 | 11665857.845 |
| WAG+I+R8 | -5832836.388 | 11671632.646 |
| LG+G4 | -5833286.434 | 11672384.272 |
| CPREV+I+R8 | -5835042.776 | 11676045.422 |
| MTINV+F+I+R8 | -5835794.102 | 11677749.565 |
| JTT+I+R8 | -5849632.615 | 11705225.100 |
| DCMUT+F+I+R8 | -5851554.601 | 11709270.563 |
| MTMET+F+I+R8 | -5866474.540 | 11739110.441 |
| PMB+F+I+R8 | -5871464.291 | 11749089.943 |
| Q.MAMMAL+F+I+R8 | -5879608.583 | 11765378.527 |
| DCMUT+I+R8 | -5896017.538 | 11797994.946 |
| PMB+I+R8 | -5910625.702 | 11827211.274 |
| Q.MAMMAL+I+R8 | -5919103.621 | 11844167.112 |
| Q.BIRD+F+I+R8 | -5921855.517 | 11849872.395 |
| MTVER+F+I+R8 | -5953153.806 | 11912468.973 |
| Q.BIRD+I+R8 | -5957996.911 | 11921953.692 |
| MTMET+I+R8 | -6022528.426 | 12051016.722 |
| MTINV+I+R8 | -6031085.554 | 12068130.978 |
| MTVER+I+R8 | -6105969.071 | 12217898.012 |
| LG+I | -6275916.415 | 12557644.234 |
| LG | -6417110.510 | 12840021.819 |
The inferred model Q.p__Marinisomatota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Marinisomatota_1+I+R8 | Q.YEAST+I+R8 |
| BIC | 11493607.552 | 11550155.082 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Marinisomatota/loop_1/tree_update/Q.p__Marinisomatota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Marinisomatota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 1160.51 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Marinisomatota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Marinisomatota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0147  
Tree 1 branch length: 51.90743  
Tree 2 branch length: 57.32393  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -5812005.427 | -5867539.447 |
The final model tree has better likelihood than the existing model tree.  
### Pairwise comparison of trees  
![Heatmap of RF distance of trees:](estimated_tree/RF_heatmap.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_heatmap.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 209086.64 seconds (58.08 h)  
