
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from scipy.stats import zscore
import matplotlib.pyplot as plt

data = pd.read_csv("ms_data_with_insurance.csv")

# part 1: analyze walking speed:
# removing outliers for walking speed
data['ws_zscore'] = zscore(data['walking_speed'])
ws_outliers = data[abs(data['ws_zscore']) > 3]
print(ws_outliers)
data2 = data[abs(data['ws_zscore']) <= 3]

# removing outliers for cost
data['cost_zscore'] = zscore(data['visit_cost'])
cost_outliers = data[abs(data['cost_zscore']) > 3]

print(cost_outliers) # no outliers found


# Multiple regression with education and age
data2 = pd.get_dummies(data2, columns=["education_level"], drop_first=True)

data2.columns = data2.columns.str.replace(' ', '_') # was having problems with spaces so replaced them with '_'

# print columns to get names
print(data2.columns)

formula = """
walking_speed ~ age + education_level_High_School + education_level_Graduate + education_level_Some_College
"""

model = smf.ols(formula=formula, data=data2).fit()
print(model.summary())

# part 2: analyze costs:
# Simple analysis of insurance type effect

# one-way anova
anova_result = stats.f_oneway(
    data2.loc[data["insurance_type"] == "Basic", "visit_cost"],
    data2.loc[data["insurance_type"] == "Premium", "visit_cost"],
    data2.loc[data["insurance_type"] == "Platinum", "visit_cost"]
)

print(anova_result) # F-statistic of 253906.32211321837 and p-value of 0.0

# Box plots and basic statistics
plt.figure(figsize=(10, 6))
data.boxplot(column="visit_cost", by="insurance_type")
plt.title("Visit Costs by Insurance Type")
plt.suptitle('')  
plt.xlabel("Insurance Type")
plt.ylabel("Visit Cost")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.savefig("insurance_plot.png", bbox_inches='tight')

summary_stats = data2.groupby("insurance_type")["visit_cost"].agg(["mean", "std", "count"]).reset_index()
print(summary_stats)

# part 3: Calculate effect sizes
# calculating cohen's d to find effect sizes
def cohens_d(x, y):
    mean_diff = x.mean() - y.mean()
    pooled_sd = ((x.std() ** 2 + y.std() ** 2) / 2) ** 0.5
    return mean_diff / pooled_sd

# Calculate effect sizes between pairs of insurance types
basic = data2.loc[data["insurance_type"] == "Basic", "visit_cost"]
premium = data2.loc[data["insurance_type"] == "Premium", "visit_cost"]
platinum = data2.loc[data["insurance_type"] == "Platinum", "visit_cost"]

print(f"Basic vs Premium: {cohens_d(basic, premium):.4f}") 
print(f"Basic vs Platinum: {cohens_d(basic, platinum):.4f}")
print(f"Premium vs Platinum: {cohens_d(premium, platinum):.4f}")