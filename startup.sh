#!/bin/bash
# This script is used to start the application
cd pg/
echo "Creating Database .. Starting application"
docker-compose up -d
echo "Starting ETL Process"
cd ../data_ingestion
python3 etl.py