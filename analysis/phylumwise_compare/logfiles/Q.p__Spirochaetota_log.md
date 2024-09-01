## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Spirochaetota  
  Taxa name: p__Spirochaetota  
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
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Spirochaetota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 1348  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Spirochaetota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Spirochaetota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Spirochaetota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Fusobacteriota as the outgroup for Phylum Spirochaetota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Spirochaetota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/subtrees -m split
```
  
Original number of taxa: 1348   
Number of pruned subtrees: 14   
Number of taxa after pruning: 1294   
Pruned node IDs (degree): 830 (238) 90 (223) 1152 (197) 674 (148) 553 (122) 1085 (65) 401 (60) 343 (58) 463 (46) 8 (36) 312 (32) 50 (29) 531 (21) 512 (19)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 14 subtree files and 119 loci files. Total number of potential alignments: 1666.  
Obtained 1602 alignments from all potential alignments.  
Remaining 1602 alignments. Deleted 64 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/subtree_update/Q.p__Spirochaetota
```
  
  Runtime: 55210.03 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Spirochaetota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 453 |
| Q.INSECT | 393 |
| LG | 313 |
| Q.PLANT | 236 |
| Q.PFAM | 204 |
| MTMET | 2 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/subtree_update/Q.p__Spirochaetota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/subtree_update/Q.p__Spirochaetota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/model_update/Q.p__Spirochaetota
```
  
  Runtime: 82355.74 seconds  
[Model update log](loop_1/model_update/Q.p__Spirochaetota.iqtree)  
BIC of the new model: 51212237.5125  
Likelihood of the new model: -23965045.4889  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Spirochaetota_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.PLANT,Q.PFAM,Q.p__Spirochaetota_1  
![Model bubble plot](loop_1/Q.p__Spirochaetota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9840331188107809  
Euclidean distance: 0.36283254752609534  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Spirochaetota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Spirochaetota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/tree_update/Q.p__Spirochaetota_1.treefile
```
  
  Runtime: 4363.11 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/tree_update/Q.p__Spirochaetota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/tree_update/Q.p__Spirochaetota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 412  
Normalized RF distance: 0.1532  
Tree 1 branch length: 180.24057  
Tree 2 branch length: 246.09273  
Time usage for Loop_1: 142447.15 seconds (39.57 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/tree_update/Q.p__Spirochaetota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/subtrees -m split
```
  
Original number of taxa: 1348   
Number of pruned subtrees: 13   
Number of taxa after pruning: 1271   
Pruned node IDs (degree): 706 (238) 1148 (201) 943 (180) 537 (148) 148 (129) 416 (122) 278 (60) 339 (46) 3 (39) 71 (36) 113 (33) 42 (20) 388 (19)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 13 subtree files and 119 loci files. Total number of potential alignments: 1547.  
Obtained 1484 alignments from all potential alignments.  
Remaining 1484 alignments. Deleted 63 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.PLANT,Q.PFAM,Q.p__Spirochaetota_1 -mdef ../Result_nova/phylum_models/Q.p__Spirochaetota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/subtree_update/Q.p__Spirochaetota
```
  
  Runtime: 44464.49 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Spirochaetota.iqtree)  
Best models for iteration 2:  
Q.p__Spirochaetota_1  

