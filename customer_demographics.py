import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_data.csv")

# Display first rows
print("First five rows:")
print(df.head())

# Age group distribution
age_counts = df["Age_Group"].value_counts()

plt.figure(figsize=(8, 5))
age_counts.plot(kind="bar")

plt.title("Customer Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("customer_demographics.png")

plt.show()
