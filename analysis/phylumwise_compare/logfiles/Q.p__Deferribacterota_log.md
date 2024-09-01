## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Deferribacterota  
  Taxa name: p__Deferribacterota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 50  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Deferribacterota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 50  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Deferribacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Deferribacterota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Deferribacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Aquificota as the outgroup for Phylum Deferribacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Deferribacterota/ref_tree.tre -l 15 -u 50 -o ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/subtree_update/Q.p__Deferribacterota
```
  
  Runtime: 819.81 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Deferribacterota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 70 |
| Q.INSECT | 32 |
| LG | 12 |
| Q.PFAM | 2 |
| Q.PLANT | 2 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/subtree_update/Q.p__Deferribacterota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/subtree_update/Q.p__Deferribacterota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/model_update/Q.p__Deferribacterota
```
  
  Runtime: 2155.77 seconds  
[Model update log](loop_1/model_update/Q.p__Deferribacterota.iqtree)  
BIC of the new model: 2495375.549  
Likelihood of the new model: -1191030.321  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Deferribacterota_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.p__Deferribacterota_1  
![Model bubble plot](loop_1/Q.p__Deferribacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9818897557418753  
Euclidean distance: 0.40984771895155625  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Deferribacterota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Deferribacterota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/tree_update/Q.p__Deferribacterota_1.treefile
```
  
  Runtime: 155.87 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/tree_update/Q.p__Deferribacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/tree_update/Q.p__Deferribacterota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0638  
Tree 1 branch length: 7.46515  
Tree 2 branch length: 11.18389  
Time usage for Loop_1: 3150.21 seconds (0.88 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/tree_update/Q.p__Deferribacterota_1.treefile -l 15 -u 50 -o ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.p__Deferribacterota_1 -mdef ../Result_nova/phylum_models/Q.p__Deferribacterota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/subtree_update/Q.p__Deferribacterota
```
  
  Runtime: 1219.37 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Deferribacterota.iqtree)  
