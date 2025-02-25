## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bdellovibrionota  
  Taxa name: p__Bdellovibrionota  
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
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 544  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bdellovibrionota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bdellovibrionota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Bdellovibrionota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/subtrees -m split
```
  
Original number of taxa: 544   
Number of pruned subtrees: 4   
Number of taxa after pruning: 544   
Pruned node IDs (degree): 166 (212) 4 (163) 408 (137) 377 (32)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 4 subtree files and 120 loci files. Total number of potential alignments: 480.  
Obtained 479 alignments from all potential alignments.  
Remaining 479 alignments. Deleted 1 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/subtree_update/Q.p__Bdellovibrionota
```
  
  Runtime: 39923.09 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bdellovibrionota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 325 |
| LG | 102 |
| Q.PFAM | 49 |
| WAG | 2 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/subtree_update/Q.p__Bdellovibrionota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/subtree_update/Q.p__Bdellovibrionota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/model_update/Q.p__Bdellovibrionota
```
  
  Runtime: 32954.78 seconds  
[Model update log](loop_1/model_update/Q.p__Bdellovibrionota.iqtree)  
BIC of the new model: 31662072.5091  
Likelihood of the new model: -15176182.7183  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bdellovibrionota_1)  
Model set for next iteration: Q.YEAST,LG,Q.PFAM,Q.p__Bdellovibrionota_1  
![Model bubble plot](loop_1/Q.p__Bdellovibrionota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9830393404094878  
Euclidean distance: 0.4313377995506942  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/Q.p__Bdellovibrionota_1.treefile
```
  
  Runtime: 3030.34 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/Q.p__Bdellovibrionota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/Q.p__Bdellovibrionota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 162  
Normalized RF distance: 0.1494  
Tree 1 branch length: 123.14296  
Tree 2 branch length: 172.54942  
Time usage for Loop_1: 76032.23 seconds (21.12 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/Q.p__Bdellovibrionota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/subtrees -m split
```
  
Original number of taxa: 544   
Number of pruned subtrees: 5   
Number of taxa after pruning: 528   
Pruned node IDs (degree): 6 (163) 247 (147) 393 (125) 170 (65) 517 (28)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 5 subtree files and 120 loci files. Total number of potential alignments: 600.  
Obtained 594 alignments from all potential alignments.  
Remaining 594 alignments. Deleted 6 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.PFAM,Q.p__Bdellovibrionota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/subtree_update/Q.p__Bdellovibrionota
```
  
  Runtime: 24882.12 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bdellovibrionota.iqtree)  
Best models for iteration 2:  
Q.p__Bdellovibrionota_1  

