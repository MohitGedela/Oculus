
# Oculus 🩺

**AI-Assisted Diabetic Retinopathy Screening Through Computer Vision**

Oculus (project name RetinaSense) is a machine learning research project that screens retinal fundus photos for referable diabetic retinopathy (DR). A photo goes through a quality check, preprocessing, and a classifier that answers one binary question: does this eye show referable DR? Flagged images go to an ophthalmologist. The model never diagnoses. It helps prioritize who gets seen.

> **Our goal:** Make preliminary retinal screening more accessible while keeping clinical decisions in the hands of qualified healthcare professionals.

Built by a team of five in the RBC Borealis "Let's SOLVE It" program, Fall 2026.

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Problem Statement](#-problem-statement)
- [Data](#-data)
- [Evaluation Protocol](#-evaluation-protocol)
- [Experiments](#-experiments)
- [Results So Far](#-results-so-far)
- [Repository Layout](#-repository-layout)
- [Team](#-team)
- [Roadmap](#-roadmap)
- [Medical Disclaimer](#-medical-disclaimer)
- [References](#-references)

---

## 🧠 About the Project

Diabetic retinopathy damages the blood vessels in the retina and can progress without symptoms, so regular screening matters. Access to specialists is uneven, particularly in rural and underserved communities. Oculus explores whether a model can do a first pass over retinal photos and flag the ones that need a specialist.

**Why sensitivity matters most.** A false negative is a missed case, which is the dangerous error. A false positive is an unnecessary referral. For that reason the decision threshold is chosen on validation data to reach 90% sensitivity, and we report specificity at that point.

## 🎯 Problem Statement

How can we develop and evaluate a computer vision pipeline that flags retinal fundus images showing referable diabetic retinopathy, while accounting for image quality, class imbalance, false negatives, and generalization across data sources?

## 🗂️ Data

All images come from **APTOS 2019** and **EyePACS**. They were preprocessed by one shared notebook: crop the black border, pad to square, resize to 512x512, save as JPEG (quality 95). Two variants exist:

| Variant | Folder | Description |
|---|---|---|
| Normalized | `processed` | Cropped, padded, resized. |
| Ben Graham | `processed_bg` | The same, plus Ben Graham lighting correction (4 x image minus 4 x Gaussian blur plus 128, with the bright edge ring removed). |

A `manifest_v2.csv` lists every image with its source, patient `group_id`, severity `grade`, binary `label`, and split. Both eyes of a patient stay in the same split, and no `group_id` appears in two splits.

### Balanced dataset (used for the transfer-learning runs)

Train was balanced by removing healthy images. Val and test keep the natural class mix on purpose.

| Split | Images | Healthy | Referable | % referable |
|---|---|---|---|---|
| Train | 30,287 | 15,126 | 15,161 | 50.1 |
| Val | 6,483 | 4,892 | 1,591 | 24.5 |
| Test | 6,491 | 4,907 | 1,584 | 24.4 |

### Imbalanced dataset

The original distribution, kept for the class-imbalance experiments. Train has 62,195 images (24.4% referable), val 13,326, test 13,318. Its val and test sets are about twice the size of the balanced ones, so comparing across the two datasets changes more than one thing at once.

### Label definition

`label` is 0 or 1, but it does not simply mean grade 2 to 4. The balanced test set's 1,584 referable images include 348 grade 1 images. We still need to confirm how `label` was derived, and we report sensitivity by `grade` to make this visible.

## ⚙️ Technical Approach

### Image Preprocessing

We will investigate a consistent preprocessing strategy for retinal fundus images.

Areas to explore:
- Standardizing image dimensions and color representation.
- Comparing resizing, cropping, and retinal-region extraction.
- Preserving retinal structures and lesions that may be relevant to classification.
- Normalizing pixel values consistently.
- Applying augmentation only to training data when appropriate.

### Image quality assessment

We will investigate how to identify images that may not be suitable for reliable classification.

Areas to explore:
- Illumination and exposure.
- Blur and focus.
- Occlusion and visible retinal area.
- Image resolution and artifacts.
- Criteria for flagging uncertain or unsuitable images.

Quality thresholds will be selected and validated rather than assumed in advance.

### Class imbalance

We will inspect the original severity-grade distribution and the final binary-label distribution.

Potential approaches include:
- Class-weighted loss functions.
- Training-only oversampling.
- Carefully selected data augmentation.
- Threshold adjustment using validation data.

We will compare these approaches based on their effect on sensitivity, precision, and overall model performance.

### Model development

Initial model candidates:
1. Baseline CNN.
2. Transfer-learning model such as ResNet.

We will establish a reproducible baseline before exploring more complex architectures.

## 📊 Evaluation Strategy

We will evaluate model performance using metrics appropriate for an imbalanced screening task.

| Metric | Why it matters |
|---|---|
| Sensitivity (Recall) | Measures how many referable cases are correctly flagged. |
| Specificity | Measures how many non-referable cases are correctly identified. |
| Precision | Measures how many flagged cases are actually referable according to the reference labels. |
| F1-score | Balances precision and recall. |
| ROC-AUC | Measures ranking performance across classification thresholds. |
| Confusion matrix | Helps inspect false positives and false negatives. |

Particular attention will be paid to false negatives, since missed referable cases are an important screening concern.

We will also investigate:
- Performance across datasets and image-quality groups.
- The impact of classification thresholds.
- Generalization to data not used during training.
- Potential patient or image overlap between training and evaluation datasets.

## 🗺️ Roadmap

- [ ] **Phase 1:** Inspect datasets and finalize initial dataset roles.
- [ ] **Phase 2:** Define image quality criteria and preprocessing decisions.
- [ ] **Phase 3:** Finalize label mapping and leakage-resistant data splits.
- [ ] **Phase 4:** Train and evaluate a baseline CNN.
- [ ] **Phase 5:** Compare against a transfer-learning model.
- [ ] **Phase 6:** Analyze errors, thresholds, and generalization.
- [ ] **Phase 7:** Document findings, limitations, and future work.

## ⚕️ Medical Disclaimer

Oculus is a research prototype, not a medical diagnostic tool. It is not intended to replace professional screening, clinical judgment, or evaluation by a qualified healthcare professional. Model predictions must not be used as a substitute for medical advice.

## 📚 References

1. Roychowdhury, S. et al. (2014). *Iterative Vessel Segmentation of Fundus Images*. [Search publication](https://scholar.google.com/scholar?q=Roychowdhury+2014+diabetic+retinopathy+fundus+images)
2. Gulshan, V. et al. (2016). *Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs*. [JAMA](https://doi.org/10.1001/jama.2016.17216)
3. APTOS 2019 Blindness Detection. [Kaggle dataset](https://www.kaggle.com/competitions/aptos2019-blindness-detection)
4. EyePACS. [Official website](https://www.eyepacs.org/)
5. MESSIDOR. [Official project website](https://www.adcis.net/en/third-party/messidor/)
6. OLIVES. [Project and dataset information](https://github.com/olivesgatech/OLIVES-Dataset)

---

*Oculus | Computer Vision Research Project*
