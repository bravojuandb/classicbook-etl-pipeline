# 🐼 Pandas Cheat Sheet for `clean_aligned_books.py`

This cheat sheet is tailored to the tools and functions you're likely using in your ETL script for cleaning and aligning book text data.

---

## 🧱 Creating & Loading DataFrames
```python
import pandas as pd

# From CSV or TSV
df = pd.read_csv("file.csv")              # default comma
df = pd.read_csv("file.tsv", sep="\t")    # tab-separated

# From dictionary or list
df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
```

---

## 🔍 Inspecting the Data
```python
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.info()           # Summary (column types, nulls)
df.shape            # Rows and columns (tuple)
df.columns          # Column names
```

---

## ✍️ Renaming Columns
```python
df.columns = ['new_col1', 'new_col2']
df.rename(columns={'old': 'new'}, inplace=True)
```

---

## 🧼 Cleaning & Text Preprocessing
```python
df.dropna()                      # Drop rows with any nulls
df.dropna(subset=['col'])       # Drop if specific column is null
df.fillna('Unknown')            # Replace nulls

df['col'] = df['col'].str.strip()      # Trim whitespace
df['col'] = df['col'].str.lower()      # Lowercase
df['col'] = df['col'].str.replace('\n', ' ')  # Replace newline

# Remove special characters (regex)
df['col'] = df['col'].str.replace(r'[^\w\s]', '', regex=True)
```

---

## 🔄 Filtering and Replacing
```python
df[df['col'] == 'value']          # Filter by value
df['col'] = df['col'].replace('old', 'new')     # Replace value
df['col'] = df['col'].apply(lambda x: x[:100])  # Truncate to first 100 chars
```

---

## 🔗 Working with Two Columns
```python
# Example: align Latin and English
df = pd.DataFrame({'latin': latins, 'english': englishs})
```

---

## 📤 Exporting Cleaned Data
```python
df.to_csv('cleaned_output.csv', index=False)
df.to_csv('cleaned_output.tsv', sep='\t', index=False)
```

---

## ✅ Useful Checks
```python
df.isnull().sum()        # Count nulls per column
df.duplicated().sum()    # Count duplicates
df['col'].value_counts() # Frequency of values
```

---

## 🛠️ Useful Options
```python
pd.set_option('display.max_colwidth', None)  # Show full text in cells
```
