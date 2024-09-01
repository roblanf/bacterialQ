## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Fibrobacterota  
  Taxa name: p__Fibrobacterota  
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
Discarded 0 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Fibrobacterota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 194  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Fibrobacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Fibrobacterota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Fibrobacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Zixibacteria as the outgroup for Phylum Fibrobacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Fibrobacterota/ref_tree.tre -l 15 -u 194 -o ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 194   
Number of pruned subtrees: 1   
Number of taxa after pruning: 194   
Pruned node IDs (degree): 1 (194)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/subtree_update/Q.p__Fibrobacterota
```
  
  Runtime: 22003.99 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Fibrobacterota.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| Q.INSECT | 49 |
| Q.PFAM | 28 |
| LG | 24 |
| Q.YEAST | 19 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/subtree_update/Q.p__Fibrobacterota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/subtree_update/Q.p__Fibrobacterota.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/model_update/Q.p__Fibrobacterota
```
  
  Runtime: 30639.92 seconds  
[Model update log](loop_1/model_update/Q.p__Fibrobacterota.iqtree)  
BIC of the new model: 6737134.4686  
Likelihood of the new model: -3168755.2941  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Fibrobacterota_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.YEAST,Q.p__Fibrobacterota_1  
![Model bubble plot](loop_1/Q.p__Fibrobacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9805649000806459  
Euclidean distance: 0.40189112105712305  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Fibrobacterota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Fibrobacterota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/tree_update/Q.p__Fibrobacterota_1.treefile
```
  
  Runtime: 1003.37 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/tree_update/Q.p__Fibrobacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/tree_update/Q.p__Fibrobacterota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 78  
Normalized RF distance: 0.2042  
Tree 1 branch length: 21.53689  
Tree 2 branch length: 29.02538  
Time usage for Loop_1: 53687.21 seconds (14.91 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/tree_update/Q.p__Fibrobacterota_1.treefile -l 15 -u 194 -o ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 194   
Number of pruned subtrees: 1   
Number of taxa after pruning: 194   
Pruned node IDs (degree): 1 (194)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,Q.p__Fibrobacterota_1 -mdef ../Result_nova/phylum_models/Q.p__Fibrobacterota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/subtree_update/Q.p__Fibrobacterota
```
  
  Runtime: 12398.28 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Fibrobacterota.iqtree)  
Best models for iteration 2:  
Q.p__Fibrobacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Fibrobacterota_1 | 107 |
| Q.PFAM | 6 |
| LG | 4 |
| Q.INSECT | 2 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/subtree_update/Q.p__Fibrobacterota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/subtree_update/Q.p__Fibrobacterota.treefile --model-joint GTR20+FO --init-model Q.p__Fibrobacterota_1 -mdef ../Result_nova/phylum_models/Q.p__Fibrobacterota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/model_update/Q.p__Fibrobacterota
```
  
  Runtime: 35831.95 seconds  
[Model update log](loop_2/model_update/Q.p__Fibrobacterota.iqtree)  
BIC of the new model: 6731352.5578  
Likelihood of the new model: -3165864.3387  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Fibrobacterota_2)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.p__Fibrobacterota_2  
![Model bubble plot](loop_2/Q.p__Fibrobacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999756878528785  
Euclidean distance: 0.019076423651943373  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/tree_update/Q.p__Fibrobacterota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Fibrobacterota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 1028.32 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Fibrobacterota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 78  
Normalized RF distance: 0.2042  
Tree 1 branch length: 21.53689  
Tree 2 branch length: 29.05847  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Fibrobacterota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Fibrobacterota/inferred_models
```

