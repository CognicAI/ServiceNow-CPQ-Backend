# FastAPI Local openFDA API

This FastAPI application provides access to three FDA device datasets through RESTful API endpoints.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
# Using uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Or using the run script
python run.py

# Or running main.py directly
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Root Endpoint
- `GET /` - Welcome message and endpoint information

### Device 510k API (`/device/510k`)
- `GET /device/510k/` - Get overview information about the 510k dataset
- `GET /device/510k/search` - Search and paginate through 510k records
  - Query parameters: `skip`, `limit`, `search`
- `GET /device/510k/{k_number}` - Get a specific 510k record by K number

### Device Classification API (`/device/classification`)
- `GET /device/classification/` - Get overview information about the classification dataset
- `GET /device/classification/search` - Search and paginate through classification records
  - Query parameters: `skip`, `limit`, `search`
- `GET /device/classification/product-code/{product_code}` - Get classification by product code
- `GET /device/classification/device-class/{device_class}` - Get classifications by device class

### Device Enforcement API (`/device/enforcement`)
- `GET /device/enforcement/` - Get overview information about the enforcement dataset
- `GET /device/enforcement/search` - Search and paginate through enforcement records
  - Query parameters: `skip`, `limit`, `search`
- `GET /device/enforcement/recall/{recall_number}` - Get enforcement by recall number
- `GET /device/enforcement/event/{event_id}` - Get enforcement by event ID
- `GET /device/enforcement/status/{status}` - Get enforcements by status

## Interactive Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Data Files

The API expects the following JSON data files in the `json files/` directory:
- `device-510k-0001-of-0001.json`
- `device-classification-0001-of-0001.json`
- `device-enforcement-0001-of-0001.json`

## Example Requests

```bash
# Get API overview
curl http://localhost:8000/

# Get 510k dataset overview
curl http://localhost:8000/device/510k/

# Search 510k records
curl "http://localhost:8000/device/510k/search?limit=10&search=cardiac"

# Get classification overview
curl http://localhost:8000/device/classification/

# Search classification records
curl "http://localhost:8000/device/classification/search?limit=5"

# Get enforcement overview
curl http://localhost:8000/device/enforcement/

# Search enforcement records by status
curl "http://localhost:8000/device/enforcement/search?search=ongoing"
```
