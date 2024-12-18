import pandas as pd
import matplotlib.pyplot as plt

def visualize_esg(csv_file):
    df = pd.read_csv(csv_file)
    df_sorted = df.sort_values(by="ESG_DISCLOSURE_SCORE", ascending=False)

    plt.bar(df_sorted["Company"], df_sorted["ESG_DISCLOSURE_SCORE"])
    plt.title("ESG Disclosure Scores")
    plt.xlabel("Companies")
    plt.ylabel("ESG Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("examples/visualized_chart.png")
    plt.show()

if __name__ == "__main__":
    visualize_esg("examples/esg_data.csv")
