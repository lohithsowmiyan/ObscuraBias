import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


folder = 'causal_datasets'
dataset = ['/physical_gender', '/physical_queerness', '/economic_gender', '/economic_race']
# Dataset
df = pd.read_csv(folder +  dataset[3] + ".csv")

# Create a new column for the unique combination of physical_appearance and gender
df['economic_race'] = df['economic_status'] + " " + df['race']

# Group by the unique combination and compute the mean of Neg_Regard and Toxicity
grouped_df = df.groupby('economic_race')[['Neg_Regard', 'Toxicity']].mean().reset_index()

# Melt the DataFrame for grouped bar plotting
melted_df = grouped_df.melt(id_vars='economic_race', var_name='Metric', value_name='Score')

# Plotting grouped bars
plt.figure(figsize=(12, 8))
sns.barplot(data=melted_df, x='economic_race', y='Score', hue='Metric', palette='coolwarm')

# Add labels and title
plt.title('Toxicity and Neg_Regard Scores by Economic Status and Race', fontsize=16)
plt.ylabel('Score', fontsize=12)
plt.xlabel('Economic Status and Race', fontsize=12)

# Save the plot in a new folder
output_folder = "plots"
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
plt.savefig(output_folder + dataset[3])

# Show the plot
plt.tight_layout()
plt.show()
plt.show()
