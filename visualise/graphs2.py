import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


folder = 'causal_datasets'
dataset = ['/physical_gender', '/physical_queerness', '/economic_gender', '/economic_race']
# Dataset
df = pd.read_csv(folder +  dataset[3] + ".csv")


df['economic_race'] = df['economic_status'] + " " + df['race']

# Group the data by Context and Appearance_Gender, then compute the means for metrics
grouped_df = df.groupby(['Context', 'economic_race'])[['Neg_Regard', 'Toxicity']].mean().reset_index()

# Create output folder
output_folder = "contextual_plots"
os.makedirs(output_folder, exist_ok=True)

# Create side-by-side plots
fig, axes = plt.subplots(1, 2, figsize=(18, 8), sharey=True)

# Plot Toxicity
sns.barplot(
    data=grouped_df,
    x='economic_race',
    y='Toxicity',
    hue='Context',
    ax=axes[0],
    palette='tab10'
)
axes[0].set_title('Toxicity Scores by Economic Status and Race across Contexts', fontsize=14)
axes[0].set_ylabel('Toxicity Score', fontsize=12)
axes[0].set_xlabel('Economic Status and Race', fontsize=12)
axes[0].legend(title='Context', fontsize=10, title_fontsize=12)

# Plot Neg_Regard
sns.barplot(
    data=grouped_df,
    x='economic_race',
    y='Neg_Regard',
    hue='Context',
    ax=axes[1],
    palette='tab10'
)
axes[1].set_title('Neg_Regard Scores by Economic Status and Race across Contexts', fontsize=14)
axes[1].set_ylabel('Neg_Regard Score', fontsize=12)
axes[1].set_xlabel('Economic Status and Race', fontsize=12)
axes[1].legend(title='Context', fontsize=10, title_fontsize=12)

# Adjust layout and save
plt.tight_layout()

plt.savefig(output_folder + dataset[3])
plt.show()



