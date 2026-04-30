import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

def load_data(file_path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()
    
def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna()
    data = data.drop_duplicates()
    data['type'] = data['type'].replace({'CASH_IN':0, 'CASH_OUT':1, 'DEBIT':2, 'PAYMENT':3, 'TRANSFER':4})
    data.drop(['nameOrig', 'nameDest'], axis=1, inplace=True)
    print(data.head())
    sea.heatmap(data.corr(),fmt=".2f",annot=True,cmap="coolwarm")
    plt.subplots_adjust(left=0.1)
    plt.title("Correlation Plot")
    plt.savefig("correlation_plot.png")
    
    return data

def main():
    df = load_data("data/Fraud.csv")
    df = preprocess_data(df)
    return


if __name__ == "__main__":
    main()
