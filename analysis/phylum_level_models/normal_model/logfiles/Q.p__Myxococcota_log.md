## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 4  
  Convergence threshold: 0.999  
  File prefix: Q.p__Myxococcota  
  Taxa name: p__Myxococcota  
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
Input a single taxa file: /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/select_id.txt. Sampling sequences for 120 loci.  
Number of input species: 878  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci...  
Select outgroup taxa for p__Myxococcota  
```bash
Rscript get_outgroup.R -t /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree -n p__Myxococcota -d 0.1 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/outgroup_id.txt -c /home/tim/project/bacterialQ/data/r220/combined_df.csv -s /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt -N 1 --detail
```
  
Outgroup selection detail: Select Phylum Deferribacterota as the outgroup for Phylum Myxococcota
  
Abstract alignment of outgroup taxa scale:  
Running sample_alignment...  
Input 2 taxa files and combine them. Sampling sequences for 120 loci.  
Remaining 120 alignments. Deleted 0 alignments.  
Concatenating loci contains outgroups...  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/ref_tree.tre -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/subtrees -m split
```
  
Original number of taxa: 878   
Number of pruned subtrees: 5   
Number of taxa after pruning: 875   
Pruned node IDs (degree): 388 (240) 646 (233) 2 (225) 231 (157) 627 (20)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 5 subtree files and 120 loci files. Total number of potential alignments: 600.  
Obtained 597 alignments from all potential alignments.  
Remaining 597 alignments. Deleted 3 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/subtree_update/Q.p__Myxococcota
```
  
  Runtime: 109988.72 seconds  
[Subtree update log](loop_1/subtree_update/Q.p__Myxococcota.iqtree)  
Best models for iteration 1:  
Q.PFAM  

| Model | Count |
|-------|-------|
| Q.PFAM | 218 |
| LG | 211 |
| Q.INSECT | 120 |
| Q.YEAST | 44 |
| Q.PLANT | 3 |
| MTART | 1 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/subtree_update/Q.p__Myxococcota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/subtree_update/Q.p__Myxococcota.treefile --model-joint GTR20+FO --init-model Q.PFAM -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/model_update/Q.p__Myxococcota
```
  
  Runtime: 259587.96 seconds  
[Model update log](loop_1/model_update/Q.p__Myxococcota.iqtree)  
BIC of the new model: 44276443.6102  
Likelihood of the new model: -21063576.3229  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Myxococcota_1)  
Model set for next iteration: Q.PFAM,LG,Q.INSECT,Q.YEAST,Q.p__Myxococcota_1  
![Model bubble plot](loop_1/Q.p__Myxococcota_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/model_update/summary  
### Check model convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9580956946679925  
Euclidean distance: 0.776327785181606  
### Tree update  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/fasttree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/ref_tree_with_outgroups.tre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/Q.p__Myxococcota_1.treefile
```
  
  Runtime: 5643.57 seconds  
[FastTree log](loop_1/tree_update/fasttree.log)  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/Q.p__Myxococcota_1_with_outgroup.treefile.  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/Q.p__Myxococcota_1.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/cophylo_plot.pdf', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 226  
Normalized RF distance: 0.129  
Tree 1 branch length: 161.44354  
Tree 2 branch length: 208.40433  
Time usage for Loop_1: 375556.58 seconds (104.32 h)  

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree.R -t /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/Q.p__Myxococcota_1.treefile -l 15 -u 250 -o /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/subtrees -m split
```
  
Original number of taxa: 878   
Number of pruned subtrees: 6   
Number of taxa after pruning: 864   
Pruned node IDs (degree): 344 (240) 602 (236) 16 (169) 187 (157) 837 (42) 583 (20)   
Pruning mode: split   
  
See detailed summary in /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/subtrees/summary  
### Extract subtree loci for training model  
Running sample_alignment...  
Input 6 subtree files and 120 loci files. Total number of potential alignments: 720.  
Obtained 717 alignments from all potential alignments.  
Remaining 717 alignments. Deleted 3 alignments.  
### Subtree update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/training_loci -m MFP -mset Q.PFAM,LG,Q.INSECT,Q.YEAST,Q.p__Myxococcota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/inferred_models/trained_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/subtree_update/constraint_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/subtree_update/Q.p__Myxococcota
```
  
  Runtime: 92153.48 seconds  
