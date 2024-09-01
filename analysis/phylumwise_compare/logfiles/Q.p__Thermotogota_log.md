## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Thermotogota  
  Taxa name: p__Thermotogota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 108  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Thermotogota/select_id.txt. Sampling sequences for 118 loci.  
Number of input species: 108  
Remaining 118 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Thermotogota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Thermotogota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Thermotogota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Thermotogota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 118 alignments. Deleted 2 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Thermotogota/ref_tree.tre -l 15 -u 108 -o ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/subtrees -m split
```
  
Original number of taxa: 108   
Number of pruned subtrees: 1   
Number of taxa after pruning: 108   
Pruned node IDs (degree): 1 (108)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/subtree_update/Q.p__Thermotogota
```
  
  Runtime: 14541.15 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Thermotogota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 56 |
| LG | 42 |
| Q.INSECT | 17 |
| Q.PFAM | 3 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/subtree_update/Q.p__Thermotogota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/subtree_update/Q.p__Thermotogota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/model_update/Q.p__Thermotogota
```
  
  Runtime: 18263.68 seconds  
[Model update log](loop_1/model_update/Q.p__Thermotogota.iqtree)  
BIC of the new model: 5481477.5034  
Likelihood of the new model: -2615250.7005  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Thermotogota_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,Q.p__Thermotogota_1  
![Model bubble plot](loop_1/Q.p__Thermotogota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9663517561462385  
Euclidean distance: 0.588920516119007  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Thermotogota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Thermotogota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/tree_update/Q.p__Thermotogota_1.treefile
```
  
  Runtime: 575.08 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/tree_update/Q.p__Thermotogota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Thermotogota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Thermotogota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/tree_update/Q.p__Thermotogota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Thermotogota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0476  
Tree 1 branch length: 16.91519  
Tree 2 branch length: 24.82416  
Time usage for Loop_1: 33417.54 seconds (9.28 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/tree_update/Q.p__Thermotogota_1.treefile -l 15 -u 108 -o ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/subtrees -m split
```
  
Original number of taxa: 108   
Number of pruned subtrees: 1   
Number of taxa after pruning: 108   
Pruned node IDs (degree): 1 (108)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,Q.p__Thermotogota_1 -mdef ../Result_nova/phylum_models/Q.p__Thermotogota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/subtree_update/Q.p__Thermotogota
```
  
  Runtime: 12128.42 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Thermotogota.iqtree)  
Best models for iteration 2:  
Q.p__Thermotogota_1  

