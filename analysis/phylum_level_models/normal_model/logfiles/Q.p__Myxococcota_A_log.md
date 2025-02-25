## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Myxococcota_A  
  Taxa name: p__Myxococcota_A  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 95  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 95  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Myxococcota_A  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Myxococcota_A -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Myxococcota_A
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/ref_tree.tre -l 15 -u 95 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/subtrees -m split
```
  
Original number of taxa: 95   
Number of pruned subtrees: 1   
Number of taxa after pruning: 95   
Pruned node IDs (degree): 1 (95)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/subtree_update/Q.p__Myxococcota_A
```
  
  Runtime: 11217.37 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Myxococcota_A.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 57 |
| Q.PFAM | 36 |
| Q.YEAST | 24 |
| Q.PLANT | 2 |
| WAG | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/subtree_update/Q.p__Myxococcota_A.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/subtree_update/Q.p__Myxococcota_A.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/model_update/Q.p__Myxococcota_A
```
  
  Runtime: 22238.09 seconds  
[Model update log](loop_1/model_update/Q.p__Myxococcota_A.iqtree)  
BIC of the new model: 5261034.4103  
Likelihood of the new model: -2526678.97  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Myxococcota_A_1)  
Model set for next iteration: LG,Q.PFAM,Q.YEAST,Q.p__Myxococcota_A_1  
![Model bubble plot](loop_1/Q.p__Myxococcota_A_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9359058075438207  
Euclidean distance: 0.94460319157496  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/tree_update/Q.p__Myxococcota_A_1.treefile
```
  
  Runtime: 655.02 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/tree_update/Q.p__Myxococcota_A_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/tree_update/Q.p__Myxococcota_A_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 32  
Normalized RF distance: 0.172  
Tree 1 branch length: 17.83992  
Tree 2 branch length: 24.05666  
Time usage for Loop_1: 34158.91 seconds (9.49 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/tree_update/Q.p__Myxococcota_A_1.treefile -l 15 -u 95 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/subtrees -m split
```
  
Original number of taxa: 95   
Number of pruned subtrees: 1   
Number of taxa after pruning: 95   
Pruned node IDs (degree): 1 (95)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.YEAST,Q.p__Myxococcota_A_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/subtree_update/Q.p__Myxococcota_A
```
  
  Runtime: 7739.71 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Myxococcota_A.iqtree)  
Best models for iteration 2:  
Q.p__Myxococcota_A_1  

