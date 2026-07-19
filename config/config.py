"""
cxr_faithfulness — config.py
Single source of truth for all pipeline settings.

PHASE 1 (current): DATASET_MODE = "kaggle15k", N_READERS = 3, CONSENSUS_RULE = 2
PHASE 2 (upgrade): DATASET_MODE = "full",       N_READERS = 5, CONSENSUS_RULE = 3
Only these 3 values change between phases. No notebook logic changes.
"""

from pathlib import Path

# ── Phase control ──────────────────────────────────────────────────────────────
DATASET_MODE   = "kaggle15k"   # "kaggle15k" | "full"
N_READERS      = 3             # 3 for Phase 1 | 5 for Phase 2
CONSENSUS_RULE = 2             # >=2 of 3 for Phase 1 | >=3 of 5 for Phase 2

# ── Models ─────────────────────────────────────────────────────────────────────
MODELS = ["densenet121", "convnextv2_tiny", "swinb_lora"]

# ── XAI parameters ─────────────────────────────────────────────────────────────
IG_STEPS     = 300
IG_BASELINE  = "zero"   # black image — represents absence of signal
LIME_SAMPLES = 1000
MIN_TEST_N   = 30       # pathologies with n < 30 flagged as exploratory

# ── Path helpers (always call with runtime GDRIVE_ROOT) ────────────────────────
def _p(root, *parts):
    return Path(root).joinpath(*parts)

def get_config_path(root):              return _p(root, "config")
def get_raw_kaggle_path(root):          return _p(root, "data", "raw", "kaggle")
def get_raw_physionet_path(root):       return _p(root, "data", "raw", "physionet")
def get_annotations_path(root):
    if DATASET_MODE == "kaggle15k":
        return _p(root, "data", "raw", "kaggle", "annotations")
    return _p(root, "data", "raw", "physionet", "annotations")
def get_processed_path(root):           return _p(root, "data", "processed")
def get_processed_images_path(root):    return _p(root, "data", "processed", "images")
def get_processed_splits_path(root):    return _p(root, "data", "processed", "splits")
def get_consensus_path(root):           return _p(root, "data", "processed", "consensus")
def get_models_path(root):              return _p(root, "models")
def get_checkpoints_path(root):         return _p(root, "models", "checkpoints")
def get_ig_maps_path(root):             return _p(root, "ig_maps")
def get_lime_maps_path(root):           return _p(root, "lime_maps")
def get_results_path(root):             return _p(root, "results")
def get_figures_path(root):             return _p(root, "figures")
def get_paper_path(root):               return _p(root, "paper")
