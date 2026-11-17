
import pandas as pd
import numpy as np

# Load dataset
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "dataset"

df = pd.read_csv(DATASET_DIR / "financial_performance.csv")

# # Display first 5 records
# print("FIRST 5 RECORDS")
print(df.head())

# # Dataset dimensions
# print("\nDATASET SHAPE")
# print(df.shape)

# # Column names
# print("\nCOLUMN NAMES")
# print(df.columns.tolist())

# # Data types
# print("\nDATA TYPES")
# print(df.dtypes)


# 2 – Dataset information and descriptive statistics


# # Dataset information
# print("DATASET INFORMATION")
# df.info()

# # Descriptive statistics
# print("\nDESCRIPTIVE STATISTICS")
# print(df.describe())

# # Check missing values
# print("\nMISSING VALUES")
# print(df.isnull().sum())

# # Check duplicate records
# print("\nDUPLICATE RECORDS")
# print(df.duplicated().sum())




# Duplicate records and date sequence

# # print("Duplicate Records:", df.duplicated().sum())

# convert date into datetime
df["month"] = pd.to_datetime(df["month"])


# # Check date sequence
# print("Date Range:")
# print(df["month"].min(), "to", df["month"].max())

# # Check monthly frequency
# print("\nNumber of Unique Months:")
# print(df["month"].nunique())

# # Check financial years
# print("\nFinancial Years:")
# print(df["financial_year"].unique())



# Phase 2-Data Cleaning & Preparation      
# Prepare the dataset for financial analysis.


# # Check negative financial values

# print(df[df["revenue_actual_inr"] < 0])
# print(df[df["cost_of_goods_sold_inr"] < 0])
# print(df[df["operating_expenses_actual_inr"] < 0])


# # Financial Data Consistency
# # verify whether Revenue is greater than COGS for every month

# print(df[df["revenue_actual_inr"] < df["cost_of_goods_sold_inr"]])


# # Check operating expenses

# print(df[df["operating_expenses_actual_inr"] <= 0])


# # Check budget and actual financial values
# # verify whether actual revenue and operating expenses are positive.

# print(df[df["revenue_actual_inr"] <= 0])
# print(df[df["revenue_budget_inr"] <= 0])
# print(df[df["operating_expenses_budget_inr"] <= 0])


# # Check financial calculations.
# # verify whether Gross Profit is positive and calculate it for analysis.


df["gross_profit"] = df["revenue_actual_inr"] - df["cost_of_goods_sold_inr"]

# print(df[["month", "gross_profit"]].head())


# Calculate Gross Profit Margin
# what percentage of revenue remains after deducting the cost of goods sold.

df["gross_profit_margin"] = (
    df["gross_profit"] / df["revenue_actual_inr"]
) * 100

# print(df[["month", "gross_profit", "gross_profit_margin"]].head().round(2))


# Calculate Operating Profit

df["operating_profit"] = (
    df["gross_profit"] - df["operating_expenses_actual_inr"]
)

# print(df[["month", "operating_profit"]].head())


# Calculate Operating Profit Margin

df["operating_profit_margin"] = (
    df["operating_profit"] / df["revenue_actual_inr"]
) * 100

# print(df[["month", "operating_profit_margin"]].head().round(2))



# Calculate Net Profit

df["net_profit"] = (
    df["operating_profit"]
    - df["depreciation_inr"]
    - df["interest_expense_inr"]
    - df["tax_expense_inr"]
).round(2)

# print(df[["month", "net_profit"]].head())


# Calculate Net Profit Margin

df["net_profit_margin"] = (
    df["net_profit"] / df["revenue_actual_inr"] * 100
).round(2)

# print(df[["month", "net_profit_margin"]].head())


# Calculate Net Cash Flow

df["net_cash_flow"] = (
    df["cash_inflows_inr"] - df["cash_outflows_inr"]
).round(2)

# print(df[["month", "net_cash_flow"]].head())


