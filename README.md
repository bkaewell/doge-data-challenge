# 🐶 DOGE Data Challenge 🚀

🏛️ A data-driven look into U.S. federal regulations using the eCFR API — exploring word counts, trends over time, and custom metrics like regulatory density to inform smarter de-regulation strategies

📜 Built to support data transparency and government-wide efficiency efforts by analyzing the Code of Federal Regulations (CFR), unleashing prosperity through de-regulation

✒️ Hamilton had his pen —— I have my keyboard... Using data to untangle the regulatory state, one agency at a time

---

## 🎯 Project Purpose

This technical assessment explores how to better understand and visualize the scale and complexity of U.S. federal regulations:

- The **eCFR** contains over **200,000 pages** of regulatory text across ~150 agencies
- The data is publicly accessible through an [official API](https://www.ecfr.gov/reader-aids/ecfr-developer-resources/rest-api-interactive-documentation)
- The goal: **build a tool to parse and analyze regulation data** for actionable insights

---

## 📌 Key Deliverables

- Download and parse regulation text from the eCFR API
- Compute word counts, track changes over time (i.e. 2020 → 2025), and generate SHA-256 checksums per agency
- Normalize nested agency structures (including children) for accurate aggregation
- Introduce a custom metric: **regulatory density** = words per CFR reference
- Visualize agency sizes and regulation growth
- Build a modular pipeline for future extension (i.e. NLP-based analysis)

---

## ⚡ Quick Setup
### 1️⃣ Clone the Repo  
```bash
git clone https://github.com/bkaewell/doge-data-challenge.git
cd doge-data-challenge
```

### 2️⃣ Bootstrap Your Environment  
```bash
python bootstrap.py
```

This will:
- ✅ Create a `.env` file if it doesn't exist
- ✅ Set the default `SNAPSHOT_DATE` to today
- ✅ Set the default `WORDCOUNT_METHOD` to `regex`
- ✅ Create the necessary data folders under `data/` and `archive/`

---

## Configuration
All configuration lives in .env. You can manually set a specific date for analysis:
```ini
SNAPSHOT_DATE=2025-03-27
WORDCOUNT_METHOD=regex  # Options: split, regex, legal, nlp

ARCHIVE_DIR=archive
DATA_DIR=data
```
  > 🔥🔥 `regex` balances speed and accuracy with NLP-style tokenization

---

## 🔢 Word Count Methods

The `WORDCOUNT_METHOD` defined in your `.env` controls how regulation text is parsed and counted. This ensures transparency and consistency across analyses — especially when comparing different agencies or dates.

| Method   | Description                                                                |
|----------|----------------------------------------------------------------------------|
| `split`  | Simple `text.split()` based on whitespace — fast but may over/under count  |
| `regex`  | Uses `\b\w+\b` to match real words — closer to Google Docs word count      |
| `legal`  | Placeholder for stricter rules (i.e. exclude citations, headers, numbers)  |
| `nlp`    | Placeholder for future spaCy/NLTK-style tokenization                       |

---

## 📂 Repository Overview  
```
doge-data-challenge/
├── README.md                   # Documentation (this file)
├── bootstrap.py                # Sets up .env and directories with default values
├── doge_data_challenge/
│   ├── __init__.py             # Marks doge_data_challenge as a Python package
│   └── helpers/                # Reusable utility functions
│       ├── __init__.py         # Exposes helper functions for import
│       ├── env_paths.py        # Loads .env and defines project paths
│       ├── init_notebook.py                    # Initializes notebooks with sys.path and paths
│       ├── print_helpers.py                    # Formats and prints directory status messages
│       ├── trim_notebook_outputs.py            # Limits notebook output size for Git
│       └── wordcount.py                        # Implements word counting strategies
├── notebooks/                                  # Data pipeline notebooks
│   ├── 01_agency_mapping_and_flattening.ipynb  # Maps agency JSON to a dataframe
│   ├── 02_data_download_and_storage.ipynb      # Downloads and caches XMLs
│   ├── 03_text_extraction_and_analysis.ipynb   # Extracts and analyzes text
│   └── 04_visualization_and_reporting.ipynb    # Generates metrics and charts
├── tests/                                      # Unit tests for reliability
│   ├── __init__.py
│   └── test_env_paths.py                       # Tests path loading and directory creation
├── .env.example                                # Template for .env configuration
├── .gitignore                                  # Ignores .env, data, checkpoints, and cache files
├── poetry.lock                                 # Locks dependency versions (git-ignored)
├── pyproject.toml                              # Poetry configuration and dependencies
├── archive/                                    # Stores metadata (git-ignored to keep repo lightweight)
└── data/                                       # Stores regulation XMLs (git-ignored to keep repo lightweight)
    └── regulations_xml/
        └── 2025-04-17/                         # Example snapshot directory
```  

---

## 📚 Additional Documentation  

TBD

---

## 🤝 Contributing & Contact    

**🎯 Looking to contribute?** Open an issue or fork the repo!  
**👨‍💻 Author:** [Brian Kaewell](https://github.com/bkaewell)  
**📧 Contact:** Please open an issue [here](https://github.com/bkaewell/doge-data-challenge/issues)

---


### Potential quick setup additions:
- bootstrap.py (at repo root) handles setting up .env (at root)
- You have your nice get_paths() helper function now that builds paths dynamically.
- Item	Location	Purpose
- .env	repo root	Single source of truth for settings
- bootstrap.py	repo root	First setup step to create .env
- helpers/env_paths.py	inside notebooks	Hide technical loading details
- notebooks	clean main workspace	only light imports, no clutter

- 🎯 Summary:
- Load .env from ROOT = two levels up if in notebooks/utils/, one level up if just notebooks/.

- Build all your major repo paths off of that ROOT.

- Your .env controls all folder names easily and portably.


### Overview
The DOGE Data Challenge processes regulation XML snapshots to map agencies, extract text, and produce analytical reports. Key features include:

- **Dynamic Configuration:** Paths and settings are managed via a .env file, with defaults set by bootstrap.py
- **Modular Utilities:** Helper functions (i.e., path management, text processing) are packaged with **Poetry** for reusability
- **Notebook Pipeline:** Several **Jupyter** notebooks handle data ingestion, processing, analysis, and visualization
- **Testing:** Unit tests ensure reliability of core utilities

### Setup
Install Poetry:
```bash
pip install poetry
```

Clone the repository:
```bash
git clone https://github.com/bkaewell/doge-data-challenge.git
cd doge-data-challenge
```

Install dependencies:
```bash
poetry install
```

Verify pyproject.toml is up to date with all dependencies (pandas, matplotlib, etc.);
poetry add python-dotenv jupyter


Bootstrap project:
```bash
poetry run python bootstrap.py
```

This creates a .env file with default values if none exists.

Run notebooks:
```bash
poetry run jupyter-notebook
```

### Usage
- Configure .env (copy .env.example and edit) to set SNAPSHOT_DATE, ARCHIVE_DIR, etc.
- Run notebooks in order (01_agency_mapping_and_flattening.ipynb to 04_visualization_and_reporting.ipynb).
- Each notebook uses init_notebook() to load paths:
```python
from doge_data_challenge.helpers import init_notebook
paths = init_notebook()
```

