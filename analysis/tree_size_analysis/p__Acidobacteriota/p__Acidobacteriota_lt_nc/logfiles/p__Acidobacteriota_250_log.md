## Initialization  
Running model estimation with the following parameters:  
  Maximum iterations: 5  
  Convergence threshold: 0.999  
  File prefix: p__Acidobacteriota_250  
  Taxa name: p__Acidobacteriota  
  Number of training loci: 400  
  Drop species threshold: 0.2  
  Drop locus threshold: 0.2  
  Initial model set: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART  
  Keep model threshold: 0.05  
  Pruning mode: upper  
  Lower limit for subtree size: 10  
  Upper limit for subtree size: 250  
### Quality trimming  
### Initial data extraction  
Running initial_data_extraction...  
Extracting training and testing loci for all species...  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/select_id.txt. Sampling sequences for 100 loci.  
Number of input species: 1891  
Remaining 100 alignments. Deleted 0 alignments.  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input a single taxa file: ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/select_id.txt. Sampling sequences for 20 loci.  
Number of input species: 1891  
Remaining 20 alignments. Deleted 0 alignments.  
### Prune reference tree  

## Iteration 1  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/ref_tree.tre -l 10 -u 250 -n 5 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 5   
Number of taxa after pruning: 935   
Pruned node IDs (degree): 1163 (214) 15 (204) 499 (185) 685 (168) 1891 (164)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 100 loci files. Total number of potential alignments: 500.  
Sub-sampling 400 alignments from 500 alignments.  
Remaining 400 alignments. Deleted 2 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/subtree_update/p__Acidobacteriota_250
```
  
  Runtime: 156103.19 seconds
[Subtree update log](loop_1/subtree_update/p__Acidobacteriota_250.iqtree)  
Best models for iteration 1:  
Q.INSECT  

| Model | Count |
|-------|-------|
| 185 | Q.INSECT |
| 84 | Q.PFAM |
| 76 | LG |
| 55 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/subtree_update/p__Acidobacteriota_250.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/subtree_update/p__Acidobacteriota_250.treefile --model-joint GTR20+FO --init-model Q.INSECT -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/model_update/p__Acidobacteriota_250
```
  
  Runtime: 110475.12 seconds
