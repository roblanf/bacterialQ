## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Fusobacteriota  
  Taxa name: p__Fusobacteriota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 138  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Fusobacteriota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 138  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Fusobacteriota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Fusobacteriota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Fusobacteriota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Fusobacteriota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Fusobacteriota/ref_tree.tre -l 15 -u 138 -o ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/subtrees -m split
```
  
Original number of taxa: 138   
Number of pruned subtrees: 1   
Number of taxa after pruning: 138   
Pruned node IDs (degree): 1 (138)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/subtree_update/Q.p__Fusobacteriota
```
  
  Runtime: 18853.30 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Fusobacteriota.iqtree)  
Best models for iteration 1:  
Q.YEAST  

| Model | Count |
|-------|-------|
| Q.YEAST | 66 |
| Q.INSECT | 25 |
| LG | 22 |
| Q.PFAM | 5 |
| Q.PLANT | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/subtree_update/Q.p__Fusobacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/subtree_update/Q.p__Fusobacteriota.treefile --model-joint GTR20+FO --init-model Q.YEAST -pre ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/model_update/Q.p__Fusobacteriota
```
  
  Runtime: 26731.70 seconds  
[Model update log](loop_1/model_update/Q.p__Fusobacteriota.iqtree)  
BIC of the new model: 4807449.7991  
Likelihood of the new model: -2245263.6642  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Fusobacteriota_1)  
Model set for next iteration: Q.YEAST,Q.INSECT,LG,Q.p__Fusobacteriota_1  
![Model bubble plot](loop_1/Q.p__Fusobacteriota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9521864838248129  
Euclidean distance: 0.7902675858830217  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Fusobacteriota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Fusobacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/tree_update/Q.p__Fusobacteriota_1.treefile
```
  
  Runtime: 693.20 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/tree_update/Q.p__Fusobacteriota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/tree_update/Q.p__Fusobacteriota_1.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 34  
Normalized RF distance: 0.1259  
Tree 1 branch length: 12.55568  
Tree 2 branch length: 21.14523  
Time usage for Loop_1: 46314.84 seconds (12.87 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/tree_update/Q.p__Fusobacteriota_1.treefile -l 15 -u 138 -o ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/subtrees -m split
```
  
Original number of taxa: 138   
Number of pruned subtrees: 1   
Number of taxa after pruning: 138   
Pruned node IDs (degree): 1 (138)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 120 loci files. Total number of potential alignments: 120.  
Obtained 120 alignments from all potential alignments.  
Remaining 120 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/training_loci -m MFP -mset Q.YEAST,Q.INSECT,LG,Q.p__Fusobacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Fusobacteriota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/subtree_update/Q.p__Fusobacteriota
```
  
  Runtime: 12538.21 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Fusobacteriota.iqtree)  
Best models for iteration 2:  
Q.p__Fusobacteriota_1  

