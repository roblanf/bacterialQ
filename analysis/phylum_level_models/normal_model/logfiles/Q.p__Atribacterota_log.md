## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Atribacterota  
  Taxa name: p__Atribacterota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 55  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 1 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 55  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Atribacterota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Atribacterota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Thermotogota as the outgroup for Phylum Atribacterota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/ref_tree.tre -l 15 -u 55 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/subtrees -m split
```
  
Original number of taxa: 55   
Number of pruned subtrees: 1   
Number of taxa after pruning: 55   
Pruned node IDs (degree): 1 (55)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/subtree_update/Q.p__Atribacterota
```
  
  Runtime: 2155.19 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Atribacterota.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 71 |
| LG | 12 |
| CPREV | 10 |
| Q.YEAST | 10 |
| JTT | 10 |
| Q.MAMMAL | 6 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/subtree_update/Q.p__Atribacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/subtree_update/Q.p__Atribacterota.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/model_update/Q.p__Atribacterota
```
  
  Runtime: 6559.35 seconds  
[Model update log](loop_1/model_update/Q.p__Atribacterota.iqtree)  
BIC of the new model: 2381467.9912  
Likelihood of the new model: -1136207.7922  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Atribacterota_1)  
Model set for next iteration: Q.PLANT,LG,CPREV,Q.YEAST,JTT,Q.MAMMAL,Q.p__Atribacterota_1  
![Model bubble plot](loop_1/Q.p__Atribacterota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9535432093805561  
Euclidean distance: 0.6530098356206864  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/Q.p__Atribacterota_1.treefile
```
  
  Runtime: 351.79 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/Q.p__Atribacterota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/Q.p__Atribacterota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
  Error:


processing file: tree_comparison.Rmd
Error in `plot.new()`:
! figure margins too large
Backtrace:
 1. global generate_cophylo_plot(tree1, tree2, output_path, nodel_label_type)
 3. phytools::plot.cophylo(...)
 4. graphics::plot.new()

Quitting from lines 118-129 [unnamed-chunk-3] (tree_comparison.Rmd)
Execution halted
  
  Exit code: 1  


processing file: tree_comparison.Rmd
Error in `plot.new()`:
! figure margins too large
Backtrace:
 1. global generate_cophylo_plot(tree1, tree2, output_path, nodel_label_type)
 3. phytools::plot.cophylo(...)
 4. graphics::plot.new()

Quitting from lines 118-129 [unnamed-chunk-3] (tree_comparison.Rmd)
Execution halted
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 14  
Normalized RF distance: 0.1321  
Tree 1 branch length: 7.63917  
Tree 2 branch length: 10.56971  
Time usage for Loop_1: 9107.51 seconds (2.53 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/Q.p__Atribacterota_1.treefile -l 15 -u 55 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/subtrees -m split
```
  
Original number of taxa: 55   
Number of pruned subtrees: 1   
Number of taxa after pruning: 55   
Pruned node IDs (degree): 1 (55)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/training_loci -m MFP -mset Q.PLANT,LG,CPREV,Q.YEAST,JTT,Q.MAMMAL,Q.p__Atribacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/subtree_update/Q.p__Atribacterota
```
  
  Runtime: 4201.53 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Atribacterota.iqtree)  
Best models for iteration 2:  
Q.p__Atribacterota_1  

