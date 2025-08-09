# ServiceNow CPQ Backend

A comprehensive Python-based FastAPI backend for FDA device data processing and analysis. This project provides both data processing capabilities and a RESTful API for accessing FDA device datasets including 510k clearances, device classifications, and enforcement actions.

## 🚀 Quick Start

### Prerequisites
- Python 3.12
- macOS/Linux (tested on macOS)
- Git

### Setup Environment
```bash
# Clone the repository (if not already done)
git clone <repository-url>
cd ServiceNow-CPQ-Backend

# Create and activate virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the API Server
```bash
# Activate virtual environment
source venv/bin/activate

# Run the FastAPI server
python main.py

# Alternative: Use the run script
python run.py

# Alternative: Use uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- **API Base URL**: `http://localhost:8000`
- **Interactive Docs (Swagger)**: `http://localhost:8000/docs`
- **Alternative Docs (ReDoc)**: `http://localhost:8000/redoc`

## 📁 Project Structure

```
ServiceNow-CPQ-Backend/
├── venv/                           # Virtual environment (Python 3.12)
├── app/                            # FastAPI application
│   ├── __init__.py
│   └── api/                        # API endpoints
│       ├── __init__.py
│       ├── classification.py       # Device classification endpoints
│       ├── data_loader.py          # Data loading utilities
│       ├── device_510k.py          # 510k clearance endpoints
│       └── enforcement.py          # Enforcement action endpoints
├── data/                           # FDA dataset files (JSON)
│   ├── device-510k-0001-of-0001.json
│   ├── device-classification-0001-of-0001.json
│   └── device-enforcement-0001-of-0001.json
├── main.py                         # FastAPI application entry point
├── run.py                          # Alternative server runner
├── requirements.txt                # Python dependencies
├── setup.sh                       # Automated setup script
├── API_README.md                   # API-specific documentation
└── README.md                      # This file
```

## 🔧 API Endpoints

### Root Endpoint
- `GET /` - Welcome message and available endpoints overview

### Device 510k Clearances (`/device/510k`)
Access FDA 510k medical device clearance data.

**Endpoints:**
- `GET /device/510k/` - Search and paginate through 510k records
  - **Query Parameters:**
    - `search` (optional): Filter string in format "field:value"
    - `skip` (default: 0): Number of records to skip for pagination
    - `limit` (default: 10): Number of records to return (max recommended: 100)

**Example Requests:**
```bash
# Get first 10 510k records
curl "http://localhost:8000/device/510k/"

# Search for cardiac devices with pagination
curl "http://localhost:8000/device/510k/?search=cardiac&skip=0&limit=5"

# Get records 20-30
curl "http://localhost:8000/device/510k/?skip=20&limit=10"
```

### Device Classifications (`/device/classification`)
Access FDA medical device classification data.

**Endpoints:**
- `GET /device/classification/` - Search and paginate through classification records
  - **Query Parameters:** Same as 510k endpoint

**Example Requests:**
```bash
# Get classification records
curl "http://localhost:8000/device/classification/?limit=5"

# Search for specific device classes
curl "http://localhost:8000/device/classification/?search=Class II"
```

### Device Enforcement Actions (`/device/enforcement`)
Access FDA device enforcement and recall data.

**Endpoints:**
- `GET /device/enforcement/` - Search and paginate through enforcement records
  - **Query Parameters:** Same as 510k endpoint

**Example Requests:**
```bash
# Get enforcement records
curl "http://localhost:8000/device/enforcement/?limit=5"

# Search for ongoing enforcement actions
curl "http://localhost:8000/device/enforcement/?search=ongoing"
```

## 📊 API Response Format

All endpoints return data in a consistent format:

```json
{
  "meta": {
    "total_count": 172419,
    "skip": 0,
    "limit": 10,
    "returned_count": 10
  },
  "results": [
    {
      // Individual record data
    }
  ]
}
```

## 🛠️ Development Features

### Interactive API Documentation
- **Swagger UI**: `http://localhost:8000/docs` - Full interactive API explorer
- **ReDoc**: `http://localhost:8000/redoc` - Alternative documentation view

### Development Mode
```bash
# Run with auto-reload for development
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Testing the API
```bash
# Test root endpoint
curl http://localhost:8000/

