## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Dependentiae  
  Taxa name: p__Dependentiae  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 123  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 18 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Dependentiae/select_id.txt. Sampling sequences for 102 loci.  
Number of input species: 123  
Remaining 102 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Dependentiae  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Dependentiae -d 0.1 -o ../Result_nova/phylum_models/Q.p__Dependentiae/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Fusobacteriota as the outgroup for Phylum Dependentiae
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 106 alignments. Deleted 14 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Dependentiae/ref_tree.tre -l 15 -u 123 -o ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/subtrees -m split
```
  
Original number of taxa: 123   
Number of pruned subtrees: 1   
Number of taxa after pruning: 123   
Pruned node IDs (degree): 1 (123)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 102 loci files. Total number of potential alignments: 102.  
Obtained 102 alignments from all potential alignments.  
Remaining 102 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/subtree_update/Q.p__Dependentiae
```
  
  Runtime: 35196.10 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Dependentiae.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 52 |
| LG | 20 |
| Q.INSECT | 18 |
| Q.PFAM | 11 |
| MTMET | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/subtree_update/Q.p__Dependentiae.best_model.nex -te ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/subtree_update/Q.p__Dependentiae.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/model_update/Q.p__Dependentiae
```
  
  Runtime: 21493.37 seconds  
[Model update log](loop_1/model_update/Q.p__Dependentiae.iqtree)  
BIC of the new model: 7336410.4495  
Likelihood of the new model: -3555102.9643  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Dependentiae_1)  
Model set for next iteration: Q.YEAST,LG,Q.INSECT,Q.PFAM,Q.p__Dependentiae_1  
![Model bubble plot](loop_1/Q.p__Dependentiae_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9839155764083505  
Euclidean distance: 0.3702036353528595  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Dependentiae/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Dependentiae/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/tree_update/Q.p__Dependentiae_1.treefile
```
  
  Runtime: 596.00 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/tree_update/Q.p__Dependentiae_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Dependentiae/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Dependentiae/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/tree_update/Q.p__Dependentiae_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Dependentiae/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 42  
Normalized RF distance: 0.175  
Tree 1 branch length: 37.04804  
Tree 2 branch length: 49.79167  
Time usage for Loop_1: 57328.33 seconds (15.92 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/tree_update/Q.p__Dependentiae_1.treefile -l 15 -u 123 -o ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/subtrees -m split
```
  
Original number of taxa: 123   
Number of pruned subtrees: 1   
Number of taxa after pruning: 123   
Pruned node IDs (degree): 1 (123)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 102 loci files. Total number of potential alignments: 102.  
Obtained 102 alignments from all potential alignments.  
Remaining 102 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/training_loci -m MFP -mset Q.YEAST,LG,Q.INSECT,Q.PFAM,Q.p__Dependentiae_1 -mdef ../Result_nova/phylum_models/Q.p__Dependentiae/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/subtree_update/Q.p__Dependentiae
```
  
  Runtime: 15213.94 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Dependentiae.iqtree)  
Best models for iteration 2:  
Q.p__Dependentiae_1  

