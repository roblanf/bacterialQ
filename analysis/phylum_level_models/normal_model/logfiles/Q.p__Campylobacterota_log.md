## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Campylobacterota  
  Taxa name: p__Campylobacterota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 1074  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Campylobacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Campylobacterota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Fusobacteriota as the outgroup for Phylum Campylobacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 1074   
Number of pruned subtrees: 9   
Number of taxa after pruning: 1062   
Pruned node IDs (degree): 231 (238) 524 (235) 7 (225) 893 (142) 783 (111) 481 (44) 758 (25) 1052 (23) 1034 (19)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 9 subtree files and 119 loci files. Total number of potential alignments: 1071.  
Obtained 1065 alignments from all potential alignments.  
Remaining 1065 alignments. Deleted 6 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/subtree_update/Q.p__Campylobacterota
```
  
  Runtime: 65696.19 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Campylobacterota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 609 |
| Q.INSECT | 193 |
| LG | 165 |
| Q.PFAM | 60 |
| Q.PLANT | 32 |
| MTMET | 5 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/subtree_update/Q.p__Campylobacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/subtree_update/Q.p__Campylobacterota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/model_update/Q.p__Campylobacterota
```
  
  Runtime: 201967.78 seconds  
[Model update log](loop_1/model_update/Q.p__Campylobacterota.iqtree)  
BIC of the new model: 34005261.1694  
Likelihood of the new model: -15570691.7423  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Campylobacterota_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.PFAM,Q.p__Campylobacterota_1  
![Model bubble plot](loop_1/Q.p__Campylobacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9758752154225324  
Euclidean distance: 0.4861156138449412  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/Q.p__Campylobacterota_1.treefile
```
  
  Runtime: 8099.41 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/Q.p__Campylobacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/Q.p__Campylobacterota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 450  
Normalized RF distance: 0.2099  
Tree 1 branch length: 90.73429  
Tree 2 branch length: 131.60746  
Time usage for Loop_1: 276292.81 seconds (76.75 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/Q.p__Campylobacterota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 1074   
Number of pruned subtrees: 9   
Number of taxa after pruning: 1071   
Pruned node IDs (degree): 797 (238) 573 (225) 44 (215) 428 (145) 321 (108) 258 (64) 10 (34) 1052 (23) 1034 (19)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 9 subtree files and 119 loci files. Total number of potential alignments: 1071.  
Obtained 1066 alignments from all potential alignments.  
Remaining 1066 alignments. Deleted 5 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.PFAM,Q.p__Campylobacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/subtree_update/Q.p__Campylobacterota
```
  
  Runtime: 52158.87 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Campylobacterota.iqtree)  
