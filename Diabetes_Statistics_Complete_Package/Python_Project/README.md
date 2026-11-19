# Diabetes Dataset Statistics Project

A simple terminal program that reads a CSV file, calculates statistics and creates graphs.

**This is an educational data-analysis project only. It does not predict, diagnose or assess diabetes.** The included CSV rows are fictional examples made for practising Python. They are not real patient records or a clinical dataset.

## 1. What the program does

1. Reads `data/diabetes_sample.csv`.
2. Checks that the required columns are present.
3. Shows the number of records, missing values and class counts.
4. Calculates count, mean, median and standard deviation.
5. Compares selected averages for dataset labels 0 and 1.
6. Creates graphs using Matplotlib.
7. Exports a statistics report to a new CSV file.

There is no machine learning in this simplified version.

## 2. Libraries used

The program directly uses only these libraries:

| Library | Use |
|---|---|
| `pandas` | Read, organize, clean and summarize CSV data |
| `matplotlib` | Create and save graphs |
| `statistics` | Calculate mean, median and standard deviation |
| `datetime` | Add the report's date and time |
| `csv` | Write the summary report as a CSV file |

`pandas` and `matplotlib` are installed with pip. `statistics`, `datetime` and `csv` are included with Python, so they do not need separate installation. Pandas may install supporting packages automatically; this project does not import them directly.

## 3. Folder structure

```text
Diabetes_Statistics_Project/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── diabetes_sample.csv
│
├── examples/
│   └── diabetes_sample.csv
│
└── reports/
    └── (graphs and report are saved here)
```

Run the program from the main project folder so the relative file paths work.

## 4. Install Python

Install Python 3.10 or newer. During Windows installation, select **Add Python to PATH**.

Check Python in PowerShell:

```powershell
py --version
```

## 5. Open the project folder

1. Extract the project ZIP file.
2. Open the extracted `diabetes_statistics_project` folder.
3. Click the File Explorer address bar.
4. Type `powershell` and press Enter.

## 6. Create a virtual environment (recommended)

```powershell
py -3 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## 7. Install the two packages

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The requirements file contains only `pandas` and `matplotlib`. Do not run `pip install statistics`, `pip install datetime` or `pip install csv`; those three modules already come with Python.

## 8. Run the program

```powershell
python main.py
```

## 9. Use the terminal menu

```text
1. Show dataset overview
2. Show statistical summary
3. Compare averages by dataset class
4. Create graphs
5. Export summary to CSV
0. Exit
```

Suggested order:

1. Enter `1` to inspect the CSV.
2. Enter `2` to calculate statistics.
3. Enter `3` to compare averages between the two dataset labels.
4. Enter `4` to create graphs.
5. Enter `5` to export the report.
6. Enter `0` to exit.

## 10. CSV file format

The CSV file must have these column headings:

```csv
Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
```

`Outcome` must contain `0` or `1`. All other columns should contain numbers. Blank or non-numeric feature values are treated as missing values for calculations. The small included file contains fictional sample rows only; it is there to make the program run immediately.

To use another compatible CSV, make a backup of the sample file and replace `data/diabetes_sample.csv` with your file. Keep the required column names.

## 11. What each part of the code does

- `load_data()` reads the CSV with Pandas and checks its columns.
- `show_overview()` displays rows, duplicates, missing values and class counts.
- `calculate_statistics()` uses Python's `statistics` module to calculate count, mean, median and standard deviation.
- `show_statistics()` displays the statistical summary for each numeric column.
- `show_group_comparison()` uses Pandas `groupby()` to compare selected averages by dataset label.
- `create_graphs()` uses Matplotlib to save a bar chart and histograms.
- `export_report()` uses `datetime` to timestamp the report and `csv.writer` to save it.
- `main()` displays the menu and calls the selected function.

## 12. Output files

After choosing menu option `4`, these graphs are created:

```text
reports/class_distribution.png
reports/feature_histograms.png
```

After choosing menu option `5`, this report is created:

```text
reports/summary_report.csv
```

## 13. Useful commands

| Task | Command |
|---|---|
| Check Python | `py --version` |
| Create environment | `py -3 -m venv .venv` |
| Activate environment | `.\.venv\Scripts\Activate.ps1` |
| Install packages | `pip install -r requirements.txt` |
| Run program | `python main.py` |
| Leave environment | `deactivate` |

## 14. Important note

The two dataset labels are used only to demonstrate CSV grouping and charting. Summary differences do not prove cause, risk or medical status. Do not use this program for diagnosis or treatment decisions, and do not enter real personal health information.
