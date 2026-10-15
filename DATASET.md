
# RetinaSense - Dataset Research and Class Imbalance

## 1. Objective

This document records the retinal image datasets being investigated for RetinaSense, a machine learning project focused on supporting diabetic retinopathy (DR) screening. The goal is to understand the available datasets, investigate their class distributions, identify potential class imbalance, and determine appropriate strategies for preparing data for model training.

RetinaSense is intended to support the identification of cases that may require further professional evaluation, not to replace clinical diagnosis.

## 2. Existing Datasets

### 2.1 APTOS 2019

**Source:** [APTOS 2019 Blindness Detection — Kaggle](https://www.kaggle.com/datasets/mariaherrerot/aptos2019)

APTOS 2019 contains retinal fundus images classified into five diabetic retinopathy severity grades, from Grade 0 (No DR) to Grade 4 (Proliferative DR).

#### Reference Class Distribution

| Grade | Severity | Number of Images | Percentage |
|---|---|---:|---:|
| 0 | No DR | 1,805 | 49.3% |
| 1 | Mild DR | 370 | 10.1% |
| 2 | Moderate DR | 999 | 27.3% |
| 3 | Severe DR | 193 | 5.3% |
| 4 | Proliferative DR | 295 | 8.1% |
| | **Total** | **3,662** | **100%** |

**Observation:** APTOS 2019 exhibits class imbalance. Grade 0 accounts for approximately half the dataset, while Grade 3 contains only 193 images. Grade 0 has approximately 9.4 times as many images as Grade 3.

These are published reference counts and should be verified against the exact dataset version used in the project.

### 2.2 Combined EyePACS, APTOS, and MESSIDOR Dataset

**Source:** [EyePACS, APTOS, MESSIDOR Diabetic Retinopathy — Kaggle](https://www.kaggle.com/datasets/ascanipek/eyepacs-aptos-messidor-diabetic-retinopathy/data)

This collection combines retinal fundus images from EyePACS, APTOS, and MESSIDOR. It is being investigated as a potential source of additional training images for diabetic retinopathy classification.

The actual label distribution, source composition, duplicate images, and label compatibility must be verified before using the combined collection for training.

#### Published Reference Distributions by Original Dataset

The following table shows published reference counts for the individual datasets. These figures are **not the verified class distribution of the combined Kaggle download**.

| Grade | Severity | EyePACS | APTOS 2019 | MESSIDOR-2 Reference |
|---|---|---:|---:|---:|
| 0 | No DR | 25,810 (73.5%) | 1,805 (49.3%) | 1,017 (58.3%) |
| 1 | Mild DR | 2,443 (7.0%) | 370 (10.1%) | 270 (15.5%) |
| 2 | Moderate DR | 5,292 (15.1%) | 999 (27.3%) | 347 (19.9%) |
| 3 | Severe DR | 873 (2.5%) | 193 (5.3%) | 75 (4.3%) |
| 4 | Proliferative DR | 708 (2.0%) | 295 (8.1%) | 35 (2.0%) |
| | **Total** | **35,126** | **3,662** | **1,744** |

**Important notes:**

- EyePACS counts represent a published labeled training distribution.
- APTOS counts represent its published five-grade labeled dataset.
- MESSIDOR-2 is a specific dataset and should not automatically be treated as identical to the original MESSIDOR dataset included in every combined collection.
- The combined Kaggle download may contain different subsets, duplicated images, or augmented images.
- The counts above must not be added together and presented as the actual distribution of the combined dataset.
- Exact class counts and percentages for the combined download remain pending local inspection.

#### Verification Tasks

1. Inspect the extracted directory structure and available label files.
2. Count images assigned to each grade, from 0 to 4.
3. Identify the source dataset for each image, if source information is available.
4. Check for duplicate images and potential overlap between source datasets.
5. Verify label compatibility before combining images for training.
6. Calculate the combined dataset's actual class percentages after these checks.

### 2.3 OLIVES Dataset

**Official source:** [Georgia Tech — OLIVES Dataset](https://alregib.ece.gatech.edu/olives-dataset/)

**Hugging Face access point:** [OLIVES Dataset](https://huggingface.co/datasets/gOLIVES/OLIVES_Dataset)

OLIVES provides retinal imaging data and associated clinical information and annotations. It includes fundus imaging and optical coherence tomography (OCT) data.

**Important consideration:** OLIVES should not automatically be treated as another five-grade DR dataset equivalent to APTOS 2019. Its modalities, annotation structure, and available labels must be inspected to determine whether they support the intended RetinaSense classification task.

The Georgia Tech website and Hugging Face repository are access points to OLIVES-related data, not necessarily two independent datasets. The specific Hugging Face configuration or subset must be checked before reporting its sample count or label distribution.

#### Five-Grade DR Severity Distribution

| Grade | Severity | Number of Images | Percentage |
|---|---|---:|---:|
| 0 | No DR | N/A | N/A |
| 1 | Mild DR | N/A | N/A |
| 2 | Moderate DR | N/A | N/A |
| 3 | Severe DR | N/A | N/A |
| 4 | Proliferative DR | N/A | N/A |
| | **Total** | **Not available** | **Not available** |

**Note:** The five-grade distribution is unavailable from the information currently verified. OLIVES disease-classification labels should not be assumed to correspond to the standard Grade 0–4 DR severity scale. These values are unavailable, not zero.

**Status:** Label compatibility and suitability for the project's classification task remain to be investigated.

## 3. Understanding Class Imbalance

Class imbalance occurs when some classes contain substantially more training examples than others.

For diabetic retinopathy classification, Grade 0 (No DR) is frequently the majority class, while severe and proliferative DR classes may contain relatively few images.

A model trained on an imbalanced dataset may favor majority classes and perform poorly on minority classes. High overall accuracy alone may therefore hide weak detection performance for clinically important cases.

### Key Observations

- APTOS 2019 has a substantial difference between the number of Grade 0 and Grade 3 images.
- The published EyePACS training distribution is heavily dominated by Grade 0.
- The combined Kaggle dataset's exact imbalance cannot be determined reliably until its labels have been counted.
- OLIVES suitability depends on the selected subset, its annotations, and the intended classification task.

## 4. Potential Strategies for Handling Class Imbalance

The following approaches are candidates for experimentation. No strategy has yet been selected as the final solution.

### 4.1 Class-Weighted Loss

Assign higher loss weights to underrepresented classes so that mistakes involving minority classes contribute more to the training objective.

**Potential benefit:** A practical first approach because it does not require generating additional images.

### 4.2 Data Augmentation

Apply medically appropriate transformations to training images, such as modest rotations, zooms, and brightness adjustments.

**Potential benefit:** Increases training variation, especially for classes with fewer examples.

**Caution:** Transformations must preserve medically meaningful retinal features and must not create misleading examples.

### 4.3 Oversampling

Sample minority-class examples more frequently during training.

**Potential benefit:** Gives the model more opportunities to learn underrepresented classes.

**Caution:** Repeatedly sampling the same images can increase overfitting.

### 4.4 Stratified Data Splitting

Maintain reasonable class representation across training, validation, and test sets. Where patient identifiers are available, ensure that images from the same patient do not leak across these sets.

**Potential benefit:** Supports more reliable evaluation and reduces the risk of overly optimistic results.

### 4.5 Evaluation Metrics

Evaluate performance using more than overall accuracy:

- Per-class precision and recall.
- Macro F1-score.
- Confusion matrix.
- Sensitivity and specificity appropriate to the defined screening task.
- ROC-AUC where suitable for the selected task and evaluation design.

For a screening-support application, particular attention should be paid to missed referable cases. The definition of referable DR must be agreed upon before selecting final metrics and decision thresholds.

## 5. Next Steps

- [ ] Inspect the actual APTOS 2019 label file and confirm its class counts.
- [ ] Inspect the combined EyePACS/APTOS/MESSIDOR download and calculate its exact Grade 0–4 distribution.
- [ ] Identify source datasets and check for duplicate or overlapping images.
- [ ] Investigate OLIVES label compatibility and determine whether it supports the selected task.
- [ ] Discuss the classification objective and imbalance-handling strategy with the project mentor.
- [ ] Establish an appropriate training, validation, and test split.
- [ ] Train a baseline model and compare imbalance-handling methods using class-sensitive evaluation metrics.

## 6. References

1. **APTOS 2019:** [Kaggle dataset](https://www.kaggle.com/datasets/mariaherrerot/aptos2019)
2. **Combined EyePACS/APTOS/MESSIDOR:** [Kaggle dataset by ascanipek](https://www.kaggle.com/datasets/ascanipek/eyepacs-aptos-messidor-diabetic-retinopathy/data)
3. **OLIVES:** [Georgia Tech official dataset page](https://alregib.ece.gatech.edu/olives-dataset/)
4. **OLIVES on Hugging Face:** [Dataset repository](https://huggingface.co/datasets/gOLIVES/OLIVES_Dataset)

---

**Document status:** Initial dataset research and published reference distributions documented. Exact label counts, source overlap, and class distribution of the combined Kaggle download remain to be verified.
