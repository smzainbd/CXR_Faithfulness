# Do Deep Chest X-Ray Classifiers Explain Where They Look?

Official code for the paper published in **Intelligence-Based Medicine** (Elsevier, 2026).

[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.ibmed.2026.100431-blue)](https://doi.org/10.1016/j.ibmed.2026.100431)
[![Paper](https://img.shields.io/badge/Paper-ScienceDirect-red)](https://www.sciencedirect.com/science/article/pii/S266652122600089X)
[![GitHub](https://img.shields.io/badge/Code-GitHub-black)](https://github.com/smzainbd/CXR_Faithfulness)

**Authors:** S.M. Zain, Eram Mahamud, Md Assaduzzaman, Nafiz Fahad, Tze Hui Liew

## Overview

We benchmark localization faithfulness of three chest X-ray classifiers — **DenseNet-121**, **ConvNeXtV2-Tiny**, and **Swin-Base + LoRA** — on VinDr-CXR using Integrated Gradients (IG). The pipeline includes:

- Decoupled faithfulness metrics (precision-mass, recall at top-50% mass, AUC-mIoU)
- Null-controlled **Type B false-positive** attribution audit
- **Attentive vs. blind** false-negative categorization
- Robustness checks (LIME, Grad-CAM++, EigenCAM, weight randomization)

> **Key finding:** Saliency–box overlap on correct predictions remains modest (max precision-mass ≈ 0.15), while wrong-class false positives still concentrate IG mass above an analytic null. Plausible heatmaps should not be treated as evidence of diagnostic correctness during pre-deployment review.

## Data (not included — download separately)

This repository does **not** contain chest X-ray images or model weights.

### VinDr-CXR (Kaggle 15k subset used in the paper)

1. Download from Kaggle:  
   **https://www.kaggle.com/datasets/vinbigdata/chest-xray-abnormalities-detection**
2. Extract DICOM files under `data/raw/kaggle/` (see `config/config.py` for paths).
3. Run preprocessing notebooks `NB00.ipynb` → `NB01.ipynb`.

The full VinDr-CXR dataset is also available via [PhysioNet](https://physionet.org/content/vindr-cxr/1.0.0/) (credentialed access).

## Reproducibility artifacts included

| Artifact | Description |
|----------|-------------|
| `data/processed/splits/` | Train / val / test CSVs (multi-label stratified split, seed = 42) |
| `models/thresholds.json` | Per-pathology operating thresholds (calibrated on validation set) |
| `config/config.py` | Pipeline settings (`DATASET_MODE=kaggle15k`, 3 readers, 2-of-3 consensus) |

## Environment

```bash
pip install -r config/requirements.txt
```

Core stack: PyTorch 2.1.0, Captum 0.7.0, LIME, timm, peft, scikit-learn, pydicom.

Training was performed on Google Colab (T4 GPU) as described in the paper.

## Notebook run order

```
NB00 → NB01 → NB02 → NB03 → NB04 / NB05 → NB06 / NB06_1 → NB07–NB10 → NB_fig_tab_gen
```

| Notebook | Purpose |
|----------|---------|
| NB00 | Kaggle download & DICOM setup |
| NB01 | Image preprocessing (224×224 PNG) |
| NB02 | Model training (DenseNet, ConvNeXt, Swin+LoRA) |
| NB03 | Classification evaluation |
| NB04 | Integrated Gradients generation |
| NB05 | LIME explanations |
| NB06 / NB06_1 | Faithfulness metrics |
| NB07 | False-positive attribution audit |
| NB08–NB10 | Severity, ablation, weight randomization |
| NB_fig_tab_gen | Paper figures and tables |

## Not included (too large for GitHub)

- Trained model checkpoints (`models/checkpoints/`)
- Precomputed IG / LIME maps (`ig_maps/`, `lime_maps/`)
- Raw / processed chest X-ray images

## Citation

If you use this code or build on our benchmark, please cite:

```bibtex
@article{zain2026cxrfaithfulness,
  title   = {Do Deep Chest X-Ray Classifiers Explain Where They Look? A Multi-Architecture Faithfulness Benchmark with False-Positive Attribution Audit on {VinDr-CXR}},
  author  = {Zain, S. M. and Mahamud, Eram and Assaduzzaman, Md and Fahad, Nafiz and Liew, Tze Hui},
  journal = {Intelligence-Based Medicine},
  number  = {100431},
  year    = {2026},
  publisher = {Elsevier},
  doi     = {10.1016/j.ibmed.2026.100431},
  url     = {https://doi.org/10.1016/j.ibmed.2026.100431}
}
```

## License

- **Code** in this repository: [MIT License](LICENSE)
- **Paper**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (Elsevier open access)
