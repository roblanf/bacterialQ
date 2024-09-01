## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Zixibacteria  
  Taxa name: p__Zixibacteria  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 133  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Zixibacteria/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 133  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Zixibacteria  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Zixibacteria -d 0.1 -o ../Result_nova/phylum_models/Q.p__Zixibacteria/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Eisenbacteria as the outgroup for Phylum Zixibacteria
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Zixibacteria/ref_tree.tre -l 15 -u 133 -o ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/subtrees -m split
```
  
Original number of taxa: 133   
Number of pruned subtrees: 1   
Number of taxa after pruning: 133   
Pruned node IDs (degree): 1 (133)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/subtree_update/Q.p__Zixibacteria
```
  
  Runtime: 20265.38 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Zixibacteria.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 44 |
| Q.INSECT | 43 |
| Q.YEAST | 18 |
| Q.PFAM | 12 |
| Q.PLANT | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/subtree_update/Q.p__Zixibacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/subtree_update/Q.p__Zixibacteria.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/model_update/Q.p__Zixibacteria
```
  
  Runtime: 28029.30 seconds  
[Model update log](loop_1/model_update/Q.p__Zixibacteria.iqtree)  
BIC of the new model: 7210286.8422  
Likelihood of the new model: -3462405.1892  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Zixibacteria_1)  
Model set for next iteration: LG,Q.INSECT,Q.YEAST,Q.PFAM,Q.p__Zixibacteria_1  
![Model bubble plot](loop_1/Q.p__Zixibacteria_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9817548428868198  
Euclidean distance: 0.46754217850125146  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Zixibacteria/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Zixibacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/tree_update/Q.p__Zixibacteria_1.treefile
```
  
  Runtime: 795.70 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/tree_update/Q.p__Zixibacteria_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/tree_update/Q.p__Zixibacteria_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 34  
Normalized RF distance: 0.1308  
Tree 1 branch length: 25.51771  
Tree 2 branch length: 33.98392  
Time usage for Loop_1: 49134.91 seconds (13.65 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/tree_update/Q.p__Zixibacteria_1.treefile -l 15 -u 133 -o ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/subtrees -m split
```
  
Original number of taxa: 133   
Number of pruned subtrees: 1   
Number of taxa after pruning: 133   
Pruned node IDs (degree): 1 (133)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/training_loci -m MFP -mset LG,Q.INSECT,Q.YEAST,Q.PFAM,Q.p__Zixibacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Zixibacteria/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/subtree_update/Q.p__Zixibacteria
```
  
  Runtime: 12802.87 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Zixibacteria.iqtree)  
Best models for iteration 2:  
Q.p__Zixibacteria_1  

