## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Margulisbacteria  
  Taxa name: p__Margulisbacteria  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 194  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 5 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Margulisbacteria/select_id.txt. Sampling sequences for 115 loci.  
Number of input species: 87  
Remaining 115 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Margulisbacteria  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Margulisbacteria -d 0.1 -o ../Result_nova/phylum_models/Q.p__Margulisbacteria/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Margulisbacteria
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 117 alignments. Deleted 3 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Margulisbacteria/ref_tree.tre -l 15 -u 194 -o ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/subtrees -m split
```
  
Original number of taxa: 87   
Number of pruned subtrees: 1   
Number of taxa after pruning: 87   
Pruned node IDs (degree): 1 (87)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 115 loci files. Total number of potential alignments: 115.  
Obtained 115 alignments from all potential alignments.  
Remaining 115 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/subtree_update/Q.p__Margulisbacteria
```
  
  Runtime: 8361.72 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Margulisbacteria.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 69 |
| LG | 23 |
| Q.INSECT | 13 |
| Q.PFAM | 10 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/subtree_update/Q.p__Margulisbacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/subtree_update/Q.p__Margulisbacteria.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/model_update/Q.p__Margulisbacteria
```
  
  Runtime: 10015.43 seconds  
[Model update log](loop_1/model_update/Q.p__Margulisbacteria.iqtree)  
BIC of the new model: 5859898.9061  
Likelihood of the new model: -2840624.4589  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Margulisbacteria_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,Q.PFAM,Q.p__Margulisbacteria_1  
![Model bubble plot](loop_1/Q.p__Margulisbacteria_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9858717844212923  
Euclidean distance: 0.3425030357506109  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Margulisbacteria/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Margulisbacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/tree_update/Q.p__Margulisbacteria_1.treefile
```
  
  Runtime: 501.92 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/tree_update/Q.p__Margulisbacteria_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/tree_update/Q.p__Margulisbacteria_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 26  
Normalized RF distance: 0.1548  
Tree 1 branch length: 26.66691  
Tree 2 branch length: 35.368  
Time usage for Loop_1: 18918.65 seconds (5.26 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/tree_update/Q.p__Margulisbacteria_1.treefile -l 15 -u 194 -o ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/subtrees -m split
```
  
Original number of taxa: 87   
Number of pruned subtrees: 1   
Number of taxa after pruning: 87   
Pruned node IDs (degree): 1 (87)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 115 loci files. Total number of potential alignments: 115.  
Obtained 115 alignments from all potential alignments.  
Remaining 115 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,Q.PFAM,Q.p__Margulisbacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Margulisbacteria/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/subtree_update/Q.p__Margulisbacteria
```
  
  Runtime: 8320.49 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Margulisbacteria.iqtree)  
Best models for iteration 2:  
Q.p__Margulisbacteria_1  

