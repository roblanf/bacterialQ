## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Eremiobacterota  
  Taxa name: p__Eremiobacterota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 167  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 167  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Eremiobacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Eremiobacterota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Eremiobacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/ref_tree.tre -l 15 -u 167 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 167   
Number of pruned subtrees: 1   
Number of taxa after pruning: 167   
Pruned node IDs (degree): 1 (167)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/subtree_update/Q.p__Eremiobacterota
```
  
  Runtime: 46989.30 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Eremiobacterota.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| Q.PFAM | 48 |
| Q.YEAST | 38 |
| LG | 32 |
| WAG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/subtree_update/Q.p__Eremiobacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/subtree_update/Q.p__Eremiobacterota.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/model_update/Q.p__Eremiobacterota
```
  
  Runtime: 36125.31 seconds  
[Model update log](loop_1/model_update/Q.p__Eremiobacterota.iqtree)  
BIC of the new model: 7324396.7632  
Likelihood of the new model: -3485217.6964  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Eremiobacterota_1)  
Model set for next iteration: Q.PFAM,Q.YEAST,LG,Q.p__Eremiobacterota_1  
![Model bubble plot](loop_1/Q.p__Eremiobacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9761010376039609  
Euclidean distance: 0.5602508372922781  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/tree_update/Q.p__Eremiobacterota_1.treefile
```
  
  Runtime: 788.60 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/tree_update/Q.p__Eremiobacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/tree_update/Q.p__Eremiobacterota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 38  
Normalized RF distance: 0.1152  
Tree 1 branch length: 25.47376  
Tree 2 branch length: 34.31294  
Time usage for Loop_1: 83947.16 seconds (23.32 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/tree_update/Q.p__Eremiobacterota_1.treefile -l 15 -u 167 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 167   
Number of pruned subtrees: 1   
Number of taxa after pruning: 167   
Pruned node IDs (degree): 1 (167)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/training_loci -m MFP -mset Q.PFAM,Q.YEAST,LG,Q.p__Eremiobacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/subtree_update/Q.p__Eremiobacterota
```
  
  Runtime: 18270.10 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Eremiobacterota.iqtree)  
Best models for iteration 2:  
Q.p__Eremiobacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Eremiobacterota_1 | 105 |
| Q.YEAST | 6 |
| LG | 5 |
| Q.PFAM | 3 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/subtree_update/Q.p__Eremiobacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/subtree_update/Q.p__Eremiobacterota.treefile --model-joint GTR20+FO --init-model Q.p__Eremiobacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/model_update/Q.p__Eremiobacterota
```
  
  Runtime: 20223.73 seconds  
[Model update log](loop_2/model_update/Q.p__Eremiobacterota.iqtree)  
BIC of the new model: 7319843.4788  
Likelihood of the new model: -3482941.0542  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Eremiobacterota_2)  
Model set for next iteration: Q.YEAST,LG,Q.PFAM,Q.p__Eremiobacterota_2  
![Model bubble plot](loop_2/Q.p__Eremiobacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999413090105781  
Euclidean distance: 0.03367061160971629  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/tree_update/Q.p__Eremiobacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 666.94 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 38  
Normalized RF distance: 0.1152  
Tree 1 branch length: 25.47376  
Tree 2 branch length: 34.4079  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Eremiobacterota_1,Q.p__Eremiobacterota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 16658.09 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Eremiobacterota_1+I+R9 | -3560705.602 | 7125100.179 |
| Q.p__Eremiobacterota_2+I+R9 | -3560730.110 | 7125149.195 |
| Q.p__Eremiobacterota_1+F+I+R9 | -3567734.541 | 7139359.466 |
| Q.p__Eremiobacterota_2+F+I+R9 | -3568258.857 | 7140408.098 |
| LG+F+I+R9 | -3575634.017 | 7155158.418 |
| Q.PFAM+F+I+R9 | -3576225.329 | 7156341.042 |
| Q.YEAST+F+I+R9 | -3579765.539 | 7163421.462 |
| Q.INSECT+F+I+R9 | -3583767.162 | 7171424.708 |
| Q.PFAM+I+R9 | -3584092.611 | 7171874.197 |
| LG+I+R9 | -3591716.792 | 7187122.559 |
| LG+R9 | -3591781.822 | 7187242.018 |
| LG+I+R8 | -3591924.761 | 7187517.296 |
| LG+R8 | -3592050.110 | 7187757.393 |
| LG+I+R7 | -3592285.322 | 7188217.217 |
| LG+R7 | -3592690.543 | 7189017.058 |
| LG+I+R6 | -3593204.928 | 7190035.228 |
| LG+R6 | -3594170.783 | 7191956.337 |
| WAG+F+I+R9 | -3594563.772 | 7193017.928 |
| LG+I+G4 | -3602695.563 | 7208921.093 |
| Q.INSECT+I+R9 | -3608082.672 | 7219854.319 |
| LG+G4 | -3608719.550 | 7220958.467 |
| WAG+I+R9 | -3608985.221 | 7221659.417 |
| JTT+F+I+R9 | -3610092.439 | 7224075.262 |
| Q.YEAST+I+R9 | -3615179.786 | 7234048.547 |
| Q.PLANT+F+I+R9 | -3619691.402 | 7243273.188 |
| JTT+I+R9 | -3620389.832 | 7244468.639 |
| DCMUT+F+I+R9 | -3624000.299 | 7251890.982 |
| CPREV+F+I+R9 | -3626928.082 | 7257746.548 |
| Q.PLANT+I+R9 | -3632783.867 | 7269256.709 |
| PMB+F+I+R9 | -3634871.526 | 7273633.436 |
| DCMUT+I+R9 | -3646760.676 | 7297210.327 |
| MTINV+F+I+R9 | -3646846.675 | 7297583.734 |
| CPREV+I+R9 | -3650058.713 | 7303806.401 |
| PMB+I+R9 | -3650138.985 | 7303966.945 |
| Q.MAMMAL+F+I+R9 | -3662651.218 | 7329192.820 |
| Q.MAMMAL+I+R9 | -3669138.459 | 7341965.893 |
| MTMET+F+I+R9 | -3681304.097 | 7366498.578 |
| Q.BIRD+F+I+R9 | -3695641.044 | 7395172.472 |
| Q.BIRD+I+R9 | -3701651.462 | 7406991.899 |
| MTVER+F+I+R9 | -3737585.378 | 7479061.140 |
| LG+I | -3870421.508 | 7744362.383 |
| MTMET+I+R9 | -3871941.330 | 7747571.635 |
| MTINV+I+R9 | -3882363.060 | 7768415.095 |
| MTVER+I+R9 | -3898582.956 | 7800854.887 |
| LG | -3960937.493 | 7925383.752 |
The inferred model Q.p__Eremiobacterota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Eremiobacterota_1+I+R9 | LG+F+I+R9 |
| BIC | 7125100.179 | 7155158.418 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loop_1/tree_update/Q.p__Eremiobacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 496.70 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Eremiobacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 33.15722  
Tree 2 branch length: 34.4079  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -3632583.426 | -3663711.525 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Eremiobacterota_2):  
Pearson's correlation: 0.9644578651148925  
Euclidean distance: 0.6352532200498292  
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
Total time usage: 140466.94 seconds (39.02 h)  