# Check API health
curl http://localhost:8000/device/510k/?limit=1
```

## � Technology Stack

### Backend Framework
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for running the FastAPI application
- **Pydantic** - Data validation and settings management

### Data Processing
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing support

### Development Tools
- **Black** - Code formatting
- **Flake8** - Code linting
- **Pytest** - Testing framework

### Additional Libraries
- **Requests** - HTTP client for external API calls
- **Matplotlib/Seaborn/Plotly** - Data visualization
- **Jupyter** - Interactive development and analysis
- **OpenPyXL** - Excel file support

### Key Dependencies
```txt
fastapi>=0.104.0          # Web framework
uvicorn>=0.24.0           # ASGI server
pandas>=2.3.0             # Data manipulation
numpy>=1.26.0             # Numerical computing
requests>=2.31.0          # HTTP requests
pydantic>=2.0.0           # Data validation
```

## 🚀 Deployment & Production

### Production Setup
```bash
# Install production dependencies
pip install -r requirements.txt

# Run with production settings
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Environment Variables
```bash
# Optional environment variables
export PORT=8000
export HOST=0.0.0.0
export WORKERS=4
```

### Docker Support (Optional)
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📈 Performance & Optimization

### API Performance Tips
1. **Pagination**: Use `skip` and `limit` parameters for large datasets
2. **Filtering**: Use `search` parameter to reduce response size
3. **Caching**: Data is loaded into memory for fast access
4. **Compression**: Enable gzip compression for responses

### System Requirements
- **RAM**: 4GB minimum (8GB recommended for large datasets)
- **Storage**: 2GB for data files and dependencies
- **CPU**: Multi-core recommended for concurrent requests

## 🔍 Data Sources

The API serves data from three FDA datasets:

### 1. Device 510k Clearances (`device-510k-0001-of-0001.json`)
- **Records**: ~172,000+ medical device clearances
- **Content**: Device descriptions, manufacturers, clearance dates, product codes
- **Update Frequency**: Regular FDA updates

### 2. Device Classifications (`device-classification-0001-of-0001.json`)
- **Records**: Medical device classification database
- **Content**: Product codes, device classes, regulations, descriptions
- **Usage**: Understanding device regulatory categories

### 3. Device Enforcement Actions (`device-enforcement-0001-of-0001.json`)
- **Records**: FDA enforcement actions and recalls
- **Content**: Recall information, affected products, enforcement status
- **Importance**: Safety and compliance monitoring

## 🔍 Troubleshooting

### Common Issues

#### Virtual Environment Problems
```bash
# Recreate virtual environment
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process (replace PID with actual process ID)
kill -9 <PID>

# Or use a different port
uvicorn main:app --port 8001
```

#### Data File Issues
```bash
# Verify data files exist
ls -la data/

# Check file permissions
chmod 644 data/*.json
```

#### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check Python path
python -c "import sys; print(sys.path)"
```

### Debug Mode
```bash
# Run with debug logging
uvicorn main:app --log-level debug --reload
```

### Health Checks
```bash
# Test API connectivity
curl -f http://localhost:8000/ || echo "API not responding"

# Check specific endpoint
curl -f "http://localhost:8000/device/510k/?limit=1" || echo "Data loading issue"
```

## 🧪 Testing

### Manual API Testing
```bash
# Test all main endpoints
curl http://localhost:8000/
curl "http://localhost:8000/device/510k/?limit=1"
curl "http://localhost:8000/device/classification/?limit=1"
curl "http://localhost:8000/device/enforcement/?limit=1"
```

### Automated Testing (Future)
```bash
# Run test suite (when implemented)
pytest tests/

# Coverage report
pytest --cov=app tests/
```

## 🤝 Contributing

### Development Setup
```bash
# Fork the repository
git clone <your-fork-url>
cd ServiceNow-CPQ-Backend

# Create development branch
git checkout -b feature/your-feature-name

# Set up environment
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Code Standards
- Follow PEP 8 style guidelines
- Use Black for code formatting: `black app/`
- Run linting: `flake8 app/`
- Add type hints where appropriate
- Document new endpoints in API_README.md

### Submission Process
1. Create feature branch
2. Make changes and test locally
3. Update documentation if needed
4. Submit pull request with description

## 📝 License & Usage

This project is designed for ServiceNow CPQ data processing and analysis. The FDA data is public domain, but please respect the FDA's terms of use for their datasets.

### Data Attribution
- Data Source: U.S. Food and Drug Administration (FDA)
- API: openFDA (https://open.fda.gov/)
- License: Public Domain

## 📞 Support

### Getting Help
1. Check this README for common solutions
2. Review the [API_README.md](API_README.md) for API-specific details
3. Test with interactive docs at `http://localhost:8000/docs`
4. Check the terminal output for error messages

### Useful Commands
```bash
# Check Python version
python --version

# List installed packages
pip list

# Check virtual environment
which python

# Test basic functionality
python -c "import fastapi, pandas, uvicorn; print('Dependencies OK')"
```

---

**🎯 Quick Reference**: After setup, run `python main.py` and visit `http://localhost:8000/docs` for interactive API exploration!