# Calculate Budget Variance

df["revenue_variance"] = (
    df["revenue_actual_inr"] - df["revenue_budget_inr"]
).round(2)

# print(df[["month", "revenue_variance"]].head())


# Calculate Revenue Budget Achievement %


df["revenue_budget_achievement"] = (
    df["revenue_actual_inr"] / df["revenue_budget_inr"] * 100
).round(2)

# print(df[["month", "revenue_budget_achievement"]].head())



# Create financial date columns

df["month_name"] = df["month"].dt.strftime("%B")
df["year"] = df["month"].dt.year

# print(df[["month", "month_name", "year", "financial_year"]].head())



# Save the prepared dataset

# df.to_csv(DATASET_DIR / "financial_performance_cleaned.csv", index=False)

# print("Cleaned dataset saved successfully.")



# Financial KPI Analysis

# Objective: Evaluate the company's overall financial performance using the calculated financial metrics.

# Calculate overall financial performance

# print("TOTAL REVENUE:", round(df["revenue_actual_inr"].sum(), 2))

# print("TOTAL COGS:", round(df["cost_of_goods_sold_inr"].sum(), 2))

# print("TOTAL GROSS PROFIT:", round(df["gross_profit"].sum(), 2))

# print("TOTAL OPERATING EXPENSES:", round(df["operating_expenses_actual_inr"].sum(), 2))

# print("TOTAL OPERATING PROFIT:", round(df["operating_profit"].sum(), 2))

# print("TOTAL NET PROFIT:", round(df["net_profit"].sum(), 2))



# Calculate Profitability Margins

gross_margin = (df["gross_profit"].sum() / df["revenue_actual_inr"].sum()) * 100

operating_margin = (df["operating_profit"].sum() / df["revenue_actual_inr"].sum()) * 100

net_margin = (df["net_profit"].sum() / df["revenue_actual_inr"].sum()) * 100

# print("Gross Profit Margin:", round(gross_margin, 2), "%")
# print("Operating Profit Margin:", round(operating_margin, 2), "%")
# print("Net Profit Margin:", round(net_margin, 2), "%")



# Expense Analysis

expense_ratio = (
    df["operating_expenses_actual_inr"].sum()
    / df["revenue_actual_inr"].sum()
) * 100

# print("Operating Expense Ratio:", round(expense_ratio, 2), "%")


# Cash Flow Performance

total_inflows = df["cash_inflows_inr"].sum()
total_outflows = df["cash_outflows_inr"].sum()
total_net_cash_flow = df["net_cash_flow"].sum()

# print("Total Cash Inflows:", round(total_inflows, 2))
# print("Total Cash Outflows:", round(total_outflows, 2))
# print("Total Net Cash Flow:", round(total_net_cash_flow, 2))


# Budget Performance Analysis


total_revenue_budget = df["revenue_budget_inr"].sum()
total_revenue_actual = df["revenue_actual_inr"].sum()

revenue_variance = total_revenue_actual - total_revenue_budget

budget_achievement = (
    total_revenue_actual / total_revenue_budget
) * 100

# print("Revenue Budget:", round(total_revenue_budget, 2))
# print("Actual Revenue:", round(total_revenue_actual, 2))
# print("Revenue Variance:", round(revenue_variance, 2))
# print("Budget Achievement:", round(budget_achievement, 2), "%")


# Exploratory Data Analysis (EDA)

# Monthly Revenue Trend Analysis

import matplotlib.pyplot as plt

# plt.figure(figsize=(12, 5))

# plt.plot(df["month"], df["revenue_actual_inr"], marker="o")

# plt.title("Monthly Revenue Trend")
# plt.xlabel("Month")
# plt.ylabel("Revenue (₹)")

# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()

# plt.show()


# Monthly Profit Trend Analysis

# plt.figure(figsize=(12, 5))