![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Fibrobacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Fibrobacterota_1,Q.p__Fibrobacterota_2 -mdef ../Result_nova/phylum_models/Q.p__Fibrobacterota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Fibrobacterota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 22281.39 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Fibrobacterota_1+I+R8 | -3284747.546 | 6573742.118 |
| Q.p__Fibrobacterota_2+I+R8 | -3284798.686 | 6573844.398 |
| Q.p__Fibrobacterota_1+F+I+R8 | -3291470.816 | 6587390.391 |
| Q.p__Fibrobacterota_2+F+I+R8 | -3291744.072 | 6587936.903 |
| Q.PFAM+I+R8 | -3297594.638 | 6599436.302 |
| LG+F+I+R8 | -3297631.282 | 6599711.323 |
| LG+I+R8 | -3298308.877 | 6600864.780 |
| LG+R8 | -3298525.972 | 6601288.352 |
| LG+I+R7 | -3298845.028 | 6601915.847 |
| Q.PFAM+F+I+R8 | -3298841.434 | 6602131.627 |
| LG+R7 | -3299364.563 | 6602944.299 |
| Q.INSECT+I+R8 | -3299419.652 | 6603086.330 |
| Q.YEAST+F+I+R8 | -3299623.005 | 6603694.769 |
| LG+I+R6 | -3299909.505 | 6604023.565 |
| LG+R6 | -3300696.716 | 6605587.370 |
| Q.YEAST+I+R8 | -3300883.019 | 6606013.064 |
| LG+I+R5 | -3301985.634 | 6608154.588 |
| Q.INSECT+F+I+R8 | -3302801.637 | 6610052.033 |
| LG+R5 | -3303599.300 | 6611371.303 |
| LG+I+G4 | -3309128.742 | 6622366.481 |
| WAG+F+I+R8 | -3313619.820 | 6631688.399 |
| WAG+I+R8 | -3314371.504 | 6632990.034 |
| LG+G4 | -3314509.669 | 6633117.718 |
| JTT+F+I+R8 | -3325794.139 | 6656037.037 |
| JTT+I+R8 | -3326949.967 | 6658146.960 |
| Q.PLANT+I+R8 | -3333465.199 | 6671177.424 |
| Q.PLANT+F+I+R8 | -3337672.258 | 6679793.275 |
| CPREV+F+I+R8 | -3341468.611 | 6687385.981 |
| CPREV+I+R8 | -3341691.081 | 6687629.188 |
| DCMUT+F+I+R8 | -3342274.057 | 6688996.873 |
| PMB+F+I+R8 | -3346823.653 | 6698096.065 |
| DCMUT+I+R8 | -3349055.481 | 6702357.988 |
| PMB+I+R8 | -3350096.343 | 6704439.712 |
| MTINV+F+I+R8 | -3354006.635 | 6712462.029 |
| Q.MAMMAL+I+R8 | -3369383.936 | 6743014.898 |
| Q.MAMMAL+F+I+R8 | -3370696.531 | 6745841.821 |
| MTMET+F+I+R8 | -3380501.249 | 6765451.257 |
| Q.BIRD+I+R8 | -3401412.515 | 6807072.056 |
| Q.BIRD+F+I+R8 | -3403755.024 | 6811958.807 |
| MTVER+F+I+R8 | -3437267.461 | 6878983.681 |
| MTMET+I+R8 | -3500781.569 | 7005810.164 |
| MTINV+I+R8 | -3505780.935 | 7015808.896 |
| LG+I | -3521014.263 | 7046126.906 |
| MTVER+I+R8 | -3543568.606 | 7091384.238 |
| LG | -3603130.260 | 7210348.282 |
The inferred model Q.p__Fibrobacterota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Fibrobacterota_1+I+R8 | Q.PFAM+I+R8 |
| BIC | 6573742.118 | 6599436.402 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Fibrobacterota/loop_1/tree_update/Q.p__Fibrobacterota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Fibrobacterota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 726.20 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Fibrobacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 27.65604  
Tree 2 branch length: 29.05847  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -3350592.861 | -3363873.814 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Fibrobacterota_2):  
Pearson's correlation: 0.9789031646256021  
Euclidean distance: 0.4487765919615461  
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
Total time usage: 126098.19 seconds (35.03 h)  
