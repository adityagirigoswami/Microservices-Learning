#!/bin/bash

# Start the gRPC server in the background
PYTHONPATH=. python address/grpc_server.py &

# Start the Django development server
python manage.py runserver 0.0.0.0:8001