# plt.plot(df["month"], df["gross_profit"], label="Gross Profit")
# plt.plot(df["month"], df["operating_profit"], label="Operating Profit")
# plt.plot(df["month"], df["net_profit"], label="Net Profit")

# plt.title("Monthly Profitability Trend")
# plt.xlabel("Month")
# plt.ylabel("Profit (₹)")

# plt.legend()
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()

# plt.show()




# Financial Year Performance Comparison


yearly_performance = df.groupby("financial_year")[[
    "revenue_actual_inr",
    "gross_profit",
    "operating_profit",
    "net_profit"
]].sum().round(2)

# print(yearly_performance)


# Calculate Year-over-Year Revenue Growth

yearly_revenue = df.groupby("financial_year")["revenue_actual_inr"].sum()

revenue_growth = yearly_revenue.pct_change() * 100

# print(revenue_growth.round(2))


# Compare Profit Margins Across Financial Years


yearly_margin = df.groupby("financial_year").agg(
    revenue=("revenue_actual_inr", "sum"),
    gross_profit=("gross_profit", "sum"),
    operating_profit=("operating_profit", "sum"),
    net_profit=("net_profit", "sum")
)

yearly_margin["gross_margin"] = (
    yearly_margin["gross_profit"] / yearly_margin["revenue"] * 100
).round(2)

yearly_margin["operating_margin"] = (
    yearly_margin["operating_profit"] / yearly_margin["revenue"] * 100
).round(2)

yearly_margin["net_margin"] = (
    yearly_margin["net_profit"] / yearly_margin["revenue"] * 100
).round(2)

# print(yearly_margin[[
#     "gross_margin",
#     "operating_margin",
#     "net_margin"
# ]])


# Revenue vs Operating Expenses Analysis


expense_analysis = df.groupby("financial_year").agg(
    revenue=("revenue_actual_inr", "sum"),
    operating_expenses=("operating_expenses_actual_inr", "sum")
)

expense_analysis["expense_ratio"] = (
    expense_analysis["operating_expenses"]
    / expense_analysis["revenue"] * 100
).round(2)

# print(expense_analysis.round(2))


# Cash Flow Analysis by Financial Year


cash_analysis = df.groupby("financial_year").agg(
    cash_inflows=("cash_inflows_inr", "sum"),
    cash_outflows=("cash_outflows_inr", "sum"),
    net_cash_flow=("net_cash_flow", "sum")
)

# print(cash_analysis.round(2))


# Revenue and Expense Relationship

# Correlation measures the strength and direction of the relationship between two numerical variables.

# correlation = df["revenue_actual_inr"].corr(
#     df["operating_expenses_actual_inr"]
# )

# print("Revenue and Expense Correlation:", round(correlation, 2))



# Financial Performance Analysis

# Check monthly revenue budget performance

# print(
#     df[[
#         "month",
#         "revenue_actual_inr",
#         "revenue_budget_inr",
#         "revenue_variance",
#         "revenue_budget_achievement"
#     ]].round(2).to_string(index=False)
# )




# Financial Year-wise Budget Performance

yearly_budget = df.groupby("financial_year").agg(
    total_revenue=("revenue_actual_inr", "sum"),
    total_budget=("revenue_budget_inr", "sum")
)

yearly_budget["variance"] = (
    yearly_budget["total_revenue"] - yearly_budget["total_budget"]
)

yearly_budget["budget_achievement"] = (
    yearly_budget["total_revenue"] /
    yearly_budget["total_budget"] * 100
)

# print(yearly_budget.round(2))




# Financial Growth Analysis

yearly_growth = df.groupby("financial_year")[
    ["revenue_actual_inr", "gross_profit",
     "operating_profit", "net_profit"]
].sum()

yearly_growth["revenue_growth"] = (
    yearly_growth["revenue_actual_inr"].pct_change() * 100
)

yearly_growth["gross_profit_growth"] = (
    yearly_growth["gross_profit"].pct_change() * 100
)

