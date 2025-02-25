# BacterialQ: Clade-Specific Models for Bacterial Protein Evolution

## Overview

BacterialQ is a specialized pipeline for inferring and analyzing clade-specific amino acid substitution models in bacterial phylogenetics. Built on the GTDB R220 dataset, it addresses the unique evolutionary patterns in bacteria that are not fully captured by general protein models.

### Key Features

- **Phylum-Specific Models**: Estimates optimized substitution models for individual bacterial phyla
- **Domain-Level Models**: Provides Q.Bac_Class and Q.Bac_Family models for broader evolutionary analysis
- **Superior Model Fit**: Demonstrates 0.2-1.9% likelihood improvements over general models
- **Flexible Analysis**: Supports various constraint modes and sampling strategies
- **Comprehensive Validation**: Includes tools for model comparison and tree topology analysis

### Performance Highlights

- Forms distinct clusters in PCA analysis, separate from existing general models
- Better captures bacterial-specific evolutionary patterns
- Provides insights into both ancient and recent evolutionary events
- Supports improved bacterial species tree reconstruction

## Installation

### Dependencies

```bash
# Create and activate conda environment
conda env create -f env.yml
conda activate bacterialq

# Install additional analysis tools
conda env create -f env_analysis.yml
conda activate bacterialq_analysis
```

### External Requirements

- IQ-TREE (v2.3.6 or later)
- FastTree (v2.1 or later)
- TreeShrink (v1.3.9 or later)
- R (v4.0 or later) with ggplot2, tidyverse packages

## Quick Start

```bash
# Run the pipeline for a specific phylum
python scripts/subtree_model_iteration.py \
    --train_loc_path /path/to/training/loci \
    --test_loc_path /path/to/test/loci \
    --tree_file /path/to/reference/tree.nwk \
    --taxa_list /path/to/taxa.txt \
    --model_dir /path/to/initial/models \
    --max_iterate 5 \
    --converge_thres 0.999
```

## Core Components

### subtree_model_iteration.py

The main engine of the BacterialQ pipeline, implementing the complete model estimation workflow.

#### Key Features

1. **Subtree Management**
   - Splits large phylogenetic trees into manageable subtrees
   - Supports multiple pruning modes: split, lower, upper, and deep
   - Handles tree rooting and outgroup management

2. **Alignment Processing**
   - Samples alignments from input loci based on specified criteria
   - Filters low-quality alignments using parsimony informative sites
   - Supports both individual and concatenated alignment processing

3. **Model Estimation**
   - Implements iterative model refinement with convergence checking
   - Supports multiple constraint modes for model estimation
   - Handles both partitioned and concatenated analyses

4. **Performance Evaluation**
   - Tests models on independent test datasets
   - Compares tree topologies using Robinson-Foulds distances
   - Evaluates model fit using BIC scores

## Pipeline Parameters

### Required Parameters

- '--train_loc_path': The directory folder of the training site sequences (F\*\* format).  
- '--test_loc_path': The directory folder of the testing site sequences (F\*\*  format).  
- '--tree_file': Reference tree file (Newick format).  
- '--taxa_list': The taxa list file used for training.  
- '--model_dir': The NEXUS format file directory containing the initial alternative model.  
- '--max_iterate': The maximum number of iterations.  
- '--converge_thres': Threshold of person correlation coef between old and new models for stopping iteration.  
### Optional Parameters
#### Path Parameters
- `--train_loc_path`: Directory containing training loci alignments
- `--test_loc_path`: Directory containing test loci alignments
- `--tree_file`: Reference tree in Newick format
- `--taxa_list`: List of taxa for analysis
- `--model_dir`: Directory containing initial models

#### Training Options
- `--max_iterate`: Maximum number of iterations
- `--converge_thres`: Convergence threshold for model correlation
- `--tree_size_upper_lim`: Maximum size for subtrees (default: 250)
- `--num_aln`: Number of alignments to sample
- `--constraint_mode`: Model estimation constraint mode (fullcon/topocon/topolink/noncon) set using the trained Q matrices and previous best-fit empirical models, and compare the resulting tree topologies using various tree distance metrics (`Q_convert.py`).  
- Perform partitioned analysis on the testing set using IQ-TREE, allowing each locus to have its own substitution model and evolutionary rate, and assess the relative fit of the different models using model fit metrics.  

#### Performance Options
- `--max_threads`: Number of threads for parallel processing (default: 4)
- `--verify_on_loop`: Enable per-iteration model validation

#### Output Control
- `--prefix`: Output file prefix
- `--keep_tmp`: Retain temporary files
- `--keep_cmd_output`: Keep detailed command logs
- `--summary_dir`: Model summary directory
- `--RESULT_DIR`: Main output directory

