================================================================================
NEXUS OPTI-ML 2026: OPERATION INSIGHT
TEAM OBSIDIAN - REPRODUCIBILITY GUIDE & DOCUMENTATION
================================================================================

1. TEAM INFORMATION
-------------------
Team Name: Obsidian
Members:
  - Niraj Kushwaha
  - Vishesh Bindal
Date: October 19, 2026


2. HARDWARE & ENVIRONMENT SPECIFICATIONS
-----------------------------------------
- Operating System: Linux (x86_64)
- Python Version: 3.10+ (tested on Python 3.14 / Linux kernel 6.x)
- RAM: >= 16 GB recommended
- CPU: Multi-core x86_64 CPU (12 threads utilized via LightGBM n_jobs=-1)
- Runtime: ~4-5 minutes for complete end-to-end training and inference


3. WORKING DIRECTORY
---------------------
Run all commands directly from the root directory of the unzipped submission folder:
  Working Directory: . (Root containing README.txt, requirements.txt, code/, and model/)

Dataset Directory:
  Ensure the official dataset folder is present in the working directory:
  ./nexus-opti-ml-2026-operation-insight/
    ├── train.csv
    ├── test.csv
    ├── customers.csv
    ├── products.csv
    ├── stores.csv
    ├── calendar.csv
    └── sample_submission.csv


4. EXACT REPRODUCTION COMMANDS
-------------------------------
Step 1: Install Dependencies
  pip install -r requirements.txt

Step 2: Execute the End-to-End Pipeline
  python code/no_catboost.py

This single command executes:
  1. Data ingestion, temporal cleaning (dropping anomalous Dec 2022 records), and typo rectification (mapping 12 category typos to 32 canonical groups).
  2. Point-in-time relational merges (merge_asof backward join on customer records to avoid 2025 data leakage).
  3. Feature engineering across physical dimensions, route corridors (cust_region -> store_region), cart bracketing signals, and inter-purchase timings.
  4. Out-of-Time Empirical Bayes Log-Odds feature generation and Tower 2 linear stacker training.
  5. Tower 1 Structural LightGBM model training with native categorical splitting.
  6. Out-of-Time validation assessment on Slice 4 (Jul-Dec 2024; 351,923 rows).
  7. Multi-seed LightGBM full-dataset refit across seeds [42, 2026, 777].
  8. Model artifact serialization into model/ (LightGBM text models and Tower 2 joblib artifact).
  9. Within-order peer smoothing (alpha=0.20) and hybrid 50/50 global/monthly rank calibration.
  10. Output generation of the final submission.csv (identical to the submitted file).


5. RANDOM SEEDS USED
--------------------
- Validation / Baseline LightGBM Seed: 42
- Full Ensemble Refitting Seeds:
    Seed 1: 42
    Seed 2: 2026
    Seed 3: 777
- Feature Fraction Seed & Bagging Seed: Matched to each respective seed (42, 2026, 777)
- Logistic Regression Solver: Deterministic L-BFGS with C=0.2


6. DIRECTORY & FILE STRUCTURE
------------------------------
Obsidian.zip
├── README.txt                     # This reproduction guide
├── requirements.txt               # Pinned package versions
├── submission.csv                 # Final submitted prediction CSV
├── writeup.txt                    # Technical writeup covering all four criteria
├── declaration.txt                # Signed declaration of originality
├── code/
│   └── no_catboost.py             # Complete, self-contained training & prediction script
└── model/
    ├── lgb_model_seed_42.txt      # Serialized LightGBM Booster (Seed 42)
    ├── lgb_model_seed_2026.txt    # Serialized LightGBM Booster (Seed 2026)
    ├── lgb_model_seed_777.txt     # Serialized LightGBM Booster (Seed 777)
    └── lr_tower2.joblib           # Serialized Tower 2 Logistic Regression Model


7. EXTERNAL DATA & PRE-TRAINED MODELS
-------------------------------------
- No external data was utilized.
- No pre-trained weights were downloaded.
- All models are trained strictly from scratch using the provided competition data.
================================================================================
