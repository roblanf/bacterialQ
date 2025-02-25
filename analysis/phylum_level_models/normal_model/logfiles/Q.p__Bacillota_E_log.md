## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_E  
  Taxa name: p__Bacillota_E  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 169  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 169  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_E  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_E -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota_E
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/ref_tree.tre -l 15 -u 169 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/subtrees -m split
```
  
Original number of taxa: 169   
Number of pruned subtrees: 1   
Number of taxa after pruning: 169   
Pruned node IDs (degree): 1 (169)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/subtree_update/Q.p__Bacillota_E
```
  
  Runtime: 34223.34 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_E.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 63 |
| Q.PFAM | 36 |
| Q.YEAST | 19 |
| WAG | 1 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/subtree_update/Q.p__Bacillota_E.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/subtree_update/Q.p__Bacillota_E.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/model_update/Q.p__Bacillota_E
```
  
  Runtime: 31209.67 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_E.iqtree)  
BIC of the new model: 9579614.6037  
Likelihood of the new model: -4599600.5933  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_E_1)  
Model set for next iteration: LG,Q.PFAM,Q.YEAST,Q.p__Bacillota_E_1  
![Model bubble plot](loop_1/Q.p__Bacillota_E_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9315105629094589  
Euclidean distance: 1.0248494281552372  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/tree_update/Q.p__Bacillota_E_1.treefile
```
  
  Runtime: 988.22 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/tree_update/Q.p__Bacillota_E_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/tree_update/Q.p__Bacillota_E_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 40  
Normalized RF distance: 0.1198  
Tree 1 branch length: 34.13942  
Tree 2 branch length: 45.71572  
Time usage for Loop_1: 66474.59 seconds (18.47 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/tree_update/Q.p__Bacillota_E_1.treefile -l 15 -u 169 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/subtrees -m split
```
  
Original number of taxa: 169   
Number of pruned subtrees: 1   
Number of taxa after pruning: 169   
Pruned node IDs (degree): 1 (169)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.YEAST,Q.p__Bacillota_E_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/subtree_update/Q.p__Bacillota_E
```
  
  Runtime: 21831.42 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_E.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_E_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_E_1 | 111 |
| LG | 5 |
| Q.YEAST | 4 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/subtree_update/Q.p__Bacillota_E.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/subtree_update/Q.p__Bacillota_E.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_E_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/model_update/Q.p__Bacillota_E
```
  
  Runtime: 22056.95 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_E.iqtree)  
BIC of the new model: 9574890.3354  
Likelihood of the new model: -4597238.4592  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_E_2)  
Model set for next iteration: LG,Q.YEAST,Q.p__Bacillota_E_2  
![Model bubble plot](loop_2/Q.p__Bacillota_E_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998194070330486  
Euclidean distance: 0.07563688595469908  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/tree_update/Q.p__Bacillota_E_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 964.21 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 40  
Normalized RF distance: 0.1198  
Tree 1 branch length: 34.13942  
Tree 2 branch length: 45.91193  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_E_1,Q.p__Bacillota_E_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 14437.77 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bacillota_E_2+I+R9 | -4683771.184 | 9371277.112 |
| Q.p__Bacillota_E_1+I+R9 | -4683778.731 | 9371292.206 |
| Q.p__Bacillota_E_1+F+I+R9 | -4707017.276 | 9417970.888 |
| LG+F+I+R9 | -4708239.285 | 9420414.906 |
| Q.p__Bacillota_E_2+F+I+R9 | -4709495.758 | 9422927.852 |
| Q.PFAM+F+I+R9 | -4710587.279 | 9425110.894 |
| Q.YEAST+F+I+R9 | -4720393.844 | 9444724.024 |
| Q.INSECT+F+I+R9 | -4730789.471 | 9465515.278 |
| WAG+F+I+R9 | -4733947.317 | 9471830.970 |
| Q.PFAM+I+R9 | -4748614.247 | 9500963.238 |
| LG+I+R9 | -4764013.457 | 9531761.658 |
| LG+R9 | -4764160.112 | 9532044.358 |
| LG+I+R8 | -4764322.620 | 9532358.764 |
| JTT+F+I+R9 | -4764458.026 | 9532852.388 |
| LG+R8 | -4764703.683 | 9533110.280 |
| LG+I+R7 | -4765171.656 | 9534035.616 |
| LG+R7 | -4765725.119 | 9535131.932 |
| LG+I+R6 | -4766770.463 | 9537212.010 |
| LG+R6 | -4767958.602 | 9539577.678 |
| Q.PLANT+F+I+R9 | -4774298.028 | 9552532.392 |
| CPREV+F+I+R9 | -4775316.506 | 9554569.348 |
| LG+I+G4 | -4779275.730 | 9562127.053 |
| WAG+I+R9 | -4782491.038 | 9568716.820 |
| PMB+F+I+R9 | -4785037.989 | 9574012.314 |
| DCMUT+F+I+R9 | -4785170.772 | 9574277.880 |
| LG+G4 | -4788977.595 | 9581520.173 |
| JTT+I+R9 | -4805007.365 | 9613749.474 |
| Q.INSECT+I+R9 | -4810489.282 | 9624713.308 |
| MTINV+F+I+R9 | -4816446.761 | 9636829.858 |
| Q.YEAST+I+R9 | -4826792.789 | 9657320.322 |
| Q.PLANT+I+R9 | -4828410.910 | 9660556.564 |
| PMB+I+R9 | -4830044.174 | 9663823.092 |
| Q.MAMMAL+F+I+R9 | -4833238.811 | 9670413.958 |
| CPREV+I+R9 | -4845191.065 | 9694116.874 |
| DCMUT+I+R9 | -4849980.059 | 9703694.862 |
| MTMET+F+I+R9 | -4862907.210 | 9729750.756 |
| Q.MAMMAL+I+R9 | -4863900.757 | 9731536.258 |
| Q.BIRD+F+I+R9 | -4873821.919 | 9751580.174 |
| Q.BIRD+I+R9 | -4906125.074 | 9815984.892 |
| MTVER+F+I+R9 | -4939347.375 | 9882631.086 |
| LG+I | -5127904.889 | 10259374.761 |
| MTMET+I+R9 | -5186106.527 | 10375947.798 |
| MTVER+I+R9 | -5203963.489 | 10411661.722 |
| MTINV+I+R9 | -5207872.557 | 10419479.858 |
| LG | -5256219.900 | 10515994.173 |
The inferred model Q.p__Bacillota_E_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bacillota_E_2+I+R9 | LG+F+I+R9 |
| BIC | 9371277.112 | 9420414.906 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loop_1/tree_update/Q.p__Bacillota_E_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 619.74 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_E/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0299  
Tree 1 branch length: 45.04993  
Tree 2 branch length: 45.91193  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -4750026.097 | -4830082.194 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bacillota_E_2):  
Pearson's correlation: 0.9298764799570488  
Euclidean distance: 1.0777774045188602  
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
Total time usage: 126625.88 seconds (35.17 h)  
