# **Paramagnetic Rim Lesions in Early Multiple Sclerosis: A 7 Tesla Imaging Study**  

This repository contains the scripts used in the study:  
**"Paramagnetic Rim Lesions in Early Multiple Sclerosis: A 7 Tesla Imaging Study"**,  
accepted at *Brain Communications*.  

## **Authors**  
Habeeb F. Kazimuddin,1-3 Jiacheng Wang,4 Ahmad A. Toubasi,1 Bryan Hernandez,1,5-7 Lili Sun,8 Taegan Vinarsky,1 Caroline Gheen,1 Zachary Rohm,1 Carynn Koch,1 James E. Eaton,9,10 Margareta A. Clarke,1 Rachael Cheek,1,11 John Kramer,9 Fei Ye,8 Ipek Oguz,4 Francesca Bagnato1,12  

### **Author Affiliations**  
1. Neuroimaging Unit, Neuroimmunology Division, Department of Neurology, Vanderbilt University Medical Center (VUMC), Nashville, TN, USA  
2. College of Arts and Science, Vanderbilt University (VU), Nashville, TN, USA  
3. National Institute of Neurological Disorders and Stroke (NINDS), National Institute of Health (NIH), Bethesda, MD, USA  
4. Vanderbilt University Department of Computer Science, Nashville, TN, USA  
5. Medical Scientist Program, VU School of Medicine, Nashville, TN, USA  
6. College of Science, Department of Biological Sciences, University of Texas at El Paso, TX, USA  
7. VU School of Medicine, Department of Biochemistry, Nashville, TN, USA  
8. Department of Biostatistics and Medicine, VUMC, Nashville, TN, USA  
9. Neuroimmunology Division, Department of Neurology, VUMC, Nashville, TN, USA  
10. Cognitive Division, Department of Neurology, VUMC, Nashville, TN, USA  
11. Meharry Medical College, School of Medicine, Nashville, TN, USA  
12. Department of Neurology, Nashville VA Medical Center, TN Valley Healthcare System, Nashville, TN, USA  

**Corresponding Author:**  
Francesca Bagnato, M.D., Ph.D.  

## **Description**  
This repository provides code used in the analysis of paramagnetic rim lesions in early multiple sclerosis using 7T MRI imaging. The scripts facilitate **image processing, registration, and quantitative analysis**.  

## **Code Overview**  

- **`make-swi`**: MATLAB script for generating **SWI phase maps** from SE-GRE acquisitions.  
- **`image_registration`**: Python scripts for **rigid image registration**, aligning T2-w FLAIR to SWI using **FLIRT (FSL)** and MP2RAGE to registered FLAIR using **ANTs** with the Mattes metric.  
- **`freesurfer_preparation`**: Processing pipeline for **MP2RAGE and T2-w FLAIR** using **FreeSurfer**, including pial surface refinement and cortical thickness extraction.  
- **`bpf_calculation`**: Python script for calculating **Brain Parenchyma Fraction (BPF)** using **SIENAX (FSL)**, refining segmentation outputs to improve NAWM volume computation.  

## **Requirements**  
The scripts require the following dependencies:  

- **Python** (for `image_registration` and `bpf_calculation`):  
  - `nibabel`  
  - `numpy`  
  - `FSL` (`FLIRT`, `SIENAX`)  
  - `ANTsPy` (if using ANTs for registration)  

- **MATLAB** (for `make-swi` processing)  
- **FreeSurfer** (for cortical thickness and pial surface refinement)  

## **Keywords**  
Chronic inflammation, susceptibility-based magnetic resonance imaging, MRI, FreeSurfer, FSL, ANTs, Brain Parenchyma Fraction (BPF).  
