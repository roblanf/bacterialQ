## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Latescibacterota  
  Taxa name: p__Latescibacterota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 82  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 82  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Latescibacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Latescibacterota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Zixibacteria as the outgroup for Phylum Latescibacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/ref_tree.tre -l 15 -u 82 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 82   
Number of pruned subtrees: 1   
Number of taxa after pruning: 82   
Pruned node IDs (degree): 1 (82)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/subtree_update/Q.p__Latescibacterota
```
  
  Runtime: 4143.72 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Latescibacterota.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 40 |
| Q.PFAM | 38 |
| LG | 28 |
| Q.YEAST | 9 |
| WAG | 3 |
| JTT | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/subtree_update/Q.p__Latescibacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/subtree_update/Q.p__Latescibacterota.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/model_update/Q.p__Latescibacterota
```
  
  Runtime: 11067.69 seconds  
[Model update log](loop_1/model_update/Q.p__Latescibacterota.iqtree)  
BIC of the new model: 3551363.4832  
Likelihood of the new model: -1687887.6568  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Latescibacterota_1)  
Model set for next iteration: Q.PLANT,Q.PFAM,LG,Q.YEAST,Q.p__Latescibacterota_1  
![Model bubble plot](loop_1/Q.p__Latescibacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9530675390834542  
Euclidean distance: 0.6233990447203666  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/tree_update/Q.p__Latescibacterota_1.treefile
```
  
  Runtime: 561.23 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/tree_update/Q.p__Latescibacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/tree_update/Q.p__Latescibacterota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 20  
Normalized RF distance: 0.125  
Tree 1 branch length: 11.62898  
Tree 2 branch length: 15.23391  
Time usage for Loop_1: 15816.70 seconds (4.39 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/tree_update/Q.p__Latescibacterota_1.treefile -l 15 -u 82 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 82   
Number of pruned subtrees: 1   
Number of taxa after pruning: 82   
Pruned node IDs (degree): 1 (82)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/training_loci -m MFP -mset Q.PLANT,Q.PFAM,LG,Q.YEAST,Q.p__Latescibacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/subtree_update/Q.p__Latescibacterota
```
  
  Runtime: 5233.96 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Latescibacterota.iqtree)  