yearly_growth["operating_profit_growth"] = (
    yearly_growth["operating_profit"].pct_change() * 100
)

yearly_growth["net_profit_growth"] = (
    yearly_growth["net_profit"].pct_change() * 100
)

# print(yearly_growth.round(2))





# Statistical Analysis
# Objective: Use statistical methods to understand relationships, variation and patterns in the company's financial performance.

# Descriptive Statistics

financial_metrics = [
    "revenue_actual_inr",
    "gross_profit",
    "operating_profit",
    "net_profit",
    "net_cash_flow"
]

statistics = df[financial_metrics].describe().T

# print(statistics.round(2))



# Correlation analysis

correlation = df[
    ["revenue_actual_inr", "cost_of_goods_sold_inr", "net_profit"]
].corr()

# print(correlation.round(2))


# Hypothesis Testing

# hypothesis-testing question

# Calculate the sample statistics
# Our business question is:
# Is the company's average monthly net profit significantly greater than ₹10 lakh?

# - Benchmark mean: ₹10,00,000
# - Significance level (α): 0.05 (5%)
# - Sample: 36 monthly net profit observations


from scipy import stats

sample_mean = df["net_profit"].mean()
sample_std = df["net_profit"].std()
sample_size = df["net_profit"].count()

# print("Sample Mean:", round(sample_mean, 2))
# print("Sample Standard Deviation:", round(sample_std, 2))
# print("Sample Size:", sample_size)


# t_stat, p_value = stats.ttest_1samp(
#     df["net_profit"],
#     popmean=1000000,
#     alternative="greater"
# )

# print("T-statistic:", round(t_stat, 4))
# print("P-value:", round(p_value, 4))

# here T-statistic: 2.2201
# P-value: 0.0165   which is less than 0.05


# What does this mean?
# We have statistically significant evidence that the company's average monthly net profit is greater than ₹10 lakh.

# In simpler terms, the observed average of ₹10.96 lakh is sufficiently above the ₹10 lakh benchmark to reject
# the null hypothesis at the 5% significance level.



# Confidence Intervals.

# We will use the t-distribution because we have a sample of 36 monthly observations and
# are estimating the population standard deviation from the sample.


from scipy import stats

net_profit = df["net_profit"]

# Calculate sample statistics
mean_profit = net_profit.mean()
std_profit = net_profit.std()
n = len(net_profit)

# Calculate standard error
standard_error = std_profit / (n ** 0.5)

# Calculate 95% confidence interval
confidence_interval = stats.t.interval(
    confidence=0.95,
    df=n - 1,
    loc=mean_profit,
    scale=standard_error
)

# print("Average Monthly Net Profit:", round(mean_profit, 2))
# print("Standard Error:", round(standard_error, 2))
# print("95% Confidence Interval:")
# print("Lower Limit:", round(confidence_interval[0], 2))
# print("Upper Limit:", round(confidence_interval[1], 2))



# This supports the conclusion from our earlier hypothesis test that average monthly net profit is greater than ₹10 lakh
# at the 5% significance level.

# 3. Business conclusion
# The company's estimated average monthly net profit is approximately ₹10.96 lakh, and the 95% confidence
# interval suggests that the underlying average is above our selected ₹10 lakh benchmark.



# Simple Linear Regression


# Business question
# How much does COGS increase when revenue increases, and how strongly does revenue explain the variation in COGS?


# Define the variables

from sklearn.linear_model import LinearRegression

# Independent and dependent variables
X = df[["revenue_actual_inr"]]
y = df["cost_of_goods_sold_inr"]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Regression coefficients
intercept = model.intercept_
slope = model.coef_[0]

# print("Intercept:", round(intercept, 2))
# print("Slope:", round(slope, 4))


# Evaluate the regression model

# calculate R-squared.

r_squared = model.score(X, y)

# print("R-squared:", round(r_squared, 4))
# print("R-squared (%):", round(r_squared * 100, 2), "%")






