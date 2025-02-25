## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Planctomycetota  
  Taxa name: p__Planctomycetota  
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
Discarded 5 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/select_id.txt. Sampling sequences for 115 loci.  
Number of input species: 2338  
Remaining 115 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Planctomycetota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Planctomycetota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Planctomycetota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/subtrees -m split
```
  
Original number of taxa: 2338   
Number of pruned subtrees: 19   
Number of taxa after pruning: 2291   
Pruned node IDs (degree): 120 (245) 1752 (233) 1417 (222) 794 (194) 1987 (193) 614 (181) 1178 (177) 2179 (158) 402 (131) 1049 (130) 1638 (82) 2 (63) 987 (61) 70 (51) 1354 (47) 536 (43) 579 (28) 377 (26) 1727 (26)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 19 subtree files and 115 loci files. Total number of potential alignments: 2185.  
Sub-sampling 2000 alignments from 2185 alignments.  
Remaining 2000 alignments. Deleted 34 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/subtree_update/Q.p__Planctomycetota
```
  
  Runtime: 157305.67 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Planctomycetota.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| Q.PFAM | 680 |
| LG | 622 |
| Q.INSECT | 440 |
| Q.YEAST | 187 |
| Q.PLANT | 67 |
| MTART | 4 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/subtree_update/Q.p__Planctomycetota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/subtree_update/Q.p__Planctomycetota.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/model_update/Q.p__Planctomycetota
```
  
  Runtime: 417357.16 seconds  
[Model update log](loop_1/model_update/Q.p__Planctomycetota.iqtree)  
BIC of the new model: 97883146.877  
Likelihood of the new model: -46192818.2849  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Planctomycetota_1)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.YEAST,Q.p__Planctomycetota_1  
![Model bubble plot](loop_1/Q.p__Planctomycetota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9727696827173027  
Euclidean distance: 0.5798604333670563  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/tree_update/Q.p__Planctomycetota_1.treefile
```
  
  Runtime: 14358.17 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/tree_update/Q.p__Planctomycetota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/tree_update/Q.p__Planctomycetota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 678  
Normalized RF distance: 0.1451  
Tree 1 branch length: 400.06987  
Tree 2 branch length: 499.57091  
Time usage for Loop_1: 591227.47 seconds (164.23 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/tree_update/Q.p__Planctomycetota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/subtrees -m split
```
  
Original number of taxa: 2338   
Number of pruned subtrees: 18   
Number of taxa after pruning: 2270   
Pruned node IDs (degree): 17 (245) 1682 (239) 1425 (237) 778 (194) 1926 (193) 598 (181) 1160 (180) 2118 (158) 341 (131) 1031 (130) 2277 (62) 1359 (62) 971 (61) 261 (51) 476 (44) 520 (43) 311 (31) 563 (28)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 18 subtree files and 115 loci files. Total number of potential alignments: 2070.  
Sub-sampling 2000 alignments from 2070 alignments.  
Remaining 2000 alignments. Deleted 26 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,Q.p__Planctomycetota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/subtree_update/Q.p__Planctomycetota
```
  
  Runtime: 119051.87 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Planctomycetota.iqtree)  
Best models for iteration 2:  
Q.p__Planctomycetota_1  

