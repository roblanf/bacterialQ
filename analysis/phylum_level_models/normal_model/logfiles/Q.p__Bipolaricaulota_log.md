## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bipolaricaulota  
  Taxa name: p__Bipolaricaulota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 106  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 13 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Bipolaricaulota/select_id.txt. Sampling sequences for 107 loci.  
Number of input species: 106  
Remaining 107 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bipolaricaulota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bipolaricaulota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Bipolaricaulota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deinococcota as the outgroup for Phylum Bipolaricaulota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 112 alignments. Deleted 8 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Bipolaricaulota/ref_tree.tre -l 15 -u 106 -o ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/subtrees -m split
```
  
Original number of taxa: 106   
Number of pruned subtrees: 1   
Number of taxa after pruning: 106   
Pruned node IDs (degree): 1 (106)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 107 loci files. Total number of potential alignments: 107.  
Obtained 107 alignments from all potential alignments.  
Remaining 107 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/subtree_update/Q.p__Bipolaricaulota
```
  
  Runtime: 22777.83 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bipolaricaulota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 51 |
| Q.PFAM | 35 |
| Q.PLANT | 9 |
| Q.YEAST | 7 |
| Q.INSECT | 5 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/subtree_update/Q.p__Bipolaricaulota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/subtree_update/Q.p__Bipolaricaulota.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/model_update/Q.p__Bipolaricaulota
```
  
  Runtime: 16014.90 seconds  
[Model update log](loop_1/model_update/Q.p__Bipolaricaulota.iqtree)  
BIC of the new model: 4381518.4549  
Likelihood of the new model: -2089570.0567  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bipolaricaulota_1)  
Model set for next iteration: LG,Q.PFAM,Q.PLANT,Q.YEAST,Q.p__Bipolaricaulota_1  
![Model bubble plot](loop_1/Q.p__Bipolaricaulota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9503073775795299  
Euclidean distance: 0.7036312185476187  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Bipolaricaulota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/tree_update/Q.p__Bipolaricaulota_1.treefile
```
  
  Runtime: 487.64 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/tree_update/Q.p__Bipolaricaulota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/tree_update/Q.p__Bipolaricaulota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.1068  
Tree 1 branch length: 16.0359  
Tree 2 branch length: 20.15149  
Time usage for Loop_1: 39327.03 seconds (10.92 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/tree_update/Q.p__Bipolaricaulota_1.treefile -l 15 -u 106 -o ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/subtrees -m split
```
  
Original number of taxa: 106   
Number of pruned subtrees: 1   
Number of taxa after pruning: 106   
Pruned node IDs (degree): 1 (106)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 107 loci files. Total number of potential alignments: 107.  
Obtained 107 alignments from all potential alignments.  
Remaining 107 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.PLANT,Q.YEAST,Q.p__Bipolaricaulota_1 -mdef ../Result_nova/phylum_models/Q.p__Bipolaricaulota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/subtree_update/Q.p__Bipolaricaulota
```
  
  Runtime: 15443.47 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bipolaricaulota.iqtree)  
Best models for iteration 2:  
Q.p__Bipolaricaulota_1  