## Pipeline Workflow

### 1. Data Preprocessing and Quality Control

#### Sequence Quality Assessment
- Calculates sequence integrity (1 - gap%) for each locus and species
- Filters loci with <30% integrity and species with <50% integrity
- Ensures robust phylogenetic signal in downstream analyses

#### Phylogenetic Quality Control
- Employs TreeShrink to identify and remove outlier taxa
- Detects and eliminates species with abnormal branch lengths
- Reduces the impact of potential sequencing artifacts or misalignments
### 2. Model Initialization and Training

#### Initial Model Selection
- Uses ModelFinder in IQ-TREE to evaluate model fit for each locus
- Tests against standard models (LG, WAG, Q.pfam, etc.)
- Selects the most frequently chosen model as starting point

#### Training Strategy
- Implements four constraint modes for model estimation:
  - **Full Constraint (fullcon)**: Fixed topology, shared tree with scalable rates
  - **Topology Constraint (topocon)**: Fixed topology, flexible branch lengths
  - **Topology Linked (topolink)**: Joint tree-model estimation, shared topology
  - **Non-constrained (noncon)**: Independent tree estimation per partition
### 3. Iterative Model Refinement

The pipeline employs an iterative approach to optimize both the substitution model and tree topology. Each iteration consists of two main steps:

#### Model Estimation Step
- Uses the previous iteration's Q matrix and tree as starting points
- Applies one of four constraint modes:

#### Convergence Assessment
- Calculates Pearson correlation between consecutive Q matrices
- Stops when correlation exceeds threshold (default: 0.999)
- Maximum iteration limit as fallback criterion

### 4. Model Comparison and Validation

#### Model Comparison
- Pearson correlation coefficients
- Matrix norms and distances
- PCA and t-SNE visualizations

#### Tree-based Metrics
- Tree topology distances
- Likelihood improvement

#### Model Fit Metrics
- AIC/BIC scores
- Cross-validation results

## Project Structure

```
├── scripts/                 # Core scripts and utilities
│   ├── subtree_model_iteration.py    # Main pipeline script
│   ├── Q_convert.py                  # Model format conversion
│   ├── get_subtree.py                # Subtree spliting
│   ├── quality_trimming.py           # Sequence quality control
│   └── analysis/                     # Analysis scripts
├── models/                  # Trained models
├── data/                    # Input data
├── analysis/               # Analysis results
└── Result_nova/            # Pipeline outputs
```

## Output

The program generates the following output files:  

### Root Directory
- `iqtree_results.csv`: Summary statistics for each iteration, including parameter settings, likelihood scores, and time usage.  
- `log.md`: Detailed markdown log of the program execution.   
- `meta.json`: Run configuration and parameters.
- `pruned_integrity_table.csv`: Summary of integrity (1 - gap%) across all loci and species.
- `select_id.txt`, `select_loci.txt`: Selected taxa and filtered loci lists.
- `outgroup_id.txt`, `outgroup_species_info.txt`: Outgroup selection information.

### estimated_tree/
- `*_FT_*_G20.treefile`: FastTree-generated trees with gamma rate categories.
- `*_reference_tree.tre`: Reference trees for comparison.
- `RF_heatmap.png`, `nRF_NMDS.png`: Tree comparison visualizations.
- `tree_pairwise_compare.csv`: Pairwise tree distance metrics.

### inferred_models/
- `Q.p__*_n`: IQ-TREE format model files for each iteration.
- `trained_model.nex`: Final NEXUS file containing trained models.
- `PCA_F.png`: PCA plot of stationary frequencies.
- `PCA_Q.png`: PCA plot of Q matrices.

### loop_n/
- `Q_diff_bubble.png`: Visualization of model changes between iterations.
- `Q_bubble.png`: Current iteration model visualization.
- `tree_comparison.html`: Tree topology comparison report.
- IQ-TREE and FastTree log files.

### final_test/
- Model comparison visualizations:
  - `best_existing_model.png`
  - `final_model.png`
  - `model_comparison.png`
- `tree_comparison.html`: Final tree topology analysis.
- `logfiles/`: IQ-TREE test results and logs.

### tree_comparison_files/
- Tree topology comparison results and visualizations.

## Future Development

### Planned Features

1. **Enhanced Model Support**
   - Support for profile mixture models (C60/C20)
   - Implementation of GTRpmix model
   - Integration with latest IQ-TREE features

2. **Performance Optimization**
   - Improved efficiency for large tree processing
   - Parallel processing enhancements


