"""Simple educational diabetes-dataset statistics project.

Direct imports are limited to pandas, matplotlib, statistics, datetime and csv.
This program describes a sample dataset; it does not predict or diagnose diabetes.
"""

import csv
from datetime import datetime
from statistics import mean, median, stdev

import pandas as pd
import matplotlib.pyplot as plt


DATA_FILE = "data/diabetes_sample.csv"
REPORT_FILE = "reports/summary_report.csv"
CHART_CLASS_FILE = "reports/class_distribution.png"
CHART_FEATURE_FILE = "reports/feature_histograms.png"

FEATURE_COLUMNS = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
]
TARGET_COLUMN = "Outcome"
NUMERIC_COLUMNS = FEATURE_COLUMNS + [TARGET_COLUMN]
GROUP_COLUMNS = ["Glucose", "BMI", "Age"]
HISTOGRAM_COLUMNS = ["Glucose", "BMI", "Age"]


def load_data(file_name=DATA_FILE):
    """Read the CSV file and check that it has the expected columns and values."""
    data = pd.read_csv(file_name)

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]
    missing_columns = [name for name in required_columns if name not in data.columns]
    if missing_columns:
        raise ValueError("Missing CSV columns: " + ", ".join(missing_columns))

    # Convert columns to numbers. Invalid or blank feature values become missing.
    for column in NUMERIC_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # The class column must be present and contain only 0 or 1.
    if data[TARGET_COLUMN].isna().any():
        raise ValueError("The Outcome column has a blank or non-numeric value.")
    if not data[TARGET_COLUMN].isin([0, 1]).all():
        raise ValueError("Outcome must contain only 0 or 1.")

    data[TARGET_COLUMN] = data[TARGET_COLUMN].astype(int)
    if data.empty:
        raise ValueError("The CSV file has no data rows.")

    return data


def show_overview(data):
    """Display the dataset size, columns, missing values and class counts."""
    print("\n========== DATASET OVERVIEW ==========")
    print("Number of records:", len(data))
    print("Number of input columns:", len(FEATURE_COLUMNS))
    print("Duplicate rows:", int(data.duplicated().sum()))

    print("\nMissing values by column:")
    print(data[NUMERIC_COLUMNS].isna().sum().to_string())

    print("\nClass counts (Outcome):")
    print(data[TARGET_COLUMN].value_counts().sort_index().to_string())
    print("\nNote: 0 and 1 are dataset labels, not a medical conclusion.")


def calculate_statistics(values):
    """Return count, mean, median and sample standard deviation for values."""
    clean_values = [float(value) for value in values if pd.notna(value)]
    if not clean_values:
        return 0, None, None, None

    average = mean(clean_values)
    middle = median(clean_values)
    spread = stdev(clean_values) if len(clean_values) > 1 else 0.0
    return len(clean_values), average, middle, spread


def show_statistics(data):
    """Use the statistics library to summarize every numeric column."""
    print("\n========== SUMMARY STATISTICS ==========")
    print(f"{'Column':30} {'Count':>7} {'Mean':>12} {'Median':>12} {'Std dev':>12}")
    print("-" * 76)

    for column in NUMERIC_COLUMNS:
        count, average, middle, spread = calculate_statistics(data[column].tolist())
        if count == 0:
            print(f"{column:30} {count:>7} {'n/a':>12} {'n/a':>12} {'n/a':>12}")
        else:
            print(
                f"{column:30} {count:>7} {average:>12.2f} "
                f"{middle:>12.2f} {spread:>12.2f}"
            )

    print("\nMean = average; median = middle value; standard deviation = spread of values.")


def show_group_comparison(data):
    """Compare selected column averages across the dataset's two class labels."""
    print("\n========== AVERAGES BY DATASET CLASS ==========")
    grouped = data.groupby(TARGET_COLUMN)[GROUP_COLUMNS].mean().round(2)
    print(grouped.to_string())
    print("\nThis is a description of this sample only; it does not show cause or diagnosis.")


def create_graphs(data):
    """Create and save a class-count chart and three feature histograms."""
    class_counts = data[TARGET_COLUMN].value_counts().sort_index()

    plt.figure(figsize=(7, 4))
    plt.bar([str(value) for value in class_counts.index], class_counts.values)
    plt.title("Number of Records in Each Dataset Class")
    plt.xlabel("Outcome label (0 or 1)")
    plt.ylabel("Number of records")
    plt.tight_layout()
    plt.savefig(CHART_CLASS_FILE, dpi=150)
    plt.close()

    figure, axes = plt.subplots(1, 3, figsize=(12, 4))
    for axis, column in zip(axes, HISTOGRAM_COLUMNS):
        values = data[column].dropna().tolist()
        axis.hist(values, bins=8, edgecolor="black")
        axis.set_title(column)
        axis.set_xlabel("Value")
        axis.set_ylabel("Frequency")

    figure.suptitle("Sample Dataset: Feature Distributions")
    figure.tight_layout()
    figure.savefig(CHART_FEATURE_FILE, dpi=150)
    plt.close(figure)

    print("\nGraphs saved successfully:")
    print("-", CHART_CLASS_FILE)
    print("-", CHART_FEATURE_FILE)
    print("Open these PNG files from the reports folder to view them.")


def export_report(data):
    """Write a compact statistics report using Python's csv and datetime modules."""
    generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(REPORT_FILE, "w", newline="", encoding="utf-8") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["Diabetes Dataset Statistics Report"])
        writer.writerow(["Generated at", generated_time])
        writer.writerow([])
        writer.writerow(["Column", "Count", "Mean", "Median", "Standard Deviation"])

        for column in NUMERIC_COLUMNS:
            count, average, middle, spread = calculate_statistics(data[column].tolist())
            writer.writerow([
                column,
                count,
                "" if average is None else round(average, 2),
                "" if middle is None else round(middle, 2),
                "" if spread is None else round(spread, 2),
            ])

        writer.writerow([])
        writer.writerow(["Dataset class", "Record count"])
        for label, count in data[TARGET_COLUMN].value_counts().sort_index().items():
            writer.writerow([int(label), int(count)])

    print("\nReport exported successfully:", REPORT_FILE)
    print("Generated at:", generated_time)


def show_menu():
    """Print the main terminal menu."""
    print("\n========================================")
    print("     DIABETES DATASET STATISTICS")
    print("========================================")
    print("1. Show dataset overview")
    print("2. Show statistical summary")
    print("3. Compare averages by dataset class")
    print("4. Create graphs")
    print("5. Export summary to CSV")
    print("0. Exit")
    print("========================================")


def main():
    """Load the sample CSV and run the terminal menu."""
    print("Starting Diabetes Dataset Statistics Project...")
    print("Educational data analysis only - not a medical diagnostic tool.\n")

    try:
        data = load_data()
    except FileNotFoundError:
        print("Dataset file not found:", DATA_FILE)
        print("Run this program from the main project folder.")
        return
    except (ValueError, pd.errors.ParserError) as error:
        print("Could not load the CSV:", error)
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_overview(data)
        elif choice == "2":
            show_statistics(data)
        elif choice == "3":
            show_group_comparison(data)
        elif choice == "4":
            create_graphs(data)
        elif choice == "5":
            export_report(data)
        elif choice == "0":
            print("Thank you for using the project. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 0, 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()
