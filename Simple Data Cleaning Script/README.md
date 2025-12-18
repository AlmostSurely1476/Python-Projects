# Auto Data Clean

A flexible Python class for automatic dataset cleaning. Easily remove duplicates and null values from your pandas DataFrames with customizable options.

## Features

- **Remove Duplicates**: Automatically detect and remove duplicate rows
- **Remove Null Values**: Clean rows containing missing/null values
- **Flexible Configuration**: Choose which cleaning operations to apply
- **Data Summary**: Get insights about your data before cleaning
- **CSV Support**: Convenience function for direct CSV file cleaning

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/auto-data-clean.git
cd auto-data-clean
```

2. Install the required dependency:
```bash
pip install pandas
```

## Usage

### Basic Usage

```python
import pandas as pd
from auto_data_clean import AutoDataClean

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Create a cleaner with desired options
cleaner = AutoDataClean(remove_duplicates=True, remove_nulls=True)

# Clean the dataset
df_cleaned = cleaner.clean(df)

# Save the cleaned dataset
df_cleaned.to_csv('your_dataset_cleaned.csv', index=False)
```

### Customizing Cleaning Options

```python
# Remove only duplicates, keep null values
cleaner = AutoDataClean(remove_duplicates=True, remove_nulls=False)
df_cleaned = cleaner.clean(df)

# Remove only null values, keep duplicates
cleaner = AutoDataClean(remove_duplicates=False, remove_nulls=True)
df_cleaned = cleaner.clean(df)
```

### Get Data Summary Before Cleaning

```python
cleaner = AutoDataClean()
summary = cleaner.get_summary(df)

print(f"Total rows: {summary['total_rows']}")
print(f"Duplicate rows: {summary['duplicate_rows']}")
print(f"Rows with nulls: {summary['rows_with_nulls']}")
print(f"Null counts per column: {summary['null_counts_per_column']}")
```

### Quick CSV Cleaning

```python
from auto_data_clean import clean_data

# Clean a CSV file directly
df_cleaned = clean_data('input.csv', 'output_cleaned.csv')
```

## API Reference

### `AutoDataClean` Class

#### Constructor
```python
AutoDataClean(remove_duplicates=True, remove_nulls=True)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `remove_duplicates` | bool | True | Whether to remove duplicate rows |
| `remove_nulls` | bool | True | Whether to remove rows with null values |

#### Methods

##### `clean(df, inplace=False)`
Clean the DataFrame based on configured options.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `df` | pd.DataFrame | - | The input DataFrame to clean |
| `inplace` | bool | False | If True, modifies the original DataFrame |

**Returns**: `pd.DataFrame` - The cleaned DataFrame

##### `get_summary(df)`
Get a summary of potential cleaning operations without modifying the data.

**Returns**: `dict` containing:
- `total_rows`: Total number of rows
- `duplicate_rows`: Number of duplicate rows
- `rows_with_nulls`: Number of rows containing null values
- `null_counts_per_column`: Null counts for each column

### `clean_data()` Function

```python
clean_data(filepath, output_filepath=None, remove_duplicates=True, remove_nulls=True)
```

Convenience function to clean a CSV file directly.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `filepath` | str | - | Path to the input CSV file |
| `output_filepath` | str | None | Path to save the cleaned CSV |
| `remove_duplicates` | bool | True | Whether to remove duplicate rows |
| `remove_nulls` | bool | True | Whether to remove rows with null values |

## Example

Run the example script to see the class in action:

```bash
python example.py
```

## Requirements

- Python 3.6+
- pandas

## License

MIT License - feel free to use this in your projects!

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
