## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__KSB1  
  Taxa name: p__KSB1  
  Number of alignment for inferring model: 2000  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.1  
  Initial model set: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV  
  Keep model threshold: 0.05  
  Pruning mode: split  
  Lower limit for subtree size: 15  
  Upper limit for subtree size: 62  
### Quality trimming  
### Initial data extraction  
Running initial_aln_extraction...  
Abstract alignment of selected taxa scale:  
Running sample_alignment...  
Discarded 2 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/select_id.txt. Sampling sequences for 118 loci.  
Number of input species: 62  
Remaining 118 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__KSB1  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__KSB1 -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Zixibacteria as the outgroup for Phylum KSB1
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 119 alignments. Deleted 1 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/ref_tree.tre -l 15 -u 62 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/subtrees -m split
```
  
Original number of taxa: 62   
Number of pruned subtrees: 1   
Number of taxa after pruning: 62   
Pruned node IDs (degree): 1 (62)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/training_loci -m MFP -mset LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/subtree_update/Q.p__KSB1
```
  
  Runtime: 3324.80 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__KSB1.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 53 |
| Q.YEAST | 48 |
| Q.PFAM | 13 |
| Q.PLANT | 4 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/subtree_update/Q.p__KSB1.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/subtree_update/Q.p__KSB1.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/model_update/Q.p__KSB1
```
  
  Runtime: 17254.02 seconds  
[Model update log](loop_1/model_update/Q.p__KSB1.iqtree)  
BIC of the new model: 3682558.9107  
Likelihood of the new model: -1774106.3592  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__KSB1_1)  
Model set for next iteration: LG,Q.YEAST,Q.PFAM,Q.p__KSB1_1  
![Model bubble plot](loop_1/Q.p__KSB1_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9835898041195966  
Euclidean distance: 0.43251940684134704  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/tree_update/Q.p__KSB1_1.treefile
```
  
  Runtime: 478.58 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/tree_update/Q.p__KSB1_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/tree_update/Q.p__KSB1_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 18  
Normalized RF distance: 0.15  
Tree 1 branch length: 12.43376  
Tree 2 branch length: 17.70444  
Time usage for Loop_1: 21099.47 seconds (5.86 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/tree_update/Q.p__KSB1_1.treefile -l 15 -u 62 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/subtrees -m split
```
  
Original number of taxa: 62   
Number of pruned subtrees: 1   
Number of taxa after pruning: 62   
Pruned node IDs (degree): 1 (62)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 1 subtree files and 118 loci files. Total number of potential alignments: 118.  
Obtained 118 alignments from all potential alignments.  
Remaining 118 alignments. Deleted 0 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/training_loci -m MFP -mset LG,Q.YEAST,Q.PFAM,Q.p__KSB1_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/subtree_update/Q.p__KSB1
```
  
  Runtime: 3140.70 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__KSB1.iqtree)  
Best models for iteration 2:  
Q.p__KSB1_1  

