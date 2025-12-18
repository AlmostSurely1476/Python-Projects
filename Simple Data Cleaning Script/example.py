"""
Example usage of the AutoDataClean class.

This script demonstrates how to use the AutoDataClean class
to clean datasets with various options.
"""

import pandas as pd
from auto_data_clean import AutoDataClean, clean_data


def main():
    # Create sample data with duplicates and null values
    print("Creating sample dataset...")
    df = pd.DataFrame({
        'ID': [1, 2, 2, 3, 4, 5, 5],
        'Name': ['Alice', 'Bob', 'Bob', 'Charlie', None, 'Eve', 'Eve'],
        'Age': [25, 30, 30, None, 28, 35, 35],
        'Salary': [50000, 60000, 60000, 70000, 55000, None, None]
    })
    
    print("\n" + "=" * 50)
    print("ORIGINAL DATA")
    print("=" * 50)
    print(df)
    print(f"\nShape: {df.shape}")
    
    # Example 1: Remove both duplicates and nulls (default behavior)
    print("\n" + "=" * 50)
    print("EXAMPLE 1: Remove duplicates AND nulls")
    print("=" * 50)
    cleaner1 = AutoDataClean(remove_duplicates=True, remove_nulls=True)
    
    # Get summary before cleaning
    summary = cleaner1.get_summary(df)
    print(f"\nBefore cleaning:")
    print(f"  - Duplicate rows: {summary['duplicate_rows']}")
    print(f"  - Rows with nulls: {summary['rows_with_nulls']}")
    print(f"  - Null counts per column: {summary['null_counts_per_column']}")
    
    print("\nCleaning...")
    df_cleaned1 = cleaner1.clean(df)
    print(f"\nResult:\n{df_cleaned1}")
    
    # Example 2: Remove only duplicates
    print("\n" + "=" * 50)
    print("EXAMPLE 2: Remove ONLY duplicates (keep nulls)")
    print("=" * 50)
    cleaner2 = AutoDataClean(remove_duplicates=True, remove_nulls=False)
    df_cleaned2 = cleaner2.clean(df)
    print(f"\nResult:\n{df_cleaned2}")
    
    # Example 3: Remove only nulls
    print("\n" + "=" * 50)
    print("EXAMPLE 3: Remove ONLY nulls (keep duplicates)")
    print("=" * 50)
    cleaner3 = AutoDataClean(remove_duplicates=False, remove_nulls=True)
    df_cleaned3 = cleaner3.clean(df)
    print(f"\nResult:\n{df_cleaned3}")
    
    # Example 4: No cleaning (just for demonstration)
    print("\n" + "=" * 50)
    print("EXAMPLE 4: No cleaning (passthrough)")
    print("=" * 50)
    cleaner4 = AutoDataClean(remove_duplicates=False, remove_nulls=False)
    df_cleaned4 = cleaner4.clean(df)
    print(f"\nResult:\n{df_cleaned4}")
    
    # Example 5: Using the convenience function with CSV files
    print("\n" + "=" * 50)
    print("EXAMPLE 5: Working with CSV files")
    print("=" * 50)
    
    # Save sample data to CSV
    df.to_csv('sample_data.csv', index=False)
    print("Saved sample data to 'sample_data.csv'")
    
    # Clean directly from CSV
    df_from_csv = clean_data('sample_data.csv', 'sample_data_cleaned.csv')
    print(f"\nCleaned data from CSV:\n{df_from_csv}")


if __name__ == "__main__":
    main()
