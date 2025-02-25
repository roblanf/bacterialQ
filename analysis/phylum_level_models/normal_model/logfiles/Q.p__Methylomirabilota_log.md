## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Methylomirabilota  
  Taxa name: p__Methylomirabilota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 89  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 89  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Methylomirabilota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Methylomirabilota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Methylomirabilota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/ref_tree.tre -l 15 -u 89 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/subtrees -m split
```
  
Original number of taxa: 89   
Number of pruned subtrees: 1   
Number of taxa after pruning: 89   
Pruned node IDs (degree): 1 (89)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/subtree_update/Q.p__Methylomirabilota
```
  
  Runtime: 5052.97 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Methylomirabilota.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 56 |
| Q.YEAST | 23 |
| Q.PFAM | 22 |
| LG | 12 |
| JTT | 3 |
| WAG | 2 |
| Q.MAMMAL | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/subtree_update/Q.p__Methylomirabilota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/subtree_update/Q.p__Methylomirabilota.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/model_update/Q.p__Methylomirabilota
```
  
  Runtime: 11562.76 seconds  
[Model update log](loop_1/model_update/Q.p__Methylomirabilota.iqtree)  
BIC of the new model: 3368045.863  
Likelihood of the new model: -1589674.5781  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Methylomirabilota_1)  
Model set for next iteration: Q.PLANT,Q.YEAST,Q.PFAM,LG,Q.p__Methylomirabilota_1  
![Model bubble plot](loop_1/Q.p__Methylomirabilota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9121819374239962  
Euclidean distance: 0.944076113018653  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/Q.p__Methylomirabilota_1.treefile
```
  
  Runtime: 719.67 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/Q.p__Methylomirabilota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/Q.p__Methylomirabilota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 20  
Normalized RF distance: 0.1149  
Tree 1 branch length: 9.8715  
Tree 2 branch length: 12.50274  
Time usage for Loop_1: 17378.16 seconds (4.83 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/Q.p__Methylomirabilota_1.treefile -l 15 -u 89 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/subtrees -m split
```
  
Original number of taxa: 89   
Number of pruned subtrees: 1   
Number of taxa after pruning: 89   
Pruned node IDs (degree): 1 (89)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/training_loci -m MFP -mset Q.PLANT,Q.YEAST,Q.PFAM,LG,Q.p__Methylomirabilota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/subtree_update/Q.p__Methylomirabilota
```
  
  Runtime: 2722.65 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Methylomirabilota.iqtree)  
Best models for iteration 2:  
Q.p__Methylomirabilota_1  

| Model | Count |
|-------|-------|
| Q.p__Methylomirabilota_1 | 116 |
| Q.PLANT | 2 |
| LG | 1 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/subtree_update/Q.p__Methylomirabilota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/subtree_update/Q.p__Methylomirabilota.treefile --model-joint GTR20+FO --init-model Q.p__Methylomirabilota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/model_update/Q.p__Methylomirabilota
```
  
  Runtime: 7159.65 seconds  
[Model update log](loop_2/model_update/Q.p__Methylomirabilota.iqtree)  
BIC of the new model: 3367560.5092  
Likelihood of the new model: -1589431.9012  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Methylomirabilota_2)  
Model set for next iteration: Q.PLANT,LG,Q.YEAST,Q.p__Methylomirabilota_2  
![Model bubble plot](loop_2/Q.p__Methylomirabilota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999890587751015  
Euclidean distance: 0.014234962560436892  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/Q.p__Methylomirabilota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 664.81 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 20  
Normalized RF distance: 0.1149  
Tree 1 branch length: 9.8715  
Tree 2 branch length: 12.50502  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Methylomirabilota_1,Q.p__Methylomirabilota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 76920.06 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Methylomirabilota_1+R8 | -1628692.555 | 3259391.167 |
| Q.p__Methylomirabilota_2+R8 | -1628703.075 | 3259412.207 |
| Q.p__Methylomirabilota_1+F+R8 | -1632286.674 | 3266781.072 |
| Q.p__Methylomirabilota_2+F+R8 | -1632375.211 | 3266958.146 |
| Q.INSECT+F+R8 | -1638905.594 | 3280018.912 |
| Q.YEAST+F+R8 | -1640993.069 | 3284193.862 |
| LG+F+R8 | -1643487.907 | 3289183.538 |
| Q.PFAM+F+R8 | -1643511.427 | 3289230.578 |
| JTT+F+R8 | -1644045.941 | 3290299.606 |
| Q.PLANT+F+R8 | -1645020.018 | 3292247.760 |
| WAG+F+R8 | -1651253.686 | 3304715.096 |
| Q.MAMMAL+F+R8 | -1658746.962 | 3319701.648 |
| DCMUT+F+R8 | -1659708.994 | 3321625.712 |
| Q.PFAM+R8 | -1660817.578 | 3323641.213 |
| JTT+R8 | -1661089.399 | 3324184.855 |
| CPREV+F+R8 | -1663712.600 | 3329632.924 |
| MTINV+F+R8 | -1667013.321 | 3336234.366 |
| LG+R8 | -1667189.900 | 3336385.857 |
| LG+I+R8 | -1667190.277 | 3336397.225 |
| LG+R9 | -1667185.767 | 3336398.819 |
| LG+I+R7 | -1667201.935 | 3336399.313 |
| LG+I+R9 | -1667186.119 | 3336410.137 |
| LG+R7 | -1667226.700 | 3336438.229 |
| LG+I+R6 | -1667294.987 | 3336564.189 |
| LG+R6 | -1667360.424 | 3336684.449 |
| Q.PLANT+R8 | -1668183.245 | 3338372.547 |
| Q.BIRD+F+R8 | -1669053.677 | 3340315.078 |
| WAG+R8 | -1669952.845 | 3341911.747 |
| LG+I+G4 | -1670194.677 | 3342268.042 |
| LG+G4 | -1672895.550 | 3347659.174 |
| Q.MAMMAL+R8 | -1673717.275 | 3349440.607 |
| Q.INSECT+R8 | -1674099.685 | 3350205.427 |
| PMB+F+R8 | -1676947.069 | 3356101.862 |
| MTMET+F+R8 | -1677891.361 | 3357990.446 |
| DCMUT+R8 | -1683602.804 | 3369211.665 |
| Q.BIRD+R8 | -1683699.653 | 3369405.363 |
| Q.YEAST+R8 | -1683934.456 | 3369874.969 |
| CPREV+R8 | -1690089.963 | 3382185.983 |
| PMB+R8 | -1695772.986 | 3393552.029 |
| MTVER+F+R8 | -1699020.484 | 3400248.692 |
| LG+I | -1750955.601 | 3503779.276 |
| MTMET+R8 | -1794698.032 | 3591402.121 |
| MTVER+R8 | -1795725.810 | 3593457.677 |
| MTINV+R8 | -1809274.374 | 3620554.805 |
| LG | -1811208.917 | 3624275.294 |
The inferred model Q.p__Methylomirabilota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Methylomirabilota_1+R8 | Q.INSECT+F+R8 |
| BIC | 3259391.167 | 3280018.912 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/Q.p__Methylomirabilota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 311.01 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loop_1/tree_update/Q.p__Methylomirabilota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 316.52 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than Q.INSECT model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Methylomirabilota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.023  
Tree 1 branch length: 12.17893  
Tree 2 branch length: 12.50502  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1703503.225 | -1737258.244 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.INSECT) and final model (Q.p__Methylomirabilota_2):  
Pearson's correlation: 0.8955553093506888  
Euclidean distance: 1.0407166862637847  
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
Total time usage: 105668.00 seconds (29.35 h)  
