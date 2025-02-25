## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Fermentibacterota  
  Taxa name: p__Fermentibacterota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 50  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 6 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/select_id.txt. Sampling sequences for 114 loci.  
Number of input species: 50  
Remaining 114 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Fermentibacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Fermentibacterota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Eisenbacteria as the outgroup for Phylum Fermentibacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 118 alignments. Deleted 2 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/ref_tree.tre -l 15 -u 50 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 114 loci files. Total number of potential alignments: 114.  
Obtained 114 alignments from all potential alignments.  
Remaining 114 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/subtree_update/Q.p__Fermentibacterota
```
  
  Runtime: 908.47 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Fermentibacterota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 42 |
| Q.PLANT | 36 |
| Q.PFAM | 19 |
| Q.YEAST | 6 |
| WAG | 6 |
| JTT | 3 |
| CPREV | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/subtree_update/Q.p__Fermentibacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/subtree_update/Q.p__Fermentibacterota.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/model_update/Q.p__Fermentibacterota
```
  
  Runtime: 2180.24 seconds  
[Model update log](loop_1/model_update/Q.p__Fermentibacterota.iqtree)  
BIC of the new model: 2187488.6567  
Likelihood of the new model: -1043755.3309  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Fermentibacterota_1)  
Model set for next iteration: LG,Q.PLANT,Q.PFAM,Q.YEAST,WAG,Q.p__Fermentibacterota_1  
![Model bubble plot](loop_1/Q.p__Fermentibacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9512961542089446  
Euclidean distance: 0.7293675382172649  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/tree_update/Q.p__Fermentibacterota_1.treefile
```
  
  Runtime: 118.92 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/tree_update/Q.p__Fermentibacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/tree_update/Q.p__Fermentibacterota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0833  
Tree 1 branch length: 7.72505  
Tree 2 branch length: 10.51009  
Time usage for Loop_1: 3228.05 seconds (0.90 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/tree_update/Q.p__Fermentibacterota_1.treefile -l 15 -u 50 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 114 loci files. Total number of potential alignments: 114.  
Obtained 114 alignments from all potential alignments.  
Remaining 114 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/training_loci -m MFP -mset LG,Q.PLANT,Q.PFAM,Q.YEAST,WAG,Q.p__Fermentibacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/subtree_update/Q.p__Fermentibacterota
```
  
  Runtime: 653.51 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Fermentibacterota.iqtree)  
Best models for iteration 2:  
Q.p__Fermentibacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Fermentibacterota_1 | 107 |
| Q.PLANT | 5 |
| Q.YEAST | 1 |
| LG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/subtree_update/Q.p__Fermentibacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/subtree_update/Q.p__Fermentibacterota.treefile --model-joint GTR20+FO --init-model Q.p__Fermentibacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/model_update/Q.p__Fermentibacterota
```
  
  Runtime: 1774.49 seconds  
[Model update log](loop_2/model_update/Q.p__Fermentibacterota.iqtree)  
BIC of the new model: 2188001.9333  
Likelihood of the new model: -1044011.9692  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Fermentibacterota_2)  
Model set for next iteration: Q.PLANT,Q.YEAST,LG,Q.p__Fermentibacterota_2  
![Model bubble plot](loop_2/Q.p__Fermentibacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999729811694033  
Euclidean distance: 0.019881361921129704  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/tree_update/Q.p__Fermentibacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 114.70 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0833  
Tree 1 branch length: 7.72505  
Tree 2 branch length: 10.53262  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Fermentibacterota_1,Q.p__Fermentibacterota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 5355.01 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Fermentibacterota_1+I+R6 | -1062724.688 | 2126586.926 |
| Q.p__Fermentibacterota_2+I+R6 | -1062730.460 | 2126598.470 |
| Q.p__Fermentibacterota_1+F+I+R6 | -1064256.109 | 2129849.892 |
| Q.p__Fermentibacterota_2+F+I+R6 | -1064309.748 | 2129957.170 |
| LG+F+I+R6 | -1067984.403 | 2137306.480 |
| Q.PFAM+F+I+R6 | -1069056.890 | 2139451.454 |
| Q.YEAST+F+I+R6 | -1069638.088 | 2140613.850 |
| Q.INSECT+F+I+R6 | -1070358.440 | 2142054.554 |
| WAG+F+I+R6 | -1071446.326 | 2144230.326 |
| JTT+F+I+R6 | -1072244.579 | 2145826.832 |
| Q.PLANT+F+I+R6 | -1072966.407 | 2147270.488 |
| Q.PFAM+I+R6 | -1073366.415 | 2147870.380 |
| LG+I+R6 | -1073823.920 | 2148785.390 |
| LG+R7 | -1073824.238 | 2148796.559 |
| LG+I+R7 | -1073822.534 | 2148803.684 |
| LG+R8 | -1073823.502 | 2148816.152 |
| LG+R6 | -1073852.824 | 2148832.665 |
| CPREV+F+I+R6 | -1074596.449 | 2150530.572 |
| LG+I+G4 | -1075370.546 | 2151783.846 |
| LG+G4 | -1076066.740 | 2153165.701 |
| Q.PLANT+I+R6 | -1076150.352 | 2153438.254 |
| JTT+I+R6 | -1076870.509 | 2154878.568 |
| Q.INSECT+I+R6 | -1076937.770 | 2155013.090 |
| WAG+I+R6 | -1078557.521 | 2158252.592 |
| Q.YEAST+I+R6 | -1079533.041 | 2160203.632 |
| DCMUT+F+I+R6 | -1081062.478 | 2163462.630 |
| Q.MAMMAL+F+I+R6 | -1081077.389 | 2163492.452 |
| MTINV+F+I+R6 | -1081564.570 | 2164466.814 |
| CPREV+I+R6 | -1081748.630 | 2164634.810 |
| Q.MAMMAL+I+R6 | -1083976.263 | 2169090.076 |
| PMB+F+I+R6 | -1084151.987 | 2169641.648 |
| MTMET+F+I+R6 | -1086890.416 | 2175118.506 |
| Q.BIRD+F+I+R6 | -1087608.508 | 2176554.690 |
| PMB+I+R6 | -1089770.305 | 2180678.160 |
| Q.BIRD+I+R6 | -1090447.591 | 2182032.732 |
| DCMUT+I+R6 | -1092299.311 | 2185736.172 |
| MTVER+F+I+R6 | -1100052.531 | 2201442.736 |
| LG+I | -1126228.791 | 2253489.803 |
| MTMET+I+R6 | -1143317.300 | 2287772.150 |
| MTINV+I+R6 | -1147618.663 | 2296374.876 |
| MTVER+I+R6 | -1155121.634 | 2311380.818 |
| LG | -1161151.185 | 2323324.058 |
The inferred model Q.p__Fermentibacterota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Fermentibacterota_1+I+R6 | LG+F+I+R6 |
| BIC | 2126586.926 | 2137306.48 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loop_1/tree_update/Q.p__Fermentibacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 109.51 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Fermentibacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 10.06156  
Tree 2 branch length: 10.53262  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1133763.075 | -1145117.283 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Fermentibacterota_2):  
Pearson's correlation: 0.9505326605878077  
Euclidean distance: 0.7410263407860663  
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
Total time usage: 11361.19 seconds (3.16 h)  
