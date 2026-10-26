# RetinaSense: Tools and Technologies

Scope: binary classification of referable diabetic retinopathy (grades 2 to 4 vs. 0 to 1), with a baseline CNN.

## 1. Data acquisition and exploration

- **Kaggle:** hosts the APTOS 2019 dataset and provides notebooks with the data attached
- **pandas:** loads the label CSV, checks grade counts, and creates the binary label
- **matplotlib:** plots grade distributions and sample fundus images

## 2. Preprocessing

- **OpenCV (cv2):** resizing, cropping black borders, and Ben Graham's local-contrast normalization
- **torchvision.transforms:** resizing, normalization, and training-time augmentation (flips, small rotations)
- **Pillow (PIL):** image loading

## 3. Modeling

- **PyTorch:** defines BaselineCNN and the training loop
- **torch.utils.data (Dataset and DataLoader):** batching and shuffling
- **BCEWithLogitsLoss with pos_weight:** binary loss that handles class imbalance
- **Adam or AdamW:** optimizer
- **torchvision pretrained ResNet (later):** transfer-learning comparison model

## 4. Evaluation

- **scikit-learn:** sensitivity, specificity, precision, F1, ROC-AUC, confusion matrix, and stratified splits
- **NumPy:** threshold sweep on the validation set

## 5. Experiment tracking and reproducibility

- **YAML or Python config file:** paths, image size, batch size, learning rate, and random seeds
- **CSV log:** records each run's config and metrics (Weights & Biases or MLflow if the team wants a dashboard)
- **torch.save:** model checkpoints

## 6. Team collaboration and code management

- **GitHub:** shared code, with data excluded from the repo
- **Google Drive or a shared Kaggle dataset:** shared data access
- **Kaggle or Google Colab:** free GPU runs for training

## 7. Reporting
- **Kaggle or Jupyter notebooks:** experiment outputs and figures
- **matplotlib or seaborn:** loss curves, ROC curves, and confusion matrices for the report