| Model | Count |
|-------|-------|
| Q.p__Margulisbacteria_1 | 97 |
| Q.YEAST | 8 |
| LG | 4 |
| Q.INSECT | 4 |
| Q.PFAM | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/subtree_update/Q.p__Margulisbacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/subtree_update/Q.p__Margulisbacteria.treefile --model-joint GTR20+FO --init-model Q.p__Margulisbacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Margulisbacteria/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/model_update/Q.p__Margulisbacteria
```
  
  Runtime: 5103.23 seconds  
[Model update log](loop_2/model_update/Q.p__Margulisbacteria.iqtree)  
BIC of the new model: 5858179.4306  
Likelihood of the new model: -2839764.7212  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Margulisbacteria_2)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,Q.PFAM,Q.p__Margulisbacteria_2  
![Model bubble plot](loop_2/Q.p__Margulisbacteria_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999525794745124  
Euclidean distance: 0.020748469113459  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/tree_update/Q.p__Margulisbacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Margulisbacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 478.90 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Margulisbacteria', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 32  
Normalized RF distance: 0.1905  
Tree 1 branch length: 26.66691  
Tree 2 branch length: 35.43374  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Margulisbacteria/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Margulisbacteria/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Margulisbacteria/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Margulisbacteria_1,Q.p__Margulisbacteria_2 -mdef ../Result_nova/phylum_models/Q.p__Margulisbacteria/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Margulisbacteria/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 8929.26 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Margulisbacteria_2+I+R8 | -2883822.971 | 5769612.964 |
| Q.p__Margulisbacteria_1+I+R8 | -2883833.353 | 5769633.728 |
| Q.p__Margulisbacteria_1+F+I+R8 | -2890854.000 | 5783875.954 |
| Q.YEAST+I+R8 | -2891140.907 | 5784248.836 |
| Q.p__Margulisbacteria_2+F+I+R8 | -2891163.543 | 5784495.040 |
| LG+F+I+R8 | -2893533.614 | 5789235.182 |
| LG+I+R8 | -2894879.853 | 5791726.728 |
| LG+R8 | -2894936.175 | 5791828.796 |
| Q.PFAM+F+I+R8 | -2894834.333 | 5791836.620 |
| LG+I+R7 | -2894984.312 | 5791914.495 |
| LG+R7 | -2895083.349 | 5792101.994 |
| LG+I+R6 | -2895283.153 | 5792491.026 |
| LG+R6 | -2895625.148 | 5793164.441 |
| LG+I+R5 | -2896129.333 | 5794162.235 |
| Q.INSECT+I+R8 | -2896276.919 | 5794520.860 |
| Q.PFAM+I+R8 | -2896379.848 | 5794726.718 |
| Q.YEAST+F+I+R8 | -2896494.088 | 5795156.130 |
| LG+R5 | -2897040.628 | 5795974.250 |
| LG+I+G4 | -2899715.958 | 5801261.458 |
| Q.INSECT+F+I+R8 | -2903115.002 | 5808397.958 |
| LG+G4 | -2904628.508 | 5811075.982 |
| WAG+F+I+R8 | -2909818.378 | 5821804.710 |
| WAG+I+R8 | -2911762.207 | 5825491.436 |
| Q.PLANT+I+R8 | -2924353.171 | 5850673.364 |
| JTT+F+I+R8 | -2924260.205 | 5850688.364 |
| Q.PLANT+F+I+R8 | -2926613.275 | 5855394.504 |
| JTT+I+R8 | -2929180.076 | 5860327.174 |
| CPREV+I+R8 | -2929292.479 | 5860551.980 |
| CPREV+F+I+R8 | -2933361.828 | 5868891.610 |
| DCMUT+F+I+R8 | -2934979.478 | 5872126.910 |
| PMB+F+I+R8 | -2936119.869 | 5874407.692 |
| MTINV+F+I+R8 | -2938393.075 | 5878954.104 |
| PMB+I+R8 | -2939990.486 | 5881947.994 |
| DCMUT+I+R8 | -2942949.978 | 5887866.978 |
| Q.MAMMAL+F+I+R8 | -2958533.936 | 5919235.826 |
| MTMET+F+I+R8 | -2960562.853 | 5923293.660 |
| Q.MAMMAL+I+R8 | -2963705.254 | 5929377.530 |
| Q.BIRD+F+I+R8 | -2981211.975 | 5964591.904 |
| Q.BIRD+I+R8 | -2985559.245 | 5973085.512 |
| MTVER+F+I+R8 | -3006669.237 | 6015506.428 |
| MTMET+I+R8 | -3056089.952 | 6114146.926 |
| MTINV+I+R8 | -3066124.027 | 6134215.076 |
| LG+I | -3070240.973 | 6142300.912 |
| MTVER+I+R8 | -3085006.928 | 6171980.878 |
| LG | -3150348.114 | 6302504.619 |
The inferred model Q.p__Margulisbacteria_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Margulisbacteria_2+I+R8 | Q.YEAST+I+R8 |
| BIC | 5769612.964 | 5784248.836 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Margulisbacteria/loop_1/tree_update/Q.p__Margulisbacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Margulisbacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 461.52 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Margulisbacteria/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0119  
Tree 1 branch length: 32.48429  
Tree 2 branch length: 35.43374  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2954266.627 | -2964578.354 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Margulisbacteria_2):  
Pearson's correlation: 0.9800417435163892  
Euclidean distance: 0.43758028664634235  
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
Total time usage: 42360.57 seconds (11.77 h)  
