## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Armatimonadota  
  Taxa name: p__Armatimonadota  
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
Discarded 1 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/select_id.txt. Sampling sequences for 119 loci.  
Number of input species: 309  
Remaining 119 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Armatimonadota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Armatimonadota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Armatimonadota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/subtrees -m split
```
  
Original number of taxa: 309   
Number of pruned subtrees: 2   
Number of taxa after pruning: 309   
Pruned node IDs (degree): 2 (220) 221 (89)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 2 subtree files and 119 loci files. Total number of potential alignments: 238.  
Obtained 237 alignments from all potential alignments.  
Remaining 237 alignments. Deleted 1 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/subtree_update/Q.p__Armatimonadota
```
  
  Runtime: 79735.26 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Armatimonadota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 107 |
| Q.PFAM | 85 |
| Q.YEAST | 41 |
| WAG | 3 |
| Q.PLANT | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/subtree_update/Q.p__Armatimonadota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/subtree_update/Q.p__Armatimonadota.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/model_update/Q.p__Armatimonadota
```
  
  Runtime: 60451.80 seconds  
[Model update log](loop_1/model_update/Q.p__Armatimonadota.iqtree)  
BIC of the new model: 18182733.1209  
Likelihood of the new model: -8734245.7838  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Armatimonadota_1)  
Model set for next iteration: LG,Q.PFAM,Q.YEAST,Q.p__Armatimonadota_1  
![Model bubble plot](loop_1/Q.p__Armatimonadota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9674170462921994  
Euclidean distance: 0.5895622268090198  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/tree_update/Q.p__Armatimonadota_1.treefile
```
  
  Runtime: 1349.79 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/tree_update/Q.p__Armatimonadota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/tree_update/Q.p__Armatimonadota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 82  
Normalized RF distance: 0.1336  
Tree 1 branch length: 66.01119  
Tree 2 branch length: 84.39652  
Time usage for Loop_1: 141620.12 seconds (39.34 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/tree_update/Q.p__Armatimonadota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/subtrees -m split
```
  
Original number of taxa: 309   
Number of pruned subtrees: 3   
Number of taxa after pruning: 309   
Pruned node IDs (degree): 76 (234) 2 (47) 49 (28)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 3 subtree files and 119 loci files. Total number of potential alignments: 357.  
Obtained 354 alignments from all potential alignments.  
Remaining 354 alignments. Deleted 3 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/training_loci -m MFP -mset LG,Q.PFAM,Q.YEAST,Q.p__Armatimonadota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/subtree_update/Q.p__Armatimonadota
```
  
  Runtime: 33270.92 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Armatimonadota.iqtree)  
Best models for iteration 2:  
Q.p__Armatimonadota_1  