| Model | Count |
|-------|-------|
| Q.p__Dependentiae_1 | 86 |
| Q.INSECT | 6 |
| LG | 5 |
| Q.PFAM | 3 |
| Q.YEAST | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/subtree_update/Q.p__Dependentiae.best_model.nex -te ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/subtree_update/Q.p__Dependentiae.treefile --model-joint GTR20+FO --init-model Q.p__Dependentiae_1 -mdef ../Result_nova/phylum_models/Q.p__Dependentiae/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/model_update/Q.p__Dependentiae
```
  
  Runtime: 15614.02 seconds  
[Model update log](loop_2/model_update/Q.p__Dependentiae.iqtree)  
BIC of the new model: 7333563.8045  
Likelihood of the new model: -3553679.6418  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Dependentiae_2)  
Model set for next iteration: Q.INSECT,LG,Q.PFAM,Q.YEAST,Q.p__Dependentiae_2  
![Model bubble plot](loop_2/Q.p__Dependentiae_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999007745313597  
Euclidean distance: 0.034144680194597175  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Dependentiae/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/tree_update/Q.p__Dependentiae_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Dependentiae/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 574.86 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Dependentiae', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Dependentiae/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Dependentiae/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Dependentiae/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 44  
Normalized RF distance: 0.1833  
Tree 1 branch length: 37.04804  
Tree 2 branch length: 50.06864  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Dependentiae/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Dependentiae/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Dependentiae/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Dependentiae_1,Q.p__Dependentiae_2 -mdef ../Result_nova/phylum_models/Q.p__Dependentiae/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Dependentiae/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 8880.17 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Dependentiae_2+I+R9 | -3592291.482 | 7187298.504 |
| Q.p__Dependentiae_1+I+R9 | -3592330.083 | 7187375.706 |
| Q.YEAST+I+R9 | -3605379.795 | 7213475.130 |
| LG+F+I+R9 | -3608314.155 | 7219542.294 |
| Q.p__Dependentiae_1+F+I+R9 | -3608999.764 | 7220913.512 |
| Q.YEAST+F+I+R9 | -3609800.633 | 7222515.250 |
| Q.p__Dependentiae_2+F+I+R9 | -3609902.274 | 7222718.532 |
| Q.PFAM+F+I+R9 | -3610457.152 | 7223828.288 |
| Q.INSECT+I+R9 | -3611621.782 | 7225959.104 |
| LG+I+R9 | -3612994.683 | 7228704.906 |
| LG+R9 | -3613128.410 | 7228961.916 |
| LG+I+R8 | -3613216.524 | 7229127.700 |
| LG+R8 | -3613412.594 | 7229509.395 |
| LG+I+R7 | -3613679.643 | 7230033.049 |
| LG+R7 | -3614236.285 | 7231135.889 |
| LG+I+R6 | -3614801.309 | 7232255.492 |
| LG+R6 | -3615760.281 | 7234162.992 |
| Q.PFAM+I+R9 | -3616315.444 | 7235346.428 |
| Q.INSECT+F+I+R9 | -3618731.721 | 7240377.426 |
| LG+I+G4 | -3624308.666 | 7251176.207 |
| WAG+F+I+R9 | -3631157.027 | 7265228.038 |
| LG+G4 | -3631373.008 | 7265294.446 |
| WAG+I+R9 | -3636888.064 | 7276491.668 |
| Q.PLANT+F+I+R9 | -3643302.151 | 7289518.286 |
| JTT+F+I+R9 | -3644015.425 | 7290944.834 |
| Q.PLANT+I+R9 | -3645961.725 | 7294638.990 |
| CPREV+I+R9 | -3655210.867 | 7313137.274 |
| JTT+I+R9 | -3656149.830 | 7315015.200 |
| CPREV+F+I+R9 | -3656619.489 | 7316152.962 |
| DCMUT+F+I+R9 | -3658674.100 | 7320262.184 |
| MTINV+F+I+R9 | -3659548.710 | 7322011.404 |
| PMB+F+I+R9 | -3671447.274 | 7345808.532 |
| DCMUT+I+R9 | -3672431.181 | 7347577.902 |
| PMB+I+R9 | -3679787.830 | 7362291.200 |
| MTMET+F+I+R9 | -3684402.386 | 7371718.756 |
| Q.MAMMAL+F+I+R9 | -3686411.689 | 7375737.362 |
| Q.MAMMAL+I+R9 | -3697930.480 | 7398576.500 |
| Q.BIRD+F+I+R9 | -3712080.287 | 7427074.558 |
| Q.BIRD+I+R9 | -3723186.093 | 7449087.726 |
| MTVER+F+I+R9 | -3736276.246 | 7475466.476 |
| MTMET+I+R9 | -3795882.833 | 7594481.206 |
| MTINV+I+R9 | -3814702.973 | 7632121.486 |
| MTVER+I+R9 | -3816181.939 | 7635079.418 |
| LG+I | -3900438.590 | 7803425.610 |
| LG | -4008784.612 | 8020107.210 |
The inferred model Q.p__Dependentiae_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Dependentiae_2+I+R9 | Q.YEAST+I+R9 |
| BIC | 7187298.504 | 7213475.130 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Dependentiae/loop_1/tree_update/Q.p__Dependentiae_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Dependentiae/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 329.52 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Dependentiae/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Dependentiae/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Dependentiae/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Dependentiae/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 8  
Normalized RF distance: 0.0333  
Tree 1 branch length: 44.10108  
Tree 2 branch length: 50.06864  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -3669479.957 | -3689940.225 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Dependentiae_2):  
Pearson's correlation: 0.9748213072514327  
Euclidean distance: 0.49587959852289143  
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
Total time usage: 98119.13 seconds (27.26 h)  
