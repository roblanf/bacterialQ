## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 3  
  Convergence threshold: 0.999  
  File prefix: Q.p__Cyanobacteriota  
  Taxa name: p__Cyanobacteriota  
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
Discarded 2 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Cyanobacteriota/select_id.txt. Sampling sequences for 118 loci.  
Number of input species: 2214  
Remaining 118 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Cyanobacteriota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Cyanobacteriota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Cyanobacteriota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Margulisbacteria as the outgroup for Phylum Cyanobacteriota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Cyanobacteriota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/subtrees -m split
```
  
Original number of taxa: 2214   
Number of pruned subtrees: 23   
Number of taxa after pruning: 2075   
Pruned node IDs (degree): 1178 (247) 1907 (237) 399 (219) 964 (192) 798 (165) 1549 (134) 276 (124) 1432 (115) 141 (106) 4 (94) 617 (80) 1685 (77) 1812 (43) 711 (40) 1871 (37) 767 (31) 1157 (22) 1788 (22) 98 (21) 255 (21) 2198 (17) 751 (16) 119 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 23 subtree files and 118 loci files. Total number of potential alignments: 2714.  
Sub-sampling 2000 alignments from 2714 alignments.  
Remaining 2000 alignments. Deleted 18 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/subtree_update/Q.p__Cyanobacteriota
```
  
  Runtime: 35453.83 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Cyanobacteriota.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 594 |
| Q.YEAST | 396 |
| Q.INSECT | 389 |
| LG | 318 |
| Q.PFAM | 291 |
| MTART | 9 |
| MTMET | 3 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/subtree_update/Q.p__Cyanobacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/subtree_update/Q.p__Cyanobacteriota.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/model_update/Q.p__Cyanobacteriota
```
  
  Runtime: 122526.18 seconds  
[Model update log](loop_1/model_update/Q.p__Cyanobacteriota.iqtree)  
BIC of the new model: 41421188.0711  
Likelihood of the new model: -18593964.1452  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Cyanobacteriota_1)  
Model set for next iteration: Q.PLANT,Q.YEAST,Q.INSECT,LG,Q.PFAM,Q.p__Cyanobacteriota_1  
![Model bubble plot](loop_1/Q.p__Cyanobacteriota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9629939682208339  
Euclidean distance: 0.5508090380362424  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Cyanobacteriota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/tree_update/Q.p__Cyanobacteriota_1.treefile
```
  
  Runtime: 12870.65 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/tree_update/Q.p__Cyanobacteriota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/tree_update/Q.p__Cyanobacteriota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 1148  
Normalized RF distance: 0.2596  
Tree 1 branch length: 148.51123  
Tree 2 branch length: 206.03522  
Time usage for Loop_1: 172546.40 seconds (47.93 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/tree_update/Q.p__Cyanobacteriota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/subtrees -m split
```
  
Original number of taxa: 2214   
Number of pruned subtrees: 23   
Number of taxa after pruning: 2064   
Pruned node IDs (degree): 799 (247) 1892 (238) 255 (219) 1053 (192) 473 (145) 1549 (134) 1399 (110) 141 (106) 1244 (104) 4 (94) 617 (80) 1685 (77) 1347 (53) 1794 (46) 702 (39) 1856 (37) 1508 (31) 778 (22) 98 (21) 2129 (21) 2198 (17) 743 (16) 119 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 23 subtree files and 118 loci files. Total number of potential alignments: 2714.  
Sub-sampling 2000 alignments from 2714 alignments.  
Remaining 2000 alignments. Deleted 14 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/training_loci -m MFP -mset Q.PLANT,Q.YEAST,Q.INSECT,LG,Q.PFAM,Q.p__Cyanobacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Cyanobacteriota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/subtree_update/Q.p__Cyanobacteriota
```
  
  Runtime: 34216.68 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Cyanobacteriota.iqtree)  
Best models for iteration 2:  
Q.p__Cyanobacteriota_1  

