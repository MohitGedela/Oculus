
# Retinal Image Preprocessing Research

## 1. Goal

Our goal is to prepare retinal fundus images from EyePACS, APTOS, and Messidor for training our diabetic retinopathy classification model.

Since the images come from different datasets, they may vary in size, lighting, and image quality. We need to make them consistent while preserving important retinal details, such as blood vessels and lesions.

Before deciding what preprocessing to apply, we should check what has already been done to the images.

## 2. Existing Dataset Investigation

The combined Kaggle dataset contains images from EyePACS, APTOS, and Messidor. It is reported to contain RGB JPEG images resized to 600 × 600 pixels, with augmented images also included.

These details should be confirmed against the downloaded files before we make changes.

### What to Check

For each dataset, we should look at:

- **Image format:** Are the images JPEG, PNG, or another format?
- **Image dimensions:** Are all images the same size?
- **Color:** Are the images RGB or in another format?
- **Black borders:** Do images have large black areas around the retina?
- **Image quality:** Are some images blurry, too bright, too dark, or affected by artifacts?
- **Existing preprocessing:** Have the images already been cropped, resized, or enhanced?
- **Augmentation and duplicates:** Are there multiple versions of the same image?
- **Labels:** Does every image have the correct diabetic retinopathy label?


### Initial Findings

The combined Kaggle dataset is reported to contain images from EyePACS, APTOS, and Messidor that have already been resized to 600 × 600 pixels and converted to RGB JPEG format. The collection also reportedly includes augmented images, and an APTOS Gaussian-filtered version is listed.

These are reported properties of the combined dataset, not yet independently verified against our downloaded files.

| Property | EyePACS | APTOS | Messidor |
|---|---|---|---|
| Original image format | JPEG | JPEG | TIFF in the original release |
| Original image dimensions | Varying | Varying | Varying |
| Image quality | Varies between images | May include blur, artifacts, and uneven lighting | Varies between images |
| Combined dataset dimensions | Reportedly 600 × 600 | Reportedly 600 × 600 | Reportedly 600 × 600 |
| Combined dataset format | Reportedly RGB JPEG | Reportedly RGB JPEG | Reportedly RGB JPEG |
| Existing augmentation | Reportedly included | Reportedly included | Reportedly included |
| Additional filtering | Not confirmed | Gaussian-filtered version reportedly included | Not confirmed |
| Black border removal | Not confirmed | Not confirmed | Not confirmed |
| Pixel normalization | Not confirmed | Not confirmed | Not confirmed |

The original dataset properties may differ from those of the combined Kaggle version. We should inspect the downloaded files and their directory structure to confirm these details before implementing additional preprocessing.

## 3. Proposed Preprocessing Steps

### Step 1: Inspect and Validate the Existing Dataset

Before applying new transformations:

- Check image formats, dimensions, and color modes.
- Confirm whether images are already 600 × 600 RGB JPEGs.
- Inspect the directory structure for separate dataset versions, filtered images, and augmented images.
- Check that image labels and identifiers are preserved.
- Identify unreadable files and potential duplicates.

**Why:** The combined dataset has reportedly already undergone some preprocessing. Checking what is available first helps us avoid repeating transformations unnecessarily.

### Step 2: Load and Validate Images

- Check that each image can be opened and contains valid pixel data.
- Convert images to RGB only when required.
- Handle corrupted or unreadable files explicitly.
- Preserve the association between each image and its original label.

**Why:** This prevents invalid images from causing errors during training and helps ensure that labels remain correctly associated with their images.

### Step 3: Crop Black Borders

- Inspect images for unnecessary black borders around the retinal field.
- Crop borders only when they are present and can be identified reliably.
- Avoid cutting off retinal tissue or lesions near the edges.
- Skip cropping when no meaningful border is present.

**Why:** Removing unnecessary background can help the model focus on the retina, but aggressive cropping could remove useful information.

### Step 4: Make Images Square and Resize if Necessary

