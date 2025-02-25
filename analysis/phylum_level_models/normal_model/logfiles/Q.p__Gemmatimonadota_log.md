## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Gemmatimonadota  
  Taxa name: p__Gemmatimonadota  
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
Input a single taxa file: ../Result_nova/phylum_models/Q.p__Gemmatimonadota/select_id.txt. Sampling sequences for 117 loci.  
Number of input species: 535  
Remaining 117 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Gemmatimonadota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Gemmatimonadota -d 0.1 -o ../Result_nova/phylum_models/Q.p__Gemmatimonadota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Eisenbacteria as the outgroup for Phylum Gemmatimonadota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Gemmatimonadota/ref_tree.tre -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/subtrees -m split
```
  
Original number of taxa: 535   
Number of pruned subtrees: 3   
Number of taxa after pruning: 523   
Pruned node IDs (degree): 322 (204) 4 (201) 205 (118)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 117 loci files. Total number of potential alignments: 351.  
Obtained 351 alignments from all potential alignments.  
Remaining 351 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/subtree_update/Q.p__Gemmatimonadota
```
  
  Runtime: 30650.29 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Gemmatimonadota.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| Q.INSECT | 113 |
| LG | 88 |
| Q.PFAM | 86 |
| Q.YEAST | 53 |
| Q.PLANT | 11 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/subtree_update/Q.p__Gemmatimonadota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/subtree_update/Q.p__Gemmatimonadota.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/model_update/Q.p__Gemmatimonadota
```
  
  Runtime: 50196.51 seconds  
[Model update log](loop_1/model_update/Q.p__Gemmatimonadota.iqtree)  
BIC of the new model: 20132809.0046  
Likelihood of the new model: -9458923.6869  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Gemmatimonadota_1)  
Model set for next iteration: Q.INSECT,LG,Q.PFAM,Q.YEAST,Q.p__Gemmatimonadota_1  
![Model bubble plot](loop_1/Q.p__Gemmatimonadota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9024314305804385  
Euclidean distance: 1.083574978616441  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/tree_update/fasttree.log -intree ../Result_nova/phylum_models/Q.p__Gemmatimonadota/ref_tree_with_outgroups.tre ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/tree_update/Q.p__Gemmatimonadota_1.treefile
```
  
  Runtime: 2911.07 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/tree_update/Q.p__Gemmatimonadota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/tree_update/Q.p__Gemmatimonadota_1.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 118  
Normalized RF distance: 0.1109  
Tree 1 branch length: 66.39753  
Tree 2 branch length: 87.1772  
Time usage for Loop_1: 83866.07 seconds (23.30 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/tree_update/Q.p__Gemmatimonadota_1.treefile -l 15 -u 250 -o ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/subtrees -m split
```
  
Original number of taxa: 535   
Number of pruned subtrees: 3   
Number of taxa after pruning: 523   
Pruned node IDs (degree): 322 (204) 4 (201) 205 (118)   
Pruning mode: split   
  
See detailed summary in ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 117 loci files. Total number of potential alignments: 351.  
Obtained 351 alignments from all potential alignments.  
Remaining 351 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/training_loci -m MFP -mset Q.INSECT,LG,Q.PFAM,Q.YEAST,Q.p__Gemmatimonadota_1 -mdef ../Result_nova/phylum_models/Q.p__Gemmatimonadota/inferred_models/trained_model.nex -te ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/subtree_update/constraint_tree.tre -pre ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/subtree_update/Q.p__Gemmatimonadota
```
  
  Runtime: 35329.11 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Gemmatimonadota.iqtree)  
Best models for iteration 2:  
Q.p__Gemmatimonadota_1  

