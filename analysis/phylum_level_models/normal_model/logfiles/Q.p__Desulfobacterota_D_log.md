## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Desulfobacterota_D  
  Taxa name: p__Desulfobacterota_D  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 55  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 55  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Desulfobacterota_D  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Desulfobacterota_D -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Desulfobacterota_D
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/ref_tree.tre -l 15 -u 55 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/subtrees -m split
```
  
Original number of taxa: 55   
Number of pruned subtrees: 1   
Number of taxa after pruning: 55   
Pruned node IDs (degree): 1 (55)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/subtree_update/Q.p__Desulfobacterota_D
```
  
  Runtime: 6772.96 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Desulfobacterota_D.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 75 |
| Q.PLANT | 34 |
| LG | 4 |
| JTT | 4 |
| CPREV | 2 |
| Q.PFAM | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/subtree_update/Q.p__Desulfobacterota_D.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/subtree_update/Q.p__Desulfobacterota_D.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/model_update/Q.p__Desulfobacterota_D
```
  
  Runtime: 4676.72 seconds  
[Model update log](loop_1/model_update/Q.p__Desulfobacterota_D.iqtree)  
BIC of the new model: 2655016.5085  
Likelihood of the new model: -1265262.2876  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Desulfobacterota_D_1)  
Model set for next iteration: Q.YEAST,Q.PLANT,Q.p__Desulfobacterota_D_1  
![Model bubble plot](loop_1/Q.p__Desulfobacterota_D_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9632896264148927  
Euclidean distance: 0.5956751238121574  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/tree_update/Q.p__Desulfobacterota_D_1.treefile
```
  
  Runtime: 232.59 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/tree_update/Q.p__Desulfobacterota_D_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/tree_update/Q.p__Desulfobacterota_D_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0566  
Tree 1 branch length: 7.64105  
Tree 2 branch length: 11.14072  
Time usage for Loop_1: 11712.78 seconds (3.25 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/tree_update/Q.p__Desulfobacterota_D_1.treefile -l 15 -u 55 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/subtrees -m split
```
  
Original number of taxa: 55   
Number of pruned subtrees: 1   
Number of taxa after pruning: 55   
Pruned node IDs (degree): 1 (55)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/training_loci -m MFP -mset Q.YEAST,Q.PLANT,Q.p__Desulfobacterota_D_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/subtree_update/Q.p__Desulfobacterota_D
```
  
  Runtime: 1371.46 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Desulfobacterota_D.iqtree)  
Best models for iteration 2:  
Q.p__Desulfobacterota_D_1  