The combined dataset is reported to contain images that are already 600 × 600 pixels.

- Check the selected model's required input dimensions.
- Avoid resizing images if they already meet those requirements.
- If resizing is necessary, use a consistent interpolation method.
- Preserve the aspect ratio and pad the shorter dimension if needed rather than stretching the image.

**Why:** Images need consistent dimensions for model input, but unnecessary resizing can reduce detail.

### Step 5: Evaluate Ben Graham Preprocessing

Ben Graham preprocessing uses Gaussian filtering to estimate background illumination and adjust the image.

The combined dataset reportedly includes a Gaussian-filtered APTOS version. However, this does not establish that every image has undergone Ben Graham preprocessing or that the existing filtering is equivalent to the exact method we might implement.

- Inspect the existing filtered images before applying additional correction.
- Keep Ben Graham preprocessing optional initially.
- Compare original and corrected images visually.
- If possible, compare model performance with and without the correction using the same data splits and training setup.

**Why:** We should avoid applying the same type of correction twice without a reason. Additional preprocessing should be retained only if it provides a benefit.

### Step 6: Normalize Pixel Values

Check the selected model's input requirements before normalizing images.

- Scaling divides pixel values by 255 to convert them from `[0, 255]` to `[0, 1]`.
- Channel-wise normalization subtracts a mean and divides by a standard deviation for each RGB channel.
- For models pretrained on ImageNet, commonly used RGB means are `[0.485, 0.456, 0.406]` and standard deviations are `[0.229, 0.224, 0.225]`.

**Recommendation:** Apply the normalization expected by the selected model. The reported RGB JPEG format does not tell us whether pixel normalization has already been applied during dataset preparation or training.

## 4. Recommended Processing Order

1. Inspect the dataset structure and existing preprocessing.
2. Load each image and validate its contents.
3. Convert to RGB if required.
4. Crop unnecessary black borders only when present.
5. Preserve the aspect ratio and pad if necessary.
6. Resize only if required by the model.
7. Apply the appropriate normalization.
8. Validate the output and preserve image-to-label mappings.

Ben Graham preprocessing should be evaluated separately. If the dataset already contains filtered versions, compare those with the original images before applying another correction.

## 5. Visual Inspection

Inspect at least 20 images from each source dataset before and after preprocessing.

Include images with different quality levels and disease grades where available.

Check for:

- Retinal tissue removed during cropping.
- Distortion from resizing.
- Loss of fine detail.
- Unexpected brightness, contrast, or color changes.
- Remaining black borders or other artifacts.
- Differences between original, augmented, and Gaussian-filtered versions.

**Why:** Automated tests can check dimensions and pixel values, but visual inspection helps identify problems that those tests might miss.

## 6. Data Integrity

- Preserve image identifiers and labels throughout preprocessing.
- Check for duplicate images and existing augmented copies.
- Determine whether augmented images can be linked to their original images.
- Split the data before applying any new augmentation.
- Keep related images, including augmented versions of the same original, in the same split.
- If patient identifiers are available, keep images from the same patient in the same split.
- Calculate dataset-specific normalization statistics using training data only, if needed.

**Why:** Related images appearing across training, validation, and test sets can make model performance look better than it really is. Since augmentation is reportedly already present in the combined dataset, checking for this is particularly important.

## 8. Final Recommendations

Start by inspecting the downloaded dataset rather than assuming all images need to be processed from scratch.

1. Confirm the reported 600 × 600 dimensions and RGB JPEG format.
2. Identify existing augmented and Gaussian-filtered images.
3. Validate image contents and preserve labels.
4. Crop black borders only when necessary.
5. Resize only if required by the selected model.
6. Apply the correct normalization.
7. Check for duplicates and related images before splitting the data.

Treat Ben Graham preprocessing as an optional experiment, especially if Gaussian-filtered images are already included.

The goal is to make images consistent without unnecessarily repeating existing preprocessing or losing details that could be important for diabetic retinopathy classification.
