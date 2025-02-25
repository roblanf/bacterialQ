## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Deinococcota  
  Taxa name: p__Deinococcota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 211  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 3 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Deinococcota/select_id.txt. Sampling sequences for 117 loci.  
Number of input species: 211  
Remaining 117 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Deinococcota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Deinococcota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Deinococcota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Bipolaricaulota as the outgroup for Phylum Deinococcota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Deinococcota/ref_tree.tre -l 15 -u 211 -o ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/subtrees -m split
```
  
Original number of taxa: 211   
Number of pruned subtrees: 1   
Number of taxa after pruning: 211   
Pruned node IDs (degree): 1 (211)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 117 loci files. Total number of potential alignments: 117.  
Obtained 117 alignments from all potential alignments.  
Remaining 117 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/subtree_update/Q.p__Deinococcota
```
  
  Runtime: 47959.33 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Deinococcota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 32 |
| Q.INSECT | 31 |
| Q.PFAM | 31 |
| Q.YEAST | 22 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/subtree_update/Q.p__Deinococcota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/subtree_update/Q.p__Deinococcota.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/model_update/Q.p__Deinococcota
```
  
  Runtime: 51093.52 seconds  
[Model update log](loop_1/model_update/Q.p__Deinococcota.iqtree)  
BIC of the new model: 6870252.0968  
Likelihood of the new model: -3192979.0728  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Deinococcota_1)  
Model set for next iteration: LG,Q.INSECT,Q.PFAM,Q.YEAST,Q.p__Deinococcota_1  
![Model bubble plot](loop_1/Q.p__Deinococcota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.937312729764107  
Euclidean distance: 0.9641776895561511  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Deinococcota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Deinococcota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/tree_update/Q.p__Deinococcota_1.treefile
```
  
  Runtime: 1169.42 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/tree_update/Q.p__Deinococcota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Deinococcota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Deinococcota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/tree_update/Q.p__Deinococcota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Deinococcota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 32  
Normalized RF distance: 0.0769  
Tree 1 branch length: 19.29548  
Tree 2 branch length: 25.55831  
Time usage for Loop_1: 100265.31 seconds (27.85 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/tree_update/Q.p__Deinococcota_1.treefile -l 15 -u 211 -o ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/subtrees -m split
```
  
Original number of taxa: 211   
Number of pruned subtrees: 1   
Number of taxa after pruning: 211   
Pruned node IDs (degree): 1 (211)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 117 loci files. Total number of potential alignments: 117.  
Obtained 117 alignments from all potential alignments.  
Remaining 117 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/training_loci -m MFP -mset LG,Q.INSECT,Q.PFAM,Q.YEAST,Q.p__Deinococcota_1 -mdef ../Result_nova/phylum_models/Q.p__Deinococcota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/subtree_update/Q.p__Deinococcota
```
  
  Runtime: 22871.42 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Deinococcota.iqtree)  
Best models for iteration 2:  
Q.p__Deinococcota_1  