| Model | Count |
|-------|-------|
| Q.p__Armatimonadota_1 | 329 |
| Q.PFAM | 15 |
| LG | 9 |
| Q.YEAST | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/subtree_update/Q.p__Armatimonadota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/subtree_update/Q.p__Armatimonadota.treefile --model-joint GTR20+FO --init-model Q.p__Armatimonadota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/model_update/Q.p__Armatimonadota
```
  
  Runtime: 56649.64 seconds  
[Model update log](loop_2/model_update/Q.p__Armatimonadota.iqtree)  
BIC of the new model: 18371058.2031  
Likelihood of the new model: -8817939.3693  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Armatimonadota_2)  
Model set for next iteration: Q.PFAM,LG,Q.p__Armatimonadota_2  
![Model bubble plot](loop_2/Q.p__Armatimonadota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999255561023708  
Euclidean distance: 0.03211437392292124  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/tree_update/Q.p__Armatimonadota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 1516.93 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 82  
Normalized RF distance: 0.1336  
Tree 1 branch length: 66.01119  
Tree 2 branch length: 84.59872  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Armatimonadota_1,Q.p__Armatimonadota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 31277.26 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Armatimonadota_1+I+R9 | -8802293.493 | 17611291.004 |
| Q.p__Armatimonadota_2+I+R9 | -8802692.708 | 17612089.434 |
| Q.p__Armatimonadota_2+F+I+R9 | -8822873.204 | 17652651.971 |
| Q.p__Armatimonadota_1+F+I+R9 | -8823248.142 | 17653401.847 |
| LG+F+I+R9 | -8832354.316 | 17671614.195 |
| Q.PFAM+F+I+R9 | -8835357.214 | 17677619.991 |
| Q.PFAM+I+R9 | -8847716.829 | 17702137.676 |
| Q.YEAST+F+I+R9 | -8848902.548 | 17704710.659 |
| LG+I+R9 | -8863820.461 | 17734344.940 |
| LG+R9 | -8864285.452 | 17735264.315 |
| LG+I+R8 | -8865128.600 | 17736940.003 |
| LG+R8 | -8866227.495 | 17739127.186 |
| Q.INSECT+F+I+R9 | -8867380.663 | 17741666.889 |
| LG+I+R7 | -8867591.840 | 17741845.268 |
| LG+R7 | -8869389.852 | 17745430.684 |
| LG+I+R6 | -8872749.215 | 17752138.803 |
| LG+R6 | -8875535.681 | 17757701.127 |
| WAG+F+I+R9 | -8882348.529 | 17771602.621 |
| LG+I+G4 | -8903234.471 | 17813013.846 |
| WAG+I+R9 | -8908704.569 | 17824113.156 |
| Q.INSECT+I+R9 | -8912908.392 | 17832520.802 |
| LG+G4 | -8916050.369 | 17838635.034 |
| Q.YEAST+I+R9 | -8929383.656 | 17865471.330 |
| JTT+F+I+R9 | -8947634.108 | 17902173.779 |
| JTT+I+R9 | -8963459.544 | 17933623.106 |
| PMB+F+I+R9 | -8964172.121 | 17935249.805 |
| CPREV+F+I+R9 | -8968495.801 | 17943897.165 |
| Q.PLANT+F+I+R9 | -8978009.728 | 17962925.019 |
| DCMUT+F+I+R9 | -8978744.923 | 17964395.409 |
| PMB+I+R9 | -8990457.518 | 17987619.054 |
| Q.PLANT+I+R9 | -9001866.523 | 18010437.064 |
| CPREV+I+R9 | -9014588.628 | 18035881.274 |
| DCMUT+I+R9 | -9025807.145 | 18058318.308 |
| MTINV+F+I+R9 | -9031718.994 | 18070343.551 |
| Q.MAMMAL+I+R9 | -9087034.647 | 18180773.312 |
| Q.MAMMAL+F+I+R9 | -9087201.451 | 18181308.465 |
| MTMET+F+I+R9 | -9128568.238 | 18264042.039 |
| Q.BIRD+I+R9 | -9180801.580 | 18368307.178 |
| Q.BIRD+F+I+R9 | -9181645.990 | 18370197.543 |
| MTVER+F+I+R9 | -9293662.374 | 18594230.311 |
| MTMET+I+R9 | -9556469.039 | 19119642.096 |
| MTINV+I+R9 | -9574363.604 | 19155431.226 |
| LG+I | -9577784.285 | 19162102.866 |
| MTVER+I+R9 | -9635972.592 | 19278649.202 |
| LG | -9707420.363 | 19421364.415 |
The inferred model Q.p__Armatimonadota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Armatimonadota_1+I+R9 | LG+F+I+R9 |
| BIC | 17611291.004 | 17671614.195 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loop_1/tree_update/Q.p__Armatimonadota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 1222.98 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Armatimonadota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 22  
Normalized RF distance: 0.0358  
Tree 1 branch length: 82.46193  
Tree 2 branch length: 84.59872  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -8868980.405 | -8930742.309 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__Armatimonadota_2):  
Pearson's correlation: 0.9675007304202173  
Euclidean distance: 0.6011742819910236  
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
Total time usage: 265867.45 seconds (73.85 h)  
