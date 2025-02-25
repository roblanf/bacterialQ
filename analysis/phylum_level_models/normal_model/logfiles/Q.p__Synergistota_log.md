## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Synergistota  
  Taxa name: p__Synergistota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 208  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Synergistota/select_id.txt. Sampling sequences for 118 loci.  
Number of input species: 208  
Remaining 118 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Synergistota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Synergistota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Synergistota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Synergistota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Synergistota/ref_tree.tre -l 15 -u 208 -o ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/subtrees -m split
```
  
Original number of taxa: 208   
Number of pruned subtrees: 1   
Number of taxa after pruning: 208   
Pruned node IDs (degree): 1 (208)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/subtree_update/Q.p__Synergistota
```
  
  Runtime: 21531.98 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Synergistota.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| Q.INSECT | 51 |
| Q.PFAM | 26 |
| Q.YEAST | 16 |
| LG | 15 |
| Q.PLANT | 10 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/subtree_update/Q.p__Synergistota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/subtree_update/Q.p__Synergistota.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/model_update/Q.p__Synergistota
```
  
  Runtime: 31352.18 seconds  
[Model update log](loop_1/model_update/Q.p__Synergistota.iqtree)  
BIC of the new model: 8992005.6013  
Likelihood of the new model: -4268054.6658  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Synergistota_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,Q.YEAST,LG,Q.PLANT,Q.p__Synergistota_1  
![Model bubble plot](loop_1/Q.p__Synergistota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Synergistota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9710938506749592  
Euclidean distance: 0.5001860851970924  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Synergistota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Synergistota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/tree_update/Q.p__Synergistota_1.treefile
```
  
  Runtime: 1332.89 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/tree_update/Q.p__Synergistota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Synergistota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Synergistota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Synergistota/loop_1/tree_update/Q.p__Synergistota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Synergistota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Synergistota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 38  
Normalized RF distance: 0.0927  
Tree 1 branch length: 27.96226  
Tree 2 branch length: 40.1495  
Time usage for Loop_1: 54260.75 seconds (15.07 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/tree_update/Q.p__Synergistota_1.treefile -l 15 -u 208 -o ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/subtrees -m split
```
  
Original number of taxa: 208   
Number of pruned subtrees: 1   
Number of taxa after pruning: 208   
Pruned node IDs (degree): 1 (208)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,Q.YEAST,LG,Q.PLANT,Q.p__Synergistota_1 -mdef ../Result_nova/phylum_models/Q.p__Synergistota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/subtree_update/Q.p__Synergistota
```
  
  Runtime: 34325.76 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Synergistota.iqtree)  
Best models for iteration 2:  
Q.p__Synergistota_1  

