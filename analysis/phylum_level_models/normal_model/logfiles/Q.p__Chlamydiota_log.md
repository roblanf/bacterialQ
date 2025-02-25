## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Chlamydiota  
  Taxa name: p__Chlamydiota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 9 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Chlamydiota/select_id.txt. Sampling sequences for 111 loci.  
Number of input species: 311  
Remaining 111 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Chlamydiota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Chlamydiota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Chlamydiota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Chlamydiota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 114 alignments. Deleted 6 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Chlamydiota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/subtrees -m split
```
  
Original number of taxa: 311   
Number of pruned subtrees: 3   
Number of taxa after pruning: 304   
Pruned node IDs (degree): 64 (245) 23 (42) 5 (17)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 111 loci files. Total number of potential alignments: 333.  
Obtained 329 alignments from all potential alignments.  
Remaining 329 alignments. Deleted 4 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/subtree_update/Q.p__Chlamydiota
```
  
  Runtime: 81263.45 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Chlamydiota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 144 |
| Q.INSECT | 95 |
| LG | 62 |
| Q.PFAM | 20 |
| Q.PLANT | 7 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/subtree_update/Q.p__Chlamydiota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/subtree_update/Q.p__Chlamydiota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/model_update/Q.p__Chlamydiota
```
  
  Runtime: 51126.06 seconds  
[Model update log](loop_1/model_update/Q.p__Chlamydiota.iqtree)  
BIC of the new model: 16758016.2041  
Likelihood of the new model: -8042428.964  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Chlamydiota_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.PFAM,Q.p__Chlamydiota_1  
![Model bubble plot](loop_1/Q.p__Chlamydiota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9858302758437701  
Euclidean distance: 0.3941019548757653  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Chlamydiota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Chlamydiota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/tree_update/Q.p__Chlamydiota_1.treefile
```
  
  Runtime: 1370.37 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/tree_update/Q.p__Chlamydiota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/tree_update/Q.p__Chlamydiota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 128  
Normalized RF distance: 0.2078  
Tree 1 branch length: 73.72264  
Tree 2 branch length: 103.15608  
Time usage for Loop_1: 133835.43 seconds (37.18 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/tree_update/Q.p__Chlamydiota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/subtrees -m split
```
  
Original number of taxa: 311   
Number of pruned subtrees: 3   
Number of taxa after pruning: 301   
Pruned node IDs (degree): 64 (245) 27 (38) 4 (18)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 111 loci files. Total number of potential alignments: 333.  
Obtained 329 alignments from all potential alignments.  
Remaining 329 alignments. Deleted 4 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.PFAM,Q.p__Chlamydiota_1 -mdef ../Result_nova/phylum_models/Q.p__Chlamydiota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/subtree_update/Q.p__Chlamydiota
```
  
  Runtime: 41823.04 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Chlamydiota.iqtree)  
Best models for iteration 2:  
Q.p__Chlamydiota_1  

| Model | Count |
|-------|-------|
| Q.p__Chlamydiota_1 | 265 |
| Q.INSECT | 27 |
| LG | 20 |
| Q.YEAST | 11 |
| Q.PFAM | 6 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/subtree_update/Q.p__Chlamydiota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/subtree_update/Q.p__Chlamydiota.treefile --model-joint GTR20+FO --init-model Q.p__Chlamydiota_1 -mdef ../Result_nova/phylum_models/Q.p__Chlamydiota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/model_update/Q.p__Chlamydiota
```
  
  Runtime: 49099.95 seconds  
[Model update log](loop_2/model_update/Q.p__Chlamydiota.iqtree)  
BIC of the new model: 16556051.6475  
Likelihood of the new model: -7944911.3765  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Chlamydiota_2)  
Model set for next iteration: Q.INSECT,LG,Q.YEAST,Q.p__Chlamydiota_2  
![Model bubble plot](loop_2/Q.p__Chlamydiota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998905635364894  
Euclidean distance: 0.04253591043986176  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/tree_update/Q.p__Chlamydiota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Chlamydiota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 1089.65 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Chlamydiota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 126  
Normalized RF distance: 0.2045  
Tree 1 branch length: 73.72264  
Tree 2 branch length: 103.59986  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (Q.p__Chlamydiota_2):  
Pearson's correlation: 0.9848911074474755  
Euclidean distance: 0.42043987218433654  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Chlamydiota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Chlamydiota/inferred_models
```

