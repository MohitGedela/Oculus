
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

## 📊 Evaluation Protocol

Every run follows the same rules so results can be compared.

1. **Splits:** train, val and test come from the manifest. Val drives early stopping and the threshold. Test is used once, at the end.
2. **Early stopping:** the best checkpoint by validation AUROC is saved. Training stops after 5 epochs with no improvement. A high epoch cap is only a safety limit, not the stopping rule.
3. **Threshold:** score all validation images and scan cutoffs from 0.000 to 1.000 in steps of 0.001. Take the highest cutoff whose validation sensitivity is at least 0.90, and freeze it in a JSON file.
4. **Test, run once:** apply the frozen threshold. Report sensitivity, specificity, precision, F1, AUROC, PR-AUC and the confusion matrix.
5. **Confidence intervals:** 1,000 bootstrap resamples that resample whole patient groups, with 95% percentile intervals.
6. **Breakdowns:** by source (EyePACS vs APTOS) and sensitivity by severity grade.
7. **Graphs:** training curves, validation and test ROC, precision-recall, confusion matrix, performance by source and grade, confidence intervals, and a false-negative gallery.
8. **Settings:** images resized to a fixed size and normalized with ImageNet mean and std, no augmentation by default, seed 42.

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
