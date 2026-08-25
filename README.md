# PTAS Data Collection and Analysis

This repository contains data-management and analysis tools for the PTAS research project. The current workflow collects course information from the University of Edinburgh Degree Regulations and Programmes of Study (DRPS), identifies accessibility-related content, and supports quantitative and qualitative analysis.

> [!WARNING]
> This is a research codebase under active development. Scripts and data formats may change, and generated results should be reviewed before they are used in publications or reports.

## What the project does

- Crawls selected DRPS school and subject pages.
- Extracts course titles, descriptions, learning outcomes, graduate attributes, skills, and keywords.
- Searches course content using a configurable accessibility vocabulary.
- Saves structured results for analysis in CSV files.
- Provides notebook and Python helpers for summary statistics, charts, and word clouds.
- Includes source data used for comparisons with Teach Access, BCS, and University of Edinburgh Graduate Attributes.

## Repository structure

```text
ptas/
├── bin/                         # Generated reports, crawl logs, and qualitative outputs
├── data_container/              # Local datasets and crawler output (ignored by Git)
├── scripts/
│   ├── analysis/                # Analysis notebooks and visualisation helpers
│   └── data_management/         # DRPS crawler and reference-data scripts
├── setting/
│   ├── basic_functions.py       # Data-loading, aggregation, and plotting helpers
│   ├── global_dirs.py           # Project-relative input and output paths
│   └── variables_config.py      # School mappings and accessibility vocabularies
├── requirements.txt             # Python dependency file (currently incomplete)
└── README.md
```

## Getting started

### Prerequisites

- Python 3.10 or later
- JupyterLab or Jupyter Notebook for the analysis notebooks
- Network access to the DRPS website when collecting data

Clone the repository and create an isolated environment:

```bash
git clone <repository-url>
cd ptas
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

The dependency file is currently empty. Until it is populated, install the packages imported by the code directly:

```bash
python -m pip install beautifulsoup4 jupyter matplotlib numpy openai pandas python-docx requests seaborn wordcloud openpyxl
```

Run commands from the repository root because the code uses project-relative paths and imports.

## Configuration

Before collecting data, review:

- `setting/variables_config.py` for school mappings, DRPS fields, and accessibility keywords.
- `scripts/data_management/main.py` for the target academic years and crawler entry point.
- `setting/global_dirs.py` for data, report, and log locations.

Create the local output directories if they do not already exist:

```bash
mkdir -p data_container bin/mining_log
```

The semantic-mining path uses the OpenAI API. Store credentials outside source control (for example, in the ignored `.env` file or an environment variable) and ensure the crawler reads them from that secure location before running it. Never commit API keys or participant data.

## Collect DRPS data

The default entry point calls `fetch_sites()` and writes timestamped CSV files beneath `data_container/`:

```bash
python scripts/data_management/main.py
```

The available collection functions are:

- `fetch_sites()` — extracts configured DRPS fields; semantic mining is disabled in the current call.
- `fetch_sites_match_any_keywords()` — records sentences matching individual accessibility keywords.
- `fetch_sites_relevant_to_keywords()` — uses semantic mining to identify relevant content.

Select the required function in the `if __name__ == "__main__"` block of `scripts/data_management/main.py` before running the script.

Crawler logs are written to `bin/mining_log/`. Generated datasets under `data_container/` are intentionally excluded from Git.

## Run the analysis

Start Jupyter from the repository root:

```bash
jupyter lab
```

The main analysis files are:

- `scripts/analysis/initial_results.ipynb` — initial exploration and results.
- `scripts/analysis/visualise_basic_statistics.ipynb` — descriptive statistics and visualisations.
- `scripts/analysis/functions_for_visualization.py` — reusable plotting, keyword-highlighting, and word-cloud helpers.
- `setting/basic_functions.py` — helpers for loading combined DRPS datasets and calculating school-level measures.

To load a timestamped DRPS export in Python:

```python
from setting.basic_functions import load_drps_full_df

df = load_drps_full_df("data_container/<export-directory>")
```

## Data handling

- Treat interview, consent, and qualitative research materials as sensitive data.
- Keep raw and identifiable participant data in the approved institutional storage location, not in this repository.
- Check `git status` before every commit; generated CSV, Excel, HTML, log, cache, and environment files should normally remain untracked.
- Record the collection date, academic year, school selection, keyword configuration, and code revision for reproducible analysis.

## Research handover notes

The latest notes in this repository report:

- DRPS parsing scripts have been prepared.
- 43 interviews were completed, 28 were proofread, and 27 were coded.
- 37 consent forms were received.
- Focus-group materials comprise four main questions with three subquestions each.
- Research materials are stored in the approved PTAS Teams location.

These figures are a historical snapshot and should be confirmed against the project record before reuse.

## Known limitations

- `requirements.txt` does not yet pin or document dependencies.
- The crawler depends on the current DRPS HTML structure and may require updates when that structure changes.
- Configuration is currently embedded in Python modules rather than exposed through a command-line interface.
- The automated test suite has not yet been established.

## Contributing

Use a short-lived branch for changes, keep generated and sensitive data out of commits, and document any changes to the collection methodology or keyword vocabulary. Before opening a pull request, rerun the relevant notebook or script and inspect its outputs for completeness and accuracy.