| Model | Count |
|-------|-------|
| Q.p__Fusobacteriota_1 | 115 |
| Q.INSECT | 3 |
| LG | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/subtree_update/Q.p__Fusobacteriota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/subtree_update/Q.p__Fusobacteriota.treefile --model-joint GTR20+FO --init-model Q.p__Fusobacteriota_1 -mdef ../Result_nova/phylum_models/Q.p__Fusobacteriota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/model_update/Q.p__Fusobacteriota
```
  
  Runtime: 22318.80 seconds  
[Model update log](loop_2/model_update/Q.p__Fusobacteriota.iqtree)  
BIC of the new model: 4805090.5971  
Likelihood of the new model: -2244084.0632  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Fusobacteriota_2)  
Model set for next iteration: Q.INSECT,LG,Q.p__Fusobacteriota_2  
![Model bubble plot](loop_2/Q.p__Fusobacteriota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.999909053075877  
Euclidean distance: 0.037883808775400415  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/tree_update/Q.p__Fusobacteriota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Fusobacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 768.51 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Fusobacteriota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 36  
Normalized RF distance: 0.1333  
Tree 1 branch length: 12.55568  
Tree 2 branch length: 21.24503  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Fusobacteriota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Fusobacteriota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Fusobacteriota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Fusobacteriota_1,Q.p__Fusobacteriota_2 -mdef ../Result_nova/phylum_models/Q.p__Fusobacteriota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Fusobacteriota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 19542.21 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Fusobacteriota_1+I+R8 | -2307252.742 | 4617562.000 |
| Q.p__Fusobacteriota_2+I+R8 | -2307277.392 | 4617611.300 |
| Q.p__Fusobacteriota_1+F+I+R8 | -2321944.179 | 4647146.519 |
| Q.p__Fusobacteriota_2+F+I+R8 | -2322446.184 | 4648150.529 |
| LG+F+I+R8 | -2322797.874 | 4648853.909 |
| Q.YEAST+F+I+R8 | -2324108.202 | 4651474.565 |
| Q.PFAM+F+I+R8 | -2325665.070 | 4654588.301 |
| Q.INSECT+F+I+R8 | -2327011.885 | 4657281.931 |
| Q.YEAST+I+R8 | -2332461.589 | 4667979.694 |
| WAG+F+I+R8 | -2335503.631 | 4674265.423 |
| JTT+F+I+R8 | -2337242.385 | 4677742.931 |
| Q.INSECT+I+R8 | -2337977.555 | 4679011.626 |
| Q.PLANT+F+I+R8 | -2342008.328 | 4687274.817 |
| CPREV+F+I+R8 | -2344709.775 | 4692677.711 |
| LG+I+R8 | -2346128.758 | 4695314.032 |
| LG+R8 | -2346166.036 | 4695377.975 |
| LG+I+R7 | -2346270.843 | 4695576.976 |
| LG+R7 | -2346470.151 | 4695964.979 |
| LG+I+R6 | -2346917.062 | 4696848.188 |
| LG+R6 | -2347365.775 | 4697735.001 |
| LG+I+R5 | -2348103.625 | 4699200.088 |
| MTINV+F+I+R8 | -2349027.775 | 4701313.711 |
| LG+R5 | -2349235.999 | 4701454.223 |
| DCMUT+F+I+R8 | -2351636.220 | 4706530.601 |
| Q.PFAM+I+R8 | -2352922.206 | 4708900.928 |
| LG+I+G4 | -2353583.717 | 4710085.982 |
| CPREV+I+R8 | -2356385.607 | 4715827.730 |
| LG+G4 | -2357928.111 | 4718764.157 |
| PMB+F+I+R8 | -2358913.725 | 4721085.611 |
| Q.PLANT+I+R8 | -2360941.952 | 4724940.420 |
| Q.MAMMAL+F+I+R8 | -2361133.397 | 4725524.955 |
| WAG+I+R8 | -2361952.023 | 4726960.562 |
| MTMET+F+I+R8 | -2363274.734 | 4729807.629 |
| JTT+I+R8 | -2365781.663 | 4734619.842 |
| Q.BIRD+F+I+R8 | -2379372.476 | 4762003.113 |
| DCMUT+I+R8 | -2386344.135 | 4775744.786 |
| PMB+I+R8 | -2389557.779 | 4782172.074 |
| Q.MAMMAL+I+R8 | -2395462.406 | 4793981.328 |
| MTVER+F+I+R8 | -2405455.322 | 4814168.805 |
| Q.BIRD+I+R8 | -2410447.234 | 4823950.984 |
| MTMET+I+R8 | -2437466.712 | 4877989.940 |
| MTINV+I+R8 | -2438515.988 | 4880088.492 |
| MTVER+I+R8 | -2479110.014 | 4961276.544 |
| LG+I | -2506994.408 | 5016896.751 |
| LG | -2587075.267 | 5177047.856 |
The inferred model Q.p__Fusobacteriota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Fusobacteriota_1+I+R8 | LG+F+I+R8 |
| BIC | 4617562.0 | 4648853.909 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Fusobacteriota/loop_1/tree_update/Q.p__Fusobacteriota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Fusobacteriota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 659.67 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/logfiles/best_final_tree.treefile', summary_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Fusobacteriota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 12  
Normalized RF distance: 0.0444  
Tree 1 branch length: 18.28851  
Tree 2 branch length: 21.24503  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -2383803.9 | -2418360.664 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Fusobacteriota_2):  
Pearson's correlation: 0.9150576017999142  
Euclidean distance: 1.0304875857280915  
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
Total time usage: 102313.22 seconds (28.42 h)  