| Model | Count |
|-------|-------|
| Q.p__Bipolaricaulota_1 | 99 |
| LG | 4 |
| Q.PLANT | 3 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/subtree_update/Q.p__Bipolaricaulota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/subtree_update/Q.p__Bipolaricaulota.treefile --model-joint GTR20+FO --init-model Q.p__Bipolaricaulota_1 -mdef ../Result_nova/phylum_models/Q.p__Bipolaricaulota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/model_update/Q.p__Bipolaricaulota
```
  
  Runtime: 7462.31 seconds  
[Model update log](loop_2/model_update/Q.p__Bipolaricaulota.iqtree)  
BIC of the new model: 4379822.181  
Likelihood of the new model: -2088721.9198  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bipolaricaulota_2)  
Model set for next iteration: LG,Q.PLANT,Q.YEAST,Q.p__Bipolaricaulota_2  
![Model bubble plot](loop_2/Q.p__Bipolaricaulota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9995160213539325  
Euclidean distance: 0.06673501925530044  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/tree_update/Q.p__Bipolaricaulota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 447.37 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Bipolaricaulota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.1068  
Tree 1 branch length: 16.0359  
Tree 2 branch length: 20.15677  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Bipolaricaulota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Bipolaricaulota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bipolaricaulota_1,Q.p__Bipolaricaulota_2 -mdef ../Result_nova/phylum_models/Q.p__Bipolaricaulota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Bipolaricaulota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 23102.45 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bipolaricaulota_2+I+R8 | -2132449.131 | 4267245.042 |
| Q.p__Bipolaricaulota_1+I+R8 | -2132455.681 | 4267258.142 |
| Q.p__Bipolaricaulota_1+F+I+R8 | -2136818.051 | 4276181.939 |
| Q.p__Bipolaricaulota_2+F+I+R8 | -2136979.179 | 4276504.195 |
| LG+F+I+R8 | -2141792.718 | 4286131.273 |
| Q.PFAM+F+I+R8 | -2142447.171 | 4287440.179 |
| Q.YEAST+F+I+R8 | -2146505.572 | 4295556.981 |
| Q.INSECT+F+I+R8 | -2150461.215 | 4303468.267 |
| WAG+F+I+R8 | -2151287.020 | 4305119.877 |
| Q.PFAM+I+R8 | -2151402.796 | 4305152.372 |
| LG+I+R8 | -2155547.557 | 4313441.894 |
| LG+I+R9 | -2155544.469 | 4313456.671 |
| LG+R8 | -2155560.576 | 4313457.455 |
| LG+R9 | -2155550.786 | 4313458.829 |
| LG+I+R7 | -2155590.964 | 4313507.755 |
| LG+R7 | -2155653.389 | 4313622.128 |
| JTT+F+I+R8 | -2155556.070 | 4313657.977 |
| LG+I+R6 | -2155786.738 | 4313878.349 |
| LG+R6 | -2156104.444 | 4314503.284 |
| Q.PLANT+F+I+R8 | -2159442.824 | 4321431.485 |
| LG+I+G4 | -2159779.978 | 4321770.539 |
| LG+G4 | -2163059.700 | 4328319.506 |
| WAG+I+R8 | -2164086.831 | 4330520.442 |
| CPREV+F+I+R8 | -2164496.965 | 4331539.767 |
| JTT+I+R8 | -2165674.879 | 4333696.538 |
| Q.INSECT+I+R8 | -2169656.918 | 4341660.616 |
| Q.PLANT+I+R8 | -2171671.856 | 4345690.492 |
| Q.YEAST+I+R8 | -2174674.697 | 4351696.174 |
| DCMUT+F+I+R8 | -2175944.503 | 4354434.843 |
| Q.MAMMAL+F+I+R8 | -2177798.907 | 4358143.651 |
| PMB+F+I+R8 | -2179226.188 | 4360998.213 |
| MTINV+F+I+R8 | -2179379.617 | 4361305.071 |
| CPREV+I+R8 | -2180343.310 | 4363033.400 |
| Q.MAMMAL+I+R8 | -2183488.598 | 4369323.976 |
| PMB+I+R8 | -2190355.943 | 4383058.666 |
| Q.BIRD+F+I+R8 | -2192329.986 | 4387205.809 |
| MTMET+F+I+R8 | -2192438.804 | 4387423.445 |
| DCMUT+I+R8 | -2195340.523 | 4393027.826 |
| Q.BIRD+I+R8 | -2198718.799 | 4399784.378 |
| MTVER+F+I+R8 | -2220685.065 | 4443915.967 |
| LG+I | -2284365.429 | 4570930.964 |
| MTMET+I+R8 | -2322033.822 | 4646414.424 |
| MTVER+I+R8 | -2328985.436 | 4660317.652 |
| MTINV+I+R8 | -2337135.360 | 4676617.500 |
| LG | -2345651.229 | 4693492.088 |
The inferred model Q.p__Bipolaricaulota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bipolaricaulota_2+I+R8 | LG+F+I+R8 |
| BIC | 4267245.042 | 4286131.273 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loop_1/tree_update/Q.p__Bipolaricaulota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Bipolaricaulota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 409.28 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Bipolaricaulota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0097  
Tree 1 branch length: 19.96497  
Tree 2 branch length: 20.15677  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2212018.589 | -2235123.463 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bipolaricaulota_2):  
Pearson's correlation: 0.9493836342963755  
Euclidean distance: 0.7040150843009119  
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
Total time usage: 86364.67 seconds (23.99 h)  
