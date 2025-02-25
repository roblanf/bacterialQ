## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 3  
  Convergence threshold: 0.999  
  File prefix: Q.p__Acidobacteriota  
  Taxa name: p__Acidobacteriota  
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
Discarded 0 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Acidobacteriota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 1891  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Acidobacteriota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Acidobacteriota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Acidobacteriota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Acidobacteriota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Acidobacteriota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/subtrees -m split
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 18   
Number of taxa after pruning: 1867   
Pruned node IDs (degree): 1163 (214) 15 (204) 499 (185) 685 (168) 1728 (164) 1565 (164) 854 (155) 1008 (120) 1450 (116) 293 (98) 422 (78) 246 (47) 1376 (39) 1415 (35) 222 (23) 401 (21) 1127 (21) 1147 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 18 subtree files and 120 loci files. Total number of potential alignments: 2160.  
Sub-sampling 2000 alignments from 2160 alignments.  
Remaining 2000 alignments. Deleted 12 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/subtree_update/Q.p__Acidobacteriota
```
  
  Runtime: 55248.78 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Acidobacteriota.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| Q.INSECT | 614 |
| Q.PFAM | 533 |
| LG | 418 |
| Q.PLANT | 258 |
| Q.YEAST | 175 |
| MTART | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/subtree_update/Q.p__Acidobacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/subtree_update/Q.p__Acidobacteriota.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/model_update/Q.p__Acidobacteriota
```
  
  Runtime: 183982.95 seconds  
[Model update log](loop_1/model_update/Q.p__Acidobacteriota.iqtree)  
BIC of the new model: 69871110.9031  
Likelihood of the new model: -32573496.6345  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Acidobacteriota_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.PLANT,Q.YEAST,Q.p__Acidobacteriota_1  
![Model bubble plot](loop_1/Q.p__Acidobacteriota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.951371340694024  
Euclidean distance: 0.6936367558602274  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Acidobacteriota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Acidobacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/tree_update/Q.p__Acidobacteriota_1.treefile
```
  
  Runtime: 9136.24 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/tree_update/Q.p__Acidobacteriota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/tree_update/Q.p__Acidobacteriota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 634  
Normalized RF distance: 0.1679  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 295.94106  
Time usage for Loop_1: 249284.00 seconds (69.25 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/tree_update/Q.p__Acidobacteriota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/subtrees -m split
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 17   
Number of taxa after pruning: 1869   
Pruned node IDs (degree): 1318 (214) 1531 (206) 510 (185) 696 (168) 116 (164) 1736 (156) 1005 (154) 1172 (145) 886 (120) 13 (104) 433 (78) 280 (47) 329 (47) 377 (23) 864 (22) 412 (21) 1158 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 17 subtree files and 120 loci files. Total number of potential alignments: 2040.  
Sub-sampling 2000 alignments from 2040 alignments.  
Remaining 2000 alignments. Deleted 10 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,Q.PLANT,Q.YEAST,Q.p__Acidobacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Acidobacteriota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/subtree_update/Q.p__Acidobacteriota
```
  
  Runtime: 55070.18 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Acidobacteriota.iqtree)  
Best models for iteration 2:  
Q.p__Acidobacteriota_1  

