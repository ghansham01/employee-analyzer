import pandas as pd 
import numpy as np 

# file_name = pd.read_excel('Book1.xlsx')

try:
    df = pd.read_excel('Book1.xlsx')

    print("\nFirst 5 rows:")
    print(df.head())

    print(f"\nShape (rows, columns): {df.shape}")
    print(f"\nColumn names: {list(df.columns)}")

    # Statistical summary
    print("\n Statical Summary (.describe()):")
    print(df.describe())

    # Mean, Mode, median for numeric colums
    print("\n Mean of numeric colums:")
    print(df.mean(numeric_only=True))
    print("\n Median of numeric colums:")
    print(df.median(numeric_only=True))
    print("\n Mode of numeric colums:")
    print(df.mode(numeric_only=True))

    # Messing values cheker
    print(df.isnull().sum())
    
    # Column-wise Analysis
    print(df.columns.tolist())
    print("\nDepartment column - Unique values and frequency:")
    print(df['Department'].value_counts())

    for col in df.columns:
        if df[col].dtype == 'object':  # text type column
            print(f"\n{col} - Unique values and frequency:")
            print(df[col].value_counts())


except FileNotFoundError:
    print("file not found")

except Exception as e:
    print(f'error are: {e}')
