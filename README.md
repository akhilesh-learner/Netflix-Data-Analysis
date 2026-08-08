# Netflix Data Analysis

An interactive Streamlit dashboard and exploratory analysis of Netflix movies and TV shows using the Netflix titles dataset.

## Project Overview

This repository contains a data analysis project that explores Netflix content metadata and provides an interactive dashboard for visualizing trends in titles, genres, release years, and producing countries.

## What’s Included

- `app.py` — Streamlit app for interactive analysis and visualization
- `notebooks/netflix_analysis.ipynb` — exploratory data analysis notebook with data cleaning, quality checks, and charts
- `data/netflix_titles.csv` — Netflix titles dataset used by the dashboard and notebook
- `requirements.txt` — Python dependencies for the project

## Features

- Filter Netflix content by type and release year
- Display KPIs for total titles, movies, and TV shows
- Visualize the distribution of movies vs TV shows
- Plot Netflix content added over time
- Show top producing countries
- Present most popular genres

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd Netflix-Data-Analysis
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal to interact with the app.

## Notebook

The notebook at `notebooks/netflix_analysis.ipynb` contains detailed analysis steps, including:

- data inspection and summary statistics
- missing value analysis
- data cleaning and transformation
- visual exploration with Matplotlib and Seaborn

## Dataset

The dataset file `data/netflix_titles.csv` contains Netflix titles metadata used by both the notebook and dashboard.

## Folder Structure

```
Netflix-Data-Analysis/
├── app.py
├── data/
│   └── netflix_titles.csv
├── notebooks/
│   └── netflix_analysis.ipynb
├── requirements.txt
└── README.md
```

## Notes

- The Streamlit app uses `pandas`, `matplotlib`, `seaborn`, and `streamlit`.
- If you want a smaller dependency set for just the dashboard, you may only need `streamlit`, `pandas`, `matplotlib`, and `seaborn`.
