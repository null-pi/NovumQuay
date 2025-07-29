#!/bin/bash

# Set the default value for PRODUCTION if not provided
PRODUCTION=${PRODUCTION:-"false"}

cd /app/src

# Run the FastAPI application based on the value of PRODUCTION
if [ -z "$PRODUCTION" ] || [ "$PRODUCTION" = "false" ]; then
    uvicorn main:app --host 0.0.0.0 --port ${SERVER_PORT:-8001} --reload --log-config="log_config.yaml"
elif [ "$PRODUCTION" = "true" ]; then
    fastapi run --host 0.0.0.0 --port ${SERVER_PORT:-8001}
else
    echo "Invalid value for PRODUCTION: $PRODUCTION"
    exit 1
fi


