## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Chloroflexota  
  Taxa name: p__Chloroflexota  
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
Discarded 1 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Chloroflexota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 2746  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Chloroflexota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Chloroflexota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Chloroflexota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Chloroflexota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Chloroflexota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/subtrees -m split
```
  
Original number of taxa: 2746   
Number of pruned subtrees: 29   
Number of taxa after pruning: 2644   
Pruned node IDs (degree): 2541 (206) 218 (198) 514 (184) 1131 (182) 1734 (178) 1382 (176) 1564 (171) 963 (159) 2310 (148) 2 (138) 852 (112) 697 (97) 1911 (96) 2081 (86) 142 (76) 2166 (59) 2224 (46) 1319 (45) 2499 (43) 417 (41) 2269 (38) 2468 (32) 2023 (28) 469 (25) 2006 (18) 827 (16) 498 (16) 798 (15) 2054 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 29 subtree files and 119 loci files. Total number of potential alignments: 3451.  
Sub-sampling 2000 alignments from 3451 alignments.  
Remaining 2000 alignments. Deleted 44 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/subtree_update/Q.p__Chloroflexota
```
  
  Runtime: 57552.27 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Chloroflexota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 564 |
| Q.PFAM | 506 |
| Q.PLANT | 387 |
| Q.INSECT | 373 |
| Q.YEAST | 168 |
| MTMET | 1 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/subtree_update/Q.p__Chloroflexota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/subtree_update/Q.p__Chloroflexota.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/model_update/Q.p__Chloroflexota
```
  
  Runtime: 131901.68 seconds  
[Model update log](loop_1/model_update/Q.p__Chloroflexota.iqtree)  
BIC of the new model: 68034750.6476  
Likelihood of the new model: -31981226.0347  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Chloroflexota_1)  
Model set for next iteration: LG,Q.PFAM,Q.PLANT,Q.INSECT,Q.YEAST,Q.p__Chloroflexota_1  
![Model bubble plot](loop_1/Q.p__Chloroflexota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9666466364828631  
Euclidean distance: 0.5838844774682637  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Chloroflexota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Chloroflexota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/tree_update/Q.p__Chloroflexota_1.treefile
```
  
  Runtime: 15765.44 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/tree_update/Q.p__Chloroflexota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/tree_update/Q.p__Chloroflexota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 752  
Normalized RF distance: 0.1371  
Tree 1 branch length: 403.00471  
Tree 2 branch length: 505.46746  
Time usage for Loop_1: 207201.14 seconds (57.56 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/tree_update/Q.p__Chloroflexota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/subtrees -m split
```
  
Original number of taxa: 2746   
Number of pruned subtrees: 30   
Number of taxa after pruning: 2641   
Pruned node IDs (degree): 2541 (206) 1093 (198) 892 (183) 379 (182) 1737 (178) 1385 (176) 1567 (171) 714 (166) 2 (138) 2310 (134) 601 (114) 281 (99) 1914 (96) 2084 (86) 142 (76) 2215 (59) 2169 (47) 1303 (45) 2499 (43) 2273 (38) 2443 (32) 2026 (28) 2474 (26) 232 (23) 2009 (18) 1364 (17) 265 (16) 585 (16) 1078 (15) 2057 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 30 subtree files and 119 loci files. Total number of potential alignments: 3570.  
Sub-sampling 2000 alignments from 3570 alignments.  
Remaining 2000 alignments. Deleted 40 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.PLANT,Q.INSECT,Q.YEAST,Q.p__Chloroflexota_1 -mdef ../Result_nova/phylum_models/Q.p__Chloroflexota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/subtree_update/Q.p__Chloroflexota
```
  
  Runtime: 64301.73 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Chloroflexota.iqtree)  
Best models for iteration 2:  
Q.p__Chloroflexota_1  