| Model | Count |
|-------|-------|
| Q.p__Planctomycetota_1 | 1670 |
| Q.INSECT | 122 |
| Q.PFAM | 102 |
| LG | 84 |
| Q.YEAST | 22 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/subtree_update/Q.p__Planctomycetota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/subtree_update/Q.p__Planctomycetota.treefile --model-joint GTR20+FO --init-model Q.p__Planctomycetota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/model_update/Q.p__Planctomycetota
```
  
  Runtime: 288212.32 seconds  
[Model update log](loop_2/model_update/Q.p__Planctomycetota.iqtree)  
BIC of the new model: 102475019.4857  
Likelihood of the new model: -48374875.1722  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Planctomycetota_2)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.p__Planctomycetota_2  
![Model bubble plot](loop_2/Q.p__Planctomycetota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999439938903557  
Euclidean distance: 0.03116505076355912  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/tree_update/Q.p__Planctomycetota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 14027.76 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 680  
Normalized RF distance: 0.1455  
Tree 1 branch length: 400.06987  
Tree 2 branch length: 499.27735  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Planctomycetota_1,Q.p__Planctomycetota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 261823.00 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Planctomycetota_2+I+R9 | -51467243.070 | 102984173.440 |
| Q.p__Planctomycetota_1+I+R9 | -51468666.130 | 102987019.560 |
| Q.p__Planctomycetota_1+F+I+R9 | -51598431.320 | 103246751.232 |
| Q.p__Planctomycetota_2+F+I+R9 | -51608321.010 | 103266530.612 |
| Q.PFAM+F+I+R9 | -51657822.490 | 103365533.572 |
| LG+F+I+R9 | -51660264.480 | 103370417.552 |
| Q.PFAM+I+R9 | -51718238.670 | 103486164.640 |
| Q.YEAST+F+I+R9 | -51738116.630 | 103526121.852 |
| Q.INSECT+F+I+R9 | -51830761.000 | 103711410.592 |
| LG+I+R9 | -51831501.260 | 103712689.820 |
| LG+R9 | -51835750.970 | 103721178.646 |
| LG+I+R8 | -51857272.430 | 103764210.971 |
| LG+R8 | -51862906.720 | 103775468.957 |
| LG+I+R7 | -51892181.620 | 103834008.163 |
| LG+R7 | -51899552.490 | 103848739.308 |
| WAG+F+I+R9 | -51916568.710 | 103883026.012 |
| LG+I+R6 | -51948720.580 | 103947064.894 |
| LG+R6 | -51960304.390 | 103970221.920 |
| WAG+I+R9 | -52037998.260 | 104125683.820 |
| Q.INSECT+I+R9 | -52073333.260 | 104196353.820 |
| Q.YEAST+I+R9 | -52159354.690 | 104368396.680 |
| LG+I+G4 | -52220624.870 | 104490778.125 |
| LG+G4 | -52258503.220 | 104566524.231 |
| JTT+F+I+R9 | -52270523.560 | 104590935.712 |
| JTT+I+R9 | -52339959.200 | 104729605.700 |
| PMB+F+I+R9 | -52463384.460 | 104976657.512 |
| CPREV+F+I+R9 | -52490070.880 | 105030030.352 |
| DCMUT+F+I+R9 | -52492485.070 | 105034858.732 |
| Q.PLANT+F+I+R9 | -52515246.190 | 105080380.972 |
| PMB+I+R9 | -52604946.080 | 105259579.460 |
| Q.PLANT+I+R9 | -52625324.190 | 105300335.680 |
| DCMUT+I+R9 | -52699743.920 | 105449175.140 |
| CPREV+I+R9 | -52724966.540 | 105499620.380 |
| MTINV+F+I+R9 | -52835167.060 | 105720222.712 |
| Q.MAMMAL+I+R9 | -53129182.550 | 106308052.400 |
| Q.MAMMAL+F+I+R9 | -53165255.680 | 106380399.952 |
| MTMET+F+I+R9 | -53411857.490 | 106873603.572 |
| Q.BIRD+I+R9 | -53716982.470 | 107483652.240 |
| Q.BIRD+F+I+R9 | -53757184.330 | 107564257.252 |
| MTVER+F+I+R9 | -54397136.540 | 108844161.672 |
| MTMET+I+R9 | -55912877.910 | 111875443.120 |
| MTINV+I+R9 | -55958335.330 | 111966357.960 |
| MTVER+I+R9 | -56434539.330 | 112918765.960 |
| LG+I | -56748816.760 | 113547151.311 |
| LG | -57076204.030 | 114201915.257 |
The inferred model Q.p__Planctomycetota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Planctomycetota_2+I+R9 | LG+F+I+R9 |
| BIC | 102984173.44 | 103370417.552 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loop_1/tree_update/Q.p__Planctomycetota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 7123.00 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Planctomycetota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 94  
Normalized RF distance: 0.0201  
Tree 1 branch length: 484.53064  
Tree 2 branch length: 499.27735  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -51543624.225 | -51907758.629 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Planctomycetota_2):  
Pearson's correlation: 0.9644326662880082  
Euclidean distance: 0.631129234900584  
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
Total time usage: 1283817.62 seconds (356.62 h)  
