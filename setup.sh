#!/bin/bash
# Setup script for ServiceNow CPQ Project
# This script sets up the Python environment and installs all dependencies

set -e  # Exit on any error

echo "🚀 Setting up ServiceNow CPQ Project Environment"
echo "================================================"

# Check if Python 3.12 is available
if ! command -v python3.12 &> /dev/null; then
    echo "❌ Python 3.12 not found. Please install Python 3.12 first."
    exit 1
fi

echo "✅ Python 3.12 found"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment with Python 3.12..."
    python3.12 -m venv .venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "📥 Installing full requirements..."
    pip install -r requirements.txt
elif [ -f "requirements-minimal.txt" ]; then
    echo "📥 Installing minimal requirements..."
    pip install -r requirements-minimal.txt
else
    echo "📥 Installing core packages..."
    pip install pandas requests
fi

echo ""
echo "✨ Setup complete! Your environment is ready."
echo ""
echo "💡 To activate the environment in the future, run:"
echo "   source .venv/bin/activate"
echo ""
echo "🧪 To verify your setup, run:"
echo "   python verify_setup.py"

# Optional: Move JSON files into data/ folder
echo ""
echo "📂 Moving JSON files into data/ folder..."
if [ -d "json files" ]; then
    mkdir -p data
    mv "json files/device-510k-0001-of-0001.json" data/device-510k.json
    mv "json files/device-classification-0001-of-0001.json" data/device-classification.json
    mv "json files/device-enforcement-0001-of-0001.json" data/device-enforcement.json
    echo "✅ JSON files moved"
else
    echo "⚠️  No 'json files' directory found; skipping JSON file move"
fi

# Start the FastAPI server
echo ""
echo "🚀 Starting the FastAPI server..."
source .venv/bin/activate
python run.py
