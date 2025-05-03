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

## Overview
The DOGE Data Challenge processes regulation XML snapshots to map agencies, extract text, and produce analytical reports. Key features include:

- **Dynamic Configuration:** Paths and settings are managed via a .env file, with defaults set by bootstrap.py
- **Modular Utilities:** Helper functions (i.e., path management, text processing) are packaged with **Poetry** for reusability
- **Notebook Pipeline:** Several **Jupyter** notebooks handle data ingestion, processing, analysis, and visualization
- **Testing:** Unit tests ensure reliability of core utilities

---

## ⚡ Quick Setup
### 1️⃣ Install Poetry:
```bash
pip install poetry
```
Manual Path Setup: If ~/.local/bin isn’t in your PATH, you may need to add it manually (e.g., export PATH="$HOME/.local/bin:$PATH")

### 2️⃣ Clone the repository:
```bash
git clone https://github.com/bkaewell/doge-data-challenge.git
cd doge-data-challenge
```

### 3️⃣ Install dependencies:
```bash
poetry install
```
Verify pyproject.toml is up to date with all dependencies (pandas, matplotlib, etc.);
poetry add python-dotenv jupyter
This doge-data-challenge project uses Poetry to manage dependencies and package doge_data_challenge/helpers/

### 4️⃣ Bootstrap project:
```bash
poetry run python bootstrap.py
```
This creates a .env file with default values if none exists.

### 5️⃣ Run notebooks:
```bash
poetry run jupyter-notebook
```

---

## Usage
- Configure .env (copy .env.example and edit) to set SNAPSHOT_DATE, ARCHIVE_DIR, etc.
- Run notebooks in order (01_agency_mapping_and_flattening.ipynb to 04_visualization_and_reporting.ipynb).
- Each notebook uses init_notebook() to load paths:
```python
from doge_data_challenge.helpers import init_notebook
paths = init_notebook()
```

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
├── README.md               # Documentation (this file)
├── bootstrap.py            # Sets up .env with default values
├── doge_data_challenge/
│   ├── __init__.py         # Marks doge_data_challenge as a Poetry Python package
│   └── helpers/            # Reusable utility functions
│       ├── __init__.py                # Exposes helper functions for import
│       ├── env_paths.py               # Loads .env and defines project paths
│       ├── init_notebook.py           # Initializes notebooks with sys.path and paths
│       ├── print_helpers.py           # Formats and prints directory status messages
│       ├── trim_notebook_outputs.py   # Limits notebook output size for Git
│       └── wordcount.py               # Implements word counting strategies
├── notebooks/                                  # Data pipeline notebooks
│   ├── 01_agency_scraper.ipynb                 # Scrapes, maps, and flattens agency JSON to a dataframe
│   ├── 02_data_download_and_storage.ipynb      # Downloads and caches XMLs
│   ├── 03_text_extraction_and_analysis.ipynb   # Extracts and analyzes text
│   └── 04_visualization_and_reporting.ipynb    # Generates metrics and charts
├── tests/                                      # Unit tests for reliability
│   ├── __init__.py
│   └── test_env_paths.py            # Tests path loading and directory creation
├── .env                             # Configuration file
├── .gitignore                       # Ignores .env, data, checkpoints, and cache files
├── poetry.lock                      # Locks dependency versions (Git-ignored)
├── pyproject.toml                   # Poetry configuration and dependencies
│
│                                    # Below is Git-ignored to keep repo lightweight
│                                    ###############################################
├── {AGENCY_METADATA_DIR}/           # Stores metadata
│   └── {SNAPSHOT_DATE}/             
│       ├── agencies.json            # Top-level JSON from API
│       └── flattened_agencies.csv   # Output from 01_agency_scraper
│   ...
└── {REGULATION_TEXT_DIR}/           # Regulation XMLs from API
│   └── {SNAPSHOT_DATE}/             
│   ...                              # Output from 02_data_download_and_storage 
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

## **BACKUP**

## 📌 Key Deliverables

- Download and parse regulation text from the eCFR API
- Compute word counts, track changes over time (i.e. 2020 → 2025), and generate SHA-256 checksums per agency
- Normalize nested agency structures (including children) for accurate aggregation
- Introduce a custom metric: **regulatory density** = words per CFR reference
- Visualize agency sizes and regulation growth
- Build a modular pipeline for future extension (i.e. NLP-based analysis)

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

Context: The project involves scraping agency metadata and regulation texts, organized by SNAPSHOT_DATE. The .env file defines AGENCY_METADATA_DIR and REGULATION_TEXT_DIR, and users may extend it for snapshot-specific configurations




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