[Subtree update log](loop_2/subtree_update/Q.p__Myxococcota.iqtree)  
Best models for iteration 2:  
Q.p__Myxococcota_1  

| Model | Count |
|-------|-------|
| Q.p__Myxococcota_1 | 569 |
| LG | 58 |
| Q.INSECT | 46 |
| Q.PFAM | 31 |
| Q.YEAST | 13 |
### Model update  
```bash
iqtree -seed 1 -T 50 -S /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/subtree_update/Q.p__Myxococcota.best_model.nex -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/subtree_update/Q.p__Myxococcota.treefile --model-joint GTR20+FO --init-model Q.p__Myxococcota_1 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/inferred_models/trained_model.nex -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/model_update/Q.p__Myxococcota
```
  
  Runtime: 167070.36 seconds  
[Model update log](loop_2/model_update/Q.p__Myxococcota.iqtree)  
BIC of the new model: 43718947.0685  
Likelihood of the new model: -20784985.0554  
Model does not meet precision requirement.  
[New model](inferred_models/Q.p__Myxococcota_2)  
Model set for next iteration: LG,Q.INSECT,Q.PFAM,Q.p__Myxococcota_2  
![Model bubble plot](loop_2/Q.p__Myxococcota_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
Generated summary for model update, see/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/model_update/summary  
### Check model convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9999594514704334  
Euclidean distance: 0.032418491216928545  
Convergence of model reached at iteration 2  

## Final test  
### Final tree estimation on all loci  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/best_final_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/Q.p__Myxococcota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/best_final_tree.treefile
```
  
  Runtime: 5608.10 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/best_final_tree_with_outgroup.treefile.  
### Tree comparison  
Compare the final tree with reference tree:  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/ref_tree.tre', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/cophylo_plot.pdf', name = 'final_tree_compare'))"
    
```
  
[Tree comparison report](tree_comparison.html)  
RF distance: 230  
Normalized RF distance: 0.1313  
Tree 1 branch length: 161.44354  
Tree 2 branch length: 208.93335  
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/bacterialQ/data/modelset_ALL.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/inferred_models/trained_model.nex /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/inferred_models
```
  
![PCA plot of Q matrultices](inferred_models/PCA_Q.png)  
![PCA plot of state frequencies](inferred_models/PCA_F.png)  
### Test model on reference tree in concatenated loci  
```bash
iqtree -seed 1 -T AUTO -ntmax 50 -s /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loci/concat_loci.faa -m TESTNEWONLY -cmin 6 -cmax 9 -mset LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER,Q.p__Myxococcota_1,Q.p__Myxococcota_2 -mdef /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/inferred_models/trained_model.nex -safe -te /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/ref_tree.tre -pre /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/reftree_best_concat_model
```
  
  Runtime: 85767.74 seconds  
[Detail result of concat test](final_test/logfiles/reftree_best_concat_model.log)  
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| Q.p__Myxococcota_1+I+R9 | -21407842.650 | 42834484.963 |
| Q.p__Myxococcota_2+I+R9 | -21408781.490 | 42836362.643 |
| Q.p__Myxococcota_1+F+I+R9 | -21475764.120 | 42970529.707 |
| Q.p__Myxococcota_2+F+I+R9 | -21478431.110 | 42975863.687 |
| Q.PFAM+F+I+R9 | -21520850.860 | 43060703.187 |
| LG+F+I+R9 | -21523063.980 | 43065129.427 |
| Q.YEAST+F+I+R9 | -21569383.360 | 43157768.187 |
| Q.PFAM+I+R9 | -21593336.640 | 43205472.943 |
| Q.INSECT+F+I+R9 | -21615439.880 | 43249881.227 |
| WAG+F+I+R9 | -21627277.690 | 43273556.847 |
| LG+I+R9 | -21659172.410 | 43337144.483 |
| LG+R9 | -21661436.340 | 43341661.722 |
| LG+I+R8 | -21666371.360 | 43351521.141 |
| LG+R8 | -21669517.020 | 43357801.839 |
| LG+I+R7 | -21677234.960 | 43373227.098 |
| LG+R7 | -21681900.660 | 43382547.877 |
| LG+I+R6 | -21696061.460 | 43410858.855 |
| LG+R6 | -21703034.380 | 43424794.074 |
| WAG+I+R9 | -21728220.350 | 43475240.363 |
| LG+I+G4 | -21795629.840 | 43609900.024 |
| Q.INSECT+I+R9 | -21806386.640 | 43631572.943 |
| LG+G4 | -21822121.670 | 43662873.063 |
| PMB+F+I+R9 | -21825990.710 | 43670982.887 |
| JTT+F+I+R9 | -21828995.380 | 43676992.227 |
| Q.YEAST+I+R9 | -21847647.600 | 43714094.863 |
| DCMUT+F+I+R9 | -21876195.300 | 43771392.067 |
| CPREV+F+I+R9 | -21887322.470 | 43793646.407 |
| JTT+I+R9 | -21903210.090 | 43825219.843 |
| PMB+I+R9 | -21938314.880 | 43895429.423 |
| Q.PLANT+F+I+R9 | -21947985.280 | 43914972.027 |
| DCMUT+I+R9 | -22018124.720 | 44055049.103 |
| Q.PLANT+I+R9 | -22055912.620 | 44130624.903 |
| CPREV+I+R9 | -22079034.210 | 44176868.083 |
| MTINV+F+I+R9 | -22100330.510 | 44219662.487 |
| Q.MAMMAL+F+I+R9 | -22228536.280 | 44476074.027 |
| Q.MAMMAL+I+R9 | -22258703.050 | 44536205.763 |
| MTMET+F+I+R9 | -22368637.060 | 44756275.587 |
| Q.BIRD+F+I+R9 | -22486992.690 | 44992986.847 |
| Q.BIRD+I+R9 | -22518529.690 | 45055859.043 |
| MTVER+F+I+R9 | -22798930.320 | 45616862.107 |
| MTMET+I+R9 | -23590787.440 | 47200374.543 |
| MTINV+I+R9 | -23593087.890 | 47204975.443 |
| LG+I | -23601942.050 | 47222513.823 |
| MTVER+I+R9 | -23803289.440 | 47625378.543 |
| LG | -23852838.180 | 47724295.461 |
The inferred model Q.p__Myxococcota_1 has better BIC value than the existing model:  

| Type | Best Inferred Model | Best Existing Model |
|------|-----------------|---------------------|
| Model | Q.p__Myxococcota_1+I+R9 | Q.PFAM+F+I+R9 |
| BIC | 42834484.963 | 43060703.187 |
### Test final tree  
#### Final tree estimation on all loci without inferred model  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -trans /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/allloci_best_existing_model_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/Q.p__Myxococcota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/allloci_best_existing_model_tree.treefile
```
  
  Runtime: 4951.42 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/allloci_best_existing_model_tree_with_outgroup.treefile.  
```bash
/home/tim/tool/FastTreeMP/FastTreeMP -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/allloci_lg_tree.log -intree /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loop_1/tree_update/Q.p__Myxococcota_1_with_outgroup.treefile /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/loci/concat_loci_with_outgroup.faa > /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/allloci_lg_tree.treefile
```
  
  Runtime: 4873.31 seconds  
Prune outgroup from the tree. The original tree is renamed as /home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/allloci_lg_tree_with_outgroup.treefile.  
Q.PFAM model has higher likelihood than LG model, use best_existing_model model for final tree.  
#### Compare final tree with existing model tree  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test', params = list(tree1_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/allloci_best_existing_model_tree.treefile', tree2_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/logfiles/best_final_tree.treefile', summary_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/tree_summary.csv', cophylo_path = '/home/tim/project/bacterialQ/Result_nova/add_phylum_models/Q.p__Myxococcota/final_test/cophylo_plot.pdf', name = 'compare_existing_model_tree'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 44  
Normalized RF distance: 0.0251  
Tree 1 branch length: 196.81574  
Tree 2 branch length: 208.93335  
Log-Likelihood of final best tree and the tree estimated without inferred model:  

| Tree | Best final tree | Existing model tree |
|------|-----------------|---------------------|
| LogL | -21474017.744 | -21655800.899 |
The final model tree has better likelihood than the existing model tree.  
### Model comparison  
Comparison between best existing model (Q.PFAM) and final model (Q.p__Myxococcota_2):  
Pearson's correlation: 0.957004916795944  
Euclidean distance: 0.8010232390733923  
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
Total time usage: 736563.72 seconds (204.60 h)  
