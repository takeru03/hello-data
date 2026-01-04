import pandas as pd

def main():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
    print(df.describe())

if __name__ == "__main__":
    main()
