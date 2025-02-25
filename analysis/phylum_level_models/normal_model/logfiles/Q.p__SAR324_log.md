## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__SAR324  
  Taxa name: p__SAR324  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 62  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/select_id.txt. Sampling sequences for 118 loci.  
Number of input species: 62  
Remaining 118 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__SAR324  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__SAR324 -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum SAR324
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 118 alignments. Deleted 2 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/ref_tree.tre -l 15 -u 62 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/subtrees -m split
```
  
Original number of taxa: 62   
Number of pruned subtrees: 1   
Number of taxa after pruning: 62   
Pruned node IDs (degree): 1 (62)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/subtree_update/Q.p__SAR324
```
  
  Runtime: 1638.25 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__SAR324.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 47 |
| Q.YEAST | 41 |
| Q.PFAM | 22 |
| Q.PLANT | 5 |
| WAG | 2 |
| JTT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/subtree_update/Q.p__SAR324.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/subtree_update/Q.p__SAR324.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/model_update/Q.p__SAR324
```
  
  Runtime: 4790.95 seconds  
[Model update log](loop_1/model_update/Q.p__SAR324.iqtree)  
BIC of the new model: 3167582.6384  
Likelihood of the new model: -1520462.1109  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__SAR324_1)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.p__SAR324_1  
![Model bubble plot](loop_1/Q.p__SAR324_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9771824110205263  
Euclidean distance: 0.4755602518896631  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/tree_update/Q.p__SAR324_1.treefile
```
  
  Runtime: 384.99 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/tree_update/Q.p__SAR324_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/tree_update/Q.p__SAR324_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 12  
Normalized RF distance: 0.1  
Tree 1 branch length: 11.46117  
Tree 2 branch length: 15.06303  
Time usage for Loop_1: 6863.47 seconds (1.91 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/tree_update/Q.p__SAR324_1.treefile -l 15 -u 62 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/subtrees -m split
```
  
Original number of taxa: 62   
Number of pruned subtrees: 1   
Number of taxa after pruning: 62   
Pruned node IDs (degree): 1 (62)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PFAM,Q.p__SAR324_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/subtree_update/Q.p__SAR324
```
  
  Runtime: 1645.35 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__SAR324.iqtree)  
Best models for iteration 2:  
Q.p__SAR324_1  