| Model | Count |
|-------|-------|
| Q.p__Zixibacteria_1 | 108 |
| Q.INSECT | 5 |
| LG | 4 |
| Q.PFAM | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/subtree_update/Q.p__Zixibacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/subtree_update/Q.p__Zixibacteria.treefile --model-joint GTR20+FO --init-model Q.p__Zixibacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Zixibacteria/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/model_update/Q.p__Zixibacteria
```
  
  Runtime: 21182.94 seconds  
[Model update log](loop_2/model_update/Q.p__Zixibacteria.iqtree)  
BIC of the new model: 7208691.0142  
Likelihood of the new model: -3461607.2752  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Zixibacteria_2)  
Model set for next iteration: Q.INSECT,LG,Q.PFAM,Q.p__Zixibacteria_2  
![Model bubble plot](loop_2/Q.p__Zixibacteria_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999900211519493  
Euclidean distance: 0.03451958129425977  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/tree_update/Q.p__Zixibacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Zixibacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 567.42 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Zixibacteria', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 34  
Normalized RF distance: 0.1308  
Tree 1 branch length: 25.51771  
Tree 2 branch length: 34.04193  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Zixibacteria/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Zixibacteria/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Zixibacteria/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Zixibacteria_1,Q.p__Zixibacteria_2 -mdef ../Result_nova/phylum_models/Q.p__Zixibacteria/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Zixibacteria/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 18649.98 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Zixibacteria_1+I+R9 | -3508798.060 | 7020566.628 |
| Q.p__Zixibacteria_2+I+R9 | -3508807.855 | 7020586.218 |
| Q.p__Zixibacteria_1+F+I+R9 | -3516537.296 | 7036246.671 |
| Q.p__Zixibacteria_2+F+I+R9 | -3516862.245 | 7036896.569 |
| LG+F+I+R9 | -3520117.818 | 7043407.715 |
| LG+I+R9 | -3522547.796 | 7048066.100 |
| LG+R9 | -3522658.616 | 7048277.131 |
| LG+I+R8 | -3522708.204 | 7048365.698 |
| LG+R8 | -3522857.605 | 7048653.891 |
| LG+I+R7 | -3523113.246 | 7049154.565 |
| LG+R7 | -3523393.725 | 7049704.914 |
| LG+I+R6 | -3523937.730 | 7050782.315 |
| Q.YEAST+F+I+R9 | -3524219.151 | 7051610.381 |
| LG+R6 | -3524557.258 | 7052010.762 |
| Q.PFAM+F+I+R9 | -3524485.436 | 7052142.951 |
| Q.YEAST+I+R9 | -3526041.520 | 7055053.548 |
| Q.PFAM+I+R9 | -3526223.120 | 7055416.748 |
| Q.INSECT+I+R9 | -3526422.540 | 7055815.588 |
| Q.INSECT+F+I+R9 | -3530641.503 | 7064455.085 |
| LG+I+G4 | -3532003.123 | 7066817.620 |
| LG+G4 | -3539676.610 | 7082153.985 |
| WAG+F+I+R9 | -3542578.166 | 7088328.411 |
| WAG+I+R9 | -3548835.348 | 7100641.204 |
| Q.PLANT+I+R9 | -3549005.099 | 7100980.706 |
| Q.PLANT+F+I+R9 | -3552079.126 | 7107330.331 |
| JTT+F+I+R9 | -3553273.044 | 7109718.167 |
| JTT+I+R9 | -3557744.137 | 7118458.782 |
| CPREV+I+R9 | -3564985.307 | 7132941.122 |
| CPREV+F+I+R9 | -3567321.497 | 7137815.073 |
| DCMUT+F+I+R9 | -3573346.996 | 7149866.071 |
| MTINV+F+I+R9 | -3578578.701 | 7160329.481 |
| PMB+F+I+R9 | -3587952.147 | 7179076.373 |
| DCMUT+I+R9 | -3588320.069 | 7179610.646 |
| PMB+I+R9 | -3594303.258 | 7191577.024 |
| Q.MAMMAL+F+I+R9 | -3594443.187 | 7192058.453 |
| Q.MAMMAL+I+R9 | -3596360.173 | 7195690.854 |
| MTMET+F+I+R9 | -3605094.304 | 7213360.687 |
| Q.BIRD+F+I+R9 | -3621629.300 | 7246430.679 |
| Q.BIRD+I+R9 | -3623075.381 | 7249121.270 |
| MTVER+F+I+R9 | -3663975.288 | 7331122.655 |
| MTMET+I+R9 | -3747069.816 | 7497110.140 |
| MTINV+I+R9 | -3756755.284 | 7516481.076 |
| LG+I | -3778854.734 | 7560510.233 |
| MTVER+I+R9 | -3788587.616 | 7580145.740 |
| LG | -3891125.954 | 7785042.064 |
The inferred model Q.p__Zixibacteria_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Zixibacteria_1+I+R9 | LG+F+I+R9 |
| BIC | 7020566.628 | 7043407.715 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Zixibacteria/loop_1/tree_update/Q.p__Zixibacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Zixibacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 460.94 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Zixibacteria/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Zixibacteria/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0077  
Tree 1 branch length: 31.72694  
Tree 2 branch length: 34.04193  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -3572727.482 | -3586200.718 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Zixibacteria_2):  
Pearson's correlation: 0.9806079391748546  
Euclidean distance: 0.4885375901010486  
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
Total time usage: 102999.25 seconds (28.61 h)  
