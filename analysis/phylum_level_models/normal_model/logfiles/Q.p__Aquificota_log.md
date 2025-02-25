## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 3  
  Convergence threshold: 0.999  
  File prefix: Q.p__Aquificota  
  Taxa name: p__Aquificota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 132  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Aquificota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 132  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Aquificota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Aquificota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Aquificota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Aquificota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Aquificota/ref_tree.tre -l 15 -u 132 -o ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/subtrees -m split
```
  
Original number of taxa: 132   
Number of pruned subtrees: 1   
Number of taxa after pruning: 132   
Pruned node IDs (degree): 1 (132)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/subtree_update/Q.p__Aquificota
```
  
  Runtime: 6660.89 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Aquificota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 57 |
| Q.YEAST | 44 |
| Q.INSECT | 17 |
| Q.PFAM | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/subtree_update/Q.p__Aquificota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/subtree_update/Q.p__Aquificota.treefile --model-joint GTR20+FO --init-model LG -pre ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/model_update/Q.p__Aquificota
```
  
  Runtime: 18210.49 seconds  
[Model update log](loop_1/model_update/Q.p__Aquificota.iqtree)  
BIC of the new model: 5180584.2164  
Likelihood of the new model: -2446842.7888  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Aquificota_1)  
Model set for next iteration: LG,Q.YEAST,Q.INSECT,Q.p__Aquificota_1  
![Model bubble plot](loop_1/Q.p__Aquificota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Aquificota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9395650519204831  
Euclidean distance: 0.8766592943825985  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Aquificota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Aquificota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/tree_update/Q.p__Aquificota_1.treefile
```
  
  Runtime: 427.45 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/tree_update/Q.p__Aquificota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Aquificota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Aquificota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Aquificota/loop_1/tree_update/Q.p__Aquificota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Aquificota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Aquificota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 18  
Normalized RF distance: 0.0698  
Tree 1 branch length: 16.16049  
Tree 2 branch length: 24.12827  
Time usage for Loop_1: 25316.93 seconds (7.03 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/tree_update/Q.p__Aquificota_1.treefile -l 15 -u 132 -o ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/subtrees -m split
```
  
Original number of taxa: 132   
Number of pruned subtrees: 1   
Number of taxa after pruning: 132   
Pruned node IDs (degree): 1 (132)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.INSECT,Q.p__Aquificota_1 -mdef ../Result_nova/phylum_models/Q.p__Aquificota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/subtree_update/Q.p__Aquificota
```
  
  Runtime: 4532.32 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Aquificota.iqtree)  
Best models for iteration 2:  
Q.p__Aquificota_1  

