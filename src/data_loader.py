import pandas as pd


class SECDataLoader:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_data(self) -> pd.DataFrame:
        """
        Load SEC filings dataset from CSV
        """
        df = pd.read_csv(self.csv_path)
        return df

    def filter_filings(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Keep only 10-K and 10-Q filings
        """
        filtered_df = df[df["Form Type"].isin(["10-K", "10-Q"])]
        return filtered_df
