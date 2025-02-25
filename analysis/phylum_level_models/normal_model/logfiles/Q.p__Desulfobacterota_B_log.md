## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Desulfobacterota_B  
  Taxa name: p__Desulfobacterota_B  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 151  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 151  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Desulfobacterota_B  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Desulfobacterota_B -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Desulfobacterota_B
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/ref_tree.tre -l 15 -u 151 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/subtrees -m split
```
  
Original number of taxa: 151   
Number of pruned subtrees: 1   
Number of taxa after pruning: 151   
Pruned node IDs (degree): 1 (151)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/subtree_update/Q.p__Desulfobacterota_B
```
  
  Runtime: 26803.85 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Desulfobacterota_B.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| Q.PFAM | 40 |
| Q.YEAST | 37 |
| Q.PLANT | 22 |
| LG | 20 |
| WAG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/subtree_update/Q.p__Desulfobacterota_B.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/subtree_update/Q.p__Desulfobacterota_B.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/model_update/Q.p__Desulfobacterota_B
```
  
  Runtime: 36607.45 seconds  
[Model update log](loop_1/model_update/Q.p__Desulfobacterota_B.iqtree)  
BIC of the new model: 6962484.2272  
Likelihood of the new model: -3312707.0683  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Desulfobacterota_B_1)  
Model set for next iteration: Q.PFAM,Q.YEAST,Q.PLANT,LG,Q.p__Desulfobacterota_B_1  
![Model bubble plot](loop_1/Q.p__Desulfobacterota_B_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9521547149537547  
Euclidean distance: 0.8352125508862387  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/tree_update/Q.p__Desulfobacterota_B_1.treefile
```
  
  Runtime: 951.96 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/tree_update/Q.p__Desulfobacterota_B_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/tree_update/Q.p__Desulfobacterota_B_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 36  
Normalized RF distance: 0.1208  
Tree 1 branch length: 21.73724  
Tree 2 branch length: 28.68361  
Time usage for Loop_1: 64414.32 seconds (17.89 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/tree_update/Q.p__Desulfobacterota_B_1.treefile -l 15 -u 151 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/subtrees -m split
```
  
Original number of taxa: 151   
Number of pruned subtrees: 1   
Number of taxa after pruning: 151   
Pruned node IDs (degree): 1 (151)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/training_loci -m MFP -mset Q.PFAM,Q.YEAST,Q.PLANT,LG,Q.p__Desulfobacterota_B_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/subtree_update/Q.p__Desulfobacterota_B
```
  
  Runtime: 24564.38 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Desulfobacterota_B.iqtree)  
Best models for iteration 2:  
Q.p__Desulfobacterota_B_1  

