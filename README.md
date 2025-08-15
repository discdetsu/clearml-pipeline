# ClearML Pipeline Project

This project sets up a complete ClearML environment using Docker Compose for experiment tracking and ML pipeline management.

## Quick Start

1. **Start ClearML services:**
   ```bash
   docker-compose up -d
   ```

2. **Access the Web UI:**
   - Open http://localhost:8080 in your browser
   - Default login: no authentication required

3. **API endpoints:**
   - Web UI: http://localhost:8080
   - API Server: http://localhost:8008
   - File Server: http://localhost:8081

## Services

- **apiserver**: Core API and logic
- **webserver**: Web UI interface
- **fileserver**: Artifact and model storage
- **elasticsearch**: Search and analytics
- **mongodb**: Metadata storage
- **redis**: Caching and job queues
- **async_delete**: Background cleanup tasks
- **agent-services**: ML task execution

## Configuration

1. Copy `.env.example` to `.env` and configure:
   ```bash
   cp .env .env.local
   ```

2. After first startup, get API credentials from the Web UI:
   - Go to Settings → Workspace → App Credentials
   - Generate new credentials
   - Update `.env` file with the keys

## Directory Structure

```
├── config/          # ClearML configuration files
├── data/            # Persistent data storage (all volumes local)
│   ├── elastic/     # Elasticsearch data
│   ├── mongo/       # MongoDB data
│   ├── redis/       # Redis data
│   ├── fileserver/  # File storage
│   └── agent/       # Agent configuration
├── logs/            # Application logs
├── experiments/     # Your ML experiments
├── scripts/         # Utility scripts
└── docker-compose.yml
```

## System Requirements

- **Memory**: Minimum 8GB, recommended 16GB
- **Ports**: 8080, 8081, 8008 must be available
- **Docker**: Docker and Docker Compose installed
- **Storage**: All data stored locally in project directory

## Usage

### Stop services:
```bash
docker-compose down
```

### View logs:
```bash
docker-compose logs -f [service_name]
```

### Reset data (caution - deletes all data):
```bash
docker-compose down -v
sudo rm -rf /opt/clearml/data
```

## Next Steps

1. Install ClearML SDK: `pip install clearml`
2. Configure your development environment
3. Start creating experiments in the `experiments/` directory