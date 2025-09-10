# Import Libraries
import pandas as pd
import numpy as np

# 1- Load the dataset (CSV, Excel, JSON) -> Only Tabular Data
def load_data(file):
    """
    Load a dataset from a file (CSV, Excel, JSON) into a pandas DataFrame.
    """
    if file.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.endswith('.xlsx') or file.endswith('.xls'):
        df = pd.read_excel(file)
    elif file.endswith(".json"):
        df = pd.read_json(file)
    else:
        raise ValueError("Unsupported file format. Please use CSV, Excel, or JSON.")
    
    return df

# 2- Data Cleaning : Missing Values, Duplicates, Outliers
def data_cleaning(df):
    """
    Run Full Cleaning Pipeline:
        - Handle Missing Values
        - Remove Duplicates
        - Clip Outliers
    """

    df = handle__missing(df)
    df = remove_duplicates(df)
    df = clip_outliers(df)

    return df

def handle__missing(df):
    """
    Fill Missing Values (Mean/ Median/ Mode).
        - Numerical Columns: Mean if not skewed, else Median
        - Categorical Columns: Mode
    """

    # Take a copy of DataFrame to avoid changing the original DataFrame
    df2 = df.copy()

    # Separate numerical and categorical columns
    num_cols = df2.select_dtypes(include=[np.number]).columns
    cat_cols = df2.select_dtypes(include=['object', 'category']).columns

    # Fill missing values in numerical columns with mean/ median
    for col in num_cols:
        if df2[col].isnull().sum() > 0:
            skewness = df2[col].skew()
            if abs(skewness) > 1:
                df2[col].fillna(df2[col].median(), inplace=True)
            else:
                df2[col].fillna(df2[col].mean(), inplace=True)

    # Fill missing values in categorical columns with mode
    for col in cat_cols:
        if df2[col].isnull().sum() > 0:
            df2[col].fillna(df2[col].mode()[0], inplace=True)

    return df2

def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    """
    df2 = df.copy()
    len_before = len(df2)
    df2 = df2.drop_duplicates()
    len_after = len(df2)

    removed = len_after - len_before
    print(f"Removed {removed} duplicate rows.")
    return df2

def clip_outliers(df):
    """
    Find Outliers using IQR and clip them to the nearest boundary.
    """

    df2 = df.copy()

    num_cols = df2.select_dtypes(include=[np.number]).columns

    for col in num_cols:
        Q1 = df2[col].quantile(0.25)
        Q3 = df2[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Clip outliers to the nearest boundary
        df2[col] = np.where(df2[col] < lower_bound, lower_bound, df2[col])
        df2[col] = np.where(df2[col] > upper_bound, upper_bound, df2[col])

    return df2
