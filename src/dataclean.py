import pandas as pd
import numpy as np

def load_clean_create_metrics(filepath):
  
    data = pd.read_excel(filepath)
    data = data.dropna(subset=['ASSIGNMENT', 'CLASS TEST'])

    ai_columns = ['GPT-ZERO', 'ZERO-GPT', 'QUILLBOT AI DETECTOR', 'GRAMMARLY AI DETECTOR']

    #  removing % in AI scores column , converting to numeric, and filling missing values with median
    for col in ai_columns:
        data[col] = data[col].astype(str).str.replace('%','', regex=False)
        data[col] = pd.to_numeric(data[col], errors='coerce')
        data[col] = data[col].fillna(data[col].median())

    
    for col in ['ASSIGNMENT', 'CLASS TEST']:
        data[col] = pd.to_numeric(data[col], errors='coerce')
        data[col] = data[col].fillna(data[col].median())

    # Derived Metrics
    data['AI_Average'] = data[ai_columns].mean(axis=1)
    data['Score_Gap'] = data['ASSIGNMENT'] - data['CLASS TEST']

    # median splits to define High/Low AI and Underperformed/Performed
    ai_median = data['AI_Average'].median()
    test_median = data['CLASS TEST'].median()

    data['High_AI'] = np.where(data['AI_Average'] >= ai_median, 'High AI Score', 'Low AI Score')
    data['Performance_Level'] = np.where(data['CLASS TEST'] < test_median, 'Underperformed', 'Performed Well')

    # Descriptive Statistics
    print("Overall Performance Counts:\n", data['Performance_Level'].value_counts())
    print("\nHigh vs Low AI Score Counts:\n", data['High_AI'].value_counts())

    cross_tab = pd.crosstab(data['High_AI'], data['Performance_Level'], margins=True)
    print("\nAI Score vs Performance:\n", cross_tab)

    summary = data.groupby('High_AI')[['ASSIGNMENT','CLASS TEST','Score_Gap']].mean()
    print("\nSummary by AI Score Group:\n", summary)

    return data
