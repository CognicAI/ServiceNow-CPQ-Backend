import json
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).parent.parent.parent
# Directory containing data files
DATA_DIR = BASE_DIR / "data"

def _load_data(filename: str) -> dict:
    """Helper to load a JSON file and return its contents as a dict."""
    path = DATA_DIR / filename
    # If exact filename missing in data/, try globbing for prefix in data/ and 'json files'
    if not path.exists():
        prefix = filename.replace('.json', '')
        # Try matching in data directory
        matches = list(DATA_DIR.glob(f"{prefix}*.json"))
        if matches:
            path = matches[0]
        else:
            # Fallback to legacy 'json files' directory
            legacy_dir = BASE_DIR / 'json files'
            matches = list(legacy_dir.glob(f"{prefix}*.json")) if legacy_dir.exists() else []
            if matches:
                path = matches[0]
            else:
                raise FileNotFoundError(f"Data file not found: {filename}")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON file {path}: {e}")

def load_510k_data() -> dict:
    """Load and return the 510k dataset."""
    # Return only the list of 510k records
    return _load_data("device-510k-0001-of-0001.json").get("results", [])

def load_classification_data() -> dict:
    """Load and return the classification dataset."""
    # Return only the list of classification records
    return _load_data("device-classification-0001-of-0001.json").get("results", [])

def load_enforcement_data() -> dict:
    """Load and return the enforcement dataset."""
    # Return only the list of enforcement records
    return _load_data("device-enforcement-0001-of-0001.json").get("results", [])

def filter_data(records, search: str = None):
    """Filter a sequence or generator of records based on 'field:value' search."""
    # If no search provided or format is invalid, return all records
    if not search or ':' not in search:
        yield from records
        return
    # Parse field and search term
    field, _, term = search.partition(':')
    field = field.strip()
    term_lower = term.strip().lower()
    # Filter records
    for record in records:
        if field in record:
            if term_lower in str(record[field]).lower():
                yield record
