## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_F  
  Taxa name: p__Bacillota_F  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 60  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 60  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_F  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_F -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota_F
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/ref_tree.tre -l 15 -u 60 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/subtrees -m split
```
  
Original number of taxa: 60   
Number of pruned subtrees: 1   
Number of taxa after pruning: 60   
Pruned node IDs (degree): 1 (60)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/subtree_update/Q.p__Bacillota_F
```
  
  Runtime: 9469.85 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_F.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 68 |
| Q.YEAST | 39 |
| Q.PLANT | 6 |
| Q.PFAM | 3 |
| CPREV | 2 |
| WAG | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/subtree_update/Q.p__Bacillota_F.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/subtree_update/Q.p__Bacillota_F.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/model_update/Q.p__Bacillota_F
```
  
  Runtime: 12786.08 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_F.iqtree)  
BIC of the new model: 3192775.4421  
Likelihood of the new model: -1527979.508  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_F_1)  
Model set for next iteration: LG,Q.YEAST,Q.PLANT,Q.p__Bacillota_F_1  
![Model bubble plot](loop_1/Q.p__Bacillota_F_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9607921662656231  
Euclidean distance: 0.6038540970633806  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/tree_update/Q.p__Bacillota_F_1.treefile
```
  
  Runtime: 396.65 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/tree_update/Q.p__Bacillota_F_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/tree_update/Q.p__Bacillota_F_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0862  
