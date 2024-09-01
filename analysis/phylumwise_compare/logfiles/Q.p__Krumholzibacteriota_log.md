## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Krumholzibacteriota  
  Taxa name: p__Krumholzibacteriota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 93  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/select_id.txt. Sampling sequences for 118 loci.  
Number of input species: 93  
Remaining 118 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Krumholzibacteriota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Krumholzibacteriota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Eisenbacteria as the outgroup for Phylum Krumholzibacteriota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/ref_tree.tre -l 15 -u 93 -o ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/subtrees -m split
```
  
Original number of taxa: 93   
Number of pruned subtrees: 1   
Number of taxa after pruning: 93   
Pruned node IDs (degree): 1 (93)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/subtree_update/Q.p__Krumholzibacteriota
```
  
  Runtime: 11365.07 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Krumholzibacteriota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 41 |
| Q.PFAM | 37 |
| Q.INSECT | 27 |
| Q.YEAST | 13 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/subtree_update/Q.p__Krumholzibacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/subtree_update/Q.p__Krumholzibacteriota.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/model_update/Q.p__Krumholzibacteriota
```
  
  Runtime: 9881.21 seconds  
[Model update log](loop_1/model_update/Q.p__Krumholzibacteriota.iqtree)  
BIC of the new model: 4886591.8742  
Likelihood of the new model: -2343615.5094  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Krumholzibacteriota_1)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,Q.p__Krumholzibacteriota_1  
![Model bubble plot](loop_1/Q.p__Krumholzibacteriota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9633442939750803  
Euclidean distance: 0.640849891425325  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/tree_update/Q.p__Krumholzibacteriota_1.treefile
```
  
  Runtime: 495.70 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/tree_update/Q.p__Krumholzibacteriota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/tree_update/Q.p__Krumholzibacteriota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 16  
Normalized RF distance: 0.0889  
Tree 1 branch length: 16.45173  
Tree 2 branch length: 21.31378  
Time usage for Loop_1: 21778.94 seconds (6.05 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/tree_update/Q.p__Krumholzibacteriota_1.treefile -l 15 -u 93 -o ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/subtrees -m split
```
  
Original number of taxa: 93   
Number of pruned subtrees: 1   
Number of taxa after pruning: 93   
Pruned node IDs (degree): 1 (93)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,Q.p__Krumholzibacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/subtree_update/Q.p__Krumholzibacteriota
```
  
  Runtime: 5512.16 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Krumholzibacteriota.iqtree)  
Best models for iteration 2:  
Q.p__Krumholzibacteriota_1  

