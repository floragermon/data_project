import seaborn as sns
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer
import matplotlib as plt 
# Load the dataset (add parentheses)
data = load_breast_cancer()  

# Print available keys
print(data.keys())  

f = pd.DataFrame(data.data, columns=data.feature_names)

# Compute the correlation matrix
corr_matrix = df.corr()

# Plot the heatmap
plt.figure(figsize=(12, 10))  # Set figure size
sns.heatmap(corr_matrix, cmap="coolwarm", annot=False, linewidths=0.5)

# Add title
plt.title("Feature Correlation Heatmap")
plt.show()


# Check if target_label is now present
print(df.columns)

# Now group by 'target_label'
grouped_df = df.groupby("target_label").mean()
print(grouped_df.head())


from scipy import stats


# Add target column (0 = Malignant, 1 = Benign)
df["target"] = data.target  

# Map target to labels for clarity
df["target_label"] = df["target"].map({0: "malignant", 1: "benign"})

# Group by 'target_label' to check mean differences
grouped = df.groupby("target_label").mean()
print(grouped)

# Extract data for ANOVA
benign = df[df["target"] == 1]["mean area"]
malignant = df[df["target"] == 0]["mean area"]

# Perform ANOVA
f_stat, p_value = stats.f_oneway(benign, malignant)

print(f"F-statistic: {f_stat:.3f}, P-value: {p_value:.5f}")

from scipy import stats
import csv

anova_results = []

# Perform ANOVA for each feature
for col in df.columns[:-2]:  # Exclude 'target' and 'target_label'
    benign = df[df["target"] == 1][col]
    malignant = df[df["target"] == 0][col]

    f_stat, p_value = stats.f_oneway(benign, malignant)

    # Append results as a dictionary to a list
    anova_results.append({"Feature": col, "F-statistic": round(f_stat, 3), "P-value": round(p_value, 5)})

# Print the list of dictionaries (Optional)
print(anova_results)
# Write to a CSV file
with open("anova_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Feature", "F-statistic", "P-value"])
    writer.writeheader()
    writer.writerows(anova_results)

print("ANOVA results saved to 'anova_results.csv'!")
