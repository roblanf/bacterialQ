## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Caldisericota  
  Taxa name: p__Caldisericota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 49  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Caldisericota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 49  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Caldisericota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Caldisericota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Caldisericota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Thermotogota as the outgroup for Phylum Caldisericota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Caldisericota/ref_tree.tre -l 15 -u 49 -o ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/subtrees -m split
```
  
Original number of taxa: 49   
Number of pruned subtrees: 1   
Number of taxa after pruning: 49   
Pruned node IDs (degree): 1 (49)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/subtree_update/Q.p__Caldisericota
```
  
  Runtime: 1686.16 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Caldisericota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 71 |
| LG | 27 |
| Q.INSECT | 16 |
| Q.PLANT | 3 |
| Q.PFAM | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/subtree_update/Q.p__Caldisericota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/subtree_update/Q.p__Caldisericota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/model_update/Q.p__Caldisericota
```
  
  Runtime: 4673.10 seconds  
[Model update log](loop_1/model_update/Q.p__Caldisericota.iqtree)  
BIC of the new model: 2584649.5203  
Likelihood of the new model: -1242549.6342  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Caldisericota_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,Q.p__Caldisericota_1  
![Model bubble plot](loop_1/Q.p__Caldisericota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9736508108113316  
Euclidean distance: 0.4618365956335315  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Caldisericota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Caldisericota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/tree_update/Q.p__Caldisericota_1.treefile
```
  
  Runtime: 242.69 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/tree_update/Q.p__Caldisericota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Caldisericota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Caldisericota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/tree_update/Q.p__Caldisericota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Caldisericota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0652  
Tree 1 branch length: 9.6693  
Tree 2 branch length: 12.61016  
Time usage for Loop_1: 6639.93 seconds (1.84 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/tree_update/Q.p__Caldisericota_1.treefile -l 15 -u 49 -o ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/subtrees -m split
```
  
Original number of taxa: 49   
Number of pruned subtrees: 1   
Number of taxa after pruning: 49   
Pruned node IDs (degree): 1 (49)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,Q.p__Caldisericota_1 -mdef ../Result_nova/phylum_models/Q.p__Caldisericota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/subtree_update/Q.p__Caldisericota
```
  
  Runtime: 1416.54 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Caldisericota.iqtree)  
Best models for iteration 2:  
Q.p__Caldisericota_1  

| Model | Count |
|-------|-------|
| Q.p__Caldisericota_1 | 110 |
| LG | 5 |
| Q.INSECT | 3 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/subtree_update/Q.p__Caldisericota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/subtree_update/Q.p__Caldisericota.treefile --model-joint GTR20+FO --init-model Q.p__Caldisericota_1 -mdef ../Result_nova/phylum_models/Q.p__Caldisericota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/model_update/Q.p__Caldisericota
```
  
  Runtime: 3625.71 seconds  
[Model update log](loop_2/model_update/Q.p__Caldisericota.iqtree)  
BIC of the new model: 2583562.6261  
Likelihood of the new model: -1242006.1871  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Caldisericota_2)  
Model set for next iteration: LG,Q.INSECT,Q.YEAST,Q.p__Caldisericota_2  
![Model bubble plot](loop_2/Q.p__Caldisericota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9995627998923104  
Euclidean distance: 0.06012343727584545  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Caldisericota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/tree_update/Q.p__Caldisericota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Caldisericota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 233.73 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Caldisericota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Caldisericota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Caldisericota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Caldisericota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0652  
Tree 1 branch length: 9.6693  
Tree 2 branch length: 12.63018  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Caldisericota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Caldisericota/inferred_models
```
  
  Error:
Loading required package: ggplot2
Error in as.data.frame.default(x[[i]], optional = TRUE) : 
  cannot coerce class ‘"formula"’ to a data.frame
Calls: generate_pca_output ... <Anonymous> -> as.data.frame -> as.data.frame.default
Execution halted
  
  Exit code: 1  
Loading required package: ggplot2
Error in as.data.frame.default(x[[i]], optional = TRUE) : 
  cannot coerce class ‘"formula"’ to a data.frame
