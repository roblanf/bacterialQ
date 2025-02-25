## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_B  
  Taxa name: p__Bacillota_B  
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
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 480  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_B  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_B -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota_B
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/subtrees -m split
```
  
Original number of taxa: 480   
Number of pruned subtrees: 3   
Number of taxa after pruning: 480   
Pruned node IDs (degree): 136 (216) 3 (134) 351 (130)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 120 loci files. Total number of potential alignments: 360.  
Obtained 360 alignments from all potential alignments.  
Remaining 360 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/subtree_update/Q.p__Bacillota_B
```
  
  Runtime: 42541.44 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_B.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 103 |
| Q.YEAST | 102 |
| Q.PLANT | 98 |
| Q.PFAM | 57 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/subtree_update/Q.p__Bacillota_B.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/subtree_update/Q.p__Bacillota_B.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/model_update/Q.p__Bacillota_B
```
  
  Runtime: 61984.50 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_B.iqtree)  
BIC of the new model: 23098582.7437  
Likelihood of the new model: -10937211.5835  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_B_1)  
Model set for next iteration: LG,Q.YEAST,Q.PLANT,Q.PFAM,Q.p__Bacillota_B_1  
![Model bubble plot](loop_1/Q.p__Bacillota_B_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9753838504091586  
Euclidean distance: 0.5381897157125641  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/tree_update/Q.p__Bacillota_B_1.treefile
```
  
  Runtime: 2560.58 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/tree_update/Q.p__Bacillota_B_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/tree_update/Q.p__Bacillota_B_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 118  
Normalized RF distance: 0.1234  
Tree 1 branch length: 67.26279  
Tree 2 branch length: 95.29779  
Time usage for Loop_1: 107203.00 seconds (29.78 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/tree_update/Q.p__Bacillota_B_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/subtrees -m split
```
  
Original number of taxa: 480   
Number of pruned subtrees: 4   
Number of taxa after pruning: 470   
Pruned node IDs (degree): 130 (198) 327 (154) 12 (66) 78 (52)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 4 subtree files and 120 loci files. Total number of potential alignments: 480.  
Obtained 480 alignments from all potential alignments.  
Remaining 480 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PLANT,Q.PFAM,Q.p__Bacillota_B_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/subtree_update/Q.p__Bacillota_B
```
  
  Runtime: 27369.14 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_B.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_B_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_B_1 | 434 |
| LG | 16 |
| Q.PFAM | 15 |
| Q.YEAST | 8 |
| Q.PLANT | 7 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/subtree_update/Q.p__Bacillota_B.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/subtree_update/Q.p__Bacillota_B.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_B_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/model_update/Q.p__Bacillota_B
```
  
  Runtime: 67498.68 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_B.iqtree)  
BIC of the new model: 22591121.7691  
Likelihood of the new model: -10683990.009  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_B_2)  
Model set for next iteration: LG,Q.PFAM,Q.YEAST,Q.PLANT,Q.p__Bacillota_B_2  
![Model bubble plot](loop_2/Q.p__Bacillota_B_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998814513881527  
Euclidean distance: 0.0426444909891605  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/tree_update/Q.p__Bacillota_B_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 3719.25 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 118  
Normalized RF distance: 0.1234  
Tree 1 branch length: 67.26279  
Tree 2 branch length: 95.7881  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_B_1,Q.p__Bacillota_B_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 70918.76 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bacillota_B_1+I+R9 | -10926436.100 | 21863207.392 |
| Q.p__Bacillota_B_2+I+R9 | -10927681.290 | 21865697.772 |
| Q.p__Bacillota_B_1+F+I+R9 | -10954695.920 | 21919928.642 |
| Q.p__Bacillota_B_2+F+I+R9 | -10956606.200 | 21923749.202 |
| LG+I+R9 | -10980441.540 | 21971218.272 |
| LG+F+I+R9 | -10981381.180 | 21973299.162 |
| LG+R9 | -10981671.360 | 21973667.301 |
| LG+I+R8 | -10983416.660 | 21977147.290 |
| Q.PFAM+I+R9 | -10983928.490 | 21978192.172 |
| LG+R8 | -10985577.970 | 21981459.299 |
| LG+I+R7 | -10988323.260 | 21986939.268 |
| Q.INSECT+I+R9 | -10991071.610 | 21992478.412 |
| LG+R7 | -10991139.380 | 21992560.896 |
| Q.YEAST+F+I+R9 | -10991520.200 | 21993577.202 |
| Q.PFAM+F+I+R9 | -10992380.890 | 21995298.582 |
| LG+I+R6 | -10996505.440 | 22003282.405 |
| LG+R6 | -11001602.940 | 22013466.794 |
| Q.INSECT+F+I+R9 | -11001792.980 | 22014122.762 |
| Q.YEAST+I+R9 | -11007494.180 | 22025323.552 |
| Q.PLANT+I+R9 | -11037305.990 | 22084947.172 |
| LG+I+G4 | -11044735.390 | 22099646.806 |
| Q.PLANT+F+I+R9 | -11045681.230 | 22101899.262 |
| WAG+F+I+R9 | -11052066.750 | 22114670.302 |
| WAG+I+R9 | -11056608.550 | 22123552.292 |
| JTT+F+I+R9 | -11056699.080 | 22123934.962 |
| JTT+I+R9 | -11057037.190 | 22124409.572 |
| LG+G4 | -11066633.630 | 22143432.675 |
| CPREV+I+R9 | -11117478.080 | 22245291.352 |
| CPREV+F+I+R9 | -11130399.840 | 22271336.482 |
| DCMUT+F+I+R9 | -11149559.950 | 22309656.702 |
| MTINV+F+I+R9 | -11155171.270 | 22320879.342 |
| Q.MAMMAL+I+R9 | -11167121.600 | 22344578.392 |
| Q.MAMMAL+F+I+R9 | -11175433.820 | 22361404.442 |
| DCMUT+I+R9 | -11180873.710 | 22372082.612 |
| PMB+F+I+R9 | -11210679.840 | 22431896.482 |
| PMB+I+R9 | -11214816.680 | 22439968.552 |
| MTMET+F+I+R9 | -11226661.240 | 22463859.282 |
| Q.BIRD+I+R9 | -11246980.430 | 22504296.052 |
| Q.BIRD+F+I+R9 | -11260178.870 | 22530894.542 |
| MTVER+F+I+R9 | -11401774.930 | 22814086.662 |
| MTMET+I+R9 | -11638496.070 | 23287327.332 |
| MTINV+I+R9 | -11683707.190 | 23377749.572 |
| MTVER+I+R9 | -11737222.320 | 23484779.832 |
| LG+I | -12038708.730 | 24087582.875 |
| LG | -12288071.870 | 24586298.543 |
The inferred model Q.p__Bacillota_B_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bacillota_B_1+I+R9 | LG+I+R9 |
| BIC | 21863207.392 | 21971218.272 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loop_1/tree_update/Q.p__Bacillota_B_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 1739.44 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_B/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 14  
Normalized RF distance: 0.0146  
Tree 1 branch length: 89.11934  
Tree 2 branch length: 95.7881  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -10995906.466 | -11047460.651 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bacillota_B_2):  
Pearson's correlation: 0.973612086350963  
Euclidean distance: 0.569002062080798  
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
Total time usage: 278838.40 seconds (77.46 h)  