Tree 1 branch length: 9.12357  
Tree 2 branch length: 13.20274  
Time usage for Loop_1: 22692.88 seconds (6.30 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/tree_update/Q.p__Bacillota_F_1.treefile -l 15 -u 60 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/subtrees -m split
```
  
Original number of taxa: 60   
Number of pruned subtrees: 1   
Number of taxa after pruning: 60   
Pruned node IDs (degree): 1 (60)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PLANT,Q.p__Bacillota_F_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/subtree_update/Q.p__Bacillota_F
```
  
  Runtime: 2316.87 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_F.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_F_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_F_1 | 113 |
| LG | 4 |
| Q.YEAST | 2 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/subtree_update/Q.p__Bacillota_F.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/subtree_update/Q.p__Bacillota_F.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_F_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/model_update/Q.p__Bacillota_F
```
  
  Runtime: 5999.61 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_F.iqtree)  
BIC of the new model: 3192836.6991  
Likelihood of the new model: -1528010.1365  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_F_2)  
Model set for next iteration: LG,Q.YEAST,Q.PLANT,Q.p__Bacillota_F_2  
![Model bubble plot](loop_2/Q.p__Bacillota_F_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9996382494155344  
Euclidean distance: 0.05630158086493666  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/tree_update/Q.p__Bacillota_F_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 343.51 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0862  
Tree 1 branch length: 9.12357  
Tree 2 branch length: 13.22469  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_F_1,Q.p__Bacillota_F_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 29766.10 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bacillota_F_2+R8 | -1561015.572 | 3123420.305 |
| Q.p__Bacillota_F_2+I+R7 | -1561021.909 | 3123422.374 |
| Q.p__Bacillota_F_1+R8 | -1561033.144 | 3123455.449 |
| Q.p__Bacillota_F_1+I+R7 | -1561039.026 | 3123456.608 |
| Q.p__Bacillota_F_1+F+R8 | -1564582.818 | 3130756.278 |
| Q.p__Bacillota_F_1+F+I+R7 | -1564588.913 | 3130757.864 |
| Q.p__Bacillota_F_2+F+R8 | -1564659.699 | 3130910.040 |
| Q.p__Bacillota_F_2+F+I+R7 | -1564665.285 | 3130910.608 |
| LG+F+I+R7 | -1568513.365 | 3138606.768 |
| LG+F+R8 | -1568509.582 | 3138609.806 |
| Q.PFAM+F+I+R7 | -1571340.352 | 3144260.742 |
| Q.PFAM+F+R8 | -1571335.201 | 3144261.044 |
| WAG+F+R8 | -1574484.841 | 3150560.324 |
| WAG+F+I+R7 | -1574491.293 | 3150562.624 |
| LG+I+R7 | -1575904.146 | 3153186.848 |
| LG+R8 | -1575900.736 | 3153190.633 |
| LG+I+R8 | -1575899.230 | 3153198.225 |
| LG+R9 | -1575900.150 | 3153210.669 |
| LG+R7 | -1575932.049 | 3153232.050 |
| Q.YEAST+F+I+R7 | -1575842.819 | 3153265.676 |
| Q.YEAST+F+R8 | -1575838.344 | 3153267.330 |
| LG+I+R6 | -1575985.835 | 3153329.018 |
| LG+R6 | -1576043.339 | 3153433.422 |
| CPREV+F+R8 | -1576330.678 | 3154251.998 |
| CPREV+F+I+R7 | -1576343.922 | 3154267.882 |
| Q.YEAST+I+R7 | -1576714.220 | 3154806.996 |
| Q.YEAST+R8 | -1576711.441 | 3154812.043 |
| LG+I+G4 | -1578122.215 | 3157506.339 |
| LG+G4 | -1580745.867 | 3162743.039 |
| Q.PFAM+I+R7 | -1580862.653 | 3163103.862 |
| Q.PFAM+R8 | -1580859.426 | 3163108.013 |
| JTT+F+R8 | -1580846.198 | 3163283.038 |
| JTT+F+I+R7 | -1580852.551 | 3163285.140 |
| Q.INSECT+F+R8 | -1581027.877 | 3163646.396 |
| Q.INSECT+F+I+R7 | -1581034.404 | 3163648.846 |
| Q.INSECT+R8 | -1582000.213 | 3165389.587 |
| Q.INSECT+I+R7 | -1582005.915 | 3165390.386 |
| Q.PLANT+F+R8 | -1582034.481 | 3165659.604 |
| Q.PLANT+F+I+R7 | -1582048.478 | 3165676.994 |
| CPREV+R8 | -1582572.488 | 3166534.137 |
| CPREV+I+R7 | -1582583.235 | 3166545.026 |
| WAG+I+R7 | -1585952.058 | 3173282.672 |
| WAG+R8 | -1585947.863 | 3173284.887 |
| Q.PLANT+R8 | -1587815.087 | 3177019.335 |
| Q.PLANT+I+R7 | -1587829.003 | 3177036.562 |
| MTINV+F+R8 | -1588133.093 | 3177856.828 |
| MTINV+F+I+R7 | -1588150.544 | 3177881.126 |
| JTT+I+R7 | -1592422.695 | 3186223.946 |
| JTT+R8 | -1592419.863 | 3186228.887 |
| PMB+F+I+R7 | -1594615.782 | 3190811.602 |
| PMB+F+R8 | -1594613.511 | 3190817.664 |
| DCMUT+F+R8 | -1594877.140 | 3191344.922 |
| DCMUT+F+I+R7 | -1594888.927 | 3191357.892 |
| MTMET+F+R8 | -1595085.908 | 3191762.458 |
| MTMET+F+I+R7 | -1595116.231 | 3191812.500 |
| Q.MAMMAL+F+R8 | -1597785.892 | 3197162.426 |
| Q.MAMMAL+F+I+R7 | -1597801.413 | 3197182.864 |
| Q.BIRD+F+R8 | -1605930.146 | 3213450.934 |
| Q.BIRD+F+I+R7 | -1605955.170 | 3213490.378 |
| DCMUT+R8 | -1610366.875 | 3222122.911 |
| DCMUT+I+R7 | -1610377.934 | 3222134.424 |
| PMB+I+R7 | -1610671.941 | 3222722.438 |
| PMB+R8 | -1610669.649 | 3222728.459 |
| Q.MAMMAL+R8 | -1611092.729 | 3223574.619 |
| Q.MAMMAL+I+R7 | -1611108.318 | 3223595.192 |
| MTVER+F+R8 | -1614684.108 | 3230958.858 |
| MTVER+F+I+R7 | -1614745.337 | 3231070.712 |
| Q.BIRD+R8 | -1617579.710 | 3236548.581 |
| Q.BIRD+I+R7 | -1617601.070 | 3236580.696 |
| LG+I | -1659384.252 | 3320019.809 |
| MTMET+R8 | -1665139.321 | 3331667.803 |
| MTMET+I+R7 | -1665176.606 | 3331731.768 |
| MTINV+R8 | -1671430.728 | 3344250.617 |
| MTINV+I+R7 | -1671449.167 | 3344276.890 |
| MTVER+R8 | -1680335.450 | 3362060.061 |
| MTVER+I+R7 | -1680387.808 | 3362154.172 |
| LG | -1722071.492 | 3445383.685 |
The inferred model Q.p__Bacillota_F_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bacillota_F_2+R8 | LG+F+I+R7 |
| BIC | 3123420.305 | 3138606.768 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loop_1/tree_update/Q.p__Bacillota_F_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 257.75 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_F/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 12.33978  
Tree 2 branch length: 13.22469  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1629133.436 | -1642387.486 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bacillota_F_2):  
Pearson's correlation: 0.9605969255613073  
Euclidean distance: 0.6077715443081343  
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
Total time usage: 61571.04 seconds (17.10 h)  
