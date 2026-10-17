# Datasets for RetinaSense

## 1. Our current source

**Eyepacs, Aptos, Messidor Diabetic Retinopathy** (Kaggle)
https://www.kaggle.com/datasets/ascanipek/eyepacs-aptos-messidor-diabetic-retinopathy

About Dataset:
- A unified set of the EyePACS, APTOS 2019, APTOS (Gaussian Filtered) and Messidor diabetic retinopathy datasets.
- Original: 92,501 JPG files, combined and randomly split into train (80%), validation (10%) and test (10%).
- Update, January 5, 2024: manual data augmentation added about 55% more images, and all images were resized to 600x600. Disk size dropped from 18.5 GB to 3.8 GB.
- After augmentation the split stayed 80:10:10 and the total is 143,669 images.

Original sources:
1. EyePACS (Kaggle Diabetic Retinopathy Detection): https://www.kaggle.com/competitions/diabetic-retinopathy-detection
2. APTOS 2019 Blindness Detection: https://www.kaggle.com/competitions/aptos2019-blindness-detection
3. APTOS Gaussian Filtered (derived from APTOS 2019): https://www.kaggle.com/datasets/sovitrath/diabetic-retinopathy-224x224-gaussian-filtered
4. Messidor: https://www.adcis.net/en/third-party/messidor/
   - Required acknowledgement: "Kindly provided by the Messidor program partners."
   - Citation: Decencière, E., et al. (2014). Feedback on a publicly distributed database: the Messidor database. Image Analysis & Stereology, 33(3), 231-234. https://doi.org/10.5566/ias.1155

Things to watch in this set:
- The split is random, not by patient or by source, and augmented copies exist. Near-duplicates can land in different splits (leakage). Split again yourself or evaluate on originals only.
- The images come from several sources, so a model can learn camera style instead of disease.

## 2. Additional data sources

Use these as external test sets (never mix them into training and testing together). Hash-check each against our Kaggle set first, since it already contains EyePACS, APTOS and Messidor images.

| Dataset | What it is | Size | Where to find it | Access |
|---|---|---|---|---|
| IDRiD | Indian clinic fundus photos with DR and macular edema grades, plus lesion masks | 516 graded + 81 with masks | [IEEE DataPort](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid) | Free IEEE account |
| DDR | Chinese hospital images, grades 0-4 plus a class 5 for ungradable | 13,673 images | [GitHub](https://github.com/nkicsl/DDR-dataset), also community copies on [Hugging Face](https://huggingface.co/datasets/ctmedtech/DDR-dataset) | Open download; CC BY-NC-SA 4.0 |
| Messidor-2 | French images, 1,748 images from 874 exams; official set has no DR labels | 1,748 images | [ADCIS](https://www.adcis.net/en/third-party/messidor2/) | Request form, emailed link; research only |
| BRSET | Brazilian tabletop camera images with ICDR grades, image quality and patient info | 16,266 images, 8,524 patients | [PhysioNet](https://physionet.org/content/brazilian-ophthalmological/) | Credentialed (CITI course + data use agreement) |
| mBRSET | Brazilian handheld smartphone camera images, ICDR grades, referable flag | 5,164 images, 1,291 patients | [PhysioNet](https://physionet.org/content/mbrset/1.0/) | Credentialed, same as BRSET |
| DeepDRiD | Regular and ultra-widefield images with DR grade and quality labels | 2,000 regular + 256 widefield | [GitHub](https://github.com/deepdrdoc/DeepDRiD) | Open download; licence not confirmed |
| FGADR | Images with pixel-level lesion masks and expert grades | 2,842 images | [Paper](https://arxiv.org/abs/2008.09772) | Access not confirmed |
| EyePACS (original) | The full Kaggle competition set. Useful for original filenames and patient-level splits | 88,702 images | [Kaggle](https://www.kaggle.com/competitions/diabetic-retinopathy-detection); a community copy is on [Hugging Face](https://huggingface.co/datasets/ctmedtech/EYEPACS) | Accept competition rules on Kaggle |
| APTOS 2019 (original) | Aravind clinic images from India, grades 0-4 | 3,662 labeled | [Kaggle](https://www.kaggle.com/competitions/aptos2019-blindness-detection) | Accept competition rules |
| DRTiD | Two-field images per eye | 3,100 images | [GitHub](https://github.com/FDU-VTS/DRTiD) | Email application + signed EULA |

Notes:
- I found Hugging Face copies of DDR and EyePACS under the account `ctmedtech`. These are community uploads, not the official source, so check the licence on the page and compare against the official one before relying on them.
- I did not find confirmed Kaggle copies of IDRiD or Messidor-2. If you search Kaggle and find one, treat it as a third-party re-upload and check its terms.
- Kaggle competition data (EyePACS, APTOS) cannot be redistributed. Do not put images on GitHub.

## 3. Quick picks for the project

- **External test set:** IDRiD (small, clean), DDR (large, different country), BRSET.
- **Low-resource camera test:** mBRSET (handheld phone camera).
- **Patient-level splits and subgroup checks:** BRSET and mBRSET (patient ID, age, sex).
- **Image-quality filtering:** DDR class 5, plus the quality columns in BRSET, mBRSET and DeepDRiD.
- **Start now:** PhysioNet credentialing takes time.

Label scales differ between datasets (for example Messidor-1 uses 0-3). Check each scheme before mapping to referable DR (grade 2 or higher).

## Sources

- Kaggle dataset: https://www.kaggle.com/datasets/ascanipek/eyepacs-aptos-messidor-diabetic-retinopathy
- IDRiD: https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid
- DDR: https://github.com/nkicsl/DDR-dataset and https://huggingface.co/datasets/ctmedtech/DDR-dataset
- Messidor-2: https://www.adcis.net/en/third-party/messidor2/
- BRSET: https://physionet.org/content/brazilian-ophthalmological/
- mBRSET: https://physionet.org/content/mbrset/1.0/
- DeepDRiD: https://github.com/deepdrdoc/DeepDRiD
- FGADR: https://arxiv.org/abs/2008.09772
- EyePACS: https://www.kaggle.com/competitions/diabetic-retinopathy-detection and https://huggingface.co/datasets/ctmedtech/EYEPACS
- APTOS 2019: https://www.kaggle.com/competitions/aptos2019-blindness-detection
- DRTiD: https://github.com/FDU-VTS/DRTiD
