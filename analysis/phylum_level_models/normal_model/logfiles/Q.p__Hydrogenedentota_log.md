## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Hydrogenedentota  
  Taxa name: p__Hydrogenedentota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 77  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 77  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Hydrogenedentota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Hydrogenedentota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Hydrogenedentota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/ref_tree.tre -l 15 -u 77 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/subtrees -m split
```
  
Original number of taxa: 77   
Number of pruned subtrees: 1   
Number of taxa after pruning: 77   
Pruned node IDs (degree): 1 (77)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/subtree_update/Q.p__Hydrogenedentota
```
  
  Runtime: 8923.30 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Hydrogenedentota.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| Q.PFAM | 46 |
| LG | 41 |
| Q.YEAST | 26 |
| Q.PLANT | 5 |
| WAG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/subtree_update/Q.p__Hydrogenedentota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/subtree_update/Q.p__Hydrogenedentota.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/model_update/Q.p__Hydrogenedentota
```
  
  Runtime: 23732.25 seconds  
[Model update log](loop_1/model_update/Q.p__Hydrogenedentota.iqtree)  
BIC of the new model: 4131356.1005  
Likelihood of the new model: -1983290.2473  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Hydrogenedentota_1)  
Model set for next iteration: Q.PFAM,LG,Q.YEAST,Q.p__Hydrogenedentota_1  
![Model bubble plot](loop_1/Q.p__Hydrogenedentota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.974772350949578  
Euclidean distance: 0.5430752386996139  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/tree_update/Q.p__Hydrogenedentota_1.treefile
```
  
  Runtime: 483.04 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/tree_update/Q.p__Hydrogenedentota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/tree_update/Q.p__Hydrogenedentota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 26  
Normalized RF distance: 0.1733  
Tree 1 branch length: 13.80254  
Tree 2 branch length: 18.75273  
Time usage for Loop_1: 33183.60 seconds (9.22 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/tree_update/Q.p__Hydrogenedentota_1.treefile -l 15 -u 77 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/subtrees -m split
```
  
Original number of taxa: 77   
Number of pruned subtrees: 1   
Number of taxa after pruning: 77   
Pruned node IDs (degree): 1 (77)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.YEAST,Q.p__Hydrogenedentota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/subtree_update/Q.p__Hydrogenedentota
```
  
  Runtime: 6899.57 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Hydrogenedentota.iqtree)  
Best models for iteration 2:  
Q.p__Hydrogenedentota_1  