| Model | Count |
|-------|-------|
| Q.p__Deinococcota_1 | 103 |
| Q.INSECT | 6 |
| LG | 4 |
| Q.PFAM | 3 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/subtree_update/Q.p__Deinococcota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/subtree_update/Q.p__Deinococcota.treefile --model-joint GTR20+FO --init-model Q.p__Deinococcota_1 -mdef ../Result_nova/phylum_models/Q.p__Deinococcota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/model_update/Q.p__Deinococcota
```
  
  Runtime: 42749.87 seconds  
[Model update log](loop_2/model_update/Q.p__Deinococcota.iqtree)  
BIC of the new model: 6864447.3342  
Likelihood of the new model: -3190076.6914  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Deinococcota_2)  
Model set for next iteration: Q.INSECT,LG,Q.PFAM,Q.p__Deinococcota_2  
![Model bubble plot](loop_2/Q.p__Deinococcota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998858656233082  
Euclidean distance: 0.06125931293444552  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Deinococcota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/tree_update/Q.p__Deinococcota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Deinococcota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 889.51 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Deinococcota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Deinococcota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Deinococcota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Deinococcota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 32  
Normalized RF distance: 0.0769  
Tree 1 branch length: 19.29548  
Tree 2 branch length: 25.60557  
### Model comparison  
Comparison between initial best model (LG) and final model (Q.p__Deinococcota_2):  
Pearson's correlation: 0.9353839441941812  
Euclidean distance: 1.010292761920314  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Deinococcota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Deinococcota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Deinococcota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Deinococcota_1,Q.p__Deinococcota_2 -mdef ../Result_nova/phylum_models/Q.p__Deinococcota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Deinococcota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 21365.83 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Deinococcota_1+I+R8 | -3278781.087 | 6562153.440 |
| Q.p__Deinococcota_2+I+R8 | -3278833.362 | 6562257.990 |
| Q.p__Deinococcota_1+F+I+R8 | -3289248.256 | 6583288.778 |
| Q.p__Deinococcota_2+F+I+R8 | -3290277.965 | 6585348.196 |
| LG+F+I+R8 | -3299948.345 | 6604688.956 |
| Q.PFAM+F+I+R8 | -3301624.232 | 6608040.730 |
| Q.YEAST+F+I+R8 | -3303020.233 | 6610832.732 |
| Q.INSECT+F+I+R8 | -3307038.793 | 6618869.852 |
| WAG+F+I+R8 | -3317912.009 | 6640616.284 |
| Q.PFAM+I+R8 | -3318431.451 | 6641454.168 |
| LG+I+R8 | -3327371.470 | 6659334.206 |
| LG+R8 | -3327473.605 | 6659527.897 |
| LG+I+R7 | -3327723.107 | 6660016.322 |
| LG+R7 | -3328058.683 | 6660676.895 |
| LG+I+R6 | -3328549.806 | 6661648.562 |
| LG+R6 | -3329456.309 | 6663450.989 |
| LG+I+R5 | -3330589.375 | 6665706.542 |
| LG+R5 | -3332531.329 | 6669579.872 |
| JTT+F+I+R8 | -3333118.468 | 6671029.202 |
| LG+I+G4 | -3337726.763 | 6679907.266 |
| WAG+I+R8 | -3338672.069 | 6681935.404 |
| Q.INSECT+I+R8 | -3344754.308 | 6694099.882 |
| LG+G4 | -3344859.691 | 6694162.543 |
| DCMUT+F+I+R8 | -3347238.388 | 6699269.042 |
| Q.PLANT+F+I+R8 | -3348247.508 | 6701287.282 |
| JTT+I+R8 | -3350159.120 | 6704909.506 |
| CPREV+F+I+R8 | -3350466.399 | 6705725.064 |
| Q.YEAST+I+R8 | -3352709.102 | 6710009.470 |
| PMB+F+I+R8 | -3355530.549 | 6715853.364 |
| Q.PLANT+I+R8 | -3372584.852 | 6749760.970 |
| DCMUT+I+R8 | -3374962.136 | 6754515.538 |
| PMB+I+R8 | -3379071.193 | 6762733.652 |
| CPREV+I+R8 | -3383408.199 | 6771407.664 |
| MTINV+F+I+R8 | -3385463.143 | 6775718.552 |
| Q.MAMMAL+F+I+R8 | -3386607.214 | 6778006.694 |
| Q.MAMMAL+I+R8 | -3396706.312 | 6798003.890 |
| MTMET+F+I+R8 | -3421074.843 | 6846941.952 |
| Q.BIRD+F+I+R8 | -3423615.187 | 6852022.640 |
| Q.BIRD+I+R8 | -3434085.503 | 6872762.272 |
| MTVER+F+I+R8 | -3481584.882 | 6967962.030 |
| LG+I | -3576780.350 | 7158003.861 |
| MTMET+I+R8 | -3614789.970 | 7234171.206 |
| MTINV+I+R8 | -3623668.609 | 7251928.484 |
| MTVER+I+R8 | -3638345.574 | 7281282.414 |
| LG | -3687014.351 | 7378461.284 |
The inferred model Q.p__Deinococcota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Deinococcota_1+I+R8 | LG+F+I+R8 |
| BIC | 6562153.44 | 6604688.956 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Deinococcota/loop_1/tree_update/Q.p__Deinococcota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Deinococcota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 852.03 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Deinococcota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Deinococcota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Deinococcota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Deinococcota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0144  
Tree 1 branch length: 25.42482  
Tree 2 branch length: 25.60557  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -3350753.694 | -3397904.292 |
The final model tree has better likelihood than the existing model tree.  
### Pairwise comparison of trees  
![Heatmap of RF distance of trees:](estimated_tree/RF_heatmap.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_heatmap.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 189182.36 seconds (52.55 h)  