| Model | Count |
|-------|-------|
| Q.p__SAR324_1 | 102 |
| LG | 7 |
| Q.YEAST | 5 |
| Q.PFAM | 4 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/subtree_update/Q.p__SAR324.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/subtree_update/Q.p__SAR324.treefile --model-joint GTR20+FO --init-model Q.p__SAR324_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/model_update/Q.p__SAR324
```
  
  Runtime: 6437.06 seconds  
[Model update log](loop_2/model_update/Q.p__SAR324.iqtree)  
BIC of the new model: 3167288.6046  
Likelihood of the new model: -1520315.094  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__SAR324_2)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.p__SAR324_2  
![Model bubble plot](loop_2/Q.p__SAR324_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999813557068351  
Euclidean distance: 0.04007948783625403  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/tree_update/Q.p__SAR324_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 420.26 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 12  
Normalized RF distance: 0.1  
Tree 1 branch length: 11.46117  
Tree 2 branch length: 15.07844  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__SAR324_1,Q.p__SAR324_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 100084.30 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__SAR324_1+R8 | -1548844.384 | 3099119.158 |
| Q.p__SAR324_1+I+R7 | -1548852.312 | 3099124.419 |
| Q.p__SAR324_2+R8 | -1548851.298 | 3099132.986 |
| Q.p__SAR324_2+I+R7 | -1548859.729 | 3099139.253 |
| Q.p__SAR324_1+R7 | -1548867.994 | 3099145.187 |
| Q.p__SAR324_2+R7 | -1548877.294 | 3099163.787 |
| Q.p__SAR324_1+F+R8 | -1550933.096 | 3103497.897 |
| Q.p__SAR324_1+F+I+R7 | -1550941.525 | 3103504.159 |
| Q.p__SAR324_1+F+R7 | -1550955.863 | 3103522.240 |
| Q.p__SAR324_2+F+R8 | -1550960.270 | 3103552.245 |
| Q.p__SAR324_2+F+I+R7 | -1550968.682 | 3103558.473 |
| Q.p__SAR324_2+F+R7 | -1550985.171 | 3103580.856 |
| LG+I+R7 | -1554359.502 | 3110138.799 |
| LG+R8 | -1554356.188 | 3110142.766 |
| LG+R7 | -1554368.084 | 3110145.367 |
| LG+I+R8 | -1554356.243 | 3110153.472 |
| LG+R9 | -1554353.733 | 3110159.047 |
| LG+F+I+R7 | -1554269.731 | 3110160.571 |
| LG+F+R8 | -1554265.421 | 3110162.547 |
| LG+F+R7 | -1554277.285 | 3110165.084 |
| LG+I+R6 | -1554457.523 | 3110313.650 |
| LG+R6 | -1554483.659 | 3110355.326 |
| Q.PFAM+I+R7 | -1555144.789 | 3111709.373 |
| Q.PFAM+R8 | -1555139.755 | 3111709.900 |
| Q.PFAM+R7 | -1555151.597 | 3111712.393 |
| Q.PFAM+F+R8 | -1555335.121 | 3112301.947 |
| Q.PFAM+F+I+R7 | -1555342.650 | 3112306.409 |
| Q.PFAM+F+R7 | -1555348.928 | 3112308.370 |
| Q.YEAST+F+I+R7 | -1555872.231 | 3113365.571 |
| Q.YEAST+F+R7 | -1555878.950 | 3113368.414 |
| Q.YEAST+F+R8 | -1555868.810 | 3113369.325 |
| LG+I+G4 | -1556249.545 | 3113802.335 |
| Q.INSECT+I+R7 | -1556516.117 | 3114452.029 |
| Q.INSECT+R8 | -1556511.466 | 3114453.322 |
| Q.INSECT+R7 | -1556523.522 | 3114456.243 |
| Q.YEAST+I+R7 | -1557200.467 | 3115820.729 |
| Q.YEAST+R8 | -1557196.911 | 3115824.212 |
| Q.YEAST+R7 | -1557208.886 | 3115826.971 |
| Q.INSECT+F+I+R7 | -1557586.695 | 3116794.499 |
| Q.INSECT+F+R7 | -1557593.136 | 3116796.786 |
| Q.INSECT+F+R8 | -1557582.674 | 3116797.053 |
| LG+G4 | -1557974.946 | 3117242.541 |
| WAG+F+I+R7 | -1560589.350 | 3122799.809 |
| WAG+F+R7 | -1560598.166 | 3122806.846 |
| WAG+F+R8 | -1560588.475 | 3122808.655 |
| WAG+I+R7 | -1562612.176 | 3126644.147 |
| WAG+R7 | -1562621.889 | 3126652.977 |
| WAG+R8 | -1562611.978 | 3126654.346 |
| JTT+F+I+R7 | -1564546.187 | 3130713.483 |
| JTT+F+R7 | -1564554.770 | 3130720.054 |
| JTT+F+R8 | -1564545.783 | 3130723.271 |
| Q.PLANT+R8 | -1564795.332 | 3131021.054 |
| Q.PLANT+I+R7 | -1564830.383 | 3131080.561 |
| Q.PLANT+R7 | -1564843.408 | 3131096.015 |
| Q.PLANT+F+R8 | -1565349.627 | 3132330.959 |
| Q.PLANT+F+I+R7 | -1565371.894 | 3132364.897 |
| Q.PLANT+F+R7 | -1565386.037 | 3132382.588 |
| JTT+I+R7 | -1566661.716 | 3134743.227 |
| JTT+R7 | -1566671.921 | 3134753.041 |
| JTT+R8 | -1566661.656 | 3134753.702 |
| CPREV+I+R7 | -1570647.789 | 3142715.373 |
| CPREV+R8 | -1570648.576 | 3142727.542 |
| CPREV+R7 | -1570663.554 | 3142736.307 |
| CPREV+F+I+R7 | -1571314.622 | 3144250.353 |
| CPREV+F+R8 | -1571312.816 | 3144257.337 |
| CPREV+F+R7 | -1571335.354 | 3144281.222 |
| DCMUT+F+I+R7 | -1573377.141 | 3148375.391 |
| DCMUT+F+R8 | -1573379.499 | 3148390.703 |
| DCMUT+F+R7 | -1573393.406 | 3148397.326 |
| MTINV+F+I+R7 | -1575400.639 | 3152422.387 |
| MTINV+F+R8 | -1575395.480 | 3152422.665 |
| MTINV+F+R7 | -1575411.467 | 3152433.448 |
| PMB+F+R7 | -1579491.202 | 3160592.918 |
| PMB+F+I+R7 | -1579487.369 | 3160595.847 |
| PMB+F+R8 | -1579486.104 | 3160603.913 |
| DCMUT+I+R7 | -1579624.708 | 3160669.211 |
| DCMUT+R8 | -1579622.907 | 3160676.204 |
| DCMUT+R7 | -1579649.334 | 3160707.867 |
| Q.MAMMAL+F+R8 | -1581529.488 | 3164690.681 |
| Q.MAMMAL+F+I+R7 | -1581546.315 | 3164713.739 |
| Q.MAMMAL+F+R7 | -1581559.051 | 3164728.616 |
| PMB+R7 | -1582355.373 | 3166119.945 |
| PMB+I+R7 | -1582351.779 | 3166123.353 |
| PMB+R8 | -1582350.357 | 3166131.104 |
| Q.MAMMAL+R8 | -1583413.143 | 3168256.676 |
| Q.MAMMAL+I+R7 | -1583425.790 | 3168271.375 |
| Q.MAMMAL+R7 | -1583431.539 | 3168272.277 |
| MTMET+F+R8 | -1584679.719 | 3170991.143 |
| MTMET+F+I+R7 | -1584706.982 | 3171035.073 |
| MTMET+F+R7 | -1584728.503 | 3171067.520 |
| Q.BIRD+F+R8 | -1592238.372 | 3186108.449 |
| Q.BIRD+F+I+R7 | -1592280.986 | 3186183.081 |
| Q.BIRD+F+R7 | -1592301.775 | 3186214.064 |
| Q.BIRD+R8 | -1593589.724 | 3188609.838 |
| Q.BIRD+I+R7 | -1593637.494 | 3188694.783 |
| Q.BIRD+R7 | -1593647.603 | 3188704.405 |
| MTVER+F+R8 | -1605598.851 | 3212829.407 |
| MTVER+F+I+R7 | -1605638.863 | 3212898.835 |
| MTVER+F+R7 | -1605685.451 | 3212981.416 |
| LG+I | -1631470.711 | 3264234.071 |
| MTMET+R8 | -1645762.351 | 3292955.092 |
| MTMET+I+R7 | -1645802.459 | 3293024.713 |
| MTMET+R7 | -1645874.072 | 3293157.343 |
| MTINV+R8 | -1654398.753 | 3310227.896 |
| MTINV+I+R7 | -1654441.862 | 3310303.519 |
| MTINV+R7 | -1654452.639 | 3310314.477 |
| MTVER+R8 | -1656744.872 | 3314920.134 |
| MTVER+I+R7 | -1656784.359 | 3314988.513 |
| MTVER+R7 | -1656859.453 | 3315128.105 |
| LG | -1679951.901 | 3361185.856 |
The inferred model Q.p__SAR324_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__SAR324_1+R8 | LG+I+R7 |
| BIC | 3099119.158 | 3110138.799 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loop_1/tree_update/Q.p__SAR324_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 151.44 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__SAR324/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0167  
Tree 1 branch length: 14.29091  
Tree 2 branch length: 15.07844  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1620367.621 | -1625465.066 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__SAR324_2):  
Pearson's correlation: 0.9752857330886318  
Euclidean distance: 0.4938421817517087  
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
Total time usage: 115760.43 seconds (32.16 h)  