| Model | Count |
|-------|-------|
| Q.p__Chloroflexota_1 | 1570 |
| Q.PLANT | 157 |
| Q.PFAM | 73 |
| LG | 70 |
| Q.INSECT | 69 |
| Q.YEAST | 61 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/subtree_update/Q.p__Chloroflexota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/subtree_update/Q.p__Chloroflexota.treefile --model-joint GTR20+FO --init-model Q.p__Chloroflexota_1 -mdef ../Result_nova/phylum_models/Q.p__Chloroflexota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/model_update/Q.p__Chloroflexota
```
  
  Runtime: 97668.30 seconds  
[Model update log](loop_2/model_update/Q.p__Chloroflexota.iqtree)  
BIC of the new model: 66265454.6421  
Likelihood of the new model: -31168140.7137  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Chloroflexota_2)  
Model set for next iteration: Q.PLANT,Q.PFAM,LG,Q.INSECT,Q.YEAST,Q.p__Chloroflexota_2  
![Model bubble plot](loop_2/Q.p__Chloroflexota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999405408990656  
Euclidean distance: 0.02293776694578519  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/tree_update/Q.p__Chloroflexota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Chloroflexota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 7289.37 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Chloroflexota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 762  
Normalized RF distance: 0.1389  
Tree 1 branch length: 403.00471  
Tree 2 branch length: 506.03156  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Chloroflexota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Chloroflexota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Chloroflexota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Chloroflexota_1,Q.p__Chloroflexota_2 -mdef ../Result_nova/phylum_models/Q.p__Chloroflexota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Chloroflexota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 974742.96 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Chloroflexota_1+I+R8 | -56353914.930 | 112766246.249 |
| Q.p__Chloroflexota_2+I+R8 | -56356072.480 | 112770561.349 |
| Q.p__Chloroflexota_1+F+I+R8 | -56439023.540 | 112936665.124 |
| Q.p__Chloroflexota_2+F+I+R8 | -56440516.980 | 112939652.004 |
| LG+F+I+R8 | -56547037.320 | 113152692.684 |
| Q.PFAM+F+I+R8 | -56565928.500 | 113190475.044 |
| Q.YEAST+F+I+R8 | -56618109.810 | 113294837.664 |
| Q.PFAM+I+R8 | -56646263.090 | 113350942.569 |
| Q.INSECT+F+I+R8 | -56662737.160 | 113384092.364 |
| LG+I+R8 | -56764041.680 | 113586499.749 |
| LG+R8 | -56770329.470 | 113599064.715 |
| LG+I+R7 | -56801761.490 | 113661918.142 |
| LG+R7 | -56810094.050 | 113678572.648 |
| WAG+F+I+R8 | -56817421.890 | 113693461.824 |
| LG+I+R6 | -56860035.080 | 113778444.095 |
| LG+R6 | -56871526.890 | 113801417.101 |
| Q.INSECT+I+R8 | -56917125.480 | 113892667.349 |
| LG+I+R5 | -56950824.210 | 113960001.128 |
| LG+R5 | -56968379.310 | 113995100.714 |
| JTT+F+I+R8 | -56994354.560 | 114047327.164 |
| WAG+I+R8 | -56999870.710 | 114058157.809 |
| Q.YEAST+I+R8 | -57055874.870 | 114170166.129 |
| JTT+I+R8 | -57094576.330 | 114247569.049 |
| Q.PLANT+F+I+R8 | -57142973.460 | 114344564.964 |
| LG+I+G4 | -57145391.910 | 114349062.234 |
| LG+G4 | -57183871.530 | 114426010.860 |
| Q.PLANT+I+R8 | -57290796.260 | 114640008.909 |
| CPREV+F+I+R8 | -57319897.460 | 114698412.964 |
| DCMUT+F+I+R8 | -57328846.110 | 114716310.264 |
| PMB+F+I+R8 | -57559410.210 | 115177438.464 |
| CPREV+I+R8 | -57608331.100 | 115275078.589 |
| MTINV+F+I+R8 | -57622938.160 | 115304494.364 |
| DCMUT+I+R8 | -57631848.770 | 115322113.929 |
| PMB+I+R8 | -57748157.140 | 115554730.669 |
| Q.MAMMAL+I+R8 | -57802324.970 | 115663066.329 |
| Q.MAMMAL+F+I+R8 | -57805323.160 | 115669264.364 |
| MTMET+F+I+R8 | -58134167.330 | 116326952.704 |
| Q.BIRD+I+R8 | -58352478.780 | 116763373.949 |
| Q.BIRD+F+I+R8 | -58365519.310 | 116789656.664 |
| MTVER+F+I+R8 | -59048222.410 | 118155062.864 |
| MTMET+I+R8 | -60662246.060 | 121382908.509 |
| MTINV+I+R8 | -60853613.340 | 121765643.069 |
| MTVER+I+R8 | -61076003.900 | 122210424.189 |
| LG+I | -61979801.350 | 124017870.500 |
| LG | -62293274.480 | 124644806.147 |
The inferred model Q.p__Chloroflexota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Chloroflexota_1+I+R8 | LG+F+I+R8 |
| BIC | 112766246.249 | 113152692.684 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Chloroflexota/loop_1/tree_update/Q.p__Chloroflexota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Chloroflexota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 11816.73 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Chloroflexota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Chloroflexota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 68  
Normalized RF distance: 0.0124  
Tree 1 branch length: 486.16301  
Tree 2 branch length: 506.03156  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -56355013.898 | -56763149.757 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Chloroflexota_2):  
Pearson's correlation: 0.9671386304602367  
Euclidean distance: 0.5814990551124227  
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
Total time usage: 1366004.41 seconds (379.45 h)  
