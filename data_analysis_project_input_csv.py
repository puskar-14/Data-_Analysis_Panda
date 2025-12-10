
# PROJECT: Data Analysis using Pandas & Matplotlib
# TASKS (with user-provided CSV):
# 1) Load CSV given by user
# 2) Perform basic analysis
# 3) Create bar chart, scatter plot, and heatmap
# 4) Display insights


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Load CSV provided by user

def load_user_csv():
    print("Enter the CSV file path (Example: sales.csv): ")
    path = input("CSV File: ").strip()

    try:
        df = pd.read_csv(path)
        print("\nCSV loaded successfully!")
        return df
    except Exception as e:
        print("\nError loading CSV:", e)
        exit()


# STEP 2: Perform basic analysis

def analyze_data(df):
    print("\n--- BASIC INFO ---")
    print(df.info())

    print("\n--- SUMMARY STATISTICS ---")
    print(df.describe())

    # Ensure required columns exist
    required = ["Category", "Region", "Units_Sold", "Unit_Price"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Compute revenue
    df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

    print("\n--- TOTAL REVENUE BY CATEGORY ---")
    category_summary = df.groupby("Category")["Revenue"].sum()
    print(category_summary)

    print("\n--- TOTAL REVENUE BY REGION ---")
    region_summary = df.groupby("Region")["Revenue"].sum()
    print(region_summary)

    return category_summary, region_summary


# STEP 3: Create Visualizations

# Bar Chart
def plot_revenue_by_category(summary):
    plt.figure(figsize=(6, 4))
    plt.bar(summary.index, summary.values)
    plt.title("Total Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("revenue_by_category.png")
    plt.close()
    print("Saved: revenue_by_category.png")

# Scatter Plot
def plot_units_vs_revenue(df):
    plt.figure(figsize=(6, 4))
    plt.scatter(df["Units_Sold"], df["Revenue"])
    plt.title("Units Sold vs Revenue")
    plt.xlabel("Units Sold")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("units_vs_revenue.png")
    plt.close()
    print("Saved: units_vs_revenue.png")

# Heatmap
def plot_monthly_heatmap(df):
    if "Date" not in df.columns:
        print("\nSkipping heatmap: 'Date' column not found.")
        return

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly = df.groupby(["Month", "Category"])["Revenue"].sum().unstack(fill_value=0)

    plt.figure(figsize=(8, 4))
    plt.imshow(monthly.values, aspect='auto')
    plt.title("Monthly Revenue by Category (Heatmap)")
    plt.xlabel("Category Index")
    plt.ylabel("Month Index")
    plt.colorbar(label="Revenue")
    plt.tight_layout()
    plt.savefig("monthly_revenue_heatmap.png")
    plt.close()
    print("Saved: monthly_revenue_heatmap.png")


# STEP 4: Insights

def generate_insights(category_summary, region_summary):
    print("\n--- INSIGHTS ---")

    top_category = category_summary.idxmax()
    top_cat_value = category_summary.max()

    top_region = region_summary.idxmax()
    top_reg_value = region_summary.max()

    print(f"1. Highest revenue category: {top_category} (${top_cat_value:.2f})")
    print(f"2. Highest revenue region: {top_region} (${top_reg_value:.2f})")
    print("3. Category with highest sales may indicate customer preference.")
    print("4. Regions with lower revenue may need better marketing.")


# MAIN FUNCTION

def main():
    df = load_user_csv()

    # Perform analysis
    cat_sum, reg_sum = analyze_data(df)

    # Create plots
    plot_revenue_by_category(cat_sum)
    plot_units_vs_revenue(df)
    plot_monthly_heatmap(df)

    # Generate insights
    generate_insights(cat_sum, reg_sum)

    print("\nALL TASKS COMPLETED SUCCESSFULLY.")


# RUN PROGRAM
if __name__ == "__main__":
    main()
