# Reddit Israel-Palestine Analysis

## Overview
Data science analysis of Reddit discussions on Israel-Palestine conflict using daily updated dataset from Kaggle.

## Setup Instructions

### Option 1: Using Poetry (Recommended)
```bash
poetry install
poetry run jupyter notebook
```

### Option 2: Using pip
```bash
pip install -r requirements.txt
jupyter notebook
```

## Dataset
- **Source:** [Kaggle - Reddit Israel-Palestine Daily Updated](https://www.kaggle.com/datasets/asaniczka/reddit-on-israel-palestine-daily-updated)
- **Size:** ~1.15GB
- **Format:** CSV files
- **Update Frequency:** Daily

## Project Structure
```
├── notebook.ipynb          # Main analysis notebook
├── data/                   # Dataset files (created when running notebook)
├── pyproject.toml          # Poetry dependencies
├── requirements.txt        # Pip dependencies
└── README.md              # This file
```

## Usage
1. Install dependencies (see Setup Instructions above)
2. Open `notebook.ipynb`
3. Run all cells - the notebook will automatically download the dataset
4. The dataset will be saved to `data/reddit-israel-palestine/` folder

## Notes
- First run requires internet connection to download dataset
- Subsequent runs can work offline
- Dataset download may take a few minutes depending on connection speed

