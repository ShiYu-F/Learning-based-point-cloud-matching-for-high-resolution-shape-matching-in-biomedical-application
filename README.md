# LearningPointCloudReg-Bio3D
## Learning-based point cloud matching for high resolution shape matching in biomedical application
This repository contains code and data pipelines for aligning longitudinal intraoral 3D scans using classical and learning-based point cloud registration methods. The goal is to enable accurate, efficient, and clinically interpretable tracking of dental morphological changes such as tooth wear, orthodontic movement, and prosthetic adaptation.
## Table of Contents
- [Project Overview](#project_overview)
- [Dataset](#dataset)
- [Model Usage](#model_usage)

---

## Project Overview

Dental professionals increasingly rely on intraoral 3D scans to monitor and plan treatment. However, accurate alignment of scans over time remains a challenge, especially in the presence of tooth movement or wear changes.

This project benchmarks various rigid registration techniques, from classical methods like Procrustes to learning-based approaches such as MLP, PointNet and Graph Convolutional Networks (GCNs), to support precise and automated dental scan comparison.

---
## Dataset

**pointcloud_raw/**  
Each sample folder (A1–A37) contains two point cloud scans of a patient’s teeth collected in different years. These scans are used as input for rigid registration algorithms.

**landmarks.zip**  
This file includes manually labeled landmark positions for each scan, which are used for training, evaluation, and baseline comparison with classical methods such as Procrustes analysis. 

---
## Model Usage
All dataset files should be unzipped and placed in the same path

## Procrustes-based pipeline(Non learning-based model)
This module implements classical rigid point cloud alignment using Procrustes analysis based on manually annotated landmarks. It serves as a baseline for comparison against learning-based models.

**procrustes/Extract_rigid_transformation_withoutS.py**
A utility script to compute rigid transformation (rotation + translation, without scale) between two sets of landmarks.

**procrustes/Teeth_Procrusters_and_Evaluation_withoutS.ipynb**
A complete notebook that performs Procrustes-based alignment and evaluates registration performance using metrics such as MSE and Chamfer distance.

**Usage:**
```bash
cd procrustes/
jupyter notebook Teeth_Procrusters_and_Evaluation_withoutS.ipynb
```

### MLP-based pipeline
A fully connected network that takes concatenated landmark pairs as input and predicts rigid transformation.
**Usage:**
```bash
# Example (assuming unzipped MLP.zip)
cd MLP/
jupyter notebook MLP.ipynb
```

### GCN-based pipeline
A Graph Convolutional Network using neighborhood structure of landmarks to predict rigid transformation.
**Usage:**
```bash
# Example (assuming unzipped GCN.zip)
cd GCN/
jupyter notebook GCN.ipynb
```
### PointNet-based pipeline
A PointNet++-style network that directly learns point-level features for registration.
**Usage:**
```bash
# Example 
jupyter notebook PointNet_based.ipynb
```
---

## Setup
```bash
git clone https://github.com/your-username/intraoral-3d-registration.git](https://github.com/ShiYu-F/LearningPointCloudReg-Bio3D.git
cd LearningPointCloudReg-Bio3D
conda create -n dentalreg python=3.10
conda activate dentalreg
```
