from src.data_loader import SECDataLoader


def main():
    loader = SECDataLoader("data/sec_filings.csv")
    df = loader.load_data()
    filtered_df = loader.filter_filings(df)

    print("Total filings:", len(df))
    print("10-K & 10-Q filings:", len(filtered_df))
    print(filtered_df.head())


if __name__ == "__main__":
    main()
