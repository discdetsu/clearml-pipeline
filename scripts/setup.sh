#!/bin/bash

# ClearML Setup Script
# This script sets up the ClearML environment and creates necessary directories

set -e

echo "🚀 Setting up ClearML environment..."

# Create required local directories
echo "📁 Creating local data directories..."
mkdir -p config data logs
mkdir -p data/{elastic,mongo/{db,configdb},redis,fileserver,agent}

# Set proper permissions
echo "🔐 Setting directory permissions..."
chmod -R 755 data config logs

echo "📋 Checking Docker and Docker Compose..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "🐳 Starting ClearML services..."
docker-compose up -d

echo "⏳ Waiting for services to start..."
sleep 30

echo "🔍 Checking service status..."
docker-compose ps

echo ""
echo "✅ ClearML setup complete!"
echo ""
echo "🌐 Access the web UI at: http://localhost:8080"
echo "📡 API server available at: http://localhost:8008"
echo "📁 File server available at: http://localhost:8081"
echo ""
echo "📖 Next steps:"
echo "1. Open http://localhost:8080 in your browser"
echo "2. Go to Settings → Workspace → App Credentials"
echo "3. Generate API credentials and update the .env file"
echo "4. Install ClearML SDK: pip install clearml"
echo "5. Run clearml-init to configure your client"
echo ""
echo "🧪 To run the example experiment:"
echo "cd experiments && python example_experiment.py"