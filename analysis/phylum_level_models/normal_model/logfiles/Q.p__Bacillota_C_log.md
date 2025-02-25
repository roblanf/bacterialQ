## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_C  
  Taxa name: p__Bacillota_C  
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
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 589  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_C  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_C -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota_C
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/subtrees -m split
```
  
Original number of taxa: 589   
Number of pruned subtrees: 6   
Number of taxa after pruning: 574   
Pruned node IDs (degree): 302 (248) 3 (166) 169 (110) 570 (18) 551 (17) 285 (15)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 6 subtree files and 120 loci files. Total number of potential alignments: 720.  
Obtained 720 alignments from all potential alignments.  
Remaining 720 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/subtree_update/Q.p__Bacillota_C
```
  
  Runtime: 40639.41 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_C.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 243 |
| Q.PLANT | 204 |
| Q.YEAST | 148 |
| Q.PFAM | 96 |
| WAG | 12 |
| JTT | 9 |
| CPREV | 8 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/subtree_update/Q.p__Bacillota_C.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/subtree_update/Q.p__Bacillota_C.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/model_update/Q.p__Bacillota_C
```
  
  Runtime: 76444.24 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_C.iqtree)  
BIC of the new model: 17254273.8811  
Likelihood of the new model: -7891031.0578  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_C_1)  
Model set for next iteration: LG,Q.PLANT,Q.YEAST,Q.PFAM,Q.p__Bacillota_C_1  
![Model bubble plot](loop_1/Q.p__Bacillota_C_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9735544269436606  
Euclidean distance: 0.46857038416677926  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/tree_update/Q.p__Bacillota_C_1.treefile
```
  
  Runtime: 3301.83 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/tree_update/Q.p__Bacillota_C_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/tree_update/Q.p__Bacillota_C_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 232  
Normalized RF distance: 0.1976  
Tree 1 branch length: 41.80345  
Tree 2 branch length: 63.05905  
Time usage for Loop_1: 120610.51 seconds (33.50 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/tree_update/Q.p__Bacillota_C_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/subtrees -m split
```
  
Original number of taxa: 589   
Number of pruned subtrees: 5   
Number of taxa after pruning: 574   
Pruned node IDs (degree): 297 (250) 4 (163) 167 (110) 551 (36) 283 (15)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 5 subtree files and 120 loci files. Total number of potential alignments: 600.  
Obtained 600 alignments from all potential alignments.  
Remaining 600 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/training_loci -m MFP -mset LG,Q.PLANT,Q.YEAST,Q.PFAM,Q.p__Bacillota_C_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/subtree_update/Q.p__Bacillota_C
```
  
  Runtime: 34736.21 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_C.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_C_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_C_1 | 538 |
| Q.PLANT | 26 |
| LG | 14 |
| Q.PFAM | 13 |
| Q.YEAST | 9 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/subtree_update/Q.p__Bacillota_C.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/subtree_update/Q.p__Bacillota_C.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_C_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/model_update/Q.p__Bacillota_C
```
  
  Runtime: 35800.88 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_C.iqtree)  
BIC of the new model: 16948803.2785  
Likelihood of the new model: -7746150.7481  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_C_2)  
Model set for next iteration: Q.PLANT,LG,Q.PFAM,Q.YEAST,Q.p__Bacillota_C_2  
![Model bubble plot](loop_2/Q.p__Bacillota_C_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999154951941112  
Euclidean distance: 0.025854343939670954  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/tree_update/Q.p__Bacillota_C_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 3891.13 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 232  
Normalized RF distance: 0.1976  
Tree 1 branch length: 41.80345  
Tree 2 branch length: 63.13451  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_C_1,Q.p__Bacillota_C_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 832934.30 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bacillota_C_2+I+R9 | -8077681.895 | 16168010.875 |
| Q.p__Bacillota_C_1+I+R9 | -8078006.428 | 16168659.941 |
| Q.p__Bacillota_C_1+F+I+R9 | -8090280.428 | 16193409.530 |
| Q.p__Bacillota_C_2+F+I+R9 | -8091136.714 | 16195122.102 |
| LG+F+I+R9 | -8119974.197 | 16252797.068 |
| Q.PFAM+I+R9 | -8121624.341 | 16255895.767 |
| LG+I+R9 | -8123054.985 | 16258757.055 |
| Q.PFAM+F+I+R9 | -8123138.283 | 16259125.240 |
| LG+R9 | -8124744.636 | 16262125.747 |
| LG+I+R8 | -8125645.638 | 16263917.141 |
| LG+R8 | -8127388.537 | 16267392.329 |
| Q.YEAST+F+I+R9 | -8127982.049 | 16268812.772 |
| LG+I+R7 | -8130036.661 | 16272677.967 |
| LG+R7 | -8132526.349 | 16277646.733 |
| Q.INSECT+I+R9 | -8133737.053 | 16280121.191 |
| Q.YEAST+I+R9 | -8135119.481 | 16282886.047 |
| LG+I+R6 | -8136635.299 | 16285854.023 |
| LG+R6 | -8140643.586 | 16293859.987 |
| Q.INSECT+F+I+R9 | -8142058.130 | 16296964.934 |
| WAG+F+I+R9 | -8157079.073 | 16327006.820 |
| WAG+I+R9 | -8160843.517 | 16334334.119 |
| LG+I+G4 | -8176251.296 | 16364990.527 |
| JTT+F+I+R9 | -8183927.381 | 16380703.436 |
| JTT+I+R9 | -8187494.140 | 16387635.365 |
| LG+G4 | -8195250.834 | 16402978.993 |
| Q.PLANT+I+R9 | -8203961.053 | 16420569.191 |
| Q.PLANT+F+I+R9 | -8209836.579 | 16432521.832 |
| CPREV+F+I+R9 | -8230639.605 | 16474127.884 |
| DCMUT+F+I+R9 | -8236934.446 | 16486717.566 |
| CPREV+I+R9 | -8238982.513 | 16490612.111 |
| DCMUT+I+R9 | -8251194.788 | 16515036.661 |
| PMB+F+I+R9 | -8264611.348 | 16542071.370 |
| MTINV+F+I+R9 | -8280648.490 | 16574145.654 |
| PMB+I+R9 | -8284201.408 | 16581049.901 |
| Q.MAMMAL+I+R9 | -8295425.207 | 16603497.499 |
| Q.MAMMAL+F+I+R9 | -8302046.201 | 16616941.076 |
| MTMET+F+I+R9 | -8346181.395 | 16705211.464 |
| Q.BIRD+I+R9 | -8371145.954 | 16754938.993 |
| Q.BIRD+F+I+R9 | -8382044.786 | 16776938.246 |
| MTVER+F+I+R9 | -8481109.081 | 16975066.836 |
| MTMET+I+R9 | -8644905.855 | 17302458.795 |
| MTINV+I+R9 | -8668766.139 | 17350179.363 |
| MTVER+I+R9 | -8720171.351 | 17452989.787 |
| LG+I | -8961004.960 | 17934487.245 |
| LG | -9200281.581 | 18413029.877 |
The inferred model Q.p__Bacillota_C_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bacillota_C_2+I+R9 | LG+F+I+R9 |
| BIC | 16168010.875 | 16252797.068 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loop_1/tree_update/Q.p__Bacillota_C_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 3138.12 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_C/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0068  
Tree 1 branch length: 60.1787  
Tree 2 branch length: 63.13451  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -8143244.113 | -8187653.964 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bacillota_C_2):  
Pearson's correlation: 0.9726768862200653  
Euclidean distance: 0.4750180204843112  
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
Total time usage: 1031725.91 seconds (286.59 h)  
