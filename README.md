# 🏛️📜 DOGE Data Challenge 🚀
- A data-driven look into U.S. federal regulations using the eCFR API — exploring word counts, trends over time, and custom metrics like regulatory density to inform de-regulation strategies
  
- Analyze and visualize the Code of Federal Regulations (CFR) to support smarter government-wide decisions on regulatory impact

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
- ✅ Create the necessary data folders under `data/` and `archive/`

---

## Configuration
All configuration lives in .env. To change analysis to a different date, simply edit the `SNAPSHOT_DATE` in `.env`:
```ini
SNAPSHOT_DATE=2025-03-27
ARCHIVE_DIR=archive
DATA_DIR=data
```

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