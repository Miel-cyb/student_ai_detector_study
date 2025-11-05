import matplotlib.pyplot as plt
import seaborn as sns

def visualizations(data):
    print("\n===== VISUALIZATIONS =====")

 
    sns.set(style="whitegrid", palette="muted")
    plt.rcParams["figure.figsize"] = (8, 5)

    #  Scatter Plot: Assignment vs Test
    plt.figure()
    sns.scatterplot(data=data, x='ASSIGNMENT', y='CLASS TEST', hue='High_AI', s=60)
    plt.title('Assignment vs Test Performance by AI Group')
    plt.xlabel('Assignment Score')
    plt.ylabel('Test Score')
    plt.legend(title='AI Score Group')
    plt.tight_layout()
    plt.savefig("viz_assignment_vs_test.png", dpi=300)
    print(" Saved: viz_assignment_vs_test.png")

    #  Boxplot: Score Gap by AI Group
    plt.figure()
    sns.boxplot(data=data, x='High_AI', y='Score_Gap', palette='coolwarm')
    plt.title('Score Gap (Assignment - Test) by AI Group')
    plt.xlabel('AI Score Group')
    plt.ylabel('Score Gap')
    plt.tight_layout()
    plt.savefig("viz_score_gap_boxplot.png", dpi=300)
    print(" Saved: viz_score_gap_boxplot.png")

    #  Heatmap: Correlation between all numeric variables
    plt.figure()
    corr = data[['ASSIGNMENT', 'CLASS TEST', 'AI_Average', 'Score_Gap']].corr()
    sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f', square=True)
    plt.title('Correlation Heatmap of Key Variables')
    plt.tight_layout()
    plt.savefig("viz_correlation_heatmap.png", dpi=300)
    print(" Saved: viz_correlation_heatmap.png")

    plt.show()