Best models for iteration 2:  
Q.p__Campylobacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Campylobacterota_1 | 915 |
| LG | 60 |
| Q.INSECT | 38 |
| Q.YEAST | 31 |
| Q.PFAM | 22 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/subtree_update/Q.p__Campylobacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/subtree_update/Q.p__Campylobacterota.treefile --model-joint GTR20+FO --init-model Q.p__Campylobacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/model_update/Q.p__Campylobacterota
```
  
  Runtime: 134501.07 seconds  
[Model update log](loop_2/model_update/Q.p__Campylobacterota.iqtree)  
BIC of the new model: 34273428.5955  
Likelihood of the new model: -15692618.1094  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Campylobacterota_2)  
Model set for next iteration: LG,Q.INSECT,Q.YEAST,Q.PFAM,Q.p__Campylobacterota_2  
![Model bubble plot](loop_2/Q.p__Campylobacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999463980807681  
Euclidean distance: 0.02436281691045737  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/Q.p__Campylobacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 7330.29 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 460  
Normalized RF distance: 0.2146  
Tree 1 branch length: 90.73429  
Tree 2 branch length: 131.57585  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Campylobacterota_1,Q.p__Campylobacterota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 1035769.51 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Campylobacterota_2+I+R9 | -15684698.040 | 31392332.862 |
| Q.p__Campylobacterota_1+I+R9 | -15684869.540 | 31392675.862 |
| Q.YEAST+I+R9 | -15752215.060 | 31527366.902 |
| Q.p__Campylobacterota_1+F+I+R9 | -15756409.070 | 31535956.494 |
| Q.p__Campylobacterota_2+F+I+R9 | -15758285.980 | 31539710.314 |
| LG+F+I+R9 | -15774329.570 | 31571797.494 |
| Q.PFAM+F+I+R9 | -15780719.140 | 31584576.634 |
| Q.YEAST+F+I+R9 | -15780740.320 | 31584618.994 |
| Q.INSECT+I+R9 | -15783894.230 | 31590725.242 |
| Q.INSECT+F+I+R9 | -15804987.140 | 31633112.634 |
| LG+I+R9 | -15826511.440 | 31675959.662 |
| LG+R9 | -15828993.790 | 31680913.753 |
| LG+I+R8 | -15832280.780 | 31687477.124 |
| LG+R8 | -15835547.580 | 31694000.115 |
| LG+I+R7 | -15840863.270 | 31704620.886 |
| Q.PFAM+I+R9 | -15842690.530 | 31708317.842 |
| LG+R7 | -15846450.930 | 31715785.596 |
| WAG+F+I+R9 | -15852369.790 | 31727877.934 |
| LG+I+R6 | -15855020.660 | 31732914.447 |
| LG+R6 | -15862783.230 | 31748428.978 |
| JTT+F+I+R9 | -15881990.540 | 31787119.434 |
| WAG+I+R9 | -15904043.630 | 31831024.042 |
| LG+I+G4 | -15937584.170 | 31897945.986 |
| Q.PLANT+F+I+R9 | -15949958.550 | 31923055.454 |
| JTT+I+R9 | -15958904.130 | 31940745.042 |
| CPREV+I+R9 | -15960851.650 | 31944640.082 |
| LG+G4 | -15970104.490 | 31962976.017 |
| CPREV+F+I+R9 | -15973740.510 | 31970619.374 |
| Q.PLANT+I+R9 | -15976491.590 | 31975919.962 |
| DCMUT+F+I+R9 | -16005390.620 | 32033919.594 |
| MTINV+F+I+R9 | -16022051.830 | 32067242.014 |
| PMB+F+I+R9 | -16022164.920 | 32067468.194 |
| DCMUT+I+R9 | -16074234.350 | 32171405.482 |
| Q.MAMMAL+F+I+R9 | -16086822.600 | 32196783.554 |
| PMB+I+R9 | -16100364.360 | 32223665.502 |
| MTMET+F+I+R9 | -16129404.200 | 32281946.754 |
| Q.MAMMAL+I+R9 | -16162521.970 | 32347980.722 |
| Q.BIRD+F+I+R9 | -16238848.190 | 32500834.734 |
| Q.BIRD+I+R9 | -16308973.340 | 32640883.462 |
| MTVER+F+I+R9 | -16419990.750 | 32863119.854 |
| MTMET+I+R9 | -16551507.320 | 33125951.422 |
| MTINV+I+R9 | -16572391.290 | 33167719.362 |
| MTVER+I+R9 | -16770445.830 | 33563828.442 |
| LG+I | -17553158.980 | 35129084.997 |
| LG | -17922604.440 | 35867965.308 |
The inferred model Q.p__Campylobacterota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Campylobacterota_2+I+R9 | Q.YEAST+I+R9 |
| BIC | 31392332.862 | 31527366.902 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/Q.p__Campylobacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 4197.13 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loop_1/tree_update/Q.p__Campylobacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 4041.65 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
Q.YEAST model has higher likelihood than LG model, use best_existing_model model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/allloci_best_existing_model_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Campylobacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 44  
Normalized RF distance: 0.0205  
Tree 1 branch length: 128.27563  
Tree 2 branch length: 131.57585  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -15750190.355 | -15817031.818 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.YEAST) and final model (Q.p__Campylobacterota_2):  
Pearson's correlation: 0.974808443852246  
Euclidean distance: 0.5001404433125226  
![Initial best model bubble plot](final_test/best_existing_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Pairwise tree distance comparison  
![Heatmap of RF distance of trees:](estimated_tree/RF_heatmap.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_heatmap.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 1515277.51 seconds (420.91 h)  