| Model | Count |
|-------|-------|
| Q.p__Aquificota_1 | 116 |
| Q.INSECT | 3 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/subtree_update/Q.p__Aquificota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/subtree_update/Q.p__Aquificota.treefile --model-joint GTR20+FO --init-model Q.p__Aquificota_1 -mdef ../Result_nova/phylum_models/Q.p__Aquificota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/model_update/Q.p__Aquificota
```
  
  Runtime: 19182.29 seconds  
[Model update log](loop_2/model_update/Q.p__Aquificota.iqtree)  
BIC of the new model: 5179619.5145  
Likelihood of the new model: -2446360.4378  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Aquificota_2)  
Model set for next iteration: Q.INSECT,Q.YEAST,Q.p__Aquificota_2  
![Model bubble plot](loop_2/Q.p__Aquificota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Aquificota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998801650959483  
Euclidean distance: 0.043014658111258916  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Aquificota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Aquificota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Aquificota/loop_1/tree_update/Q.p__Aquificota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Aquificota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Aquificota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 632.84 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Aquificota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Aquificota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Aquificota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Aquificota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Aquificota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Aquificota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 18  
Normalized RF distance: 0.0698  
Tree 1 branch length: 16.16049  
Tree 2 branch length: 24.18494  
### Model comparison  
Comparison between initial best model (LG) and final model (Q.p__Aquificota_2):  
Pearson's correlation: 0.9385361864858699  
Euclidean distance: 0.898148036974618  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Aquificota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Aquificota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Aquificota/loci/concat_loci.faa -m TESTNEWONLY -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Aquificota_1,Q.p__Aquificota_2 -mdef ../Result_nova/phylum_models/Q.p__Aquificota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Aquificota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Aquificota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 22022.12 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Aquificota_1+I+R9 | -2502034.246 | 5007019.425 |
| Q.p__Aquificota_2+I+R9 | -2502053.137 | 5007057.207 |
| Q.p__Aquificota_1+F+I+R9 | -2512975.688 | 5029103.992 |
| Q.p__Aquificota_2+F+I+R9 | -2513392.224 | 5029937.064 |
| LG+F+I+R9 | -2516957.351 | 5037067.318 |
| Q.PFAM+F+I+R9 | -2522356.788 | 5047866.192 |
| Q.YEAST+F+I+R9 | -2523453.536 | 5050059.688 |
| Q.INSECT+F+I+R9 | -2529140.740 | 5061434.096 |
| Q.YEAST+I+R9 | -2531470.362 | 5065891.657 |
| LG+I+R9 | -2534842.988 | 5072636.909 |
| LG+R9 | -2534858.196 | 5072656.710 |
| LG+I+R10 | -2534842.791 | 5072657.745 |
| LG+R10 | -2534849.547 | 5072660.642 |
| LG+I+R8 | -2534879.414 | 5072688.531 |
| LG+R8 | -2534944.728 | 5072808.545 |
| LG+I+R7 | -2535037.553 | 5072983.580 |
| LG+R7 | -2535174.340 | 5073246.539 |
| LG+I+R6 | -2535368.741 | 5073624.726 |
| WAG+F+I+R9 | -2535293.771 | 5073740.158 |
| LG+R6 | -2535701.461 | 5074279.551 |
| LG+I+R5 | -2536376.594 | 5075619.202 |
| Q.INSECT+I+R9 | -2536938.379 | 5076827.691 |
| LG+R5 | -2537322.524 | 5077500.447 |
| LG+I+R4 | -2538956.481 | 5080757.746 |
| LG+I+G4 | -2540327.639 | 5083446.988 |
| LG+R4 | -2541411.020 | 5085656.210 |
| CPREV+F+I+R9 | -2541997.904 | 5087148.424 |
| JTT+F+I+R9 | -2542703.008 | 5088558.632 |
| Q.PFAM+I+R9 | -2544000.624 | 5090952.181 |
| LG+G4 | -2545422.033 | 5093625.161 |
| LG+I+R3 | -2546250.421 | 5095324.397 |
| Q.PLANT+F+I+R9 | -2547358.988 | 5097870.592 |
| CPREV+I+R9 | -2548419.893 | 5099790.719 |
| LG+R3 | -2553569.373 | 5109951.686 |
| MTINV+F+I+R9 | -2556649.945 | 5116452.506 |
| PMB+F+I+R9 | -2556670.936 | 5116494.488 |
| WAG+I+R9 | -2561551.872 | 5126054.677 |
| Q.PLANT+I+R9 | -2562345.310 | 5127641.553 |
| DCMUT+F+I+R9 | -2563194.920 | 5129542.456 |
| JTT+I+R9 | -2569002.310 | 5140955.553 |
| Q.MAMMAL+F+I+R9 | -2569519.611 | 5142191.838 |
| LG+I+R2 | -2571896.774 | 5146595.873 |
| PMB+I+R9 | -2579207.953 | 5161366.839 |
| MTMET+F+I+R9 | -2579788.349 | 5162729.314 |
| Q.BIRD+F+I+R9 | -2591083.243 | 5185319.102 |
| Q.MAMMAL+I+R9 | -2593559.111 | 5190069.155 |
| LG+R2 | -2594518.238 | 5191828.186 |
| DCMUT+I+R9 | -2601680.043 | 5206311.019 |
| Q.BIRD+I+R9 | -2613525.798 | 5230002.529 |
| MTVER+F+I+R9 | -2641170.170 | 5285492.956 |
| MTINV+I+R9 | -2691617.950 | 5386186.833 |
| LG+I | -2696492.239 | 5395765.573 |
| MTMET+I+R9 | -2697331.196 | 5397613.325 |
| MTVER+I+R9 | -2755784.387 | 5514519.707 |
| LG | -2783279.118 | 5569328.716 |
The inferred model Q.p__Aquificota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Aquificota_1+I+R9 | LG+F+I+R9 |
| BIC | 5007019.425 | 5037067.318 |
### Pairwise comparison of trees  
![Heatmap of RF distance of trees:](estimated_tree/RF_dist.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_dist.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 71783.75 seconds (19.94 h)  