Best models for iteration 2:  
Q.p__Deferribacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Deferribacterota_1 | 116 |
| LG | 1 |
| Q.INSECT | 1 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/subtree_update/Q.p__Deferribacterota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/subtree_update/Q.p__Deferribacterota.treefile --model-joint GTR20+FO --init-model Q.p__Deferribacterota_1 -mdef ../Result_nova/phylum_models/Q.p__Deferribacterota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/model_update/Q.p__Deferribacterota
```
  
  Runtime: 1825.59 seconds  
[Model update log](loop_2/model_update/Q.p__Deferribacterota.iqtree)  
BIC of the new model: 2495794.1169  
Likelihood of the new model: -1191239.605  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Deferribacterota_2)  
Model set for next iteration: LG,Q.INSECT,Q.YEAST,Q.p__Deferribacterota_2  
![Model bubble plot](loop_2/Q.p__Deferribacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9995730547336629  
Euclidean distance: 0.06082324346652678  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/tree_update/Q.p__Deferribacterota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Deferribacterota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 163.57 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Deferribacterota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 6  
Normalized RF distance: 0.0638  
Tree 1 branch length: 7.46515  
Tree 2 branch length: 11.18056  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Deferribacterota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Deferribacterota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Deferribacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Deferribacterota_1,Q.p__Deferribacterota_2 -mdef ../Result_nova/phylum_models/Q.p__Deferribacterota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Deferribacterota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 20358.96 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Deferribacterota_2+R7 | -1213489.360 | 2428134.886 |
| Q.p__Deferribacterota_2+I+R6 | -1213497.556 | 2428140.671 |
| Q.p__Deferribacterota_1+R7 | -1213495.402 | 2428146.970 |
| Q.p__Deferribacterota_1+I+R6 | -1213503.442 | 2428152.443 |
| Q.p__Deferribacterota_1+F+R7 | -1215349.649 | 2432056.998 |
| Q.p__Deferribacterota_1+F+I+R6 | -1215357.769 | 2432062.631 |
| Q.p__Deferribacterota_2+F+R7 | -1215357.847 | 2432073.394 |
| Q.p__Deferribacterota_2+F+I+R6 | -1215365.983 | 2432079.059 |
| LG+F+R7 | -1218080.393 | 2437518.486 |
| LG+F+I+R6 | -1218088.837 | 2437524.767 |
| Q.YEAST+R7 | -1218998.670 | 2439153.506 |
| Q.YEAST+I+R6 | -1219010.865 | 2439167.289 |
| Q.YEAST+F+R7 | -1218968.838 | 2439295.376 |
| Q.YEAST+F+I+R6 | -1218980.572 | 2439308.237 |
| Q.PFAM+F+R7 | -1219724.506 | 2440806.712 |
| Q.PFAM+F+I+R6 | -1219737.271 | 2440821.635 |
| Q.INSECT+F+R7 | -1220433.677 | 2442225.054 |
| Q.INSECT+F+I+R6 | -1220444.491 | 2442236.075 |
| Q.INSECT+R7 | -1220803.848 | 2442763.862 |
| Q.INSECT+I+R6 | -1220815.107 | 2442775.773 |
| LG+R7 | -1223037.916 | 2447231.998 |
| LG+I+R6 | -1223044.136 | 2447233.831 |
| LG+I+R7 | -1223038.941 | 2447244.655 |
| LG+R8 | -1223035.772 | 2447248.924 |
| LG+R6 | -1223080.434 | 2447295.820 |
| LG+I+G4 | -1224879.318 | 2450808.732 |
| WAG+F+R7 | -1224883.928 | 2451125.556 |
| WAG+F+I+R6 | -1224889.484 | 2451126.061 |
| Q.PFAM+R7 | -1225558.083 | 2452272.332 |
| Q.PFAM+I+R6 | -1225568.008 | 2452281.575 |
| LG+G4 | -1226261.619 | 2453562.727 |
| JTT+F+R7 | -1228013.604 | 2457384.908 |
| JTT+F+I+R6 | -1228028.324 | 2457403.741 |
| Q.PLANT+F+R7 | -1228719.166 | 2458796.032 |
| Q.PLANT+F+I+R6 | -1228734.903 | 2458816.899 |
| WAG+I+R6 | -1231329.818 | 2463805.195 |
| WAG+R7 | -1231325.570 | 2463807.306 |
| Q.PLANT+R7 | -1231488.158 | 2464132.482 |
| Q.PLANT+I+R6 | -1231505.246 | 2464156.051 |
| CPREV+F+R7 | -1231425.641 | 2464208.982 |
| CPREV+F+I+R6 | -1231433.104 | 2464213.301 |
| DCMUT+F+R7 | -1232600.182 | 2466558.064 |
| DCMUT+F+I+R6 | -1232609.929 | 2466566.951 |
| MTINV+F+R7 | -1232933.055 | 2467223.810 |
| MTINV+F+I+R6 | -1232950.228 | 2467247.549 |
| CPREV+R7 | -1234567.189 | 2470290.544 |
| CPREV+I+R6 | -1234576.877 | 2470299.313 |
| JTT+R7 | -1235049.448 | 2471255.062 |
| JTT+I+R6 | -1235063.968 | 2471273.495 |
| PMB+F+R7 | -1237363.371 | 2476084.442 |
| PMB+F+I+R6 | -1237372.556 | 2476092.205 |
| MTMET+F+R7 | -1240771.888 | 2482901.476 |
| MTMET+F+I+R6 | -1240797.894 | 2482942.881 |
| Q.MAMMAL+F+R7 | -1240949.592 | 2483256.884 |
| Q.MAMMAL+F+I+R6 | -1240969.828 | 2483286.749 |
| DCMUT+R7 | -1242601.311 | 2486358.788 |
| DCMUT+I+R6 | -1242608.151 | 2486361.861 |
| PMB+R7 | -1245396.298 | 2491948.762 |
| PMB+I+R6 | -1245405.192 | 2491955.943 |
| Q.BIRD+F+R7 | -1250200.026 | 2501757.752 |
| Q.BIRD+F+I+R6 | -1250228.058 | 2501803.209 |
| Q.MAMMAL+R7 | -1250500.478 | 2502157.122 |
| Q.MAMMAL+I+R6 | -1250514.819 | 2502175.197 |
| Q.BIRD+R7 | -1258679.000 | 2518514.166 |
| Q.BIRD+I+R6 | -1258701.412 | 2518548.383 |
| MTVER+F+R7 | -1260276.826 | 2521911.352 |
| MTVER+F+I+R6 | -1260316.623 | 2521980.339 |
| LG+I | -1278466.841 | 2557973.171 |
| MTMET+R7 | -1281688.967 | 2564534.100 |
| MTMET+I+R6 | -1281721.966 | 2564589.491 |
| MTINV+R7 | -1283739.703 | 2568635.572 |
| MTINV+I+R6 | -1283764.107 | 2568673.773 |
| MTVER+R7 | -1301330.014 | 2603816.194 |
| MTVER+I+R6 | -1301377.897 | 2603901.353 |
| LG | -1323668.560 | 2648366.002 |
The inferred model Q.p__Deferribacterota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Deferribacterota_2+R7 | LG+F+R7 |
| BIC | 2428134.886 | 2437518.486 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Deferribacterota/loop_1/tree_update/Q.p__Deferribacterota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Deferribacterota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 119.91 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Deferribacterota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Deferribacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 0  
Normalized RF distance: 0.0  
Tree 1 branch length: 10.07957  
Tree 2 branch length: 11.18056  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1282484.091 | -1292275.379 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Deferribacterota_2):  
Pearson's correlation: 0.9662673797796095  
Euclidean distance: 0.5690088437927743  
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
Total time usage: 26933.96 seconds (7.48 h)  
