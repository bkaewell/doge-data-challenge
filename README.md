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
doge-data-challenge/                                # Root directory for the DOGE data challenge
    ├── <ARCHIVE_DIR>/                              # 🚫 Stores metadata (.gitignored)
    ├── <DATA_DIR>/                                 # 🚫 Stores downloaded regulation XMLs (.gitignored)
        ├── regulations_xml/
            ├── <SNAPSHOT_DATE>/                    # Example snapshot path for each unique date
    ├── notebooks/                                  # Data pipeline notebooks
        ├── 01_agency_mapping_and_flatening.ipynb   # Flatten agency JSON to dataframe
        ├── 02_data_download_and_storage.ipynb      # Download and cache XMLs
        ├── 03_text_extraction_and_analysis.ipynb   # Extract, parse, and analyze text
        ├── 04_visualization_and_reporting.ipynb    # Metrics + charts + reporting
        └── utils/
            ├── paths.py                            # Loads .env and builds file paths
            └── print_helpers.py                    # Shortens paths, nice output
            └── trim_notebook_outputs.py            # Optional: limit notebook output cell size for Git
            └── wordcount.py                        # Word counting strategies 
    ├── .env.example                                # Template for local env config
    ├── .gitignore                                  # Prevents .env, data, checkpoints from being tracked
    ├── bootstrap.py                                # Sets up directory structure and config
    ├── README.md                                   # Documentation (this file)  
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