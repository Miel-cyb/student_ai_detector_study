import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

def correlation_analysis(data):
    print("\n===== CORRELATION ANALYSIS =====")

    #  Select key numeric features
    cols = ['ASSIGNMENT', 'CLASS TEST', 'AI_Average', 'Score_Gap']
    corr_matrix = data[cols].corr(method='pearson')
    print("\nPearson Correlation Matrix:\n", corr_matrix)

    #  Spearman correlation (for non-linear relationships)
    spearman_matrix = data[cols].corr(method='spearman')
    print("\nSpearman Correlation Matrix:\n", spearman_matrix)

    #  Specific correlation: AI_Average vs Performance gap
    pear_corr, pear_p = pearsonr(data['AI_Average'], data['Score_Gap'])
    print(f"\nPearson correlation between AI_Average and Score_Gap: {pear_corr:.3f} (p={pear_p:.4f})")

    spear_corr, spear_p = spearmanr(data['AI_Average'], data['Score_Gap'])
    print(f"Spearman correlation between AI_Average and Score_Gap: {spear_corr:.3f} (p={spear_p:.4f})")

    #  Cohen’s d (effect size) between High_AI vs Low_AI on test scores
    high_ai = data[data['High_AI'] == 'High AI Score']['CLASS TEST']
    low_ai = data[data['High_AI'] == 'Low AI Score']['CLASS TEST']

    if len(high_ai) > 1 and len(low_ai) > 1:
        mean_diff = high_ai.mean() - low_ai.mean()
        pooled_std = np.sqrt((high_ai.var() + low_ai.var()) / 2)
        cohens_d = mean_diff / pooled_std
        print(f"\nCohen’s d (High vs Low AI on CLASS TEST): {cohens_d:.3f}")
    else:
        print("\nCohen’s d could not be calculated — insufficient group data.")

    #  Save correlation matrix to file
    corr_matrix.to_excel("correlation_results.xlsx")
    print("\n Correlation results saved as 'correlation_results.xlsx'")