| Model | Count |
|-------|-------|
| Q.p__Myxococcota_A_1 | 105 |
| LG | 8 |
| Q.YEAST | 5 |
| Q.PFAM | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/subtree_update/Q.p__Myxococcota_A.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/subtree_update/Q.p__Myxococcota_A.treefile --model-joint GTR20+FO --init-model Q.p__Myxococcota_A_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/model_update/Q.p__Myxococcota_A
```
  
  Runtime: 7522.97 seconds  
[Model update log](loop_2/model_update/Q.p__Myxococcota_A.iqtree)  
BIC of the new model: 5258863.4587  
Likelihood of the new model: -2525593.4942  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Myxococcota_A_2)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.p__Myxococcota_A_2  
![Model bubble plot](loop_2/Q.p__Myxococcota_A_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998142613519827  
Euclidean distance: 0.05419226732261973  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/tree_update/Q.p__Myxococcota_A_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 618.43 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 32  
Normalized RF distance: 0.172  
Tree 1 branch length: 17.83992  
Tree 2 branch length: 24.14252  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Myxococcota_A_1,Q.p__Myxococcota_A_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 69952.11 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Myxococcota_A_2+I+R9 | -2574861.424 | 5151888.356 |
| Q.p__Myxococcota_A_1+I+R9 | -2574866.227 | 5151897.962 |
| Q.p__Myxococcota_A_2+R9 | -2574875.523 | 5151905.939 |
| Q.p__Myxococcota_A_1+R9 | -2574878.611 | 5151912.115 |
| Q.p__Myxococcota_A_1+F+I+R9 | -2584620.359 | 5171607.916 |
| Q.p__Myxococcota_A_1+F+R9 | -2584632.249 | 5171621.080 |
| Q.p__Myxococcota_A_2+F+I+R9 | -2585250.648 | 5172868.494 |
| Q.p__Myxococcota_A_2+F+R9 | -2585264.142 | 5172884.866 |
| LG+F+R9 | -2591969.993 | 5186296.568 |
| LG+F+I+R9 | -2591965.072 | 5186297.342 |
| Q.PFAM+F+I+R9 | -2592631.416 | 5187630.030 |
| Q.PFAM+F+R9 | -2592641.343 | 5187639.268 |
| Q.YEAST+F+I+R9 | -2597019.741 | 5196406.680 |
| Q.YEAST+F+R9 | -2597034.203 | 5196424.988 |
| Q.INSECT+F+I+R9 | -2601759.855 | 5205886.908 |
| Q.INSECT+F+R9 | -2601772.655 | 5205901.892 |
| WAG+F+R9 | -2604476.576 | 5211309.734 |
| WAG+F+I+R9 | -2604485.439 | 5211338.076 |
| Q.PFAM+I+R9 | -2613747.502 | 5229660.512 |
| Q.PFAM+R9 | -2613756.038 | 5229666.969 |
| JTT+F+R9 | -2621017.200 | 5244390.982 |
| JTT+F+I+R9 | -2621013.967 | 5244395.132 |
| LG+R9 | -2623580.725 | 5249316.343 |
| LG+I+R9 | -2623575.866 | 5249317.240 |
| LG+I+R8 | -2623602.012 | 5249348.302 |
| LG+R8 | -2623697.487 | 5249528.636 |
| LG+I+R7 | -2623739.701 | 5249602.449 |
| LG+R7 | -2623849.520 | 5249811.472 |
| LG+I+R6 | -2624061.989 | 5250225.795 |
| LG+R6 | -2624440.463 | 5250972.127 |
| CPREV+F+R9 | -2626055.060 | 5254466.702 |
| CPREV+F+I+R9 | -2626054.143 | 5254475.484 |
| Q.PLANT+F+I+R9 | -2626335.400 | 5255037.998 |
| Q.PLANT+F+R9 | -2626358.701 | 5255073.984 |
| DCMUT+F+I+R9 | -2628542.263 | 5259451.724 |
| DCMUT+F+R9 | -2628562.511 | 5259481.604 |
| LG+I+G4 | -2629303.404 | 5260613.088 |
| WAG+R9 | -2630590.685 | 5263336.263 |
| WAG+I+R9 | -2630607.510 | 5263380.528 |
| LG+G4 | -2634785.940 | 5271567.544 |
| PMB+F+R9 | -2638358.167 | 5279072.916 |
| PMB+F+I+R9 | -2638380.875 | 5279128.948 |
| JTT+R9 | -2642870.736 | 5287896.365 |
| JTT+I+R9 | -2642880.525 | 5287926.558 |
| Q.INSECT+I+R9 | -2643768.711 | 5289702.930 |
| Q.INSECT+R9 | -2643779.788 | 5289714.469 |
| Q.YEAST+I+R9 | -2651133.845 | 5304433.198 |
| Q.YEAST+R9 | -2651140.399 | 5304435.691 |
| MTINV+F+I+R9 | -2651538.025 | 5305443.248 |
| MTINV+F+R9 | -2651587.495 | 5305531.572 |
| Q.PLANT+I+R9 | -2653859.314 | 5309884.136 |
| Q.PLANT+R9 | -2653876.004 | 5309906.901 |
| Q.MAMMAL+F+I+R9 | -2659377.744 | 5321122.686 |
| Q.MAMMAL+F+R9 | -2659411.078 | 5321178.738 |
| DCMUT+R9 | -2661694.156 | 5325543.205 |
| DCMUT+I+R9 | -2661693.178 | 5325551.864 |
| PMB+R9 | -2665712.128 | 5333579.149 |
| PMB+I+R9 | -2665737.429 | 5333640.366 |
| CPREV+R9 | -2667244.408 | 5336643.709 |
| CPREV+I+R9 | -2667247.784 | 5336661.076 |
| MTMET+F+I+R9 | -2675516.547 | 5353400.292 |
| MTMET+F+R9 | -2675585.957 | 5353528.496 |
| Q.MAMMAL+I+R9 | -2675700.597 | 5353566.702 |
| Q.MAMMAL+R9 | -2675725.632 | 5353606.157 |
| Q.BIRD+F+I+R9 | -2681549.589 | 5365466.376 |
| Q.BIRD+F+R9 | -2681590.255 | 5365537.092 |
| Q.BIRD+I+R9 | -2699172.371 | 5400510.250 |
| Q.BIRD+R9 | -2699206.081 | 5400567.055 |
| MTVER+F+I+R9 | -2714101.228 | 5430569.654 |
| MTVER+F+R9 | -2714193.916 | 5430744.414 |
| LG+I | -2805420.690 | 5612837.044 |
| MTMET+I+R9 | -2857359.382 | 5716884.272 |
| MTMET+R9 | -2857421.068 | 5716997.029 |
| MTVER+I+R9 | -2866751.328 | 5735668.164 |
| MTVER+R9 | -2866816.278 | 5735787.449 |
| MTINV+I+R9 | -2867256.523 | 5736678.554 |
| MTINV+R9 | -2867330.535 | 5736815.963 |
| LG | -2904217.932 | 5810420.913 |
The inferred model Q.p__Myxococcota_A_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Myxococcota_A_2+I+R9 | LG+F+R9 |
| BIC | 5151888.356 | 5186296.568 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loop_1/tree_update/Q.p__Myxococcota_A_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 284.51 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota_A/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 10  
Normalized RF distance: 0.0538  
Tree 1 branch length: 23.04775  
Tree 2 branch length: 24.14252  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2656185.264 | -2700027.594 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Myxococcota_A_2):  
Pearson's correlation: 0.9346483287453722  
Euclidean distance: 0.9715270304010017  
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
Total time usage: 120461.01 seconds (33.46 h)  
