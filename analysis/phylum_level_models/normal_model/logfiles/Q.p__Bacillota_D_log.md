## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_D  
  Taxa name: p__Bacillota_D  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 118  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 118  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_D  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_D -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota_D
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/ref_tree.tre -l 15 -u 118 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/subtrees -m split
```
  
Original number of taxa: 118   
Number of pruned subtrees: 1   
Number of taxa after pruning: 118   
Pruned node IDs (degree): 1 (118)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/subtree_update/Q.p__Bacillota_D
```
  
  Runtime: 20669.24 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_D.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 57 |
| LG | 27 |
| Q.PFAM | 18 |
| Q.YEAST | 17 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/subtree_update/Q.p__Bacillota_D.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/subtree_update/Q.p__Bacillota_D.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/model_update/Q.p__Bacillota_D
```
  
  Runtime: 27491.78 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_D.iqtree)  
BIC of the new model: 5830478.7868  
Likelihood of the new model: -2787688.5729  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_D_1)  
Model set for next iteration: Q.PLANT,LG,Q.PFAM,Q.YEAST,Q.p__Bacillota_D_1  
![Model bubble plot](loop_1/Q.p__Bacillota_D_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9560878438328612  
Euclidean distance: 0.6492904812550943  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/tree_update/Q.p__Bacillota_D_1.treefile
```
  
  Runtime: 764.27 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/tree_update/Q.p__Bacillota_D_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/tree_update/Q.p__Bacillota_D_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 12  
Normalized RF distance: 0.0517  
Tree 1 branch length: 18.69507  
Tree 2 branch length: 26.22083  
Time usage for Loop_1: 48971.90 seconds (13.60 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/tree_update/Q.p__Bacillota_D_1.treefile -l 15 -u 118 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/subtrees -m split
```
  
Original number of taxa: 118   
Number of pruned subtrees: 1   
Number of taxa after pruning: 118   
Pruned node IDs (degree): 1 (118)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/training_loci -m MFP -mset Q.PLANT,LG,Q.PFAM,Q.YEAST,Q.p__Bacillota_D_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/subtree_update/Q.p__Bacillota_D
```
  
  Runtime: 17700.91 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_D.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_D_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_D_1 | 114 |
| LG | 2 |
| Q.PLANT | 2 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/subtree_update/Q.p__Bacillota_D.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/subtree_update/Q.p__Bacillota_D.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_D_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/model_update/Q.p__Bacillota_D
```
  
  Runtime: 24060.17 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_D.iqtree)  
BIC of the new model: 5829121.9587  
Likelihood of the new model: -2787010.1589  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_D_2)  
Model set for next iteration: LG,Q.PLANT,Q.YEAST,Q.p__Bacillota_D_2  
![Model bubble plot](loop_2/Q.p__Bacillota_D_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999329185852996  
Euclidean distance: 0.034647415666698725  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/tree_update/Q.p__Bacillota_D_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 509.22 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 14  
Normalized RF distance: 0.0603  
Tree 1 branch length: 18.69507  
Tree 2 branch length: 26.29877  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_D_1,Q.p__Bacillota_D_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 22462.66 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bacillota_D_2+I+R9 | -2831033.555 | 5664715.041 |
| Q.p__Bacillota_D_1+I+R9 | -2831033.836 | 5664715.603 |
| Q.p__Bacillota_D_1+F+I+R9 | -2838463.542 | 5679776.257 |
| Q.p__Bacillota_D_2+F+I+R9 | -2838914.390 | 5680677.953 |
| LG+F+I+R9 | -2849240.570 | 5701330.313 |
| LG+I+R9 | -2849861.848 | 5702371.627 |
| LG+R9 | -2849872.267 | 5702381.873 |
| LG+I+R8 | -2849898.513 | 5702423.773 |
| LG+R8 | -2849976.630 | 5702569.416 |
| LG+I+R7 | -2850069.818 | 5702745.200 |
| LG+R7 | -2850261.715 | 5703118.402 |
| LG+I+R6 | -2850752.287 | 5704088.954 |
| LG+R6 | -2851106.491 | 5704786.771 |
| Q.PFAM+I+R9 | -2851838.362 | 5706324.655 |
| Q.INSECT+I+R9 | -2852197.722 | 5707043.375 |
| Q.PFAM+F+I+R9 | -2852741.702 | 5708332.577 |
| Q.YEAST+F+I+R9 | -2853008.281 | 5708865.735 |
| Q.PLANT+I+R9 | -2854168.382 | 5710984.695 |
| Q.INSECT+F+I+R9 | -2854910.642 | 5712670.457 |
| Q.YEAST+I+R9 | -2855851.420 | 5714350.771 |
| Q.PLANT+F+I+R9 | -2856050.647 | 5714950.467 |
| LG+I+G4 | -2857026.632 | 5716542.319 |
| LG+G4 | -2862886.605 | 5728251.673 |
| JTT+F+I+R9 | -2863204.054 | 5729257.281 |
| JTT+I+R9 | -2865703.880 | 5734055.691 |
| WAG+F+I+R9 | -2866277.606 | 5735404.385 |
| WAG+I+R9 | -2869432.645 | 5741513.221 |
| CPREV+I+R9 | -2878320.905 | 5759289.741 |
| CPREV+F+I+R9 | -2880212.797 | 5763274.767 |
| MTINV+F+I+R9 | -2883026.850 | 5768902.873 |
| Q.MAMMAL+F+I+R9 | -2887433.591 | 5777716.355 |
| Q.MAMMAL+I+R9 | -2887865.950 | 5778379.831 |
| DCMUT+F+I+R9 | -2888661.311 | 5780171.795 |
| MTMET+F+I+R9 | -2894713.219 | 5792275.611 |
| DCMUT+I+R9 | -2900680.235 | 5804008.401 |
| Q.BIRD+I+R9 | -2903964.624 | 5810577.179 |
| Q.BIRD+F+I+R9 | -2904481.954 | 5811813.081 |
| PMB+F+I+R9 | -2911576.873 | 5826002.919 |
| PMB+I+R9 | -2913770.657 | 5830189.245 |
| MTVER+F+I+R9 | -2929971.654 | 5862792.481 |
| MTMET+I+R9 | -3012207.951 | 6027063.833 |
| MTINV+I+R9 | -3028826.312 | 6060300.555 |
| MTVER+I+R9 | -3033126.401 | 6068900.733 |
| LG+I | -3054552.050 | 6111582.563 |
| LG | -3157070.541 | 6316608.953 |
The inferred model Q.p__Bacillota_D_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bacillota_D_2+I+R9 | LG+F+I+R9 |
| BIC | 5664715.041 | 5701330.313 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loop_1/tree_update/Q.p__Bacillota_D_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 382.86 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_D/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 24.42664  
Tree 2 branch length: 26.29877  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2906564.257 | -2924713.373 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bacillota_D_2):  
Pearson's correlation: 0.9637840338337712  
Euclidean distance: 0.6817313432158525  
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
Total time usage: 114280.35 seconds (31.74 h)  