[Model update log](loop_1/model_update/p__Acidobacteriota_250.iqtree)  
BIC of the new model: 24848755.0673  
Likelihood of the new model: -11638720.0623  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_250_1)  
Model set for next iteration: Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_250_1  
![Model bubble plot](loop_1/p__Acidobacteriota_250_model_1.png)  
![Model difference plot](loop_1/model_diff_1.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile
```
  
  Runtime: 6999.84 seconds
[FastTree log](loop_1/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/tree_summary.csv', name = 'loop_1'))"
    
```
  
[Tree comparison report](loop_1/tree_comparison.html)  
RF distance: 632  
Normalized RF distance: 0.1674  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 307.647610904  
### Check convergence  
Iteration 1: Checking convergence  
Pearson's correlation: 0.9859419683105491  
Euclidean distance: 1.0135153166593618  
Time usage for Loop_1: 273649.59 seconds (76.01 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loci/concat_testing_loci.faa -m TESTONLY -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_250_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/test_model/p__Acidobacteriota_250
```
  
  Runtime: 906.85 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_250_1+I+G4 | -5319430.471 | 10672272.920 |
| p__Acidobacteriota_250_1+F+I+G4 | -5332641.294 | 10698862.466 |
| Q.YEAST+F+I+G4 | -5343741.136 | 10721062.150 |
| Q.INSECT+F+I+G4 | -5344549.796 | 10722679.470 |
| LG+F+I+G4 | -5346096.175 | 10725772.228 |
| Q.PFAM+F+I+G4 | -5350372.993 | 10734325.864 |
| Q.PFAM+I+G4 | -5354614.097 | 10742640.172 |
| LG+I+G4 | -5362662.172 | 10758736.322 |
| Q.INSECT+I+G4 | -5365873.746 | 10765159.470 |
| Q.INSECT+G4 | -5372308.264 | 10778019.669 |
| Q.YEAST+I+G4 | -5379982.509 | 10793376.996 |
| Q.INSECT+I | -5893380.847 | 11820164.835 |
| Q.INSECT | -5956214.348 | 11945823.001 |

## Iteration 2  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile -l 10 -u 250 -n 5 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 5   
Number of taxa after pruning: 944   
Pruned node IDs (degree): 1141 (214) 1670 (213) 333 (185) 519 (168) 1403 (164)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 100 loci files. Total number of potential alignments: 500.  
Sub-sampling 400 alignments from 500 alignments.  
Remaining 400 alignments. Deleted 2 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/training_loci -m MFP -mset Q.INSECT,Q.PFAM,LG,Q.YEAST,p__Acidobacteriota_250_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/subtree_update/p__Acidobacteriota_250
```
  
  Runtime: 94785.76 seconds
[Subtree update log](loop_2/subtree_update/p__Acidobacteriota_250.iqtree)  
Best models for iteration 2:  
p__Acidobacteriota_250_1  

| Model | Count |
|-------|-------|
| 348 | p__Acidobacteriota_250_1 |
| 26 | Q.PFAM |
| 14 | Q.INSECT |
| 11 | LG |
| 1 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/subtree_update/p__Acidobacteriota_250.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/subtree_update/p__Acidobacteriota_250.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_250_1 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/model_update/p__Acidobacteriota_250
```
  
  Runtime: 162593.95 seconds
[Model update log](loop_2/model_update/p__Acidobacteriota_250.iqtree)  
BIC of the new model: 25107861.2529  
Likelihood of the new model: -11764435.1216  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_250_2)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_2  
![Model bubble plot](loop_2/p__Acidobacteriota_250_model_2.png)  
![Model difference plot](loop_2/model_diff_2.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile
```
  
  Runtime: 6742.27 seconds
[FastTree log](loop_2/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_1/tree_update/p__Acidobacteriota_250_1.treefile', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/tree_summary.csv', name = 'loop_2'))"
    
```
  
[Tree comparison report](loop_2/tree_comparison.html)  
RF distance: 56  
Normalized RF distance: 0.0148  
Tree 1 branch length: 307.647610904  
Tree 2 branch length: 303.150342512  
### Check convergence  
Iteration 2: Checking convergence  
Pearson's correlation: 0.9979025123937266  
Euclidean distance: 0.4392521211870694  
Time usage for Loop_2: 264153.94 seconds (73.38 h)  
### Test model performance  
```bash
iqtree -T 50 -s ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loci/concat_testing_loci.faa -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_2 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/test_model/p__Acidobacteriota_250
```
  
  Runtime: 2160.41 seconds
Model testing results (concat):  

| Model | LogL | BIC |
|-------|------|-----|
| p__Acidobacteriota_250_2+I+G4 | -5322557.598 | 10678527.174 |
| p__Acidobacteriota_250_2+F+I+G4 | -5336371.764 | 10706323.406 |
| Q.YEAST+F+I+G4 | -5343437.365 | 10720454.608 |
| Q.INSECT+F+I+G4 | -5344254.263 | 10722088.404 |
| LG+F+I+G4 | -5345811.226 | 10725202.330 |
| Q.PFAM+F+I+G4 | -5350078.364 | 10733736.606 |
| Q.PFAM+I+G4 | -5354316.090 | 10742044.158 |
| LG+I+G4 | -5362371.722 | 10758155.422 |
| Q.INSECT+I+G4 | -5365591.589 | 10764595.156 |
| LG+G4 | -5368338.062 | 10770079.265 |
| Q.YEAST+I+G4 | -5379692.628 | 10792797.234 |
| MTMET+F+I+G4 | -5505188.012 | 11043955.902 |
| MTART+F+I+G4 | -5618589.159 | 11270758.196 |
| MTMET+I+G4 | -5743227.078 | 11519866.134 |
| MTART+I+G4 | -5854353.065 | 11742118.108 |
| LG+I | -5877820.474 | 11789044.089 |
| LG | -5936322.973 | 11906040.251 |

## Iteration 3  
### Prune subtrees  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile -l 10 -u 250 -n 5 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/subtrees -m upper
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 5   
Number of taxa after pruning: 944   
Pruned node IDs (degree): 998 (214) 1527 (213) 190 (185) 376 (168) 1260 (164)   
Pruning mode: upper   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/subtrees/summary  
### Extract subtree loci for trainning  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 5 subtree files and 100 loci files. Total number of potential alignments: 500.  
Sub-sampling 400 alignments from 500 alignments.  
Remaining 400 alignments. Deleted 1 alignments.  
### Subtree update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/training_loci -m MFP -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_2 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/subtree_update/p__Acidobacteriota_250
```
  
  Runtime: 77079.00 seconds
[Subtree update log](loop_3/subtree_update/p__Acidobacteriota_250.iqtree)  
Best models for iteration 3:  
p__Acidobacteriota_250_2  

| Model | Count |
|-------|-------|
| 334 | p__Acidobacteriota_250_2 |
| 37 | Q.INSECT |
| 15 | Q.PFAM |
| 11 | LG |
| 3 | Q.YEAST |
### Model update  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/subtree_update/p__Acidobacteriota_250.best_scheme.nex -te ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/subtree_update/p__Acidobacteriota_250.treefile --model-joint GTR20+FO --init-model p__Acidobacteriota_250_2 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/model_update/p__Acidobacteriota_250
```
  
  Runtime: 72933.61 seconds
[Model update log](loop_3/model_update/p__Acidobacteriota_250.iqtree)  
BIC of the new model: 24660485.646  
Likelihood of the new model: -11540576.3537  
Model does not meet precision requirement.  
[New model](trained_models/p__Acidobacteriota_250_3)  
Model set for next iteration: LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_3  
![Model bubble plot](loop_3/p__Acidobacteriota_250_model_3.png)  
![Model difference plot](loop_3/model_diff_3.png)  
### Tree update  
```bash
/home/tim/project/tool/FastTreeMP/FastTreeMP -trans ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/model_update/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/tree_update/fasttree.log -intree ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/ref_tree.tre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loci/concat_training_loci.faa > ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/tree_update/p__Acidobacteriota_250_3.treefile
```
  
  Runtime: 8645.56 seconds
[FastTree log](loop_3/tree_update/fasttree.log)  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_2/tree_update/p__Acidobacteriota_250_2.treefile', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/tree_update/p__Acidobacteriota_250_3.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/tree_summary.csv', name = 'loop_3'))"
    
```
  
[Tree comparison report](loop_3/tree_comparison.html)  
RF distance: 4  
Normalized RF distance: 0.0011  
Tree 1 branch length: 303.150342512  
Tree 2 branch length: 304.673081805  
### Check convergence  
Iteration 3: Checking convergence  
Pearson's correlation: 0.9999606025454464  
Euclidean distance: 0.05779427131880103  
Time usage for Loop_3: 158695.75 seconds (44.08 h)  
Convergence reached at iteration 3  

## Final test  
### Tree comparison  
```bash

    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/final_test', params = list(tree1_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/ref_tree.tre', tree2_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/tree_update/p__Acidobacteriota_250_3.treefile', root = FALSE, summary_path = '../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/tree_summary.csv', name = 'final_test'))"
    
```
  
[Tree comparison report](final_test/tree_comparison.html)  
RF distance: 636  
Normalized RF distance: 0.1684  
Tree 1 branch length: 224.21641  
Tree 2 branch length: 304.673081805  
### Model comparison  
Comparison between initial best model (Q.INSECT) and final model (p__Acidobacteriota_250_3):  
Pearson's correlation: 0.9775464318548722  
Euclidean distance: 1.342684129574678  
![Initial best model bubble plot](final_test/initial_best_model.png)  
![Final model bubble plot](final_test/final_model.png)  
![Model comparison plot](final_test/model_comparison.png)  
### Extract subtree loci for testing  
```bash
Rscript prune_subtree_2.R -t ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/loop_3/tree_update/p__Acidobacteriota_250_3.treefile -l 10 -u 250 -o ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/final_test/subtrees -m random
```
  
Original number of taxa: 1891   
Number of pruned subtrees: 18   
Number of taxa after pruning: 1879   
Pruned node IDs (degree): 149 (158) 152 (47) 1670 (213) 1141 (214) 1356 (35) 200 (23) 1391 (12) 1403 (164) 1566 (105) 995 (145) 981 (15) 519 (168) 235 (21) 961 (21) 256 (78) 333 (185) 688 (155) 842 (120)   
Pruning mode: random   
  
See detailed summary in ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/final_test/subtrees/summary  
Running sample_alignment...  
Discarded 0 loci based on the loci filter.  
Sampling alignments...  
Input 18 subtree files and 20 loci files. Total number of potential alignments: 360.  
Obtained 360 alignments from all potential alignments.  
Remaining 360 alignments. Deleted 0 alignments.  
### Final model testing  
```bash
iqtree -T 50 -S ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/final_test/testing_alignment -m TESTONLY -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,p__Acidobacteriota_250_3 -mdef ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex -pre ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/final_test/p__Acidobacteriota_250
```
  
  Runtime: 569.55 seconds
Best models for test data:  
p__Acidobacteriota_250_3  

| Model | Count |
|-------|-------|
| 271 | p__Acidobacteriota_250_3 |
| 37 | Q.INSECT |
| 25 | LG |
| 13 | Q.PFAM |
| 10 | Q.YEAST |
| 4 | MTART |
### PCA Plot for all models  
```bash
Rscript PCA_Q.R /home/tim/project/GTDB_TREE/data/modelset_ALL.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models/trained_model.nex ../Result_rona/treesize_p__Acidobacteriota/p__Acidobacteriota_250/trained_models
```
  
![PCA plot of Q matrices](trained_models/PCA_Q.png)  
![PCA plot of state frequencies](trained_models/PCA_F.png)  
### Record files  
[Summary of IQtree result](iqtree_results.csv)  
[Summary of tree comparison](tree_comparison.csv)  
Total time usage: 700468.04 seconds (194.57 h)  
