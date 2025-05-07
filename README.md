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

---
## Dataset

**pointcloud_raw/**  
Each sample folder (A1–A37) contains two point cloud scans of a patient’s teeth collected in different years. These scans are used as input for rigid registration algorithms.

**landmarks.zip**  
This file includes manually labeled landmark positions for each scan, which are used for training, evaluation, and baseline comparison with classical methods such as Procrustes analysis. 

---
## Model Usage
All dataset files should be unzipped and placed in the same path

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


```bash
git clone https://github.com/your-username/intraoral-3d-registration.git
cd intraoral-3d-registration
conda create -n dentalreg python=3.8
conda activate dentalreg
pip install -r requirements.txt
