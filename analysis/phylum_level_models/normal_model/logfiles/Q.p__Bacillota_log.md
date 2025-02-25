## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Bacillota  
  Taxa name: p__Bacillota  
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
Discarded 0 loci based on the loci filter.  
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 3868  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Bacillota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Bacillota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Poribacteria as the outgroup for Phylum Bacillota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/subtrees -m split
```
  
Original number of taxa: 3868   
Number of pruned subtrees: 33   
Number of taxa after pruning: 3784   
Pruned node IDs (degree): 242 (249) 3495 (244) 2602 (228) 680 (211) 2191 (203) 2829 (203) 2000 (188) 3134 (188) 1623 (164) 938 (160) 528 (151) 3350 (146) 1236 (145) 1097 (139) 3738 (115) 1786 (115) 2443 (113) 3041 (94) 1433 (85) 4 (84) 137 (59) 1523 (57) 1900 (55) 2393 (51) 891 (47) 90 (46) 1954 (45) 1392 (41) 1582 (41) 199 (40) 492 (36) 2577 (26) 2555 (15)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 33 subtree files and 120 loci files. Total number of potential alignments: 3960.  
Sub-sampling 2000 alignments from 3960 alignments.  
Remaining 2000 alignments. Deleted 9 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/subtree_update/Q.p__Bacillota
```
  
  Runtime: 62209.18 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Bacillota.iqtree)  
Best models for iteration 1:  
LG  

| Model | Count |
|-------|-------|
| LG | 498 |
| Q.INSECT | 479 |
| Q.YEAST | 472 |
| Q.PLANT | 419 |
| Q.PFAM | 124 |
| MTART | 4 |
| MTMET | 4 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/subtree_update/Q.p__Bacillota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/subtree_update/Q.p__Bacillota.treefile --model-joint GTR20+FO --init-model LG -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/model_update/Q.p__Bacillota
```
  
  Runtime: 275092.92 seconds  
[Model update log](loop_1/model_update/Q.p__Bacillota.iqtree)  
BIC of the new model: 47199686.4578  
Likelihood of the new model: -20677794.8416  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_1)  
Model set for next iteration: LG,Q.INSECT,Q.YEAST,Q.PLANT,Q.PFAM,Q.p__Bacillota_1  
![Model bubble plot](loop_1/Q.p__Bacillota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9704987042967779  
Euclidean distance: 0.5431208917902519  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/tree_update/Q.p__Bacillota_1.treefile
```
  
  Runtime: 29680.63 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/tree_update/Q.p__Bacillota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/tree_update/Q.p__Bacillota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 1674  
Normalized RF distance: 0.2165  
Tree 1 branch length: 202.27962  
Tree 2 branch length: 300.01663  
Time usage for Loop_1: 373511.56 seconds (103.75 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/tree_update/Q.p__Bacillota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/subtrees -m split
```
  
Original number of taxa: 3868   
Number of pruned subtrees: 32   
Number of taxa after pruning: 3767   
Pruned node IDs (degree): 1860 (249) 316 (244) 757 (228) 2298 (211) 985 (203) 1420 (203) 3618 (188) 1672 (188) 3098 (164) 2694 (160) 2146 (151) 171 (146) 3475 (143) 1292 (128) 2568 (127) 3261 (115) 559 (112) 1197 (94) 2908 (85) 4 (84) 91 (59) 2998 (57) 3375 (55) 1622 (51) 2509 (47) 3818 (46) 3429 (45) 2867 (41) 3057 (41) 684 (40) 2110 (36) 732 (26)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 32 subtree files and 120 loci files. Total number of potential alignments: 3840.  
Sub-sampling 2000 alignments from 3840 alignments.  
Remaining 2000 alignments. Deleted 8 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/training_loci -m MFP -mset LG,Q.INSECT,Q.YEAST,Q.PLANT,Q.PFAM,Q.p__Bacillota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/subtree_update/Q.p__Bacillota
```
  
  Runtime: 99479.81 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Bacillota.iqtree)  
Best models for iteration 2:  
Q.p__Bacillota_1  

| Model | Count |
|-------|-------|
| Q.p__Bacillota_1 | 1720 |
| Q.PLANT | 125 |
| LG | 54 |
| Q.PFAM | 50 |
| Q.INSECT | 28 |
| Q.YEAST | 23 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/subtree_update/Q.p__Bacillota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/subtree_update/Q.p__Bacillota.treefile --model-joint GTR20+FO --init-model Q.p__Bacillota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/model_update/Q.p__Bacillota
```
  
  Runtime: 158789.76 seconds  
[Model update log](loop_2/model_update/Q.p__Bacillota.iqtree)  
BIC of the new model: 49187151.7975  
Likelihood of the new model: -21586566.9467  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Bacillota_2)  
Model set for next iteration: Q.PLANT,LG,Q.PFAM,Q.INSECT,Q.p__Bacillota_2  
![Model bubble plot](loop_2/Q.p__Bacillota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9998043270348529  
Euclidean distance: 0.041375594567607706  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loop_1/tree_update/Q.p__Bacillota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 24578.95 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 1692  
Normalized RF distance: 0.2188  
Tree 1 branch length: 202.27962  
Tree 2 branch length: 299.24059  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Bacillota_1,Q.p__Bacillota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Bacillota/final_test/logfiles/reftree_best_concat_model
```
  
  Error:
Terminated
  
  Exit code: 143  
  Runtime: 1679463.96 seconds  
Terminated
  
