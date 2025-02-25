## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Elusimicrobiota  
  Taxa name: p__Elusimicrobiota  
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
Discarded 3 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/select_id.txt. Sampling sequences for 117 loci.  
Number of input species: 376  
Remaining 117 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Elusimicrobiota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Elusimicrobiota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Elusimicrobiota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 118 alignments. Deleted 2 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/subtrees -m split
```
  
Original number of taxa: 376   
Number of pruned subtrees: 3   
Number of taxa after pruning: 367   
Pruned node IDs (degree): 5 (237) 267 (103) 241 (27)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 117 loci files. Total number of potential alignments: 351.  
Obtained 348 alignments from all potential alignments.  
Remaining 348 alignments. Deleted 3 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/subtree_update/Q.p__Elusimicrobiota
```
  
  Runtime: 56855.34 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Elusimicrobiota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 130 |
| Q.PFAM | 82 |
| LG | 73 |
| Q.PLANT | 44 |
| JTT | 11 |
| CPREV | 3 |
| Q.MAMMAL | 3 |
| WAG | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/subtree_update/Q.p__Elusimicrobiota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/subtree_update/Q.p__Elusimicrobiota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/model_update/Q.p__Elusimicrobiota
```
  
  Runtime: 39265.98 seconds  
[Model update log](loop_1/model_update/Q.p__Elusimicrobiota.iqtree)  
BIC of the new model: 15832835.8089  
Likelihood of the new model: -7495020.598  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Elusimicrobiota_1)  
Model set for next iteration: Q.YEAST,Q.PFAM,LG,Q.PLANT,Q.p__Elusimicrobiota_1  
![Model bubble plot](loop_1/Q.p__Elusimicrobiota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9749511156277935  
Euclidean distance: 0.46061135428439937  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/tree_update/Q.p__Elusimicrobiota_1.treefile
```
  
  Runtime: 1767.08 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/tree_update/Q.p__Elusimicrobiota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/tree_update/Q.p__Elusimicrobiota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 114  
Normalized RF distance: 0.1524  
Tree 1 branch length: 56.05702  
Tree 2 branch length: 74.46183  
Time usage for Loop_1: 97985.89 seconds (27.22 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/tree_update/Q.p__Elusimicrobiota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/subtrees -m split
```
  
Original number of taxa: 376   
Number of pruned subtrees: 3   
Number of taxa after pruning: 367   
Pruned node IDs (degree): 29 (237) 265 (112) 12 (18)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 117 loci files. Total number of potential alignments: 351.  
Obtained 347 alignments from all potential alignments.  
Remaining 347 alignments. Deleted 4 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.PFAM,LG,Q.PLANT,Q.p__Elusimicrobiota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/subtree_update/Q.p__Elusimicrobiota
```
  
  Runtime: 31696.68 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Elusimicrobiota.iqtree)  
Best models for iteration 2:  
Q.p__Elusimicrobiota_1  

