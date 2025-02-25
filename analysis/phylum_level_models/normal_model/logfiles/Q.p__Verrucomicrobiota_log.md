## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Verrucomicrobiota  
  Taxa name: p__Verrucomicrobiota  
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
Discarded 3 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/select_id.txt. Sampling sequences for 117 loci.  
Number of input species: 2454  
Remaining 117 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Verrucomicrobiota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Verrucomicrobiota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Chlamydiota as the outgroup for Phylum Verrucomicrobiota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/subtrees -m split
```
  
Original number of taxa: 2454   
Number of pruned subtrees: 21   
Number of taxa after pruning: 2382   
Pruned node IDs (degree): 1275 (246) 2212 (243) 476 (235) 2007 (206) 191 (195) 855 (185) 1593 (142) 1808 (132) 1160 (110) 11 (94) 385 (92) 105 (83) 1039 (79) 1735 (73) 1940 (68) 710 (68) 810 (42) 1531 (27) 1571 (23) 1127 (22) 784 (17)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 21 subtree files and 117 loci files. Total number of potential alignments: 2457.  
Sub-sampling 2000 alignments from 2457 alignments.  
Remaining 2000 alignments. Deleted 63 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/subtree_update/Q.p__Verrucomicrobiota
```
  
  Runtime: 107181.33 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Verrucomicrobiota.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| Q.INSECT | 615 |
| Q.PFAM | 609 |
| LG | 426 |
| Q.YEAST | 194 |
| Q.PLANT | 153 |
| MTMET | 2 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/subtree_update/Q.p__Verrucomicrobiota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/subtree_update/Q.p__Verrucomicrobiota.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/model_update/Q.p__Verrucomicrobiota
```
  
  Runtime: 325274.91 seconds  
[Model update log](loop_1/model_update/Q.p__Verrucomicrobiota.iqtree)  
BIC of the new model: 73831439.014  
Likelihood of the new model: -34335456.0094  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Verrucomicrobiota_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.YEAST,Q.PLANT,Q.p__Verrucomicrobiota_1  
![Model bubble plot](loop_1/Q.p__Verrucomicrobiota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9647327888461743  
Euclidean distance: 0.5554886842537484  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/tree_update/Q.p__Verrucomicrobiota_1.treefile
```
  
  Runtime: 16622.36 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/tree_update/Q.p__Verrucomicrobiota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/tree_update/Q.p__Verrucomicrobiota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 718  
Normalized RF distance: 0.1464  
Tree 1 branch length: 301.49877  
Tree 2 branch length: 395.08517  
Time usage for Loop_1: 450684.28 seconds (125.19 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/tree_update/Q.p__Verrucomicrobiota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/subtrees -m split
```
  
Original number of taxa: 2454   
Number of pruned subtrees: 21   
Number of taxa after pruning: 2377   
Pruned node IDs (degree): 1345 (246) 2212 (243) 476 (235) 2007 (206) 108 (195) 939 (181) 1662 (142) 1808 (132) 1229 (110) 839 (101) 10 (94) 302 (92) 393 (84) 1152 (75) 1940 (68) 710 (68) 811 (25) 1640 (23) 1604 (23) 784 (17) 1132 (17)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 21 subtree files and 117 loci files. Total number of potential alignments: 2457.  
Sub-sampling 2000 alignments from 2457 alignments.  
Remaining 2000 alignments. Deleted 63 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,Q.PLANT,Q.p__Verrucomicrobiota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/subtree_update/Q.p__Verrucomicrobiota
```
  
  Runtime: 107223.25 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Verrucomicrobiota.iqtree)  
Best models for iteration 2:  
Q.p__Verrucomicrobiota_1  

