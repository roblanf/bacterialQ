## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Cloacimonadota  
  Taxa name: p__Cloacimonadota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 143  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Cloacimonadota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 143  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Cloacimonadota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Cloacimonadota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Cloacimonadota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Zixibacteria as the outgroup for Phylum Cloacimonadota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Cloacimonadota/ref_tree.tre -l 15 -u 143 -o ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/subtrees -m split
```
  
Original number of taxa: 143   
Number of pruned subtrees: 1   
Number of taxa after pruning: 143   
Pruned node IDs (degree): 1 (143)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/subtree_update/Q.p__Cloacimonadota
```
  
  Runtime: 27700.11 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Cloacimonadota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 65 |
| Q.INSECT | 41 |
| LG | 8 |
| Q.PLANT | 3 |
| Q.PFAM | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/subtree_update/Q.p__Cloacimonadota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/subtree_update/Q.p__Cloacimonadota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/model_update/Q.p__Cloacimonadota
```
  
  Runtime: 19128.73 seconds  
[Model update log](loop_1/model_update/Q.p__Cloacimonadota.iqtree)  
BIC of the new model: 6912789.4563  
Likelihood of the new model: -3303268.1104  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Cloacimonadota_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.p__Cloacimonadota_1  
![Model bubble plot](loop_1/Q.p__Cloacimonadota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9777738081996458  
Euclidean distance: 0.4646053998955874  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Cloacimonadota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Cloacimonadota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/tree_update/Q.p__Cloacimonadota_1.treefile
```
  
  Runtime: 684.92 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/tree_update/Q.p__Cloacimonadota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/tree_update/Q.p__Cloacimonadota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.0786  
Tree 1 branch length: 22.18114  
Tree 2 branch length: 31.70701  
Time usage for Loop_1: 47541.80 seconds (13.21 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/tree_update/Q.p__Cloacimonadota_1.treefile -l 15 -u 143 -o ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/subtrees -m split
```
  
Original number of taxa: 143   
Number of pruned subtrees: 1   
Number of taxa after pruning: 143   
Pruned node IDs (degree): 1 (143)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.p__Cloacimonadota_1 -mdef ../Result_nova/phylum_models/Q.p__Cloacimonadota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/subtree_update/Q.p__Cloacimonadota
```
  
  Runtime: 17015.23 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Cloacimonadota.iqtree)  
Best models for iteration 2:  
Q.p__Cloacimonadota_1  