| Model | Count |
|-------|-------|
| Q.p__Elusimicrobiota_1 | 249 |
| Q.PFAM | 47 |
| LG | 31 |
| Q.PLANT | 13 |
| Q.YEAST | 7 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/subtree_update/Q.p__Elusimicrobiota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/subtree_update/Q.p__Elusimicrobiota.treefile --model-joint GTR20+FO --init-model Q.p__Elusimicrobiota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/model_update/Q.p__Elusimicrobiota
```
  
  Runtime: 44249.84 seconds  
[Model update log](loop_2/model_update/Q.p__Elusimicrobiota.iqtree)  
BIC of the new model: 15847301.8079  
Likelihood of the new model: -7501650.4577  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Elusimicrobiota_2)  
Model set for next iteration: Q.PFAM,LG,Q.PLANT,Q.p__Elusimicrobiota_2  
![Model bubble plot](loop_2/Q.p__Elusimicrobiota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998210375474197  
Euclidean distance: 0.04241668765702074  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/tree_update/Q.p__Elusimicrobiota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 2037.35 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 120  
Normalized RF distance: 0.1604  
Tree 1 branch length: 56.05702  
Tree 2 branch length: 74.6622  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Elusimicrobiota_1,Q.p__Elusimicrobiota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 115853.48 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Elusimicrobiota_2+I+R9 | -7791392.526 | 15590902.591 |
| Q.p__Elusimicrobiota_1+I+R9 | -7791785.925 | 15591689.389 |
| Q.p__Elusimicrobiota_1+F+I+R9 | -7809969.329 | 15628257.546 |
| Q.p__Elusimicrobiota_2+F+I+R9 | -7810870.614 | 15630060.116 |
| LG+F+I+R9 | -7826786.636 | 15661892.160 |
| Q.YEAST+F+I+R9 | -7826948.792 | 15662216.472 |
| Q.PFAM+F+I+R9 | -7827905.236 | 15664129.360 |
| Q.YEAST+I+R9 | -7830414.183 | 15668945.905 |
| Q.PFAM+I+R9 | -7832982.078 | 15674081.695 |
| Q.INSECT+I+R9 | -7834039.003 | 15676195.545 |
| LG+I+R9 | -7835212.756 | 15678543.051 |
| LG+R9 | -7835793.285 | 15679693.512 |
| Q.INSECT+F+I+R9 | -7835805.597 | 15679930.082 |
| LG+I+R8 | -7836444.127 | 15680984.598 |
| LG+R8 | -7837210.123 | 15682505.993 |
| LG+I+R7 | -7838566.332 | 15685207.814 |
| LG+R7 | -7840100.585 | 15688265.723 |
| LG+I+R6 | -7842736.580 | 15693527.115 |
| LG+R6 | -7845402.148 | 15698847.654 |
| LG+I+G4 | -7869173.615 | 15746305.809 |
| WAG+F+I+R9 | -7870321.300 | 15748961.488 |
| JTT+F+I+R9 | -7870663.669 | 15749646.226 |
| WAG+I+R9 | -7876333.340 | 15760784.219 |
| LG+G4 | -7881612.009 | 15771172.000 |
| JTT+I+R9 | -7885867.449 | 15779852.437 |
| Q.PLANT+F+I+R9 | -7891724.498 | 15791767.884 |
| Q.PLANT+I+R9 | -7891903.992 | 15791925.523 |
| CPREV+I+R9 | -7921949.329 | 15852016.197 |
| CPREV+F+I+R9 | -7932923.429 | 15874165.746 |
| MTINV+F+I+R9 | -7937430.292 | 15883179.472 |
| DCMUT+F+I+R9 | -7938146.584 | 15884612.056 |
| PMB+F+I+R9 | -7956395.118 | 15921109.124 |
| Q.MAMMAL+F+I+R9 | -7959534.695 | 15927388.278 |
| DCMUT+I+R9 | -7961860.679 | 15931838.897 |
| PMB+I+R9 | -7965744.016 | 15939605.571 |
| Q.MAMMAL+I+R9 | -7976252.188 | 15960621.915 |
| MTMET+F+I+R9 | -7991773.506 | 15991865.900 |
| Q.BIRD+F+I+R9 | -8024962.183 | 16058243.254 |
| Q.BIRD+I+R9 | -8038984.028 | 16086085.595 |
| MTVER+F+I+R9 | -8120187.380 | 16248693.648 |
| MTMET+I+R9 | -8280352.003 | 16568821.545 |
| MTINV+I+R9 | -8299423.782 | 16606965.103 |
| MTVER+I+R9 | -8370674.567 | 16749466.673 |
| LG+I | -8438207.017 | 16884362.016 |
| LG | -8569308.123 | 17146553.631 |
The inferred model Q.p__Elusimicrobiota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Elusimicrobiota_2+I+R9 | LG+F+I+R9 |
| BIC | 15590902.591 | 15661892.16 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loop_1/tree_update/Q.p__Elusimicrobiota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 974.21 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Elusimicrobiota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.008  
Tree 1 branch length: 70.30288  
Tree 2 branch length: 74.6622  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -7862163.939 | -7904959.905 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Elusimicrobiota_2):  
Pearson's correlation: 0.9716455229169361  
Euclidean distance: 0.5271988568670272  
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
Total time usage: 293083.97 seconds (81.41 h)  
