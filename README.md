# Microservices with Django and gRPC

A demonstration project for microservices architecture using Django for web services and gRPC for high-performance inter-service communication.

## Architecture Overview

The system consists of two primary services:

- **User Service (`service-2`)**: Manages user profiles and coordinates with the Address service to retrieve location details.
- **Address Service (`service-1`)**: Manages a database of addresses and exposes a gRPC server for low-latency lookups.

Inter-service communication is handled via gRPC using Protocol Buffers defined in the `protos/` directory.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.10+ (for local development)

### Running with Docker

The easiest way to get the entire system up and running is using Docker Compose:

```bash
docker-compose up --build
```

This will start:
- **User Service**: [http://localhost:8000](http://localhost:8000)
- **Address Service**: [http://localhost:8001](http://localhost:8001)
- **Address gRPC Server**: `localhost:50051`

## Project Structure

- `protos/`: Protocol Buffer definitions (`.proto` files).
- `service-1/`: Address microservice (Django).
- `service-2/`: User microservice (Django).
- `docker-compose.yml`: Container orchestration for all services.

## Development

To generate gRPC code from `.proto` files after making changes:

```bash
python -m grpc_tools.protoc -I./protos --python_out=./service-1/address/grpc_gen --grpc_python_out=./service-1/address/grpc_gen ./protos/address.proto
python -m grpc_tools.protoc -I./protos --python_out=./service-2/user/grpc_gen --grpc_python_out=./service-2/user/grpc_gen ./protos/address.proto
```