Best models for iteration 2:  
Q.p__Latescibacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Latescibacterota_1 | 114 |
| Q.PLANT | 3 |
| LG | 2 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/subtree_update/Q.p__Latescibacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/subtree_update/Q.p__Latescibacterota.treefile --model-joint GTR20+FO --init-model Q.p__Latescibacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/model_update/Q.p__Latescibacterota
```
  
  Runtime: 9810.90 seconds  
[Model update log](loop_2/model_update/Q.p__Latescibacterota.iqtree)  
BIC of the new model: 3546427.7224  
Likelihood of the new model: -1685419.7763  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Latescibacterota_2)  
Model set for next iteration: Q.PLANT,LG,Q.YEAST,Q.p__Latescibacterota_2  
![Model bubble plot](loop_2/Q.p__Latescibacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999575707819245  
Euclidean distance: 0.018936685110026816  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/tree_update/Q.p__Latescibacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 610.37 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 20  
Normalized RF distance: 0.125  
Tree 1 branch length: 11.62898  
Tree 2 branch length: 15.2258  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Latescibacterota_1,Q.p__Latescibacterota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 118378.51 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Latescibacterota_2+R7 | -1736885.098 | 3475606.759 |
| Q.p__Latescibacterota_2+I+R7 | -1736880.155 | 3475607.489 |
| Q.p__Latescibacterota_1+R7 | -1736902.459 | 3475641.481 |
| Q.p__Latescibacterota_1+I+R7 | -1736897.748 | 3475642.675 |
| Q.p__Latescibacterota_1+F+R7 | -1738882.961 | 3479804.189 |
| Q.p__Latescibacterota_2+F+R7 | -1738883.248 | 3479804.763 |
| Q.p__Latescibacterota_2+F+I+R7 | -1738879.030 | 3479806.943 |
| Q.p__Latescibacterota_1+F+I+R7 | -1738879.198 | 3479807.279 |
| LG+F+R7 | -1743852.565 | 3489743.397 |
| LG+F+I+R7 | -1743852.262 | 3489753.407 |
| Q.PFAM+F+R7 | -1744352.803 | 3490743.873 |
| Q.PFAM+F+I+R7 | -1744353.886 | 3490756.655 |
| Q.YEAST+F+R7 | -1745579.346 | 3493196.959 |
| Q.YEAST+F+I+R7 | -1745576.929 | 3493202.741 |
| Q.INSECT+F+R7 | -1746866.316 | 3495770.899 |
| Q.INSECT+F+I+R7 | -1746863.525 | 3495775.933 |
| Q.PFAM+R7 | -1748323.781 | 3498484.125 |
| Q.PFAM+I+R7 | -1748324.852 | 3498496.883 |
| WAG+F+R7 | -1750473.209 | 3502984.685 |
| WAG+F+I+R7 | -1750477.394 | 3503003.671 |
| LG+R7 | -1751054.719 | 3503946.001 |
| LG+I+R7 | -1751050.530 | 3503948.239 |
| LG+R8 | -1751049.306 | 3503956.407 |
| LG+I+R8 | -1751048.468 | 3503965.347 |
| LG+I+R6 | -1751094.912 | 3504015.771 |
| LG+R6 | -1751188.756 | 3504192.843 |
| JTT+F+R7 | -1751579.377 | 3505197.021 |
| JTT+F+I+R7 | -1751577.433 | 3505203.749 |
| LG+I+G4 | -1753343.010 | 3508416.423 |
| Q.PLANT+F+I+R7 | -1753560.192 | 3509169.267 |
| Q.PLANT+F+R7 | -1753566.714 | 3509171.695 |
| LG+G4 | -1755213.420 | 3512146.627 |
| JTT+I+R7 | -1756120.368 | 3514087.915 |
| JTT+R7 | -1756126.194 | 3514088.951 |
| WAG+R7 | -1757490.431 | 3516817.425 |
| WAG+I+R7 | -1757495.114 | 3516837.407 |
| Q.INSECT+I+R7 | -1757714.828 | 3517276.835 |
| Q.INSECT+R7 | -1757721.030 | 3517278.623 |
| Q.PLANT+I+R7 | -1758928.426 | 3519704.031 |
| Q.PLANT+R7 | -1758937.701 | 3519711.965 |
| CPREV+F+I+R7 | -1759971.673 | 3521992.229 |
| CPREV+F+R7 | -1759999.980 | 3522038.227 |
| Q.YEAST+R7 | -1763026.681 | 3527889.925 |
| Q.YEAST+I+R7 | -1763023.266 | 3527893.711 |
| DCMUT+F+I+R7 | -1766817.602 | 3535684.087 |
| DCMUT+F+R7 | -1766835.813 | 3535709.893 |
| Q.MAMMAL+F+I+R7 | -1767443.710 | 3536936.303 |
| Q.MAMMAL+F+R7 | -1767477.863 | 3536993.993 |
| MTINV+F+I+R7 | -1769644.951 | 3541338.785 |
| MTINV+F+R7 | -1769654.728 | 3541347.723 |
| CPREV+I+R7 | -1769857.041 | 3541561.261 |
| Q.MAMMAL+I+R7 | -1769868.447 | 3541584.073 |
| CPREV+R7 | -1769879.905 | 3541596.373 |
| Q.MAMMAL+R7 | -1769898.941 | 3541634.445 |
| PMB+F+R7 | -1773001.456 | 3548041.179 |
| PMB+F+I+R7 | -1773004.684 | 3548058.251 |
| DCMUT+I+R7 | -1778746.018 | 3559339.215 |
| MTMET+F+I+R7 | -1778655.598 | 3559360.079 |
| DCMUT+R7 | -1778776.720 | 3559390.003 |
| MTMET+F+R7 | -1778677.285 | 3559392.837 |
| Q.BIRD+F+I+R7 | -1779069.571 | 3560188.025 |
| Q.BIRD+F+R7 | -1779130.459 | 3560299.185 |
| PMB+R7 | -1779353.904 | 3560544.371 |
| PMB+I+R7 | -1779358.757 | 3560564.693 |
| Q.BIRD+I+R7 | -1781149.419 | 3564146.017 |
| Q.BIRD+R7 | -1781207.806 | 3564252.175 |
| MTVER+F+I+R7 | -1799553.350 | 3601155.583 |
| MTVER+F+R7 | -1799596.104 | 3601230.475 |
| LG+I | -1834976.292 | 3671672.371 |
| MTMET+I+R7 | -1869316.441 | 3740480.061 |
| MTMET+R7 | -1869357.083 | 3740550.729 |
| MTVER+I+R7 | -1877576.096 | 3756999.371 |
| MTVER+R7 | -1877643.459 | 3757123.481 |
| MTINV+I+R7 | -1881511.691 | 3764870.561 |
| MTINV+R7 | -1881528.924 | 3764894.411 |
| LG | -1882514.606 | 3766738.383 |
The inferred model Q.p__Latescibacterota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Latescibacterota_2+R7 | LG+F+R7 |
| BIC | 3475606.759 | 3489743.397 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loop_1/tree_update/Q.p__Latescibacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 214.33 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Latescibacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 14.64981  
Tree 2 branch length: 15.2258  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1799374.664 | -1812967.161 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Latescibacterota_2):  
Pearson's correlation: 0.9592150961494647  
Euclidean distance: 0.5959332600432496  
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
Total time usage: 150264.54 seconds (41.74 h)  