| Model | Count |
|-------|-------|
| Q.p__Spirochaetota_1 | 1025 |
| Q.PLANT | 142 |
| Q.YEAST | 98 |
| LG | 91 |
| Q.PFAM | 83 |
| Q.INSECT | 45 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/subtree_update/Q.p__Spirochaetota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/subtree_update/Q.p__Spirochaetota.treefile --model-joint GTR20+FO --init-model Q.p__Spirochaetota_1 -mdef ../Result_nova/phylum_models/Q.p__Spirochaetota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/model_update/Q.p__Spirochaetota
```
  
  Runtime: 73162.33 seconds  
[Model update log](loop_2/model_update/Q.p__Spirochaetota.iqtree)  
BIC of the new model: 49738642.9779  
Likelihood of the new model: -23265709.3793  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Spirochaetota_2)  
Model set for next iteration: Q.PLANT,Q.YEAST,LG,Q.PFAM,Q.p__Spirochaetota_2  
![Model bubble plot](loop_2/Q.p__Spirochaetota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999261573950291  
Euclidean distance: 0.02755035557110201  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/tree_update/Q.p__Spirochaetota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Spirochaetota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 4460.84 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Spirochaetota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 408  
Normalized RF distance: 0.1517  
Tree 1 branch length: 180.24057  
Tree 2 branch length: 246.78282  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Spirochaetota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Spirochaetota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Spirochaetota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Spirochaetota_1,Q.p__Spirochaetota_2 -mdef ../Result_nova/phylum_models/Q.p__Spirochaetota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Spirochaetota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 76931.06 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Spirochaetota_1+I+R8 | -25421764.700 | 50872276.920 |
| Q.p__Spirochaetota_2+I+R8 | -25422032.440 | 50872812.400 |
| Q.p__Spirochaetota_1+F+I+R8 | -25469804.060 | 50968557.339 |
| Q.p__Spirochaetota_2+F+I+R8 | -25473646.560 | 50976242.339 |
| Q.YEAST+I+R8 | -25499303.350 | 51027354.220 |
| LG+F+I+R8 | -25501794.760 | 51032538.739 |
| Q.PFAM+F+I+R8 | -25508839.490 | 51046628.199 |
| Q.YEAST+F+I+R8 | -25512596.440 | 51054142.099 |
| Q.INSECT+I+R8 | -25514792.130 | 51058331.780 |
| Q.PFAM+I+R8 | -25520627.880 | 51070003.280 |
| LG+I+R8 | -25521615.470 | 51071978.460 |
| LG+R8 | -25525980.880 | 51080698.664 |
| LG+I+R7 | -25539287.510 | 51107301.308 |
| LG+R7 | -25545578.170 | 51119872.012 |
| Q.INSECT+F+I+R8 | -25551537.690 | 51132024.599 |
| LG+I+R6 | -25566118.070 | 51160941.197 |
| LG+R6 | -25575963.970 | 51180622.381 |
| LG+I+R5 | -25611608.680 | 51251901.185 |
| LG+R5 | -25627858.280 | 51284389.769 |
| WAG+F+I+R8 | -25638154.710 | 51305258.639 |
| WAG+I+R8 | -25662740.600 | 51354228.720 |
| LG+I+G4 | -25701661.520 | 51431932.555 |
| JTT+F+I+R8 | -25718783.560 | 51466516.339 |
| LG+G4 | -25731214.960 | 51491028.819 |
| JTT+I+R8 | -25753366.730 | 51535480.980 |
| Q.PLANT+I+R8 | -25788131.750 | 51605011.020 |
| Q.PLANT+F+I+R8 | -25810719.110 | 51650387.439 |
| CPREV+I+R8 | -25826643.760 | 51682035.040 |
| DCMUT+F+I+R8 | -25879379.550 | 51787708.319 |
| CPREV+F+I+R8 | -25880211.990 | 51789373.199 |
| PMB+F+I+R8 | -25902150.490 | 51833250.199 |
| PMB+I+R8 | -25931381.090 | 51891509.700 |
| MTINV+F+I+R8 | -25950096.680 | 51929142.579 |
| DCMUT+I+R8 | -25952512.590 | 51933772.700 |
| Q.MAMMAL+F+I+R8 | -26064827.030 | 52158603.279 |
| Q.MAMMAL+I+R8 | -26082187.390 | 52193122.300 |
| MTMET+F+I+R8 | -26175636.380 | 52380221.979 |
| Q.BIRD+F+I+R8 | -26317818.960 | 52664587.139 |
| Q.BIRD+I+R8 | -26335545.220 | 52699837.960 |
| MTVER+F+I+R8 | -26674580.530 | 53378110.279 |
| MTINV+I+R8 | -27033407.770 | 54095563.060 |
| MTMET+I+R8 | -27034659.300 | 54098066.120 |
| MTVER+I+R8 | -27429118.970 | 54886985.460 |
| LG+I | -28074327.780 | 56177254.459 |
| LG | -28335119.560 | 56698827.403 |
The inferred model Q.p__Spirochaetota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Spirochaetota_1+I+R8 | Q.YEAST+I+R8 |
| BIC | 50872276.92 | 51027354.220 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Spirochaetota/loop_1/tree_update/Q.p__Spirochaetota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Spirochaetota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 4248.03 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Spirochaetota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Spirochaetota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 42  
Normalized RF distance: 0.0156  
Tree 1 branch length: 232.68062  
Tree 2 branch length: 246.78282  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -25480443.451 | -25578901.981 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Spirochaetota_2):  
Pearson's correlation: 0.9812342089232687  
Euclidean distance: 0.431189408133574  
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
Total time usage: 346608.07 seconds (96.28 h)  
