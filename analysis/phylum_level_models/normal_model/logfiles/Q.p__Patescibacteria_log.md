## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Patescibacteria  
  Taxa name: p__Patescibacteria  
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
Discarded 13 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Patescibacteria/select_id.txt. Sampling sequences for 107 loci.  
Number of input species: 4567  
Remaining 107 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Patescibacteria  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Patescibacteria -d 0.1 -o ../Result_nova/phylum_models/Q.p__Patescibacteria/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Margulisbacteria as the outgroup for Phylum Patescibacteria
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Patescibacteria/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/subtrees -m split
```
  
Original number of taxa: 4567   
Number of pruned subtrees: 40   
Number of taxa after pruning: 4362   
Pruned node IDs (degree): 2559 (250) 2279 (250) 1539 (250) 751 (248) 4003 (240) 3086 (237) 503 (236) 1876 (222) 4259 (220) 3339 (219) 1327 (212) 3719 (199) 2808 (179) 253 (164) 998 (159) 4 (112) 416 (88) 1802 (75) 180 (72) 2999 (71) 3937 (64) 3600 (61) 116 (52) 2200 (51) 1157 (50) 4478 (47) 1283 (44) 3557 (43) 2529 (31) 2114 (29) 2178 (23) 3693 (21) 2251 (21) 4527 (20) 1251 (19) 3322 (18) 2097 (18) 3675 (17) 1207 (15) 3071 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 40 subtree files and 107 loci files. Total number of potential alignments: 4280.  
Sub-sampling 2000 alignments from 4280 alignments.  
Remaining 2000 alignments. Deleted 185 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/subtree_update/Q.p__Patescibacteria
```
  
  Runtime: 146122.99 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Patescibacteria.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 805 |
| LG | 611 |
| Q.PFAM | 324 |
| Q.INSECT | 216 |
| Q.PLANT | 36 |
| MTMET | 7 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/subtree_update/Q.p__Patescibacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/subtree_update/Q.p__Patescibacteria.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/model_update/Q.p__Patescibacteria
```
  
  Runtime: 207132.64 seconds  
[Model update log](loop_1/model_update/Q.p__Patescibacteria.iqtree)  
BIC of the new model: 103980832.5892  
Likelihood of the new model: -49567772.6577  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Patescibacteria_1)  
Model set for next iteration: Q.YEAST,LG,Q.PFAM,Q.INSECT,Q.p__Patescibacteria_1  
![Model bubble plot](loop_1/Q.p__Patescibacteria_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9816979765733074  
Euclidean distance: 0.3912303387920359  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Patescibacteria/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Patescibacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/tree_update/Q.p__Patescibacteria_1.treefile
```
  
  Runtime: 15853.29 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/tree_update/Q.p__Patescibacteria_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/tree_update/Q.p__Patescibacteria_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 1938  
Normalized RF distance: 0.2123  
Tree 1 branch length: 1153.72525  
Tree 2 branch length: 1420.3527  
Time usage for Loop_1: 372356.64 seconds (103.43 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/tree_update/Q.p__Patescibacteria_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/subtrees -m split
```
  
Original number of taxa: 4567   
Number of pruned subtrees: 39   
Number of taxa after pruning: 4321   
Pruned node IDs (degree): 1460 (250) 1728 (250) 2404 (249) 1111 (246) 3585 (240) 510 (232) 3841 (220) 4342 (219) 873 (219) 2652 (219) 3298 (199) 4160 (183) 2125 (181) 3009 (179) 347 (164) 6 (104) 256 (92) 173 (82) 2305 (75) 3188 (64) 3521 (64) 814 (60) 121 (52) 761 (50) 1989 (50) 4060 (47) 1370 (43) 2082 (43) 2870 (37) 1429 (31) 2906 (29) 2968 (23) 3272 (21) 4108 (20) 3253 (18) 2042 (18) 2379 (18) 745 (15) 1356 (15)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 39 subtree files and 107 loci files. Total number of potential alignments: 4173.  
Sub-sampling 2000 alignments from 4173 alignments.  
Remaining 2000 alignments. Deleted 177 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.PFAM,Q.INSECT,Q.p__Patescibacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Patescibacteria/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/subtree_update/Q.p__Patescibacteria
```
  
  Runtime: 97684.78 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Patescibacteria.iqtree)  
Best models for iteration 2:  
Q.p__Patescibacteria_1  

| Model | Count |
|-------|-------|
| Q.p__Patescibacteria_1 | 1496 |
| LG | 191 |
| Q.PFAM | 113 |
| Q.INSECT | 100 |
| Q.YEAST | 100 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/subtree_update/Q.p__Patescibacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/subtree_update/Q.p__Patescibacteria.treefile --model-joint GTR20+FO --init-model Q.p__Patescibacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Patescibacteria/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/model_update/Q.p__Patescibacteria
```
  
  Runtime: 141389.53 seconds  
[Model update log](loop_2/model_update/Q.p__Patescibacteria.iqtree)  
BIC of the new model: 102767904.822  
Likelihood of the new model: -48946449.9629  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Patescibacteria_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,Q.p__Patescibacteria_2  
![Model bubble plot](loop_2/Q.p__Patescibacteria_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998427013317646  
Euclidean distance: 0.04188446950769767  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Patescibacteria/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Patescibacteria/loop_1/tree_update/Q.p__Patescibacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Patescibacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Patescibacteria/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 10480.09 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Patescibacteria/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Patescibacteria', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Patescibacteria/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 1936  
Normalized RF distance: 0.2121  
Tree 1 branch length: 1153.72525  
Tree 2 branch length: 1428.3501  
### Model comparison  
Comparison between initial best model (Q.YEAST) and final model (Q.p__Patescibacteria_2):  
Pearson's correlation: 0.9806924996273835  
Euclidean distance: 0.4089693608880496  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Patescibacteria/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Patescibacteria/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Patescibacteria/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Patescibacteria_1,Q.p__Patescibacteria_2 -mdef ../Result_nova/phylum_models/Q.p__Patescibacteria/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Patescibacteria/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Patescibacteria/final_test/logfiles/reftree_best_concat_model
```
  
