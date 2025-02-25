## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota_G  
  Taxa name: p__Bacillota_G  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 166  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 166  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota_G  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota_G -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota_G
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/ref_tree.tre -l 15 -u 166 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/subtrees -m split
```
  
Original number of taxa: 166   
Number of pruned subtrees: 1   
Number of taxa after pruning: 166   
Pruned node IDs (degree): 1 (166)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/subtree_update/Q.p__Bacillota_G
```
  
  Runtime: 21080.93 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota_G.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 53 |
| Q.PFAM | 32 |
| Q.YEAST | 21 |
| Q.PLANT | 14 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/subtree_update/Q.p__Bacillota_G.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/subtree_update/Q.p__Bacillota_G.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/model_update/Q.p__Bacillota_G
```
  
  Runtime: 48068.17 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota_G.iqtree)  
BIC of the new model: 8905926.763  
Likelihood of the new model: -4261296.94  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_G_1)  
Model set for next iteration: LG,Q.PFAM,Q.YEAST,Q.PLANT,Q.p__Bacillota_G_1  
![Model bubble plot](loop_1/Q.p__Bacillota_G_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9753265319912867  
Euclidean distance: 0.5623782703279848  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/tree_update/Q.p__Bacillota_G_1.treefile
```
  
  Runtime: 961.17 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/tree_update/Q.p__Bacillota_G_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/tree_update/Q.p__Bacillota_G_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 48  
Normalized RF distance: 0.1463  
Tree 1 branch length: 27.53604  
Tree 2 branch length: 39.52614  
Time usage for Loop_1: 70160.61 seconds (19.49 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/tree_update/Q.p__Bacillota_G_1.treefile -l 15 -u 166 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/subtrees -m split
```
  
Original number of taxa: 166   
Number of pruned subtrees: 1   
Number of taxa after pruning: 166   
Pruned node IDs (degree): 1 (166)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.YEAST,Q.PLANT,Q.p__Bacillota_G_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/subtree_update/Q.p__Bacillota_G
```
  
  Runtime: 21631.98 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota_G.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_G_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_G_1 | 113 |
| LG | 4 |
| Q.YEAST | 2 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/subtree_update/Q.p__Bacillota_G.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/subtree_update/Q.p__Bacillota_G.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_G_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/model_update/Q.p__Bacillota_G
```
  
  Runtime: 28273.66 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota_G.iqtree)  
BIC of the new model: 8905154.2075  
Likelihood of the new model: -4260910.6622  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_G_2)  
Model set for next iteration: LG,Q.YEAST,Q.PLANT,Q.p__Bacillota_G_2  
![Model bubble plot](loop_2/Q.p__Bacillota_G_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998405591336655  
Euclidean distance: 0.0543535290319288  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/tree_update/Q.p__Bacillota_G_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 626.92 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 48  
Normalized RF distance: 0.1463  
Tree 1 branch length: 27.53604  
Tree 2 branch length: 39.67605  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_G_1,Q.p__Bacillota_G_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 17607.99 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Bacillota_G_1+I+R9 | -4338082.801 | 8679836.601 |
| Q.p__Bacillota_G_2+I+R9 | -4338110.760 | 8679892.519 |
| Q.p__Bacillota_G_1+F+I+R9 | -4350416.219 | 8704705.023 |
| Q.p__Bacillota_G_2+F+I+R9 | -4351766.831 | 8707406.247 |
| LG+F+I+R9 | -4353670.620 | 8711213.825 |
| Q.PFAM+F+I+R9 | -4358244.162 | 8720360.909 |
| Q.PFAM+I+R9 | -4361079.689 | 8725830.377 |
| Q.YEAST+F+I+R9 | -4362248.360 | 8728369.305 |
| LG+I+R9 | -4363101.722 | 8729874.443 |
| LG+R9 | -4363208.596 | 8730077.581 |
| LG+I+R8 | -4363449.693 | 8730549.165 |
| LG+R8 | -4363713.862 | 8731066.893 |
| LG+I+R7 | -4364082.690 | 8731793.939 |
| LG+R7 | -4364800.317 | 8733218.583 |
| LG+I+R6 | -4365536.014 | 8734679.368 |
| LG+R6 | -4367038.442 | 8737673.614 |
| Q.INSECT+F+I+R9 | -4370743.653 | 8745359.891 |
| LG+I+G4 | -4378178.185 | 8759868.221 |
| WAG+F+I+R9 | -4379031.315 | 8761935.215 |
| Q.INSECT+I+R9 | -4383688.155 | 8771047.309 |
| LG+G4 | -4387183.956 | 8777869.153 |
| Q.YEAST+I+R9 | -4390230.876 | 8784132.751 |
| WAG+I+R9 | -4390471.113 | 8784613.225 |
| JTT+F+I+R9 | -4392866.058 | 8789604.701 |
| Q.PLANT+F+I+R9 | -4393240.811 | 8790354.207 |
| Q.PLANT+I+R9 | -4399282.934 | 8802236.867 |
| JTT+I+R9 | -4399872.269 | 8803415.537 |
| CPREV+F+I+R9 | -4408966.538 | 8821805.661 |
| CPREV+I+R9 | -4421218.511 | 8846108.021 |
| DCMUT+F+I+R9 | -4423196.727 | 8850266.039 |
| PMB+F+I+R9 | -4435934.279 | 8875741.143 |
| MTINV+F+I+R9 | -4436084.100 | 8876040.785 |
| Q.MAMMAL+I+R9 | -4444361.105 | 8892393.209 |
| Q.MAMMAL+F+I+R9 | -4445470.816 | 8894814.217 |
| DCMUT+I+R9 | -4446472.972 | 8896616.943 |
| PMB+I+R9 | -4446998.052 | 8897667.103 |
| MTMET+F+I+R9 | -4468707.007 | 8941286.599 |
| Q.BIRD+I+R9 | -4476986.917 | 8957644.833 |
| Q.BIRD+F+I+R9 | -4478464.890 | 8960802.365 |
| MTVER+F+I+R9 | -4536213.604 | 9076299.793 |
| MTMET+I+R9 | -4680858.109 | 9365387.217 |
| LG+I | -4700213.196 | 9403927.633 |
| MTINV+I+R9 | -4700587.416 | 9404845.831 |
| MTVER+I+R9 | -4712445.883 | 9428562.765 |
| LG | -4827088.940 | 9657668.512 |
The inferred model Q.p__Bacillota_G_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Bacillota_G_1+I+R9 | LG+F+I+R9 |
| BIC | 8679836.601 | 8711213.825 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loop_1/tree_update/Q.p__Bacillota_G_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 438.92 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota_G/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0183  
Tree 1 branch length: 37.68337  
Tree 2 branch length: 39.67605  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -4403728.039 | -4428921.418 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Bacillota_G_2):  
Pearson's correlation: 0.9739168417474793  
Euclidean distance: 0.5992630044021772  
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
Total time usage: 138951.73 seconds (38.60 h)  