| Model | Count |
|-------|-------|
| Q.p__KSB1_1 | 105 |
| Q.PFAM | 6 |
| Q.YEAST | 4 |
| LG | 3 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/subtree_update/Q.p__KSB1.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/subtree_update/Q.p__KSB1.treefile --model-joint GTR20+FO --init-model Q.p__KSB1_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/model_update/Q.p__KSB1
```
  
  Runtime: 11016.46 seconds  
[Model update log](loop_2/model_update/Q.p__KSB1.iqtree)  
BIC of the new model: 3683142.483  
Likelihood of the new model: -1774398.1454  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__KSB1_2)  
Model set for next iteration: Q.PFAM,Q.YEAST,LG,Q.p__KSB1_2  
![Model bubble plot](loop_2/Q.p__KSB1_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999334252792734  
Euclidean distance: 0.029666373977521303  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/tree_update/Q.p__KSB1_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 349.34 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 18  
Normalized RF distance: 0.15  
Tree 1 branch length: 12.43376  
Tree 2 branch length: 17.77488  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__KSB1_1,Q.p__KSB1_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 32831.39 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__KSB1_1+I+R8 | -1809902.923 | 3621246.556 |
| Q.p__KSB1_2+I+R8 | -1809921.754 | 3621284.218 |
| Q.p__KSB1_1+F+I+R8 | -1812738.144 | 3627118.273 |
| Q.p__KSB1_2+F+I+R8 | -1812829.533 | 3627301.051 |
| LG+I+R8 | -1815444.170 | 3632329.050 |
| LG+I+R9 | -1815446.099 | 3632354.095 |
| LG+R9 | -1815453.824 | 3632358.951 |
| LG+R8 | -1815465.019 | 3632360.154 |
| LG+I+R7 | -1815476.094 | 3632371.711 |
| LG+R7 | -1815540.810 | 3632490.549 |
| LG+I+R6 | -1815592.061 | 3632582.458 |
| LG+R6 | -1815678.433 | 3632744.609 |
| LG+F+I+R8 | -1815918.505 | 3633478.995 |
| Q.PFAM+I+R8 | -1817316.932 | 3636074.574 |
| Q.PFAM+F+I+R8 | -1817838.659 | 3637319.303 |
| LG+I+G4 | -1818087.844 | 3637478.683 |
| Q.YEAST+F+I+R8 | -1818151.620 | 3637945.225 |
| Q.INSECT+I+R8 | -1818804.665 | 3639050.040 |
| Q.YEAST+I+R8 | -1819048.442 | 3639537.594 |
| LG+G4 | -1821470.015 | 3644232.431 |
| Q.INSECT+F+I+R8 | -1821386.414 | 3644414.813 |
| WAG+F+I+R8 | -1826294.947 | 3654231.879 |
| WAG+I+R8 | -1829251.145 | 3659943.000 |
| Q.PLANT+I+R8 | -1830268.797 | 3661978.304 |
| Q.PLANT+F+I+R8 | -1831888.435 | 3665418.855 |
| JTT+F+I+R8 | -1833356.690 | 3668355.365 |
| JTT+I+R8 | -1835510.485 | 3672461.680 |
| CPREV+I+R8 | -1838261.945 | 3677964.600 |
| DCMUT+F+I+R8 | -1840114.955 | 3681871.895 |
| CPREV+F+I+R8 | -1840433.962 | 3682509.909 |
| MTINV+F+I+R8 | -1845166.977 | 3691975.939 |
| DCMUT+I+R8 | -1848324.150 | 3698089.010 |
| PMB+F+I+R8 | -1848894.588 | 3699431.161 |
| PMB+I+R8 | -1852023.545 | 3705487.800 |
| Q.MAMMAL+F+I+R8 | -1854758.329 | 3711158.643 |
| Q.MAMMAL+I+R8 | -1856000.450 | 3713441.610 |
| MTMET+F+I+R8 | -1858152.203 | 3717946.391 |
| Q.BIRD+F+I+R8 | -1867450.906 | 3736543.797 |
| Q.BIRD+I+R8 | -1868359.910 | 3738160.530 |
| MTVER+F+I+R8 | -1886262.687 | 3774167.359 |
| LG+I | -1924794.806 | 3850882.013 |
| MTMET+I+R8 | -1931811.150 | 3865063.010 |
| MTINV+I+R8 | -1940451.739 | 3882344.188 |
| MTVER+I+R8 | -1947063.489 | 3895567.688 |
| LG | -1999268.576 | 3999818.960 |
The inferred model Q.p__KSB1_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__KSB1_1+I+R8 | LG+I+R8 |
| BIC | 3621246.556 | 3632329.05 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loop_1/tree_update/Q.p__KSB1_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 318.39 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
LG model has higher likelihood than LG model, use LG model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/allloci_lg_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__KSB1/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 2  
Normalized RF distance: 0.0167  
Tree 1 branch length: 16.26047  
Tree 2 branch length: 17.77488  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -1880015.077 | -1885333.038 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (LG) and final model (Q.p__KSB1_2):  
Pearson's correlation: 0.9830169427866298  
Euclidean distance: 0.44904059625468556  
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
Total time usage: 68937.92 seconds (19.15 h)  