| Model | Count |
|-------|-------|
| Q.p__Thermotogota_1 | 115 |
| Q.INSECT | 2 |
| LG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/subtree_update/Q.p__Thermotogota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/subtree_update/Q.p__Thermotogota.treefile --model-joint GTR20+FO --init-model Q.p__Thermotogota_1 -mdef ../Result_nova/phylum_models/Q.p__Thermotogota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/model_update/Q.p__Thermotogota
```
  
  Runtime: 14123.27 seconds  
[Model update log](loop_2/model_update/Q.p__Thermotogota.iqtree)  
BIC of the new model: 5479100.984  
Likelihood of the new model: -2614062.4408  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Thermotogota_2)  
Model set for next iteration: Q.INSECT,LG,Q.p__Thermotogota_2  
![Model bubble plot](loop_2/Q.p__Thermotogota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999334014062422  
Euclidean distance: 0.03234225744589924  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Thermotogota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/tree_update/Q.p__Thermotogota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Thermotogota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 593.77 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Thermotogota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Thermotogota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Thermotogota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Thermotogota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0476  
Tree 1 branch length: 16.91519  
Tree 2 branch length: 24.93941  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Thermotogota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Thermotogota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Thermotogota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Thermotogota_1,Q.p__Thermotogota_2 -mdef ../Result_nova/phylum_models/Q.p__Thermotogota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Thermotogota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 14862.20 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Thermotogota_2+I+R9 | -2662346.131 | 5327128.306 |
| Q.p__Thermotogota_1+I+R9 | -2662352.798 | 5327141.640 |
| Q.p__Thermotogota_1+F+I+R9 | -2672304.106 | 5347245.495 |
| Q.p__Thermotogota_2+F+I+R9 | -2672758.764 | 5348154.811 |
| LG+F+I+R9 | -2675920.880 | 5354479.043 |
| Q.PFAM+F+I+R9 | -2680568.021 | 5363773.325 |
| Q.YEAST+F+I+R9 | -2681409.915 | 5365457.113 |
| Q.YEAST+I+R9 | -2683992.191 | 5370420.426 |
| Q.INSECT+F+I+R9 | -2686667.910 | 5375973.103 |
| Q.INSECT+I+R9 | -2689017.521 | 5380471.086 |
| LG+I+R9 | -2692131.305 | 5386698.654 |
| LG+R9 | -2692146.856 | 5386719.165 |
| LG+I+R8 | -2692181.819 | 5386778.499 |
| LG+R8 | -2692220.228 | 5386844.726 |
| LG+I+R7 | -2692304.868 | 5387003.414 |
| LG+R7 | -2692378.372 | 5387139.831 |
| LG+I+R6 | -2692619.615 | 5387611.725 |
| LG+R6 | -2692909.187 | 5388180.278 |
| WAG+F+I+R9 | -2693313.358 | 5389263.999 |
| JTT+F+I+R9 | -2695682.790 | 5394002.863 |
| Q.PLANT+F+I+R9 | -2696367.877 | 5395373.037 |
| LG+I+G4 | -2697192.214 | 5396661.600 |
| Q.PFAM+I+R9 | -2700761.180 | 5403958.404 |
| CPREV+F+I+R9 | -2700972.182 | 5404581.647 |
| LG+G4 | -2701565.837 | 5405398.254 |
| CPREV+I+R9 | -2706879.836 | 5416195.716 |
| Q.PLANT+I+R9 | -2707244.427 | 5416924.898 |
| MTINV+F+I+R9 | -2707777.075 | 5418191.433 |
| WAG+I+R9 | -2717407.906 | 5437251.856 |
| DCMUT+F+I+R9 | -2717824.867 | 5438287.017 |
| JTT+I+R9 | -2719057.126 | 5440550.296 |
| Q.MAMMAL+F+I+R9 | -2719137.540 | 5440912.363 |
| PMB+F+I+R9 | -2720224.512 | 5443086.307 |
| MTMET+F+I+R9 | -2724450.255 | 5451537.793 |
| Q.BIRD+F+I+R9 | -2736871.814 | 5476380.911 |
| PMB+I+R9 | -2741997.974 | 5486431.992 |
| Q.MAMMAL+I+R9 | -2743592.223 | 5489620.490 |
| DCMUT+I+R9 | -2753445.602 | 5509327.248 |
| Q.BIRD+I+R9 | -2759429.456 | 5521294.956 |
| MTVER+F+I+R9 | -2774712.888 | 5552063.059 |
| MTINV+I+R9 | -2820017.709 | 5642471.462 |
| MTMET+I+R9 | -2820550.838 | 5643537.720 |
| LG+I | -2855713.372 | 5713693.324 |
| MTVER+I+R9 | -2874864.730 | 5752165.504 |
| LG | -2928875.367 | 5860006.723 |
The inferred model Q.p__Thermotogota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Thermotogota_2+I+R9 | LG+F+I+R9 |
| BIC | 5327128.306 | 5354479.043 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Thermotogota/loop_1/tree_update/Q.p__Thermotogota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Thermotogota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 490.71 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Thermotogota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Thermotogota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Thermotogota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Thermotogota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 22.11759  
Tree 2 branch length: 24.93941  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2736085.732 | -2763553.187 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Thermotogota_2):  
Pearson's correlation: 0.9497142517485853  
Euclidean distance: 0.7443886882950363  
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
Total time usage: 75814.13 seconds (21.06 h)  