| Model | Count |
|-------|-------|
| Q.p__Desulfobacterota_B_1 | 114 |
| LG | 2 |
| Q.YEAST | 2 |
| Q.PFAM | 1 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/subtree_update/Q.p__Desulfobacterota_B.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/subtree_update/Q.p__Desulfobacterota_B.treefile --model-joint GTR20+FO --init-model Q.p__Desulfobacterota_B_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/model_update/Q.p__Desulfobacterota_B
```
  
  Runtime: 17045.04 seconds  
[Model update log](loop_2/model_update/Q.p__Desulfobacterota_B.iqtree)  
BIC of the new model: 6960309.0547  
Likelihood of the new model: -3311619.482  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Desulfobacterota_B_2)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.PLANT,Q.p__Desulfobacterota_B_2  
![Model bubble plot](loop_2/Q.p__Desulfobacterota_B_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997356740745799  
Euclidean distance: 0.06427237795656583  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/tree_update/Q.p__Desulfobacterota_B_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 661.57 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 40  
Normalized RF distance: 0.1342  
Tree 1 branch length: 21.73724  
Tree 2 branch length: 28.74232  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Desulfobacterota_B_1,Q.p__Desulfobacterota_B_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 17267.31 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Desulfobacterota_B_2+I+R9 | -3393953.422 | 6791262.466 |
| Q.p__Desulfobacterota_B_1+I+R9 | -3394023.383 | 6791402.388 |
| Q.p__Desulfobacterota_B_1+F+I+R9 | -3407018.341 | 6817594.066 |
| Q.p__Desulfobacterota_B_2+F+I+R9 | -3408180.168 | 6819917.720 |
| LG+F+I+R9 | -3416038.812 | 6835635.008 |
| Q.PFAM+F+I+R9 | -3416481.641 | 6836520.666 |
| Q.YEAST+F+I+R9 | -3416836.628 | 6837230.640 |
| Q.INSECT+F+I+R9 | -3418149.288 | 6839855.960 |
| WAG+F+I+R9 | -3434206.897 | 6871971.178 |
| JTT+F+I+R9 | -3436576.750 | 6876710.884 |
| Q.PFAM+I+R9 | -3436991.122 | 6877337.866 |
| Q.PLANT+F+I+R9 | -3439744.088 | 6883045.560 |
| LG+I+R9 | -3447794.210 | 6898944.042 |
| LG+R9 | -3447828.094 | 6899001.191 |
| LG+I+R8 | -3447909.933 | 6899154.250 |
| LG+R8 | -3448030.999 | 6899385.763 |
| LG+I+R7 | -3448215.924 | 6899744.994 |
| LG+R7 | -3448463.356 | 6900229.239 |
| LG+I+R6 | -3448877.152 | 6901046.212 |
| LG+R6 | -3449635.613 | 6902552.514 |
| LG+I+G4 | -3456803.866 | 6916804.068 |
| DCMUT+F+I+R9 | -3458612.338 | 6920782.060 |
| JTT+I+R9 | -3459295.448 | 6921946.518 |
| WAG+I+R9 | -3460157.431 | 6923670.484 |
| LG+G4 | -3463869.323 | 6930924.363 |
| CPREV+F+I+R9 | -3463889.775 | 6931336.934 |
| Q.INSECT+I+R9 | -3465765.478 | 6934886.578 |
| Q.PLANT+I+R9 | -3469596.759 | 6942549.140 |
| Q.MAMMAL+F+I+R9 | -3477858.768 | 6959274.920 |
| MTINV+F+I+R9 | -3478324.501 | 6960206.386 |
| Q.YEAST+I+R9 | -3479417.412 | 6962190.446 |
| PMB+F+I+R9 | -3483482.488 | 6970522.360 |
| DCMUT+I+R9 | -3494672.897 | 6992701.416 |
| Q.MAMMAL+I+R9 | -3496160.091 | 6995675.804 |
| CPREV+I+R9 | -3500875.223 | 7005106.068 |
| Q.BIRD+F+I+R9 | -3503620.941 | 7010799.266 |
| MTMET+F+I+R9 | -3505081.811 | 7013721.006 |
| PMB+I+R9 | -3508731.893 | 7020819.408 |
| Q.BIRD+I+R9 | -3522687.864 | 7048731.350 |
| MTVER+F+I+R9 | -3555201.032 | 7113959.448 |
| LG+I | -3689913.988 | 7383013.693 |
| MTMET+I+R9 | -3722598.123 | 7448551.868 |
| MTVER+I+R9 | -3734864.344 | 7473084.310 |
| MTINV+I+R9 | -3741370.808 | 7486097.238 |
| LG | -3799569.071 | 7602313.240 |
The inferred model Q.p__Desulfobacterota_B_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Desulfobacterota_B_2+I+R9 | LG+F+I+R9 |
| BIC | 6791262.466 | 6835635.008 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loop_1/tree_update/Q.p__Desulfobacterota_B_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 519.29 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_B/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 27.44113  
Tree 2 branch length: 28.74232  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -3468878.199 | -3518917.181 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Desulfobacterota_B_2):  
Pearson's correlation: 0.938343288107784  
Euclidean distance: 0.9111353213880441  
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
Total time usage: 124683.62 seconds (34.63 h)  