| Model | Count |
|-------|-------|
| Q.p__Cyanobacteriota_1 | 1271 |
| Q.PLANT | 279 |
| Q.PFAM | 126 |
| LG | 114 |
| Q.YEAST | 111 |
| Q.INSECT | 99 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/subtree_update/Q.p__Cyanobacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/subtree_update/Q.p__Cyanobacteriota.treefile --model-joint GTR20+FO --init-model Q.p__Cyanobacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Cyanobacteriota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/model_update/Q.p__Cyanobacteriota
```
  
  Runtime: 104654.07 seconds  
[Model update log](loop_2/model_update/Q.p__Cyanobacteriota.iqtree)  
BIC of the new model: 41485215.5879  
Likelihood of the new model: -18631038.6932  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Cyanobacteriota_2)  
Model set for next iteration: Q.PLANT,Q.PFAM,LG,Q.YEAST,Q.INSECT,Q.p__Cyanobacteriota_2  
![Model bubble plot](loop_2/Q.p__Cyanobacteriota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998671105893278  
Euclidean distance: 0.03395423066174437  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Cyanobacteriota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loop_1/tree_update/Q.p__Cyanobacteriota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Cyanobacteriota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 8028.82 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Cyanobacteriota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Cyanobacteriota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Cyanobacteriota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 1164  
Normalized RF distance: 0.2632  
Tree 1 branch length: 148.51123  
Tree 2 branch length: 205.99134  
### Model comparison  
Comparison between initial best model (Q.PLANT) and final model (Q.p__Cyanobacteriota_2):  
Pearson's correlation: 0.9617345633315048  
Euclidean distance: 0.561160907108667  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Cyanobacteriota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Cyanobacteriota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Cyanobacteriota/loci/concat_loci.faa -m TESTNEWONLY -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Cyanobacteriota_1,Q.p__Cyanobacteriota_2 -mdef ../Result_nova/phylum_models/Q.p__Cyanobacteriota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Cyanobacteriota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Cyanobacteriota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 2226813.02 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Cyanobacteriota_1+I+R10 | -27181005.200 | 54409016.596 |
| Q.p__Cyanobacteriota_2+I+R10 | -27183692.970 | 54414392.136 |
| Q.p__Cyanobacteriota_2+F+I+R10 | -27238226.660 | 54523660.488 |
| Q.p__Cyanobacteriota_1+F+I+R10 | -27240073.940 | 54527355.048 |
| Q.INSECT+I+R10 | -27274467.240 | 54595940.676 |
| Q.YEAST+I+R10 | -27275728.080 | 54598462.356 |
| LG+F+I+R10 | -27328184.640 | 54703576.448 |
| LG+I+R10 | -27329743.570 | 54706493.336 |
| Q.PFAM+I+R10 | -27330796.310 | 54708598.816 |
| LG+R10 | -27333394.190 | 54713783.999 |
| Q.PFAM+F+I+R10 | -27335303.420 | 54717814.008 |
| LG+I+R9 | -27339743.640 | 54726472.321 |
| LG+R9 | -27343667.970 | 54734310.404 |
| Q.INSECT+F+I+R10 | -27346737.340 | 54740681.848 |
| Q.YEAST+F+I+R10 | -27348266.520 | 54743740.208 |
| LG+I+R8 | -27351900.770 | 54750765.426 |
| LG+R8 | -27358109.290 | 54763171.889 |
| LG+I+R7 | -27371393.450 | 54789729.632 |
| LG+R7 | -27379512.080 | 54805956.314 |
| LG+I+R6 | -27402330.970 | 54851583.517 |
| LG+R6 | -27414018.550 | 54874948.099 |
| WAG+I+R10 | -27419663.770 | 54886333.736 |
| WAG+F+I+R10 | -27420535.270 | 54888277.708 |
| JTT+F+I+R10 | -27442581.660 | 54932370.488 |
| LG+I+R5 | -27452680.560 | 54952261.542 |
| JTT+I+R10 | -27463975.830 | 54974957.856 |
| LG+R5 | -27470256.200 | 54987402.244 |
| Q.PLANT+I+R10 | -27508658.490 | 55064323.176 |
| Q.PLANT+F+I+R10 | -27522921.360 | 55093049.888 |
| CPREV+I+R10 | -27544180.890 | 55135367.976 |
| LG+I+R4 | -27544752.540 | 55136384.347 |
| LG+I+G4 | -27557648.220 | 55162122.820 |
| LG+R4 | -27575332.470 | 55197533.629 |
| LG+G4 | -27595036.670 | 55236889.142 |
| CPREV+F+I+R10 | -27598838.530 | 55244884.228 |
| MTINV+F+I+R10 | -27637388.120 | 55321983.408 |
| DCMUT+F+I+R10 | -27655712.160 | 55358631.488 |
| DCMUT+I+R10 | -27694810.100 | 55436626.396 |
| LG+I+R3 | -27738285.970 | 55523430.052 |
| PMB+F+I+R10 | -27774701.390 | 55596609.948 |
| LG+R3 | -27790242.530 | 55627332.595 |
| PMB+I+R10 | -27810260.560 | 55667527.316 |
| Q.MAMMAL+F+I+R10 | -27814985.380 | 55677177.928 |
| Q.MAMMAL+I+R10 | -27829566.070 | 55706138.336 |
| MTMET+F+I+R10 | -27834463.040 | 55716133.248 |
| Q.BIRD+F+I+R10 | -28077347.740 | 56201902.648 |
| Q.BIRD+I+R10 | -28081488.210 | 56209982.616 |
| LG+I+R2 | -28236264.390 | 56519365.737 |
| MTVER+F+I+R10 | -28284299.840 | 56615806.848 |
| LG+R2 | -28361927.590 | 56770681.560 |
| MTMET+I+R10 | -28638899.600 | 57324805.396 |
| MTINV+I+R10 | -28689543.160 | 57426092.516 |
| MTVER+I+R10 | -28940529.020 | 57928064.236 |
| LG+I | -30340131.170 | 60727078.142 |
| LG | -30711891.720 | 61470588.665 |
The inferred model Q.p__Cyanobacteriota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Cyanobacteriota_1+I+R10 | LG+F+I+R10 |
| BIC | 54409016.596 | 54703576.448 |
### Pairwise comparison of trees  
![Heatmap of RF distance of trees:](estimated_tree/RF_dist.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_dist.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 2547535.57 seconds (707.65 h)  