| Model | Count |
|-------|-------|
| Q.p__Acidobacteriota_1 | 1640 |
| Q.INSECT | 150 |
| Q.PFAM | 79 |
| LG | 78 |
| Q.PLANT | 35 |
| Q.YEAST | 18 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/subtree_update/Q.p__Acidobacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/subtree_update/Q.p__Acidobacteriota.treefile --model-joint GTR20+FO --init-model Q.p__Acidobacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Acidobacteriota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/model_update/Q.p__Acidobacteriota
```
  
  Runtime: 192108.46 seconds  
[Model update log](loop_2/model_update/Q.p__Acidobacteriota.iqtree)  
BIC of the new model: 73763970.9096  
Likelihood of the new model: -34379844.6959  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Acidobacteriota_2)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.p__Acidobacteriota_2  
![Model bubble plot](loop_2/Q.p__Acidobacteriota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999268211975213  
Euclidean distance: 0.029735472876390456  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Acidobacteriota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Acidobacteriota/loop_1/tree_update/Q.p__Acidobacteriota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Acidobacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Acidobacteriota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 8974.14 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Acidobacteriota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Acidobacteriota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Acidobacteriota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 638  
Normalized RF distance: 0.169  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 296.04497  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (Q.p__Acidobacteriota_2):  
Pearson's correlation: 0.9510478355834133  
Euclidean distance: 0.702906157763456  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Acidobacteriota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Acidobacteriota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Acidobacteriota/loci/concat_loci.faa -m TESTNEWONLY -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Acidobacteriota_1,Q.p__Acidobacteriota_2 -mdef ../Result_nova/phylum_models/Q.p__Acidobacteriota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Acidobacteriota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Acidobacteriota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 1068874.78 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Acidobacteriota_2+I+R10 | -35664768.060 | 71369875.273 |
| Q.p__Acidobacteriota_1+I+R10 | -35665906.440 | 71372152.033 |
| Q.p__Acidobacteriota_1+F+I+R10 | -35746330.460 | 71533201.875 |
| Q.p__Acidobacteriota_2+F+I+R10 | -35750529.520 | 71541599.995 |
| LG+F+I+R10 | -35830267.490 | 71701075.935 |
| Q.YEAST+F+I+R10 | -35831108.330 | 71702757.615 |
| Q.PFAM+F+I+R10 | -35834908.160 | 71710357.275 |
| Q.INSECT+F+I+R10 | -35842995.430 | 71726531.815 |
| Q.PFAM+I+R10 | -35906067.570 | 71852474.293 |
| LG+I+R10 | -35986679.950 | 72013699.053 |
| LG+R10 | -35989397.180 | 72019122.892 |
| LG+I+R9 | -35997170.610 | 72034659.130 |
| LG+R9 | -36000885.260 | 72042077.809 |
| LG+I+R8 | -36013775.550 | 72067847.768 |
| LG+R8 | -36018477.010 | 72077240.067 |
| WAG+F+I+R10 | -36020975.930 | 72082492.815 |
| LG+I+R7 | -36037920.730 | 72116116.886 |
| LG+R7 | -36044910.760 | 72130086.325 |
| LG+I+R6 | -36075599.750 | 72191453.684 |
| Q.INSECT+I+R10 | -36080373.370 | 72201085.893 |
| LG+R6 | -36087316.610 | 72214876.782 |
| JTT+F+I+R10 | -36097838.530 | 72236218.015 |
| WAG+I+R10 | -36134337.830 | 72309014.813 |
| LG+I+R5 | -36139691.630 | 72319616.201 |
| LG+R5 | -36157350.580 | 72354923.480 |
| Q.YEAST+I+R10 | -36177857.510 | 72396054.173 |
| JTT+I+R10 | -36189599.150 | 72419537.453 |
| Q.PLANT+F+I+R10 | -36219581.240 | 72479703.435 |
| LG+I+R4 | -36251927.730 | 72544067.159 |
| LG+I+G4 | -36268056.510 | 72576271.613 |
| LG+R4 | -36279065.880 | 72598332.838 |
| LG+G4 | -36304196.860 | 72648541.692 |
| DCMUT+F+I+R10 | -36315851.250 | 72672243.455 |
| Q.PLANT+I+R10 | -36338867.990 | 72718075.133 |
| CPREV+F+I+R10 | -36414142.140 | 72868825.235 |
| PMB+F+I+R10 | -36474791.410 | 72990123.775 |
| LG+I+R3 | -36491733.860 | 73023658.177 |
| DCMUT+I+R10 | -36515543.640 | 73071426.433 |
| LG+R3 | -36542530.210 | 73125240.255 |
| MTINV+F+I+R10 | -36547869.970 | 73136280.895 |
| CPREV+I+R10 | -36574900.820 | 73190140.793 |
| PMB+I+R10 | -36594631.050 | 73229601.253 |
| Q.MAMMAL+F+I+R10 | -36624780.360 | 73290101.675 |
| Q.MAMMAL+I+R10 | -36655816.500 | 73351972.153 |
| MTMET+F+I+R10 | -36905539.720 | 73851620.395 |
| Q.BIRD+F+I+R10 | -36996695.670 | 74033932.295 |
| Q.BIRD+I+R10 | -37029340.190 | 74099019.533 |
| LG+I+R2 | -37106406.220 | 74252981.654 |
| LG+R2 | -37217007.600 | 74474173.793 |
| MTVER+F+I+R10 | -37555048.570 | 75150638.095 |
| MTMET+I+R10 | -38677133.630 | 77394606.413 |
| MTINV+I+R10 | -38745500.480 | 77531340.113 |
| MTVER+I+R10 | -39016243.520 | 78072826.193 |
| LG+I | -39627683.450 | 79295514.872 |
| LG | -39952985.790 | 79946108.931 |
The inferred model Q.p__Acidobacteriota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Acidobacteriota_2+I+R10 | LG+F+I+R10 |
| BIC | 71369875.273 | 71701075.935 |
### Pairwise comparison of trees  
![Heatmap of RF distance of trees:](estimated_tree/RF_dist.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_dist.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 1575627.48 seconds (437.67 h)  