| Model | Count |
|-------|-------|
| Q.p__Hydrogenedentota_1 | 111 |
| Q.YEAST | 4 |
| LG | 3 |
| Q.PFAM | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/subtree_update/Q.p__Hydrogenedentota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/subtree_update/Q.p__Hydrogenedentota.treefile --model-joint GTR20+FO --init-model Q.p__Hydrogenedentota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/model_update/Q.p__Hydrogenedentota
```
  
  Runtime: 9113.49 seconds  
[Model update log](loop_2/model_update/Q.p__Hydrogenedentota.iqtree)  
BIC of the new model: 4129278.3112  
Likelihood of the new model: -1982251.3526  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Hydrogenedentota_2)  
Model set for next iteration: Q.YEAST,LG,Q.PFAM,Q.p__Hydrogenedentota_2  
![Model bubble plot](loop_2/Q.p__Hydrogenedentota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998291867717918  
Euclidean distance: 0.046315519882875474  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/tree_update/Q.p__Hydrogenedentota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 440.84 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 26  
Normalized RF distance: 0.1733  
Tree 1 branch length: 13.80254  
Tree 2 branch length: 18.81174  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Hydrogenedentota_1,Q.p__Hydrogenedentota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 21092.11 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Hydrogenedentota_2+I+R8 | -2022995.064 | 4047750.846 |
| Q.p__Hydrogenedentota_2+R8 | -2023015.073 | 4047780.257 |
| Q.p__Hydrogenedentota_1+I+R8 | -2023010.429 | 4047781.576 |
| Q.p__Hydrogenedentota_1+R8 | -2023030.296 | 4047810.703 |
| Q.p__Hydrogenedentota_1+F+I+R8 | -2026760.289 | 4055482.824 |
| Q.p__Hydrogenedentota_1+F+R8 | -2026778.672 | 4055508.983 |
| Q.p__Hydrogenedentota_2+F+I+R8 | -2027147.924 | 4056258.094 |
| Q.p__Hydrogenedentota_2+F+R8 | -2027166.238 | 4056284.115 |
| LG+F+I+R8 | -2031744.308 | 4065450.862 |
| LG+F+R8 | -2031749.784 | 4065451.207 |
| Q.PFAM+F+I+R8 | -2033147.661 | 4068257.568 |
| Q.PFAM+F+R8 | -2033154.064 | 4068259.767 |
| Q.YEAST+F+I+R8 | -2034068.530 | 4070099.306 |
| Q.YEAST+F+R8 | -2034084.607 | 4070120.853 |
| Q.PFAM+R8 | -2035476.132 | 4072702.375 |
| Q.PFAM+I+R8 | -2035471.795 | 4072704.308 |
| Q.INSECT+F+I+R8 | -2036768.709 | 4075499.664 |
| Q.INSECT+F+R8 | -2036784.905 | 4075521.449 |
| LG+R8 | -2037276.795 | 4076303.701 |
| LG+I+R8 | -2037272.701 | 4076306.120 |
| LG+R9 | -2037273.144 | 4076317.613 |
| LG+I+R9 | -2037270.150 | 4076322.231 |
| LG+I+R7 | -2037296.002 | 4076331.508 |
| LG+R7 | -2037358.322 | 4076445.542 |
| LG+I+R6 | -2037472.296 | 4076662.883 |
| LG+R6 | -2037649.523 | 4077006.730 |
| LG+I+G4 | -2041002.303 | 4083627.436 |
| WAG+F+I+R8 | -2042908.582 | 4087779.410 |
| WAG+F+R8 | -2042919.540 | 4087790.719 |
| Q.INSECT+R8 | -2044875.031 | 4091500.173 |
| Q.INSECT+I+R8 | -2044869.913 | 4091500.544 |
| LG+G4 | -2045263.370 | 4092138.964 |
| WAG+I+R8 | -2048780.996 | 4099322.710 |
| WAG+R8 | -2048792.359 | 4099334.829 |
| Q.YEAST+I+R8 | -2049606.162 | 4100973.042 |
| Q.YEAST+R8 | -2049621.703 | 4100993.517 |
| JTT+F+I+R8 | -2051722.100 | 4105406.446 |
| JTT+F+R8 | -2051727.859 | 4105407.357 |
| Q.PLANT+F+I+R8 | -2052808.710 | 4107579.666 |
| Q.PLANT+F+R8 | -2052826.341 | 4107604.321 |
| JTT+I+R8 | -2055050.799 | 4111862.316 |
| JTT+R8 | -2055057.931 | 4111865.973 |
| Q.PLANT+I+R8 | -2056940.607 | 4115641.932 |
| Q.PLANT+R8 | -2056961.170 | 4115672.451 |
| CPREV+F+I+R8 | -2058867.607 | 4119697.460 |
| CPREV+F+R8 | -2058882.463 | 4119716.565 |
| DCMUT+F+I+R8 | -2059341.831 | 4120645.908 |
| DCMUT+F+R8 | -2059358.929 | 4120669.497 |
| CPREV+I+R8 | -2069562.661 | 4140886.040 |
| CPREV+R8 | -2069577.696 | 4140905.503 |
| DCMUT+I+R8 | -2070233.050 | 4142226.818 |
| DCMUT+R8 | -2070248.124 | 4142246.359 |
| MTINV+F+I+R8 | -2070411.466 | 4142785.178 |
| PMB+F+I+R8 | -2070413.295 | 4142788.836 |
| PMB+F+R8 | -2070419.808 | 4142791.255 |
| MTINV+F+R8 | -2070433.346 | 4142818.331 |
| PMB+I+R8 | -2077195.602 | 4156151.922 |
| PMB+R8 | -2077201.203 | 4156152.517 |
| Q.MAMMAL+F+I+R8 | -2078871.298 | 4159704.842 |
| Q.MAMMAL+F+R8 | -2078886.218 | 4159724.075 |
| Q.MAMMAL+I+R8 | -2079596.292 | 4160953.302 |
| Q.MAMMAL+R8 | -2079618.342 | 4160986.795 |
| MTMET+F+I+R8 | -2087008.625 | 4175979.496 |
| MTMET+F+R8 | -2087057.086 | 4176065.811 |
| Q.BIRD+F+I+R8 | -2095922.617 | 4193807.480 |
| Q.BIRD+F+R8 | -2095938.372 | 4193828.383 |
| Q.BIRD+I+R8 | -2096172.599 | 4194105.916 |
| Q.BIRD+R8 | -2096195.238 | 4194140.587 |
| MTVER+F+I+R8 | -2117592.259 | 4237146.764 |
| MTVER+F+R8 | -2117635.978 | 4237223.595 |
| LG+I | -2169455.736 | 4340523.696 |
| MTMET+I+R8 | -2186961.723 | 4375684.164 |
| MTMET+R8 | -2187027.831 | 4375805.773 |
| MTINV+I+R8 | -2197324.054 | 4396408.826 |
| MTINV+R8 | -2197357.079 | 4396464.269 |
| MTVER+I+R8 | -2198592.419 | 4398945.556 |
| MTVER+R8 | -2198707.185 | 4399164.481 |
| LG | -2253449.616 | 4508500.849 |
The inferred model Q.p__Hydrogenedentota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Hydrogenedentota_2+I+R8 | LG+F+I+R8 |
| BIC | 4047750.846 | 4065450.862 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loop_1/tree_update/Q.p__Hydrogenedentota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 393.19 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Hydrogenedentota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0267  
Tree 1 branch length: 17.66619  
Tree 2 branch length: 18.81174  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2092436.325 | -2106765.985 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Hydrogenedentota_2):  
Pearson's correlation: 0.9698734339037316  
Euclidean distance: 0.5756084387296408  
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
Total time usage: 71313.26 seconds (19.81 h)  