# Data Visualization

# Bar Chart – Financial Year-wise Profitability

import matplotlib.pyplot as plt

# yearly_profit = df.groupby("financial_year")[
#     ["revenue_actual_inr", "gross_profit",
#      "operating_profit", "net_profit"]
# ].sum()

# yearly_profit.plot(
#     kind="bar",
#     figsize=(10, 6)
# )

# plt.title("Financial Year-wise Revenue and Profit Comparison")
# plt.xlabel("Financial Year")
# plt.ylabel("Amount (₹)")
# plt.xticks(rotation=0)
# plt.legend([
#     "Revenue",
#     "Gross Profit",
#     "Operating Profit",
#     "Net Profit"
# ])
# plt.tight_layout()
# plt.show()




# Histogram

import seaborn as sns

# plt.figure(figsize=(9, 5))

# sns.histplot(
#     data=df,
#     x="revenue_actual_inr",
#     bins=8,
#     kde=True,
#     edgecolor="black"
# )

# plt.title("Distribution of Monthly Revenue")
# plt.xlabel("Monthly Revenue (₹)")
# plt.ylabel("Frequency (Number of Months)")

# plt.tight_layout()
# plt.show()







# Box Plot – Monthly Revenue

# plt.figure(figsize=(9, 4))

# sns.boxplot(
#     x=df["revenue_actual_inr"]
# )

# plt.title("Box Plot of Monthly Revenue")
# plt.xlabel("Monthly Revenue (₹)")

# plt.tight_layout()
# plt.show()




# scatter Plot – Revenue vs COGS
# Business question: How does COGS change as revenue increases?

# plt.figure(figsize=(9, 5))

# sns.regplot(
#     data=df,
#     x="revenue_actual_inr",
#     y="cost_of_goods_sold_inr",
#     line_kws={"color": "red"}
# )

# plt.title("Relationship Between Revenue and COGS")
# plt.xlabel("Revenue (₹)")
# plt.ylabel("COGS (₹)")

# plt.tight_layout()
# plt.show()


# Financial Performance Comparison Charts
# Financial Year-wise Profit Margin Comparison Chart.

# yearly_margin = df.groupby("financial_year").agg(
#     revenue=("revenue_actual_inr", "sum"),
#     gross_profit=("gross_profit", "sum"),
#     operating_profit=("operating_profit", "sum"),
#     net_profit=("net_profit", "sum")
# )

# yearly_margin["Gross Margin"] = (
#     yearly_margin["gross_profit"] /
#     yearly_margin["revenue"] * 100
# )

# yearly_margin["Operating Margin"] = (
#     yearly_margin["operating_profit"] /
#     yearly_margin["revenue"] * 100
# )

# yearly_margin["Net Margin"] = (
#     yearly_margin["net_profit"] /
#     yearly_margin["revenue"] * 100
# )

# yearly_margin[
#     ["Gross Margin", "Operating Margin", "Net Margin"]
# ].plot(kind="bar", figsize=(10, 6))

# plt.title("Financial Year-wise Profit Margin Comparison")
# plt.xlabel("Financial Year")
# plt.ylabel("Profit Margin (%)")
# plt.xticks(rotation=0)
# plt.legend()
# plt.tight_layout()
# plt.show()

# Key findings:
# 1. Gross Margin: Highest in FY 2024–25 at 41.25%, followed by a decline to 40.37% in FY 2025–26.
# 2. Operating Margin: Improved in FY 2024–25 but declined slightly in FY 2025–26.
# 3. Net Margin: FY 2024–25 performed best at 11.11%. It declined to 10.86% in FY 2025–26.


# Business interpretation:

# FY 2024–25 was the strongest year in terms of profitability efficiency. Although revenue and absolute
# profit increased in FY 2025–26, profit margins declined slightly.

# This suggests that the company generated more revenue and profit, but retained a slightly smaller
# percentage of revenue as profit.