Calls: generate_pca_output ... <Anonymous> -> as.data.frame -> as.data.frame.default
Execution halted
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Caldisericota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Caldisericota_1,Q.p__Caldisericota_2 -mdef ../Result_nova/phylum_models/Q.p__Caldisericota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Caldisericota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 6942.34 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Caldisericota_2+R7 | -1262876.566 | 2526887.396 |
| Q.p__Caldisericota_1+R7 | -1262884.585 | 2526903.434 |
| Q.p__Caldisericota_2+F+R7 | -1265579.706 | 2532495.088 |
| Q.p__Caldisericota_1+F+R7 | -1265647.159 | 2532629.994 |
| LG+F+R7 | -1267449.300 | 2536234.276 |
| Q.PFAM+F+R7 | -1268355.535 | 2538046.746 |
| Q.YEAST+R7 | -1269192.504 | 2539519.272 |
| Q.YEAST+F+R7 | -1269722.675 | 2540781.026 |
| Q.INSECT+R7 | -1271342.122 | 2543818.508 |
| LG+R7 | -1271421.978 | 2543978.220 |
| LG+I+R7 | -1271422.266 | 2543989.397 |
| LG+I+R6 | -1271433.616 | 2543990.896 |
| LG+R8 | -1271421.453 | 2543998.372 |
| LG+I+R8 | -1271420.666 | 2544007.398 |
| LG+R6 | -1271466.534 | 2544046.131 |
| LG+I+R5 | -1271495.778 | 2544094.019 |
| LG+R5 | -1271561.491 | 2544214.844 |
| Q.INSECT+F+R7 | -1271688.276 | 2544712.228 |
| LG+I+G4 | -1272667.057 | 2546362.372 |
| WAG+F+R7 | -1272638.491 | 2546612.658 |
| LG+G4 | -1273633.130 | 2548283.918 |
| Q.PFAM+R7 | -1273667.243 | 2548468.750 |
| JTT+F+R7 | -1275173.863 | 2551683.402 |
| Q.PLANT+F+R7 | -1276427.206 | 2554190.088 |
| CPREV+F+R7 | -1277605.055 | 2556545.786 |
| Q.PLANT+R7 | -1278859.612 | 2558853.488 |
| CPREV+R7 | -1279271.267 | 2559676.798 |
| MTINV+F+R7 | -1279280.690 | 2559897.056 |
| WAG+R7 | -1280046.132 | 2561226.528 |
| JTT+R7 | -1282121.544 | 2565377.352 |
| DCMUT+F+R7 | -1282889.369 | 2567114.414 |
| PMB+F+R7 | -1283476.270 | 2568288.216 |
| Q.MAMMAL+F+R7 | -1285182.747 | 2571701.170 |
| MTMET+F+R7 | -1285966.092 | 2573267.860 |
| PMB+R7 | -1290201.285 | 2581536.834 |
| Q.BIRD+F+R7 | -1292552.317 | 2586440.310 |
| Q.MAMMAL+R7 | -1294009.486 | 2589153.236 |
| DCMUT+R7 | -1295355.311 | 2591844.886 |
| Q.BIRD+R7 | -1300239.111 | 2601612.486 |
| MTVER+F+R7 | -1304129.994 | 2609595.664 |
| LG+I | -1316859.001 | 2634735.660 |
| MTMET+R7 | -1333881.932 | 2668898.128 |
| MTINV+R7 | -1337675.205 | 2676484.674 |
| LG | -1346180.770 | 2693368.597 |
| MTVER+R7 | -1352696.245 | 2706526.754 |
The inferred model Q.p__Caldisericota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Caldisericota_2+R7 | LG+F+R7 |
| BIC | 2526887.396 | 2536234.276 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Caldisericota/loop_1/tree_update/Q.p__Caldisericota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Caldisericota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 170.03 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Caldisericota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Caldisericota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Caldisericota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Caldisericota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 11.83737  
Tree 2 branch length: 12.63018  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1335066.759 | -1344514.178 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Caldisericota_2):  
Pearson's correlation: 0.9653861660415188  
Euclidean distance: 0.5464036214335474  
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
Total time usage: 19194.35 seconds (5.33 h)  
