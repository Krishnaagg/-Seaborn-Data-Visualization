# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Set Seaborn style & context
sns.set_style("whitegrid")
sns.set_context("talk")

# 2. Generate realistic synthetic data (customer spending by segment)
np.random.seed(42)
n_customers = 300

segments = np.random.choice(["Budget", "Standard", "Premium"],
                            size=n_customers, p=[0.3, 0.5, 0.2])
spend = np.empty(n_customers)

mask_budget = segments == "Budget"
mask_standard = segments == "Standard"
mask_premium = segments == "Premium"

spend[mask_budget] = np.random.normal(100, 20, mask_budget.sum())
spend[mask_standard] = np.random.normal(300, 50, mask_standard.sum())
spend[mask_premium] = np.random.normal(600, 100, mask_premium.sum())

df = pd.DataFrame({
    "Customer Segment": segments,
    "Monthly Spending ($)": spend
})

# 3. Create figure (8x8 inches -> with dpi=64 → 512x512 px)
plt.figure(figsize=(8, 8))

# 4. Draw boxplot
ax = sns.boxplot(
    x="Customer Segment",
    y="Monthly Spending ($)",
    data=df,
    palette="Set2",
    width=0.6,
    showmeans=True,
    meanprops={"marker": "o", "markerfacecolor": "black", "markeredgecolor": "black"}
)

# 5. Title & labels
ax.set_title("Customer Monthly Spending by Segment", fontsize=16, weight="bold")
ax.set_xlabel("Segment", fontsize=12)
ax.set_ylabel("Spending ($)", fontsize=12)

# 6. Save PNG exactly 512x512 pixels (8 in * 64 dpi = 512 px)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
