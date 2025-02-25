## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Eisenbacteria  
  Taxa name: p__Eisenbacteria  
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
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Eisenbacteria/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 50  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Eisenbacteria  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Eisenbacteria -d 0.1 -o ../Result_nova/phylum_models/Q.p__Eisenbacteria/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Krumholzibacteriota as the outgroup for Phylum Eisenbacteria
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Eisenbacteria/ref_tree.tre -l 15 -u 50 -o ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/subtrees -m split
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/subtree_update/Q.p__Eisenbacteria
```
  
  Runtime: 2313.62 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Eisenbacteria.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 49 |
| Q.PFAM | 37 |
| Q.INSECT | 19 |
| Q.YEAST | 13 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/subtree_update/Q.p__Eisenbacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/subtree_update/Q.p__Eisenbacteria.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/model_update/Q.p__Eisenbacteria
```
  
  Runtime: 8113.51 seconds  
[Model update log](loop_1/model_update/Q.p__Eisenbacteria.iqtree)  
BIC of the new model: 3221175.4155  
Likelihood of the new model: -1557597.445  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Eisenbacteria_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,Q.p__Eisenbacteria_1  
![Model bubble plot](loop_1/Q.p__Eisenbacteria_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9509615644755987  
Euclidean distance: 0.7502179361087946  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Eisenbacteria/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Eisenbacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/tree_update/Q.p__Eisenbacteria_1.treefile
```
  
  Runtime: 251.69 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/tree_update/Q.p__Eisenbacteria_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/tree_update/Q.p__Eisenbacteria_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
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
Normalized RF distance: 0.1489  
Tree 1 branch length: 11.90697  
Tree 2 branch length: 15.24105  
Time usage for Loop_1: 10712.87 seconds (2.98 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/tree_update/Q.p__Eisenbacteria_1.treefile -l 15 -u 50 -o ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/subtrees -m split
```
  
Original number of taxa: 50   
Number of pruned subtrees: 1   
Number of taxa after pruning: 50   
Pruned node IDs (degree): 1 (50)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 119 loci files. Total number of potential alignments: 119.  
Obtained 119 alignments from all potential alignments.  
Remaining 119 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,Q.p__Eisenbacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Eisenbacteria/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/subtree_update/Q.p__Eisenbacteria
```
  
  Runtime: 2105.26 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Eisenbacteria.iqtree)  
Best models for iteration 2:  
Q.p__Eisenbacteria_1  

| Model | Count |
|-------|-------|
| Q.p__Eisenbacteria_1 | 105 |
| LG | 8 |
| Q.INSECT | 3 |
| Q.PFAM | 3 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/subtree_update/Q.p__Eisenbacteria.best_model.nex -te ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/subtree_update/Q.p__Eisenbacteria.treefile --model-joint GTR20+FO --init-model Q.p__Eisenbacteria_1 -mdef ../Result_nova/phylum_models/Q.p__Eisenbacteria/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/model_update/Q.p__Eisenbacteria
```
  
  Runtime: 3767.89 seconds  
[Model update log](loop_2/model_update/Q.p__Eisenbacteria.iqtree)  
BIC of the new model: 3218826.3385  
Likelihood of the new model: -1556422.9065  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Eisenbacteria_2)  
Model set for next iteration: LG,Q.INSECT,Q.PFAM,Q.p__Eisenbacteria_2  
![Model bubble plot](loop_2/Q.p__Eisenbacteria_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999830940246716  
Euclidean distance: 0.017828420794720662  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/tree_update/Q.p__Eisenbacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Eisenbacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 246.55 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Eisenbacteria', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
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
RF distance: 14  
Normalized RF distance: 0.1489  
Tree 1 branch length: 11.90697  
Tree 2 branch length: 15.27492  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Eisenbacteria/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Eisenbacteria/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Eisenbacteria/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Eisenbacteria_1,Q.p__Eisenbacteria_2 -mdef ../Result_nova/phylum_models/Q.p__Eisenbacteria/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Eisenbacteria/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 26789.84 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Eisenbacteria_1+I+R7 | -1585246.062 | 3171658.960 |
| Q.p__Eisenbacteria_1+R7 | -1585255.855 | 3171667.938 |
| Q.p__Eisenbacteria_1+I+R6 | -1585273.329 | 3171692.279 |
| Q.p__Eisenbacteria_2+I+R7 | -1585270.439 | 3171707.714 |
| Q.p__Eisenbacteria_2+R7 | -1585280.102 | 3171716.432 |
| Q.p__Eisenbacteria_2+I+R6 | -1585298.349 | 3171742.319 |
| Q.p__Eisenbacteria_1+F+I+R7 | -1587617.323 | 3176603.026 |
| Q.p__Eisenbacteria_1+F+R7 | -1587627.240 | 3176612.253 |
| Q.p__Eisenbacteria_1+F+I+R6 | -1587646.730 | 3176640.625 |
| Q.p__Eisenbacteria_2+F+I+R7 | -1587723.209 | 3176814.798 |
| Q.p__Eisenbacteria_2+F+R7 | -1587733.457 | 3176824.687 |
| Q.p__Eisenbacteria_2+F+I+R6 | -1587753.038 | 3176853.241 |
| LG+F+I+R7 | -1591633.036 | 3184634.452 |
| LG+F+R7 | -1591641.323 | 3184640.419 |
| LG+F+I+R6 | -1591657.612 | 3184662.389 |
| Q.PFAM+F+I+R7 | -1592259.327 | 3185887.034 |
| Q.PFAM+F+R7 | -1592266.883 | 3185891.539 |
| Q.PFAM+F+I+R6 | -1592285.568 | 3185918.301 |
| Q.YEAST+F+I+R7 | -1594234.904 | 3189838.188 |
| Q.YEAST+F+R7 | -1594253.780 | 3189865.333 |
| Q.YEAST+F+I+R6 | -1594273.375 | 3189893.915 |
| Q.INSECT+F+I+R7 | -1596674.010 | 3194716.400 |
| Q.INSECT+F+R7 | -1596689.291 | 3194736.355 |
| Q.INSECT+F+I+R6 | -1596717.053 | 3194781.271 |
| WAG+F+R7 | -1599556.541 | 3200470.855 |
| WAG+F+I+R7 | -1599552.314 | 3200473.008 |
| WAG+F+I+R6 | -1599568.266 | 3200483.697 |
| Q.PFAM+I+R7 | -1603586.449 | 3208339.734 |
| Q.PFAM+R7 | -1603592.470 | 3208341.168 |
| Q.PFAM+I+R6 | -1603600.482 | 3208346.585 |
| LG+R7 | -1608075.200 | 3217306.628 |
| LG+I+R6 | -1608082.199 | 3217310.019 |
| LG+I+R7 | -1608074.250 | 3217315.336 |
| LG+R8 | -1608072.391 | 3217322.226 |
| LG+R6 | -1608122.328 | 3217379.669 |
| JTT+F+I+R7 | -1609241.324 | 3219851.028 |
| JTT+F+R7 | -1609251.274 | 3219860.321 |
| JTT+F+I+R6 | -1609282.279 | 3219911.723 |
| LG+I+G4 | -1609520.681 | 3220091.514 |
| LG+G4 | -1611771.425 | 3224582.395 |
| Q.PLANT+F+I+R7 | -1613881.101 | 3229130.582 |
| Q.PLANT+F+R7 | -1613900.863 | 3229159.499 |
| Q.PLANT+F+I+R6 | -1613936.739 | 3229220.643 |
| WAG+R7 | -1614356.316 | 3229868.860 |
| WAG+I+R7 | -1614351.433 | 3229869.702 |
| WAG+I+R6 | -1614376.092 | 3229897.805 |
| DCMUT+F+I+R7 | -1614308.172 | 3229984.724 |
| DCMUT+F+R7 | -1614324.379 | 3230006.531 |
| DCMUT+F+I+R6 | -1614364.351 | 3230075.867 |
| CPREV+F+I+R7 | -1614569.389 | 3230507.158 |
| CPREV+F+R7 | -1614590.214 | 3230538.201 |
| CPREV+F+I+R6 | -1614604.409 | 3230555.983 |
| PMB+F+R7 | -1615625.390 | 3232608.553 |
| PMB+F+I+R6 | -1615632.646 | 3232612.457 |
| PMB+F+I+R7 | -1615623.231 | 3232614.842 |
| JTT+I+R7 | -1621340.954 | 3243848.744 |
| JTT+R7 | -1621351.148 | 3243858.524 |
| JTT+I+R6 | -1621366.027 | 3243877.675 |
| Q.INSECT+I+R7 | -1621614.215 | 3244395.266 |
| Q.INSECT+R7 | -1621620.085 | 3244396.398 |
| Q.INSECT+I+R6 | -1621635.770 | 3244417.161 |
| Q.YEAST+I+R7 | -1626659.848 | 3254486.532 |
| Q.YEAST+R7 | -1626666.197 | 3254488.622 |
| Q.YEAST+I+R6 | -1626677.432 | 3254500.485 |
| MTINV+F+I+R7 | -1627323.172 | 3256014.724 |
| MTINV+F+R7 | -1627348.296 | 3256054.365 |
| MTINV+F+I+R6 | -1627398.117 | 3256143.399 |
| PMB+I+R6 | -1629561.857 | 3260269.335 |
| PMB+R7 | -1629557.544 | 3260271.316 |
| PMB+I+R7 | -1629554.886 | 3260276.608 |
| Q.PLANT+I+R7 | -1629589.920 | 3260346.676 |
| Q.PLANT+R7 | -1629617.510 | 3260391.248 |
| Q.PLANT+I+R6 | -1629650.983 | 3260447.587 |
| Q.MAMMAL+F+I+R7 | -1632047.873 | 3265464.126 |
| Q.MAMMAL+F+R7 | -1632063.710 | 3265485.193 |
| Q.MAMMAL+F+I+R6 | -1632089.235 | 3265525.635 |
| DCMUT+I+R7 | -1635004.135 | 3271175.106 |
| DCMUT+R7 | -1635018.798 | 3271193.824 |
| CPREV+I+R7 | -1635030.480 | 3271227.796 |
| CPREV+R7 | -1635044.619 | 3271245.466 |
| CPREV+I+R6 | -1635052.893 | 3271251.407 |
| DCMUT+I+R6 | -1635059.553 | 3271264.727 |
| Q.MAMMAL+I+R7 | -1642301.292 | 3285769.420 |
| Q.MAMMAL+R7 | -1642311.599 | 3285779.426 |
| Q.MAMMAL+I+R6 | -1642328.528 | 3285802.677 |
| MTMET+F+I+R7 | -1643093.212 | 3287554.804 |
| MTMET+F+R7 | -1643137.570 | 3287632.913 |
| MTMET+F+I+R6 | -1643212.447 | 3287772.059 |
| Q.BIRD+F+I+R7 | -1646135.591 | 3293639.562 |
| Q.BIRD+F+R7 | -1646158.762 | 3293675.297 |
| Q.BIRD+F+I+R6 | -1646191.195 | 3293729.555 |
| Q.BIRD+I+R7 | -1656647.788 | 3314462.412 |
| Q.BIRD+R7 | -1656663.829 | 3314483.886 |
| Q.BIRD+I+R6 | -1656684.873 | 3314515.367 |
| MTVER+F+I+R7 | -1668902.236 | 3339172.852 |
| MTVER+F+R7 | -1668953.591 | 3339264.955 |
| MTVER+F+I+R6 | -1669059.230 | 3339465.625 |
| LG+I | -1680352.679 | 3361744.903 |
| LG | -1733728.005 | 3468484.947 |
| MTMET+I+R7 | -1752551.667 | 3506270.170 |
| MTMET+R7 | -1752583.165 | 3506322.558 |
| MTMET+I+R6 | -1752666.536 | 3506478.693 |
| MTINV+I+R7 | -1759421.606 | 3520010.048 |
| MTINV+R7 | -1759444.430 | 3520045.088 |
| MTINV+I+R6 | -1759481.130 | 3520107.881 |
| MTVER+I+R7 | -1761271.921 | 3523710.678 |
| MTVER+R7 | -1761303.506 | 3523763.240 |
| MTVER+I+R6 | -1761436.747 | 3524019.115 |
The inferred model Q.p__Eisenbacteria_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Eisenbacteria_1+I+R7 | LG+F+I+R7 |
| BIC | 3171658.96 | 3184634.452 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Eisenbacteria/loop_1/tree_update/Q.p__Eisenbacteria_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Eisenbacteria/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 247.86 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Eisenbacteria/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0213  
Tree 1 branch length: 14.98923  
Tree 2 branch length: 15.27492  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1648378.133 | -1671827.691 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Eisenbacteria_2):  
Pearson's correlation: 0.9505060192594534  
Euclidean distance: 0.7608750379619321  
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
Total time usage: 44038.30 seconds (12.23 h)  

