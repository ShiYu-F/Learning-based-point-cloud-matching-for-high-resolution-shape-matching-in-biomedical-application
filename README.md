# LearningPointCloudReg-Bio3D
## Learning-based point cloud matching for high resolution shape matching in biomedical application
This repository contains code and data pipelines for aligning longitudinal intraoral 3D scans using classical and learning-based point cloud registration methods. The goal is to enable accurate, efficient, and clinically interpretable tracking of dental morphological changes such as tooth wear, orthodontic movement, and prosthetic adaptation.
## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Methodology](#methodology)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Evaluation Metrics](#evaluation-metrics)
- [Results](#results)
- [Contributors](#contributors)
- [License](#license)

---

## Project Overview

Dental professionals increasingly rely on intraoral 3D scans to monitor and plan treatment. However, accurate alignment of scans over time remains a challenge, especially in the presence of tooth movement or wear changes.

This project benchmarks various rigid registration techniques, from classical methods like Iterative Closest Point (ICP) to modern deep learning approaches such as PointNet and Graph Convolutional Networks (GCNs), to support precise and automated dental scan comparison.

---

## Features
- Semi-automated landmark annotation workflow (via Blender)
- Baseline registration using Procrustes alignment
- Classical ICP-based registration
- Learning-based registration (MLP, PointNet, GCN, etc.)
- Evaluation via mesh-based Chamfer Distance and MSE
- Modular, extensible code structure for custom method integration

---

## Methodology

### Registration Pipeline
1. **Annotation Strategy Development**  
   Landmark subsets selected based on anatomical relevance and labeling efficiency.

2. **Data Preparation**  
   Longitudinal intraoral scans labeled using Blender and processed into point clouds or meshes.

3. **Registration Methods**
   - **ICP** (classical rigid alignment)
   - **Procrustes** (landmark-based baseline)
   - **MLP** / **PointNet** / **GCN** (deep learning-based models)

4. **Evaluation Metrics**
   - **Mean Squared Error (MSE)**
   - **Chamfer Distance (CD)**

---

## Installation

```bash
git clone https://github.com/your-username/intraoral-3d-registration.git
cd intraoral-3d-registration
conda create -n dentalreg python=3.8
conda activate dentalreg
pip install -r requirements.txt