| Model | Count |
|-------|-------|
| Q.p__Bdellovibrionota_1 | 507 |
| LG | 35 |
| Q.PFAM | 27 |
| Q.YEAST | 25 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/subtree_update/Q.p__Bdellovibrionota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/subtree_update/Q.p__Bdellovibrionota.treefile --model-joint GTR20+FO --init-model Q.p__Bdellovibrionota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/model_update/Q.p__Bdellovibrionota
```
  
  Runtime: 28689.33 seconds  
[Model update log](loop_2/model_update/Q.p__Bdellovibrionota.iqtree)  
BIC of the new model: 30419133.0129  
Likelihood of the new model: -14564132.8439  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bdellovibrionota_2)  
Model set for next iteration: LG,Q.PFAM,Q.YEAST,Q.p__Bdellovibrionota_2  
![Model bubble plot](loop_2/Q.p__Bdellovibrionota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9994550590247245  
Euclidean distance: 0.08192660853463204  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/Q.p__Bdellovibrionota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 2239.90 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 166  
Normalized RF distance: 0.1531  
Tree 1 branch length: 123.14296  
Tree 2 branch length: 175.06622  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bdellovibrionota_1,Q.p__Bdellovibrionota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 115768.49 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bdellovibrionota_1+I+R9 | -15340177.640 | 30692060.117 |
| Q.p__Bdellovibrionota_2+I+R9 | -15343448.180 | 30698601.197 |
| Q.YEAST+I+R9 | -15380163.750 | 30772032.337 |
| Q.p__Bdellovibrionota_1+F+I+R9 | -15394920.070 | 30801746.785 |
| Q.p__Bdellovibrionota_2+F+I+R9 | -15399593.220 | 30811093.085 |
| Q.INSECT+I+R9 | -15404466.920 | 30820638.677 |
| LG+I+R9 | -15408388.330 | 30828481.497 |
| LG+F+I+R9 | -15408429.180 | 30828765.005 |
| LG+R9 | -15410151.320 | 30831996.856 |
| Q.PFAM+I+R9 | -15411530.070 | 30834764.977 |
| LG+I+R8 | -15413336.300 | 30838356.194 |
| LG+R8 | -15415846.190 | 30843365.353 |
| Q.PFAM+F+I+R9 | -15415839.160 | 30843584.965 |
| LG+I+R7 | -15420731.410 | 30853125.171 |
| LG+R7 | -15424806.630 | 30861264.990 |
| Q.YEAST+F+I+R9 | -15426369.710 | 30864646.065 |
| LG+I+R6 | -15433572.010 | 30878785.128 |
| LG+R6 | -15439847.960 | 30891326.407 |
| Q.INSECT+F+I+R9 | -15458720.170 | 30929346.985 |
| LG+I+G4 | -15504494.180 | 31020533.875 |
| WAG+I+R9 | -15505648.930 | 31023002.697 |
| WAG+F+I+R9 | -15506827.070 | 31025560.785 |
| LG+G4 | -15528905.810 | 31069346.514 |
| JTT+F+I+R9 | -15608993.800 | 31229894.245 |
| Q.PLANT+I+R9 | -15615598.660 | 31242902.157 |
| JTT+I+R9 | -15620723.570 | 31253151.977 |
| PMB+F+I+R9 | -15631367.080 | 31274640.805 |
| CPREV+I+R9 | -15633398.970 | 31278502.777 |
| PMB+I+R9 | -15637943.370 | 31287591.577 |
| Q.PLANT+F+I+R9 | -15649241.640 | 31310389.925 |
| DCMUT+F+I+R9 | -15653947.510 | 31319801.665 |
| CPREV+F+I+R9 | -15663655.800 | 31339218.245 |
| MTINV+F+I+R9 | -15677186.710 | 31366280.065 |
| DCMUT+I+R9 | -15682681.010 | 31377066.857 |
| MTMET+F+I+R9 | -15827694.140 | 31667294.925 |
| Q.MAMMAL+I+R9 | -15828062.050 | 31667828.937 |
| Q.MAMMAL+F+I+R9 | -15842676.970 | 31697260.585 |
| Q.BIRD+I+R9 | -15986617.530 | 31984939.897 |
| Q.BIRD+F+I+R9 | -16003239.860 | 32018386.365 |
| MTVER+F+I+R9 | -16134477.070 | 32280860.785 |
| MTINV+I+R9 | -16285914.070 | 32583532.977 |
| MTMET+I+R9 | -16290029.480 | 32591763.797 |
| MTVER+I+R9 | -16520290.350 | 33052285.537 |
| LG+I | -16837858.270 | 33687251.434 |
| LG | -17076707.090 | 34164938.452 |
The inferred model Q.p__Bdellovibrionota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bdellovibrionota_1+I+R9 | Q.YEAST+I+R9 |
| BIC | 30692060.117 | 30772032.337 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/Q.p__Bdellovibrionota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 2889.93 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loop_1/tree_update/Q.p__Bdellovibrionota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 2762.14 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
Q.YEAST model has higher likelihood than LG model, use best_existing_model model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/allloci_best_existing_model_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bdellovibrionota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 16  
Normalized RF distance: 0.0148  
Tree 1 branch length: 166.08284  
Tree 2 branch length: 175.06622  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -15407143.965 | -15444648.687 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.YEAST) and final model (Q.p__Bdellovibrionota_2):  
Pearson's correlation: 0.9821552621305829  
Euclidean distance: 0.4628288048453785  
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
Total time usage: 253567.41 seconds (70.44 h)  