| Model | Count |
|-------|-------|
| Q.p__Gemmatimonadota_1 | 316 |
| Q.INSECT | 17 |
| Q.PFAM | 8 |
| LG | 7 |
| Q.YEAST | 3 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/subtree_update/Q.p__Gemmatimonadota.best_model.nex -te ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/subtree_update/Q.p__Gemmatimonadota.treefile --model-joint GTR20+FO --init-model Q.p__Gemmatimonadota_1 -mdef ../Result_nova/phylum_models/Q.p__Gemmatimonadota/inferred_models/trained_model.nex -pre ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/model_update/Q.p__Gemmatimonadota
```
  
  Runtime: 83958.83 seconds  
[Model update log](loop_2/model_update/Q.p__Gemmatimonadota.iqtree)  
BIC of the new model: 20122745.9602  
Likelihood of the new model: -9453892.1647  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Gemmatimonadota_2)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.p__Gemmatimonadota_2  
![Model bubble plot](loop_2/Q.p__Gemmatimonadota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998740295160302  
Euclidean distance: 0.055143497298410504  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/best_final_tree.log -intree ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/tree_update/Q.p__Gemmatimonadota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 2115.77 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Gemmatimonadota', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/ref_tree.tre', tree2_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 118  
Normalized RF distance: 0.1109  
Tree 1 branch length: 66.39753  
Tree 2 branch length: 87.29721  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (Q.p__Gemmatimonadota_2):  
Pearson's correlation: 0.9005191069083022  
Euclidean distance: 1.117480542244872  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex ../Result_nova/phylum_models/Q.p__Gemmatimonadota/inferred_models/trained_model.nex ../Result_nova/phylum_models/Q.p__Gemmatimonadota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loci/concat_loci.faa -m TESTNEWONLY -cmin 5 -cmax 8 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Gemmatimonadota_1,Q.p__Gemmatimonadota_2 -mdef ../Result_nova/phylum_models/Q.p__Gemmatimonadota/inferred_models/trained_model.nex -safe -te ../Result_nova/phylum_models/Q.p__Gemmatimonadota/ref_tree.tre -pre ../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 25978.74 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Gemmatimonadota_1+I+R8 | -9936126.684 | 19883725.077 |
| Q.p__Gemmatimonadota_2+I+R8 | -9936131.302 | 19883734.313 |
| Q.p__Gemmatimonadota_1+F+I+R8 | -9986288.031 | 19984249.215 |
| Q.p__Gemmatimonadota_2+F+I+R8 | -9990114.804 | 19991902.761 |
| LG+F+I+R8 | -10000782.250 | 20013237.653 |
| Q.PFAM+F+I+R8 | -10003009.240 | 20017691.633 |
| Q.YEAST+F+I+R8 | -10011814.280 | 20035301.713 |
| Q.INSECT+F+I+R8 | -10020843.610 | 20053360.373 |
| WAG+F+I+R8 | -10046698.240 | 20105069.633 |
| Q.PFAM+I+R8 | -10087075.120 | 20185621.949 |
| JTT+F+I+R8 | -10093629.880 | 20198932.913 |
| LG+I+R8 | -10127064.150 | 20265600.009 |
| LG+R8 | -10128425.230 | 20268311.566 |
| LG+I+R7 | -10131131.770 | 20273714.044 |
| Q.PLANT+F+I+R8 | -10132513.880 | 20276700.913 |
| LG+R7 | -10134145.380 | 20279730.662 |
| DCMUT+F+I+R8 | -10135114.410 | 20281901.973 |
| LG+I+R6 | -10138742.100 | 20288913.499 |
| LG+R6 | -10142695.460 | 20296809.617 |
| WAG+I+R8 | -10145963.730 | 20303399.169 |
| CPREV+F+I+R8 | -10147247.670 | 20306168.493 |
| LG+I+R5 | -10153066.550 | 20317541.195 |
| LG+R5 | -10160304.530 | 20332006.552 |
| JTT+I+R8 | -10173762.190 | 20358996.089 |
| PMB+F+I+R8 | -10176698.340 | 20365069.833 |
| LG+I+G4 | -10184271.530 | 20379876.939 |
| Q.INSECT+I+R8 | -10184718.190 | 20380908.089 |
| LG+G4 | -10204543.720 | 20420410.716 |
| Q.YEAST+I+R8 | -10221894.490 | 20455260.689 |
| Q.PLANT+I+R8 | -10239286.610 | 20490044.929 |
| MTINV+F+I+R8 | -10242096.590 | 20495866.333 |
| DCMUT+I+R8 | -10258630.530 | 20528732.769 |
| Q.MAMMAL+F+I+R8 | -10259760.840 | 20531194.833 |
| PMB+I+R8 | -10283507.660 | 20578487.029 |
| CPREV+I+R8 | -10308825.660 | 20629123.029 |
| Q.MAMMAL+I+R8 | -10314630.440 | 20640732.589 |
| MTMET+F+I+R8 | -10354253.200 | 20720179.553 |
| Q.BIRD+F+I+R8 | -10363398.530 | 20738470.213 |
| Q.BIRD+I+R8 | -10419444.230 | 20850360.169 |
| MTVER+F+I+R8 | -10521126.090 | 21053925.333 |
| MTMET+I+R8 | -11010413.690 | 22032299.089 |
| MTINV+I+R8 | -11029749.080 | 22070969.869 |
| MTVER+I+R8 | -11070398.060 | 22152267.829 |
| LG+I | -11139611.860 | 22290546.996 |
| LG | -11379439.690 | 22770192.054 |
The inferred model Q.p__Gemmatimonadota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Gemmatimonadota_1+I+R8 | LG+F+I+R8 |
| BIC | 19883725.077 | 20013237.653 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/allloci_lg_tree.log -intree ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loop_1/tree_update/Q.p__Gemmatimonadota_1_with_outgroup.treefile ../Result_nova/phylum_models/Q.p__Gemmatimonadota/loci/concat_loci_with_outgroup.faa > ../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 2356.19 seconds  
Prune outgroup from the tree. The original tree is renamed as ../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test', params = list(tree1_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/logfiles/best_final_tree.treefile', root = FALSE, summary_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/tree_summary.csv', cophylo_path = '../Result_nova/phylum_models/Q.p__Gemmatimonadota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 24  
Normalized RF distance: 0.0226  
Tree 1 branch length: 85.06588  
Tree 2 branch length: 87.29721  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -10001579.476 | -10191344.058 |
The final model tree has better likelihood than the existing model tree.  
### Pairwise comparison of trees  
![Heatmap of RF distance of trees:](estimated_tree/RF_dist.png)  
![Heatmap of nRF distance of trees:](estimated_tree/nRF_dist.png)  
[Pairwise tree distance metrics: ](estimated_tree/tree_pairwise_compare.csv)  
### Record files  
[Record of IQ-TREE result](iqtree_results.csv)  
[Record of tree comparison](tree_summary.csv)  
Total time usage: 233896.80 seconds (64.97 h)  