| Model | Count |
|-------|-------|
| Q.p__Synergistota_1 | 109 |
| Q.INSECT | 5 |
| LG | 2 |
| Q.PLANT | 1 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/subtree_update/Q.p__Synergistota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/subtree_update/Q.p__Synergistota.treefile --model-joint GTR20+FO --init-model Q.p__Synergistota_1 -mdef ../Result_nova/phylum_models/Q.p__Synergistota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/model_update/Q.p__Synergistota
```
  
  Runtime: 36456.24 seconds  
[Model update log](loop_2/model_update/Q.p__Synergistota.iqtree)  
BIC of the new model: 8989525.251  
Likelihood of the new model: -4266814.4906  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Synergistota_2)  
Model set for next iteration: Q.INSECT,LG,Q.PLANT,Q.YEAST,Q.p__Synergistota_2  
![Model bubble plot](loop_2/Q.p__Synergistota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Synergistota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999662430286371  
Euclidean distance: 0.021938511736536586  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Synergistota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/tree_update/Q.p__Synergistota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Synergistota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 1157.92 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Synergistota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Synergistota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Synergistota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Synergistota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 38  
Normalized RF distance: 0.0927  
Tree 1 branch length: 27.96226  
Tree 2 branch length: 40.22167  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (Q.p__Synergistota_2):  
Pearson's correlation: 0.9707984432268479  
Euclidean distance: 0.5085347971509019  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Synergistota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Synergistota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Synergistota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Synergistota_1,Q.p__Synergistota_2 -mdef ../Result_nova/phylum_models/Q.p__Synergistota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Synergistota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 36226.43 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Synergistota_1+I+R8 | -4361978.217 | 8728490.186 |
| Q.p__Synergistota_2+I+R8 | -4362013.439 | 8728560.630 |
| Q.p__Synergistota_1+F+I+R8 | -4375801.290 | 8756337.596 |
| Q.p__Synergistota_2+F+I+R8 | -4376306.823 | 8757348.662 |
| LG+F+I+R8 | -4383027.216 | 8770789.448 |
| Q.YEAST+F+I+R8 | -4386427.440 | 8777589.896 |
| Q.PFAM+F+I+R8 | -4386816.013 | 8778367.042 |
| Q.INSECT+F+I+R8 | -4390361.416 | 8785457.848 |
| Q.PFAM+I+R8 | -4392688.172 | 8789910.096 |
| LG+I+R8 | -4393348.356 | 8791230.464 |
| Q.INSECT+I+R8 | -4393480.054 | 8791493.860 |
| LG+R8 | -4393724.707 | 8791972.573 |
| LG+I+R7 | -4394142.176 | 8792796.918 |
| LG+R7 | -4395068.421 | 8794638.815 |
| LG+I+R6 | -4396047.820 | 8796587.020 |
| LG+R6 | -4397507.430 | 8799495.647 |
| Q.YEAST+I+R8 | -4398932.195 | 8802398.142 |
| LG+I+R5 | -4399817.949 | 8804106.092 |
| LG+R5 | -4402767.260 | 8809994.122 |
| WAG+F+I+R8 | -4406625.296 | 8817985.608 |
| JTT+F+I+R8 | -4408478.507 | 8821692.030 |
| LG+I+G4 | -4410098.518 | 8824593.080 |
| Q.PLANT+I+R8 | -4412259.482 | 8829052.716 |
| Q.PLANT+F+I+R8 | -4413154.886 | 8831044.788 |
| JTT+I+R8 | -4416396.669 | 8837327.090 |
| LG+G4 | -4419184.893 | 8842755.237 |
| WAG+I+R8 | -4419808.965 | 8844151.682 |
| CPREV+F+I+R8 | -4426407.349 | 8857549.714 |
| CPREV+I+R8 | -4437542.302 | 8879618.356 |
| MTINV+F+I+R8 | -4445080.474 | 8894895.964 |
| DCMUT+F+I+R8 | -4446204.056 | 8897143.128 |
| Q.MAMMAL+F+I+R8 | -4452442.951 | 8909620.918 |
| Q.MAMMAL+I+R8 | -4453304.563 | 8911142.878 |
| PMB+F+I+R8 | -4458412.026 | 8921559.068 |
| PMB+I+R8 | -4468659.167 | 8941852.086 |
| DCMUT+I+R8 | -4470487.190 | 8945508.132 |
| MTMET+F+I+R8 | -4473131.114 | 8950997.244 |
| Q.BIRD+F+I+R8 | -4486807.295 | 8978349.606 |
| Q.BIRD+I+R8 | -4487337.986 | 8979209.724 |
| MTVER+F+I+R8 | -4544415.852 | 9093566.720 |
| MTMET+I+R8 | -4653245.905 | 9311025.562 |
| MTINV+I+R8 | -4658552.896 | 9321639.544 |
| MTVER+I+R8 | -4717542.200 | 9439618.152 |
| LG+I | -4769213.106 | 9542811.663 |
| LG | -4895997.334 | 9796369.526 |
The inferred model Q.p__Synergistota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Synergistota_1+I+R8 | LG+F+I+R8 |
| BIC | 8728490.186 | 8770789.448 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Synergistota/loop_1/tree_update/Q.p__Synergistota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Synergistota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 896.81 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Synergistota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Synergistota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Synergistota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Synergistota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 38.38101  
Tree 2 branch length: 40.22167  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -4437414.734 | -4468208.558 |
The final model tree has better likelihood than the existing model tree.  
### Pairwise comparison of trees  

![Heatmap of RF distance of trees:](estimated_tree/RF_dist.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_dist.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 163519.27 seconds (45.42 h)  