| Model | Count |
|-------|-------|
| Q.p__Desulfobacterota_D_1 | 112 |
| Q.YEAST | 5 |
| Q.PLANT | 3 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/subtree_update/Q.p__Desulfobacterota_D.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/subtree_update/Q.p__Desulfobacterota_D.treefile --model-joint GTR20+FO --init-model Q.p__Desulfobacterota_D_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/model_update/Q.p__Desulfobacterota_D
```
  
  Runtime: 3856.06 seconds  
[Model update log](loop_2/model_update/Q.p__Desulfobacterota_D.iqtree)  
BIC of the new model: 2654766.0939  
Likelihood of the new model: -1265137.0802  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Desulfobacterota_D_2)  
Model set for next iteration: Q.YEAST,Q.PLANT,Q.p__Desulfobacterota_D_2  
![Model bubble plot](loop_2/Q.p__Desulfobacterota_D_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999619385197721  
Euclidean distance: 0.021769495579391285  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/tree_update/Q.p__Desulfobacterota_D_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 244.23 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0566  
Tree 1 branch length: 7.64105  
Tree 2 branch length: 11.15977  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Desulfobacterota_D_1,Q.p__Desulfobacterota_D_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 22991.98 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Desulfobacterota_D_1+R7 | -1291535.528 | 2584334.018 |
| Q.p__Desulfobacterota_D_1+I+R6 | -1291550.527 | 2584353.403 |
| Q.p__Desulfobacterota_D_2+R7 | -1291548.029 | 2584359.020 |
| Q.p__Desulfobacterota_D_2+I+R6 | -1291563.077 | 2584378.503 |
| Q.p__Desulfobacterota_D_1+F+R7 | -1295772.187 | 2593008.985 |
| Q.p__Desulfobacterota_D_1+F+I+R6 | -1295784.909 | 2593023.816 |
| Q.p__Desulfobacterota_D_2+F+R7 | -1295869.085 | 2593202.781 |
| Q.p__Desulfobacterota_D_2+F+I+R6 | -1295881.860 | 2593217.718 |
| LG+F+R7 | -1299299.414 | 2600063.439 |
| LG+F+I+R6 | -1299307.558 | 2600069.114 |
| Q.YEAST+F+R7 | -1300194.514 | 2601853.639 |
| Q.YEAST+F+I+R6 | -1300204.694 | 2601863.386 |
| Q.PFAM+F+R7 | -1300633.808 | 2602732.227 |
| Q.PFAM+F+I+R6 | -1300642.336 | 2602738.670 |
| Q.PLANT+F+R7 | -1300736.528 | 2602937.667 |
| Q.PLANT+F+I+R6 | -1300749.509 | 2602953.016 |
| Q.YEAST+R7 | -1301261.771 | 2603786.504 |
| Q.YEAST+I+R6 | -1301272.612 | 2603797.573 |
| Q.INSECT+F+R7 | -1301637.450 | 2604739.511 |
| Q.INSECT+F+I+R6 | -1301647.636 | 2604749.270 |
| JTT+F+R7 | -1301800.633 | 2605065.877 |
| JTT+F+I+R6 | -1301809.145 | 2605072.288 |
| WAG+F+R7 | -1303775.276 | 2609015.163 |
| WAG+F+I+R6 | -1303783.245 | 2609020.488 |
| Q.INSECT+R7 | -1303911.079 | 2609085.120 |
| Q.INSECT+I+R6 | -1303921.714 | 2609095.777 |
| Q.PLANT+R7 | -1305734.148 | 2612731.258 |
| Q.PLANT+I+R6 | -1305747.892 | 2612748.133 |
| CPREV+F+R7 | -1306827.626 | 2615119.863 |
| CPREV+F+I+R6 | -1306841.356 | 2615136.710 |
| LG+R7 | -1307373.121 | 2616009.204 |
| LG+I+R6 | -1307380.876 | 2616014.101 |
| LG+I+R7 | -1307373.711 | 2616020.997 |
| LG+R8 | -1307372.129 | 2616028.446 |
| LG+R6 | -1307422.776 | 2616087.287 |
| LG+I+G4 | -1309022.932 | 2619202.694 |
| MTINV+F+R7 | -1309373.964 | 2620212.539 |
| MTINV+F+I+R6 | -1309385.856 | 2620225.710 |
| Q.PFAM+R7 | -1309719.436 | 2620701.834 |
| Q.PFAM+I+R6 | -1309726.960 | 2620706.269 |
| LG+G4 | -1310536.822 | 2622219.861 |
| CPREV+R7 | -1310789.411 | 2622841.784 |
| CPREV+I+R6 | -1310800.322 | 2622852.993 |
| Q.MAMMAL+F+R7 | -1311069.244 | 2623603.099 |
| Q.MAMMAL+F+I+R6 | -1311080.186 | 2623614.370 |
| JTT+R7 | -1312147.346 | 2625557.654 |
| JTT+I+R6 | -1312155.494 | 2625563.337 |
| DCMUT+F+R7 | -1312829.160 | 2627122.931 |
| DCMUT+F+I+R6 | -1312843.401 | 2627140.800 |
| MTMET+F+R7 | -1314101.370 | 2629667.351 |
| MTMET+F+I+R6 | -1314117.746 | 2629689.490 |
| WAG+R7 | -1314462.241 | 2630187.444 |
| WAG+I+R6 | -1314469.229 | 2630190.807 |
| Q.BIRD+F+R7 | -1317043.837 | 2635552.285 |
| Q.BIRD+F+I+R6 | -1317058.518 | 2635571.034 |
| PMB+F+R7 | -1320165.350 | 2641795.311 |
| PMB+F+I+R6 | -1320175.588 | 2641805.174 |
| Q.MAMMAL+R7 | -1322740.898 | 2646744.758 |
| Q.MAMMAL+I+R6 | -1322751.293 | 2646754.935 |
| DCMUT+R7 | -1327287.785 | 2655838.532 |
| DCMUT+I+R6 | -1327302.674 | 2655857.697 |
| Q.BIRD+R7 | -1327823.516 | 2656909.994 |
| Q.BIRD+I+R6 | -1327837.472 | 2656927.293 |
| PMB+R7 | -1331512.615 | 2664288.192 |
| PMB+I+R6 | -1331522.731 | 2664297.811 |
| MTVER+F+R7 | -1331611.339 | 2664687.289 |
| MTVER+F+I+R6 | -1331639.236 | 2664732.470 |
| LG+I | -1364433.294 | 2730012.805 |
| MTMET+R7 | -1366569.537 | 2734402.036 |
| MTMET+I+R6 | -1366588.858 | 2734430.065 |
| MTINV+R7 | -1370104.093 | 2741471.148 |
| MTINV+I+R6 | -1370120.518 | 2741493.385 |
| MTVER+R7 | -1386416.533 | 2774096.028 |
| MTVER+I+R6 | -1386453.139 | 2774158.627 |
| LG | -1409992.930 | 2821121.464 |
The inferred model Q.p__Desulfobacterota_D_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Desulfobacterota_D_1+R7 | LG+F+R7 |
| BIC | 2584334.018 | 2600063.439 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loop_1/tree_update/Q.p__Desulfobacterota_D_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 181.00 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Desulfobacterota_D/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0377  
Tree 1 branch length: 10.10199  
Tree 2 branch length: 11.15977  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1361720.564 | -1377869.298 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Desulfobacterota_D_2):  
Pearson's correlation: 0.9385376199889978  
Euclidean distance: 0.7788949587472208  
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
Total time usage: 40523.40 seconds (11.26 h)  