| Model | Count |
|-------|-------|
| Q.p__Verrucomicrobiota_1 | 1557 |
| Q.INSECT | 114 |
| Q.PFAM | 102 |
| LG | 98 |
| Q.PLANT | 80 |
| Q.YEAST | 49 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/subtree_update/Q.p__Verrucomicrobiota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/subtree_update/Q.p__Verrucomicrobiota.treefile --model-joint GTR20+FO --init-model Q.p__Verrucomicrobiota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/model_update/Q.p__Verrucomicrobiota
```
  
  Runtime: 239082.93 seconds  
[Model update log](loop_2/model_update/Q.p__Verrucomicrobiota.iqtree)  
BIC of the new model: 73580610.1772  
Likelihood of the new model: -34231825.3355  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Verrucomicrobiota_2)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.PLANT,Q.YEAST,Q.p__Verrucomicrobiota_2  
![Model bubble plot](loop_2/Q.p__Verrucomicrobiota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999576883624495  
Euclidean distance: 0.02063646771006965  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/tree_update/Q.p__Verrucomicrobiota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 13363.81 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 724  
Normalized RF distance: 0.1476  
Tree 1 branch length: 301.49877  
Tree 2 branch length: 395.98464  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Verrucomicrobiota_1,Q.p__Verrucomicrobiota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 355814.48 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Verrucomicrobiota_1+I+R9 | -42725369.140 | 85502929.006 |
| Q.p__Verrucomicrobiota_2+I+R9 | -42726532.110 | 85505254.946 |
| Q.p__Verrucomicrobiota_1+F+I+R9 | -42807023.860 | 85666439.913 |
| Q.p__Verrucomicrobiota_2+F+I+R9 | -42811178.280 | 85674748.753 |
| Q.PFAM+F+I+R9 | -42900963.230 | 85854318.653 |
| LG+F+I+R9 | -42905017.190 | 85862426.573 |
| Q.PFAM+I+R9 | -42907267.220 | 85866725.166 |
| Q.YEAST+F+I+R9 | -42935676.530 | 85923745.253 |
| Q.INSECT+F+I+R9 | -42964076.460 | 85980545.113 |
| LG+I+R9 | -42985255.770 | 86022702.266 |
| LG+R9 | -42989348.810 | 86030877.742 |
| LG+I+R8 | -43006096.170 | 86064361.859 |
| LG+R8 | -43011729.180 | 86075617.275 |
| LG+I+R7 | -43036931.920 | 86126012.151 |
| LG+R7 | -43044517.060 | 86141171.828 |
| Q.INSECT+I+R9 | -43076715.930 | 86205622.586 |
| LG+I+R6 | -43086017.020 | 86224161.144 |
| LG+R6 | -43098691.520 | 86249499.541 |
| WAG+F+I+R9 | -43104280.250 | 86260952.693 |
| WAG+I+R9 | -43142518.340 | 86337227.406 |
| Q.YEAST+I+R9 | -43152588.060 | 86357366.846 |
| JTT+F+I+R9 | -43271976.740 | 86596345.673 |
| JTT+I+R9 | -43297018.380 | 86646227.486 |
| LG+I+G4 | -43322178.820 | 86696389.312 |
| LG+G4 | -43362175.260 | 86776371.589 |
| Q.PLANT+F+I+R9 | -43471526.800 | 86995445.793 |
| Q.PLANT+I+R9 | -43508319.040 | 87068828.806 |
| DCMUT+F+I+R9 | -43531462.800 | 87115317.793 |
| CPREV+F+I+R9 | -43562708.100 | 87177808.393 |
| PMB+F+I+R9 | -43589714.520 | 87231821.233 |
| DCMUT+I+R9 | -43632619.710 | 87317430.146 |
| CPREV+I+R9 | -43647408.820 | 87347008.366 |
| PMB+I+R9 | -43650227.350 | 87352645.426 |
| MTINV+F+I+R9 | -43779807.840 | 87612007.873 |
| Q.MAMMAL+I+R9 | -43899990.800 | 87852172.326 |
| Q.MAMMAL+F+I+R9 | -43944934.610 | 87942261.413 |
| MTMET+F+I+R9 | -44203815.550 | 88460023.293 |
| Q.BIRD+I+R9 | -44378625.610 | 88809441.946 |
| Q.BIRD+F+I+R9 | -44428449.700 | 88909291.593 |
| MTVER+F+I+R9 | -44979621.150 | 90011634.493 |
| MTMET+I+R9 | -46045817.390 | 92143825.506 |
| MTINV+I+R9 | -46096643.660 | 92245478.046 |
| MTVER+I+R9 | -46498573.480 | 93049337.686 |
| LG+I | -47308939.200 | 94669899.469 |
| LG | -47651606.350 | 95355223.165 |
The inferred model Q.p__Verrucomicrobiota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Verrucomicrobiota_1+I+R9 | LG+F+I+R9 |
| BIC | 85502929.006 | 85862426.573 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loop_1/tree_update/Q.p__Verrucomicrobiota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 14768.81 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Verrucomicrobiota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 72  
Normalized RF distance: 0.0147  
Tree 1 branch length: 381.67564  
Tree 2 branch length: 395.98464  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -42754006.793 | -43010384.039 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Verrucomicrobiota_2):  
Pearson's correlation: 0.9692891428130074  
Euclidean distance: 0.5529503185790342  
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
Total time usage: 1183161.17 seconds (328.66 h)  
