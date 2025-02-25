## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Nitrospirota  
  Taxa name: p__Nitrospirota  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 558  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Nitrospirota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Nitrospirota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Nitrospirota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/subtrees -m split
```
  
Original number of taxa: 558   
Number of pruned subtrees: 5   
Number of taxa after pruning: 548   
Pruned node IDs (degree): 278 (250) 3 (231) 233 (26) 534 (25) 259 (16)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 5 subtree files and 120 loci files. Total number of potential alignments: 600.  
Obtained 597 alignments from all potential alignments.  
Remaining 597 alignments. Deleted 3 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/subtree_update/Q.p__Nitrospirota
```
  
  Runtime: 73475.92 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Nitrospirota.iqtree)  
Best models for iteration 1:  
Q.PLANT  

| Model | Count |
|-------|-------|
| Q.PLANT | 338 |
| LG | 92 |
| Q.YEAST | 75 |
| Q.PFAM | 73 |
| JTT | 14 |
| Q.MAMMAL | 3 |
| CPREV | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/subtree_update/Q.p__Nitrospirota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/subtree_update/Q.p__Nitrospirota.treefile --model-joint GTR20+FO --init-model Q.PLANT -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/model_update/Q.p__Nitrospirota
```
  
  Runtime: 39018.73 seconds  
[Model update log](loop_1/model_update/Q.p__Nitrospirota.iqtree)  
BIC of the new model: 20293946.5558  
Likelihood of the new model: -9450437.8195  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Nitrospirota_1)  
Model set for next iteration: Q.PLANT,LG,Q.YEAST,Q.PFAM,Q.p__Nitrospirota_1  
![Model bubble plot](loop_1/Q.p__Nitrospirota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9772405491746207  
Euclidean distance: 0.4367993177333627  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/Q.p__Nitrospirota_1.treefile
```
  
  Runtime: 2797.47 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/Q.p__Nitrospirota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/Q.p__Nitrospirota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 144  
Normalized RF distance: 0.1295  
Tree 1 branch length: 59.40699  
Tree 2 branch length: 81.86121  
Time usage for Loop_1: 115430.98 seconds (32.06 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/Q.p__Nitrospirota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/subtrees -m split
```
  
Original number of taxa: 558   
Number of pruned subtrees: 4   
Number of taxa after pruning: 529   
Pruned node IDs (degree): 264 (250) 2 (228) 233 (26) 520 (25)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 4 subtree files and 120 loci files. Total number of potential alignments: 480.  
Obtained 478 alignments from all potential alignments.  
Remaining 478 alignments. Deleted 2 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/training_loci -m MFP -mset Q.PLANT,LG,Q.YEAST,Q.PFAM,Q.p__Nitrospirota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/subtree_update/Q.p__Nitrospirota
```
  
  Runtime: 66175.81 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Nitrospirota.iqtree)  
Best models for iteration 2:  
Q.p__Nitrospirota_1  