| Model | Count |
|-------|-------|
| Q.p__Cloacimonadota_1 | 111 |
| Q.INSECT | 4 |
| LG | 3 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/subtree_update/Q.p__Cloacimonadota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/subtree_update/Q.p__Cloacimonadota.treefile --model-joint GTR20+FO --init-model Q.p__Cloacimonadota_1 -mdef ../Result_nova/phylum_models/Q.p__Cloacimonadota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/model_update/Q.p__Cloacimonadota
```
  
  Runtime: 19756.25 seconds  
[Model update log](loop_2/model_update/Q.p__Cloacimonadota.iqtree)  
BIC of the new model: 6910055.9195  
Likelihood of the new model: -3301901.342  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Cloacimonadota_2)  
Model set for next iteration: Q.INSECT,LG,Q.YEAST,Q.p__Cloacimonadota_2  
![Model bubble plot](loop_2/Q.p__Cloacimonadota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999566742282183  
Euclidean distance: 0.02282774577332177  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/tree_update/Q.p__Cloacimonadota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Cloacimonadota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 791.21 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Cloacimonadota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.0786  
Tree 1 branch length: 22.18114  
Tree 2 branch length: 31.77012  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Cloacimonadota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Cloacimonadota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Cloacimonadota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Cloacimonadota_1,Q.p__Cloacimonadota_2 -mdef ../Result_nova/phylum_models/Q.p__Cloacimonadota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Cloacimonadota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 11766.48 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Cloacimonadota_1+I+R8 | -3362926.321 | 6729014.376 |
| Q.p__Cloacimonadota_2+I+R8 | -3362931.429 | 6729024.592 |
| Q.YEAST+I+R8 | -3376840.974 | 6756843.682 |
| Q.p__Cloacimonadota_1+F+I+R8 | -3378226.939 | 6759817.200 |
| Q.p__Cloacimonadota_2+F+I+R8 | -3378529.050 | 6760421.422 |
| LG+F+I+R8 | -3379680.428 | 6762724.178 |
| Q.INSECT+I+R8 | -3381012.058 | 6765185.850 |
| Q.PFAM+F+I+R8 | -3383063.899 | 6769491.120 |
| Q.YEAST+F+I+R8 | -3383509.694 | 6770382.710 |
| Q.INSECT+F+I+R8 | -3387134.094 | 6777631.510 |
| LG+I+R8 | -3388419.018 | 6779999.770 |
| LG+R8 | -3388537.883 | 6780226.891 |
| LG+I+R7 | -3388786.815 | 6780714.145 |
| LG+R7 | -3389074.234 | 6781278.373 |
| LG+I+R6 | -3389542.691 | 6782204.677 |
| LG+R6 | -3390409.117 | 6783926.919 |
| LG+I+R5 | -3391508.980 | 6786116.035 |
| LG+R5 | -3393396.935 | 6789881.335 |
| Q.PFAM+I+R8 | -3395256.724 | 6793675.182 |
| WAG+F+I+R8 | -3395709.565 | 6794782.452 |
| LG+I+G4 | -3397858.166 | 6798740.138 |
| LG+G4 | -3404689.674 | 6812392.545 |
| JTT+F+I+R8 | -3405933.845 | 6815231.012 |
| Q.PLANT+F+I+R8 | -3407966.065 | 6819295.452 |
| WAG+I+R8 | -3410270.784 | 6823703.302 |
| Q.PLANT+I+R8 | -3413629.039 | 6830419.812 |
| CPREV+I+R8 | -3420261.489 | 6843684.712 |
| CPREV+F+I+R8 | -3421443.867 | 6846251.056 |
| JTT+I+R8 | -3422963.251 | 6849088.236 |
| DCMUT+F+I+R8 | -3423159.791 | 6849682.904 |
| MTINV+F+I+R8 | -3426691.846 | 6856747.014 |
| PMB+F+I+R8 | -3438041.467 | 6879446.256 |
| DCMUT+I+R8 | -3444843.527 | 6892848.788 |
| Q.MAMMAL+F+I+R8 | -3446326.570 | 6896016.462 |
| MTMET+F+I+R8 | -3450271.656 | 6903906.634 |
| PMB+I+R8 | -3454855.819 | 6912873.372 |
| Q.MAMMAL+I+R8 | -3466644.477 | 6936450.688 |
| Q.BIRD+F+I+R8 | -3473545.517 | 6950454.356 |
| Q.BIRD+I+R8 | -3492490.895 | 6988143.524 |
| MTVER+F+I+R8 | -3507876.732 | 7019116.786 |
| MTMET+I+R8 | -3549103.262 | 7101368.258 |
| MTINV+I+R8 | -3555741.079 | 7114643.892 |
| MTVER+I+R8 | -3594362.682 | 7191887.098 |
| LG+I | -3648589.499 | 7300192.195 |
| LG | -3757181.108 | 7517364.803 |
The inferred model Q.p__Cloacimonadota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Cloacimonadota_1+I+R8 | Q.YEAST+I+R8 |
| BIC | 6729014.376 | 6756843.682 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Cloacimonadota/loop_1/tree_update/Q.p__Cloacimonadota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Cloacimonadota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 783.38 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Cloacimonadota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0071  
Tree 1 branch length: 29.01089  
Tree 2 branch length: 31.77012  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -3436767.818 | -3460744.223 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Cloacimonadota_2):  
Pearson's correlation: 0.9562264591400992  
Euclidean distance: 0.6609628304070756  
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
Total time usage: 97785.02 seconds (27.16 h)  