![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Chlamydiota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Chlamydiota_1,Q.p__Chlamydiota_2 -mdef ../Result_nova/phylum_models/Q.p__Chlamydiota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Chlamydiota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 27178.16 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Chlamydiota_1+I+R8 | -8185229.287 | 16377143.636 |
| Q.p__Chlamydiota_2+I+R8 | -8185291.313 | 16377267.688 |
| Q.YEAST+I+R8 | -8214355.137 | 16435395.336 |
| Q.INSECT+I+R8 | -8221294.064 | 16449273.190 |
| Q.p__Chlamydiota_1+F+I+R8 | -8222135.344 | 16451156.091 |
| Q.p__Chlamydiota_2+F+I+R8 | -8222410.665 | 16451706.733 |
| LG+F+I+R8 | -8227620.215 | 16462125.833 |
| Q.YEAST+F+I+R8 | -8232506.370 | 16471898.143 |
| Q.PFAM+F+I+R8 | -8233071.908 | 16473029.219 |
| LG+I+R8 | -8233514.568 | 16473714.198 |
| LG+R8 | -8234618.978 | 16475912.474 |
| LG+I+R7 | -8236688.093 | 16480040.160 |
| LG+R7 | -8238853.660 | 16484360.749 |
| Q.PFAM+I+R8 | -8241548.151 | 16489781.364 |
| LG+I+R6 | -8241910.047 | 16490462.979 |
| LG+R6 | -8245601.449 | 16497835.239 |
| Q.INSECT+F+I+R8 | -8248632.242 | 16504149.887 |
| LG+I+R5 | -8252704.449 | 16512030.694 |
| LG+R5 | -8258771.658 | 16524154.568 |
| LG+I+G4 | -8277524.278 | 16561596.543 |
| WAG+F+I+R8 | -8283074.514 | 16573034.431 |
| WAG+I+R8 | -8292923.394 | 16592531.850 |
| LG+G4 | -8293610.738 | 16593758.918 |
| Q.PLANT+I+R8 | -8299276.852 | 16605238.766 |
| Q.PLANT+F+I+R8 | -8307328.497 | 16621542.397 |
| JTT+F+I+R8 | -8310405.945 | 16627697.293 |
| JTT+I+R8 | -8329042.409 | 16664769.880 |
| CPREV+I+R8 | -8334566.564 | 16675818.190 |
| CPREV+F+I+R8 | -8344331.502 | 16695548.407 |
| MTINV+F+I+R8 | -8347029.593 | 16700944.589 |
| DCMUT+F+I+R8 | -8357403.452 | 16721692.307 |
| PMB+F+I+R8 | -8378899.460 | 16764684.323 |
| DCMUT+I+R8 | -8381571.262 | 16769827.586 |
| PMB+I+R8 | -8385350.447 | 16777385.956 |
| MTMET+F+I+R8 | -8405683.830 | 16818253.063 |
| Q.MAMMAL+I+R8 | -8410161.987 | 16827009.036 |
| Q.MAMMAL+F+I+R8 | -8410259.482 | 16827404.367 |
| Q.BIRD+I+R8 | -8475660.642 | 16958006.346 |
| Q.BIRD+F+I+R8 | -8475952.455 | 16958790.313 |
| MTVER+F+I+R8 | -8534915.218 | 17076715.839 |
| MTMET+I+R8 | -8655167.547 | 17317020.156 |
| MTINV+I+R8 | -8683201.259 | 17373087.580 |
| MTVER+I+R8 | -8731916.147 | 17470517.356 |
| LG+I | -9055258.085 | 18117053.612 |
| LG | -9260755.004 | 18528036.906 |
The inferred model Q.p__Chlamydiota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Chlamydiota_1+I+R8 | Q.YEAST+I+R8 |
| BIC | 16377143.636 | 16435395.336 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Chlamydiota/loop_1/tree_update/Q.p__Chlamydiota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Chlamydiota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 1872.19 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Chlamydiota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Chlamydiota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 18  
Normalized RF distance: 0.0292  
Tree 1 branch length: 93.70802  
Tree 2 branch length: 103.59986  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -8294165.275 | -8340641.383 |
The final model tree has better likelihood than the existing model tree.  
### Pairwise comparison of trees  
![Heatmap of RF distance of trees:](estimated_tree/RF_heatmap.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_heatmap.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 255131.96 seconds (70.87 h)  