| Model | Count |
|-------|-------|
| Q.p__Krumholzibacteriota_1 | 98 |
| Q.INSECT | 10 |
| LG | 5 |
| Q.YEAST | 3 |
| Q.PFAM | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/subtree_update/Q.p__Krumholzibacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/subtree_update/Q.p__Krumholzibacteriota.treefile --model-joint GTR20+FO --init-model Q.p__Krumholzibacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/model_update/Q.p__Krumholzibacteriota
```
  
  Runtime: 7503.51 seconds  
[Model update log](loop_2/model_update/Q.p__Krumholzibacteriota.iqtree)  
BIC of the new model: 4885627.7785  
Likelihood of the new model: -2343133.4615  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Krumholzibacteriota_2)  
Model set for next iteration: Q.INSECT,LG,Q.YEAST,Q.PFAM,Q.p__Krumholzibacteriota_2  
![Model bubble plot](loop_2/Q.p__Krumholzibacteriota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999765452276394  
Euclidean distance: 0.04742989685979683  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/tree_update/Q.p__Krumholzibacteriota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 485.05 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Krumholzibacteriota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 16  
Normalized RF distance: 0.0889  
Tree 1 branch length: 16.45173  
Tree 2 branch length: 21.33021  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Krumholzibacteriota_1,Q.p__Krumholzibacteriota_2 -mdef ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 27524.38 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Krumholzibacteriota_2+R9 | -2383930.440 | 4769970.687 |
| Q.p__Krumholzibacteriota_1+R9 | -2383942.476 | 4769994.759 |
| Q.p__Krumholzibacteriota_1+F+R9 | -2389442.262 | 4781195.770 |
| Q.p__Krumholzibacteriota_2+F+R9 | -2389710.482 | 4781732.210 |
| LG+F+R9 | -2394568.454 | 4791448.154 |
| Q.PFAM+F+R9 | -2395456.585 | 4793224.416 |
| Q.YEAST+F+R9 | -2398210.906 | 4798733.058 |
| Q.INSECT+F+R9 | -2401985.373 | 4806281.992 |
| Q.PFAM+R9 | -2404328.469 | 4810766.745 |
| WAG+F+R9 | -2404845.238 | 4812001.722 |
| LG+R9 | -2409230.395 | 4820570.597 |
| LG+I+R9 | -2409231.961 | 4820584.331 |
| LG+I+R8 | -2409254.160 | 4820607.525 |
| LG+R8 | -2409297.618 | 4820683.839 |
| LG+I+R7 | -2409365.737 | 4820809.475 |
| LG+R7 | -2409421.219 | 4820909.837 |
| LG+I+R6 | -2409556.985 | 4821170.767 |
| LG+R6 | -2409860.203 | 4821766.601 |
| LG+I+G4 | -2413683.047 | 4829327.472 |
| JTT+F+R9 | -2417037.215 | 4836385.676 |
| LG+G4 | -2417684.018 | 4837318.812 |
| WAG+R9 | -2418801.423 | 4839712.653 |
| Q.INSECT+R9 | -2423422.331 | 4848954.469 |
| Q.PLANT+F+R9 | -2424300.513 | 4850912.272 |
| CPREV+F+R9 | -2427226.235 | 4856763.716 |
| JTT+R9 | -2427382.912 | 4856875.631 |
| DCMUT+F+R9 | -2428325.027 | 4858961.300 |
| Q.YEAST+R9 | -2428788.899 | 4859687.605 |
| PMB+F+R9 | -2433820.114 | 4869951.474 |
| Q.PLANT+R9 | -2435724.711 | 4873559.229 |
| MTINV+F+R9 | -2446562.475 | 4895436.196 |
| CPREV+R9 | -2447248.797 | 4896607.401 |
| PMB+R9 | -2447713.840 | 4897537.487 |
| Q.MAMMAL+F+R9 | -2449585.685 | 4901482.616 |
| DCMUT+R9 | -2449887.798 | 4901885.403 |
| Q.MAMMAL+R9 | -2457272.350 | 4916654.507 |
| MTMET+F+R9 | -2467371.176 | 4937053.598 |
| Q.BIRD+F+R9 | -2470835.024 | 4943981.294 |
| Q.BIRD+R9 | -2478610.898 | 4959331.603 |
| MTVER+F+R9 | -2505674.722 | 5013660.690 |
| LG+I | -2561006.516 | 5123963.808 |
| MTMET+R9 | -2608125.648 | 5218361.103 |
| MTINV+R9 | -2615849.539 | 5233808.885 |
| MTVER+R9 | -2627221.245 | 5256552.297 |
| LG | -2637369.875 | 5276679.924 |
The inferred model Q.p__Krumholzibacteriota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Krumholzibacteriota_2+R9 | LG+F+R9 |
| BIC | 4769970.687 | 4791448.154 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loop_1/tree_update/Q.p__Krumholzibacteriota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 428.14 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Krumholzibacteriota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0222  
Tree 1 branch length: 21.03463  
Tree 2 branch length: 21.33021  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2445814.301 | -2471585.07 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Krumholzibacteriota_2):  
Pearson's correlation: 0.9620593433942953  
Euclidean distance: 0.6513300547138953  
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
Total time usage: 63403.08 seconds (17.61 h)  
