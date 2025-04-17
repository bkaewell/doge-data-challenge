# doge-data-challenge
A data-driven look into U.S. federal regulations using the eCFR API — exploring word counts, trends over time, and custom metrics like regulatory density to inform de-regulation strategies


---

## 📂 Repository Overview  
```
doge-data-challenge                                  # Root directory for the DOGE data challenge
    ├── archive                                      # Stores raw API snapshots and backups before processing
    ├── data                                         # Output directory for cleaned and transformed datasets
    └── notebooks                                    # Jupyter notebooks for exploration, processing, and analysis
        ├── 01_agency_mapping_and_flatening.ipynb    # Notebook for mapping agency structure and flattening nested data
        ├── 02_<placeholder>.ipynb                   # Placeholder notebook
        ├── 03_<placeholder>.ipynb                   # Placeholder notebook
        ├── 04_<placeholder>.ipynb                   # Placeholder notebook
        └── utils
            └── trim_notebook_outputs.py
    ├── README.md                                    # Documentation (this file)  
```

```
doge-data-challenge/
    ├── .env.example                                # Template config for users
    ├── .gitignore                                  # Ignores .env, data, checkpoints, etc.
    ├── bootstrap.py                                # Bootstraps folders & environment from .env
    ├── archive/                                    # 🚫 Generated CSV/metrics — ignored by Git
    ├── data/                                       # 🚫 Downloaded XMLs — ignored by Git
    ├── notebooks/                                  # Data pipeline notebooks
        ├── 01_agency_mapping_and_flatening.ipynb   # Flatten agency JSON to dataframe
    │   ├── 02_data_download_and_storage.ipynb      # Download and cache XMLs
    │   ├── 03_text_extraction_and_analysis.ipynb   # Extract, parse, and analyze text
    │   ├── 04_visualization_and_reporting.ipynb    # Metrics + charts + reporting
        └── utils/
            ├── paths.py                            # Loads .env and builds file paths
            └── print_helpers.py                    # Shortens paths, nice output
    ├── README.md                                   # Documentation (this file)  
```  

---