| Model | Count |
|-------|-------|
| Q.p__Nitrospirota_1 | 428 |
| Q.PFAM | 20 |
| Q.PLANT | 15 |
| LG | 13 |
| Q.YEAST | 2 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/subtree_update/Q.p__Nitrospirota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/subtree_update/Q.p__Nitrospirota.treefile --model-joint GTR20+FO --init-model Q.p__Nitrospirota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/model_update/Q.p__Nitrospirota
```
  
  Runtime: 44463.14 seconds  
[Model update log](loop_2/model_update/Q.p__Nitrospirota.iqtree)  
BIC of the new model: 19269126.0114  
Likelihood of the new model: -8970826.0246  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Nitrospirota_2)  
Model set for next iteration: Q.PFAM,Q.PLANT,LG,Q.p__Nitrospirota_2  
![Model bubble plot](loop_2/Q.p__Nitrospirota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9997852932673611  
Euclidean distance: 0.04516828153409562  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/Q.p__Nitrospirota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 3885.11 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 144  
Normalized RF distance: 0.1295  
Tree 1 branch length: 59.40699  
Tree 2 branch length: 81.92877  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Nitrospirota_1,Q.p__Nitrospirota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 249006.92 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Nitrospirota_2+I+R9 | -9642262.026 | 19296524.828 |
| Q.p__Nitrospirota_1+I+R9 | -9642535.512 | 19297071.800 |
| Q.p__Nitrospirota_1+F+I+R9 | -9660009.590 | 19332221.739 |
| Q.p__Nitrospirota_2+F+I+R9 | -9662005.351 | 19336213.261 |
| Q.INSECT+F+I+R9 | -9693576.482 | 19399355.523 |
| Q.YEAST+F+I+R9 | -9699540.030 | 19411282.619 |
| Q.INSECT+I+R9 | -9700048.038 | 19412096.852 |
| Q.PLANT+I+R9 | -9701965.337 | 19415931.450 |
| Q.PLANT+F+I+R9 | -9704369.937 | 19420942.433 |
| LG+F+I+R9 | -9712405.516 | 19437013.591 |
| Q.PFAM+F+I+R9 | -9720111.870 | 19452426.299 |
| JTT+F+I+R9 | -9721232.421 | 19454667.401 |
| Q.PFAM+I+R9 | -9724638.901 | 19461278.578 |
| LG+I+R9 | -9725978.792 | 19463958.360 |
| Q.YEAST+I+R9 | -9726221.635 | 19464444.046 |
| LG+R9 | -9726752.336 | 19465494.828 |
| LG+I+R8 | -9728310.941 | 19468601.418 |
| LG+R8 | -9729857.031 | 19471682.978 |
| JTT+I+R9 | -9730372.677 | 19472746.130 |
| LG+I+R7 | -9732275.084 | 19476508.464 |
| LG+R7 | -9734467.056 | 19480881.787 |
| LG+I+R6 | -9739373.168 | 19490683.391 |
| LG+R6 | -9743180.500 | 19498287.435 |
| WAG+F+I+R9 | -9773398.219 | 19558998.997 |
| LG+I+G4 | -9782108.382 | 19576058.238 |
| WAG+I+R9 | -9788378.148 | 19588757.072 |
| Q.MAMMAL+I+R9 | -9789782.094 | 19591564.964 |
| Q.MAMMAL+F+I+R9 | -9794032.988 | 19600268.535 |
| LG+G4 | -9799670.503 | 19611171.860 |
| MTINV+F+I+R9 | -9818341.547 | 19648885.653 |
| CPREV+I+R9 | -9828784.277 | 19669569.330 |
| DCMUT+F+I+R9 | -9830083.569 | 19672369.697 |
| CPREV+F+I+R9 | -9836499.294 | 19685201.147 |
| Q.BIRD+I+R9 | -9852892.425 | 19717785.626 |
| Q.BIRD+F+I+R9 | -9858405.467 | 19729013.493 |
| MTMET+F+I+R9 | -9870245.530 | 19752693.619 |
| DCMUT+I+R9 | -9873291.380 | 19758583.536 |
| PMB+F+I+R9 | -9926707.005 | 19865616.569 |
| PMB+I+R9 | -9933685.679 | 19879372.134 |
| MTVER+F+I+R9 | -10024739.840 | 20061682.239 |
| MTMET+I+R9 | -10249236.230 | 20510473.236 |
| MTINV+I+R9 | -10297156.100 | 20606312.976 |
| MTVER+I+R9 | -10347553.890 | 20707108.556 |
| LG+I | -10624964.410 | 21261759.674 |
| LG | -10826057.310 | 21663934.854 |
The inferred model Q.p__Nitrospirota_2 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Nitrospirota_2+I+R9 | Q.INSECT+F+I+R9 |
| BIC | 19296524.828 | 19399355.523 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/Q.p__Nitrospirota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 1698.46 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loop_1/tree_update/Q.p__Nitrospirota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 1749.86 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
Q.INSECT model has higher likelihood than LG model, use best_existing_model model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/allloci_best_existing_model_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Nitrospirota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0018  
Tree 1 branch length: 78.72234  
Tree 2 branch length: 81.92877  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -9707767.435 | -9764701.219 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.INSECT) and final model (Q.p__Nitrospirota_2):  
Pearson's correlation: 0.9703714949433314  
Euclidean distance: 0.5132624601962832  
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
Total time usage: 482744.63 seconds (134.10 h)  
