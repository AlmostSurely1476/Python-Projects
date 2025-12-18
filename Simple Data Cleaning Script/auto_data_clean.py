"""
Auto Data Clean - A flexible Python class for automatic dataset cleaning.

This module provides the AutoDataClean class that allows you to selectively
apply various data cleaning operations to pandas DataFrames.
"""

import pandas as pd


class AutoDataClean:
    """
    A class for automatic data cleaning with customizable options.
    
    Parameters
    ----------
    remove_duplicates : bool, default=True
        If True, removes duplicate rows from the dataset.
    remove_nulls : bool, default=True
        If True, removes rows containing null/missing values.
    
    Attributes
    ----------
    remove_duplicates : bool
        Flag indicating whether to remove duplicates.
    remove_nulls : bool
        Flag indicating whether to remove null values.
    
    Examples
    --------
    >>> import pandas as pd
    >>> from auto_data_clean import AutoDataClean
    >>> 
    >>> # Create sample data
    >>> df = pd.DataFrame({'A': [1, 1, 2, None], 'B': ['x', 'x', 'y', 'z']})
    >>> 
    >>> # Clean with both options enabled
    >>> cleaner = AutoDataClean(remove_duplicates=True, remove_nulls=True)
    >>> df_cleaned = cleaner.clean(df)
    >>> 
    >>> # Clean with only duplicate removal
    >>> cleaner = AutoDataClean(remove_duplicates=True, remove_nulls=False)
    >>> df_cleaned = cleaner.clean(df)
    """
    
    def __init__(self, remove_duplicates: bool = True, remove_nulls: bool = True):
        """
        Initialize the AutoDataClean instance with cleaning options.
        
        Parameters
        ----------
        remove_duplicates : bool, default=True
            Whether to remove duplicate rows.
        remove_nulls : bool, default=True
            Whether to remove rows with null values.
        """
        self.remove_duplicates = remove_duplicates
        self.remove_nulls = remove_nulls
    
    def clean(self, df: pd.DataFrame, inplace: bool = False) -> pd.DataFrame:
        """
        Clean the DataFrame based on the configured options.
        
        Parameters
        ----------
        df : pd.DataFrame
            The input DataFrame to clean.
        inplace : bool, default=False
            If True, modifies the original DataFrame. If False, returns a copy.
        
        Returns
        -------
        pd.DataFrame
            The cleaned DataFrame.
        
        Notes
        -----
        - Duplicate removal is performed first, then null removal.
        - The original DataFrame is not modified unless inplace=True.
        """
        if not inplace:
            df = df.copy()
        
        original_rows = len(df)
        
        if self.remove_duplicates:
            df.drop_duplicates(inplace=True)
            duplicates_removed = original_rows - len(df)
            print(f"Removed {duplicates_removed} duplicate rows.")
        
        rows_before_null_removal = len(df)
        
        if self.remove_nulls:
            df.dropna(inplace=True)
            nulls_removed = rows_before_null_removal - len(df)
            print(f"Removed {nulls_removed} rows with null values.")
        
        print(f"Cleaning complete. Original rows: {original_rows}, Final rows: {len(df)}")
        
        return df
    
    def get_summary(self, df: pd.DataFrame) -> dict:
        """
        Get a summary of potential cleaning operations without modifying the data.
        
        Parameters
        ----------
        df : pd.DataFrame
            The DataFrame to analyze.
        
        Returns
        -------
        dict
            A dictionary containing:
            - 'total_rows': Total number of rows
            - 'duplicate_rows': Number of duplicate rows
            - 'rows_with_nulls': Number of rows containing null values
            - 'null_counts_per_column': Null counts for each column
        """
        return {
            'total_rows': len(df),
            'duplicate_rows': df.duplicated().sum(),
            'rows_with_nulls': df.isnull().any(axis=1).sum(),
            'null_counts_per_column': df.isnull().sum().to_dict()
        }


def clean_data(filepath: str, output_filepath: str = None, 
               remove_duplicates: bool = True, remove_nulls: bool = True) -> pd.DataFrame:
    """
    Convenience function to clean a CSV file directly.
    
    Parameters
    ----------
    filepath : str
        Path to the input CSV file.
    output_filepath : str, optional
        Path to save the cleaned CSV. If None, appends '_cleaned' to the original filename.
    remove_duplicates : bool, default=True
        Whether to remove duplicate rows.
    remove_nulls : bool, default=True
        Whether to remove rows with null values.
    
    Returns
    -------
    pd.DataFrame
        The cleaned DataFrame.
    
    Examples
    --------
    >>> df_cleaned = clean_data('data.csv', 'data_cleaned.csv')
    """
    # Load the dataset
    df = pd.read_csv(filepath)
    
    # Create cleaner and clean the data
    cleaner = AutoDataClean(remove_duplicates=remove_duplicates, remove_nulls=remove_nulls)
    df_cleaned = cleaner.clean(df)
    
    # Save if output path provided
    if output_filepath is None:
        output_filepath = filepath.replace('.csv', '_cleaned.csv')
    
    df_cleaned.to_csv(output_filepath, index=False)
    print(f"Cleaned data saved to: {output_filepath}")
    
    return df_cleaned


if __name__ == "__main__":
    # Example usage
    print("AutoDataClean - Example Usage")
    print("=" * 40)
    
    # Create sample data with duplicates and nulls
    sample_data = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie', None],
        'Age': [25, 30, 25, 35, 40],
        'City': ['NYC', 'LA', 'NYC', None, 'Chicago']
    })
    
    print("\nOriginal Data:")
    print(sample_data)
    
    # Get summary before cleaning
    cleaner = AutoDataClean()
    summary = cleaner.get_summary(sample_data)
    print(f"\nData Summary:")
    print(f"  Total rows: {summary['total_rows']}")
    print(f"  Duplicate rows: {summary['duplicate_rows']}")
    print(f"  Rows with nulls: {summary['rows_with_nulls']}")
    
    # Clean the data
    print("\nCleaning data...")
    df_cleaned = cleaner.clean(sample_data)
    
    print("\nCleaned Data:")
    print(df_cleaned)
