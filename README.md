# ServiceNow CPQ Project Files

A Python-based data processing toolkit for ServiceNow CPQ data analysis and FDA device data processing.

## 🚀 Quick Start

### Prerequisites
- Python 3.12
- macOS (current setup)

### Setup Environment
```bash
# Option 1: Use the setup script (recommended)
./setup.sh

# Option 2: Manual setup
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Verify Installation
```bash
source .venv/bin/activate
python verify_setup.py
```

## 📁 Project Structure

```
servicenow-cpq-project-files/
├── .venv/                          # Virtual environment
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Full dependencies
├── requirements-minimal.txt        # Minimal dependencies
├── setup.sh                       # Automated setup script
├── verify_setup.py                # Environment verification
├── unzip.py                       # Main data processing script
├── testapi.py                     # FDA API testing script
└── README.md                      # This file
```

## 🔧 Core Scripts

### `unzip.py` - Data Processing Pipeline
Intelligently processes ZIP files containing JSON data and converts them to optimized CSV files.

**Features:**
- **Size-based chunking**: Splits large files into manageable chunks (default: 25MB each)
- **Smart optimization**: Removes empty columns and compresses output
- **Flexible configuration**: Easy-to-adjust settings for different use cases

**Usage:**
```bash
python unzip.py
```

**Configuration Options:**
```python
CONFIG = {
    'max_size_mb': 25,           # Max size per chunk in MB
    'sample_size': None,         # Limit rows (None = all rows)
    'remove_empty_columns': True, # Remove mostly empty columns
    'empty_threshold': 0.8,      # Empty column threshold
    'compress': True,            # Gzip compression
    'max_columns': None,         # Limit columns (None = all)
}
```

### `testapi.py` - FDA API Testing
Tests connectivity to the OpenFDA API and retrieves sample data.

**Usage:**
```bash
python testapi.py
```

## 📊 Data Processing Examples

### Processing Large Datasets
Your script automatically handles large files by:

1. **Loading JSON data** from ZIP files
2. **Analyzing structure** and removing empty columns
3. **Estimating optimal chunk size** based on target file size
4. **Splitting into manageable pieces** (e.g., 18 chunks for 172k+ rows)
5. **Compressing output** with gzip for 60-80% size reduction

**Example Output:**
```
device-510k-0001-of-0001_chunk_001.csv.gz (20,050 rows, 22.11 MB)
device-510k-0001-of-0001_chunk_002.csv.gz (20,050 rows, 22.28 MB)
...
device-510k-0001-of-0001_chunk_009.csv.gz (12,057 rows, 13.52 MB)
```

### Loading Processed Data
```python
import pandas as pd

# Load a single chunk
df = pd.read_csv('device-510k-0001-of-0001_chunk_001.csv.gz')

# Load all chunks
import glob
chunks = []
for file in glob.glob('device-510k-*_chunk_*.csv.gz'):
    chunk = pd.read_csv(file)
    chunks.append(chunk)
combined_df = pd.concat(chunks, ignore_index=True)
```

## 📋 Dependencies

### Core Libraries (Minimal)
- `pandas>=2.3.0` - Data manipulation and analysis
- `requests>=2.31.0` - HTTP requests for API calls

### Full Environment
- `numpy>=1.26.0` - Numerical computing
- `matplotlib>=3.8.0` - Plotting and visualization
- `seaborn>=0.13.0` - Statistical data visualization
- `plotly>=5.17.0` - Interactive plotting
- `openpyxl>=3.1.0` - Excel file support
- `scipy>=1.11.0` - Scientific computing
- `tqdm>=4.66.0` - Progress bars
- Development tools: `pytest`, `black`, `flake8`

## 🎯 Common Use Cases

### 1. Quick Data Exploration
```bash
# Process data with sampling for quick preview
python -c "
from unzip import CONFIG
CONFIG['sample_size'] = 1000
CONFIG['max_size_mb'] = 5
exec(open('unzip.py').read())
"
```

### 2. Production Processing
```bash
# Process all data with optimal settings
python unzip.py
```

### 3. Memory-Constrained Environments
```bash
# Smaller chunks for limited memory
python -c "
from unzip import CONFIG
CONFIG['max_size_mb'] = 10
CONFIG['remove_empty_columns'] = True
exec(open('unzip.py').read())
"
```

## 🔍 Troubleshooting

### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf .venv
./setup.sh
```

### Package Installation Issues
```bash
# Install minimal requirements only
pip install -r requirements-minimal.txt
```

### Large File Processing
- Reduce `max_size_mb` in CONFIG
- Enable `sample_size` for testing
- Use `remove_empty_columns` to reduce size

## 📈 Performance Tips

1. **Use compression**: Keep `compress: True` for 60-80% size reduction
2. **Remove empty data**: Enable `remove_empty_columns` 
3. **Right-size chunks**: Adjust `max_size_mb` based on your system
4. **Sample for testing**: Use `sample_size` during development

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `python verify_setup.py`
5. Submit a pull request

## 📝 License

This project is for internal ServiceNow CPQ data processing and analysis.

---

**Need help?** Run `python verify_setup.py` to check your environment or review the configuration options in `unzip.py`.