| Model | Count |
|-------|-------|
| Q.p__Atribacterota_1 | 116 |
| Q.PLANT | 2 |
| LG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/subtree_update/Q.p__Atribacterota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/subtree_update/Q.p__Atribacterota.treefile --model-joint GTR20+FO --init-model Q.p__Atribacterota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/model_update/Q.p__Atribacterota
```
  
  Runtime: 7182.71 seconds  
[Model update log](loop_2/model_update/Q.p__Atribacterota.iqtree)  
BIC of the new model: 2379316.5768  
Likelihood of the new model: -1135132.085  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Atribacterota_2)  
Model set for next iteration: Q.PLANT,LG,Q.p__Atribacterota_2  
![Model bubble plot](loop_2/Q.p__Atribacterota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998738851614528  
Euclidean distance: 0.03623361942370071  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/Q.p__Atribacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 365.05 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
  Error:


processing file: tree_comparison.Rmd
Error in `plot.new()`:
! figure margins too large
Backtrace:
 1. global generate_cophylo_plot(tree1, tree2, output_path, nodel_label_type)
 3. phytools::plot.cophylo(...)
 4. graphics::plot.new()

Quitting from lines 118-129 [unnamed-chunk-3] (tree_comparison.Rmd)
Execution halted
  
  Exit code: 1  


processing file: tree_comparison.Rmd
Error in `plot.new()`:
! figure margins too large
Backtrace:
 1. global generate_cophylo_plot(tree1, tree2, output_path, nodel_label_type)
 3. phytools::plot.cophylo(...)
 4. graphics::plot.new()

Quitting from lines 118-129 [unnamed-chunk-3] (tree_comparison.Rmd)
Execution halted
  
[Tree comparison report](tree_comparison.html)  
RF distance: 16  
Normalized RF distance: 0.1509  
Tree 1 branch length: 7.63917  
Tree 2 branch length: 10.59388  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Atribacterota_1,Q.p__Atribacterota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 105951.07 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Atribacterota_1+R7 | -1160108.749 | 2321479.752 |
| Q.p__Atribacterota_1+I+R6 | -1160118.124 | 2321487.895 |
| Q.p__Atribacterota_2+R7 | -1160124.571 | 2321511.396 |
| Q.p__Atribacterota_2+I+R6 | -1160134.551 | 2321520.749 |
| Q.p__Atribacterota_1+F+R7 | -1161650.180 | 2324764.151 |
| Q.p__Atribacterota_1+F+I+R6 | -1161659.677 | 2324772.538 |
| Q.p__Atribacterota_2+F+R7 | -1161732.882 | 2324929.555 |
| Q.p__Atribacterota_2+F+I+R6 | -1161743.158 | 2324939.500 |
| Q.PLANT+F+R7 | -1168113.010 | 2337689.811 |
| Q.PLANT+F+I+R6 | -1168124.049 | 2337701.282 |
| JTT+F+R7 | -1168400.685 | 2338265.161 |
| JTT+F+I+R6 | -1168408.627 | 2338270.438 |
| LG+F+R7 | -1169510.466 | 2340484.723 |
| LG+F+I+R6 | -1169517.738 | 2340488.660 |
| Q.PFAM+F+R7 | -1170477.190 | 2342418.171 |
| Q.PFAM+F+I+R6 | -1170487.174 | 2342427.532 |
| Q.YEAST+F+R7 | -1170862.960 | 2343189.711 |
| Q.YEAST+F+I+R6 | -1170871.678 | 2343196.540 |
| Q.INSECT+F+R7 | -1171311.870 | 2344087.531 |
| Q.INSECT+F+I+R6 | -1171321.524 | 2344096.232 |
| Q.PLANT+R7 | -1171832.578 | 2344927.410 |
| Q.PLANT+I+R6 | -1171843.620 | 2344938.887 |
| Q.MAMMAL+F+R7 | -1172790.534 | 2347044.859 |
| Q.MAMMAL+F+I+R6 | -1172814.415 | 2347082.014 |
| Q.YEAST+R7 | -1173130.308 | 2347522.870 |
| Q.YEAST+I+R6 | -1173137.744 | 2347527.135 |
| Q.INSECT+R7 | -1173183.133 | 2347628.520 |
| Q.INSECT+I+R6 | -1173191.830 | 2347635.307 |
| LG+R7 | -1173610.927 | 2348484.108 |
| LG+I+R6 | -1173616.565 | 2348484.777 |
| LG+I+R7 | -1173611.696 | 2348496.253 |
| LG+R8 | -1173610.128 | 2348503.725 |
| LG+R6 | -1173660.314 | 2348561.668 |
| WAG+F+R7 | -1174148.340 | 2349760.471 |
| WAG+F+I+R6 | -1174194.096 | 2349841.376 |
| LG+I+G4 | -1174610.026 | 2350376.235 |
| CPREV+R7 | -1174683.161 | 2350628.576 |
| CPREV+I+R6 | -1174690.538 | 2350632.723 |
| LG+G4 | -1175758.639 | 2352662.853 |
| JTT+R7 | -1176062.908 | 2353388.070 |
| JTT+I+R6 | -1176070.427 | 2353392.501 |
| Q.PFAM+R7 | -1176096.234 | 2353454.722 |
| Q.PFAM+I+R6 | -1176103.984 | 2353459.615 |
| CPREV+F+I+R6 | -1176226.857 | 2353906.898 |
| CPREV+F+R7 | -1176223.016 | 2353909.823 |
| MTINV+F+R7 | -1176728.493 | 2354920.777 |
| MTINV+F+I+R6 | -1176740.164 | 2354933.512 |
| Q.BIRD+F+R7 | -1176909.866 | 2355283.523 |
| Q.BIRD+F+I+R6 | -1176931.843 | 2355316.870 |
| MTMET+F+R7 | -1178363.196 | 2358190.183 |
| MTMET+F+I+R6 | -1178377.759 | 2358208.702 |
| WAG+R7 | -1181675.475 | 2364613.204 |
| WAG+I+R6 | -1181714.952 | 2364681.551 |
| Q.MAMMAL+R7 | -1181931.940 | 2365126.134 |
| Q.MAMMAL+I+R6 | -1181943.611 | 2365138.869 |
| Q.BIRD+R7 | -1185195.205 | 2371652.664 |
| Q.BIRD+I+R6 | -1185208.870 | 2371669.387 |
| DCMUT+F+I+R6 | -1186055.902 | 2373564.988 |
| DCMUT+F+R7 | -1186051.329 | 2373566.449 |
| PMB+F+R7 | -1188948.042 | 2379359.875 |
| PMB+F+I+R6 | -1188966.665 | 2379386.514 |
| MTVER+F+R7 | -1190514.605 | 2382493.001 |
| MTVER+F+I+R6 | -1190531.748 | 2382516.680 |
| PMB+R7 | -1194703.713 | 2390669.680 |
| PMB+I+R6 | -1194717.611 | 2390686.869 |
| DCMUT+I+R6 | -1198849.472 | 2398950.591 |
| DCMUT+R7 | -1198845.157 | 2398952.568 |
| LG+I | -1214925.000 | 2430995.575 |
| MTMET+R7 | -1226449.094 | 2454160.442 |
| MTMET+I+R6 | -1226475.980 | 2454203.607 |
| MTINV+R7 | -1233888.617 | 2469039.488 |
| MTINV+I+R6 | -1233907.225 | 2469066.097 |
| MTVER+R7 | -1238388.963 | 2478040.180 |
| MTVER+I+R6 | -1238426.363 | 2478104.373 |
| LG | -1251504.350 | 2504143.668 |
The inferred model Q.p__Atribacterota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Atribacterota_1+R7 | Q.PLANT+F+R7 |
| BIC | 2321479.752 | 2337689.811 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/Q.p__Atribacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 128.98 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loop_1/tree_update/Q.p__Atribacterota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 122.66 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
Q.PLANT model has higher likelihood than LG model, use best_existing_model model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/allloci_best_existing_model_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Atribacterota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0189  
Tree 1 branch length: 10.85308  
Tree 2 branch length: 10.59388  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1231110.575 | -1244323.998 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.PLANT) and final model (Q.p__Atribacterota_2):  
Pearson's correlation: 0.9533742567673706  
Euclidean distance: 0.6582148070780628  
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
Total time usage: 127247.64 seconds (35.35 h)  
