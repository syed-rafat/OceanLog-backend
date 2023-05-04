#!/usr/bin/env bash

# This script is used to initialize the database for the first time.
# It will create the database, create the tables, and populate the tables with data.

sudo service postgresql start

DB_NAME=oc
PG_USER=ocmanager
PG_PASSWORD=ocpostgres

# Check if database and user already exist
if sudo -u postgres psql -t -c "\l | grep -w $DB_NAME" | grep -q $DB_NAME && sudo -u postgres psql -t -c "SELECT 1 FROM pg_user WHERE usename='$PG_USER'" | grep -q 1; then
    echo "Database and user already exist"
    exit 0
else
    # Create the database if it doesn't exist
    if ! sudo -u postgres psql -t -c "\l | grep -w $DB_NAME" | grep -q $DB_NAME; then
        sudo -u postgres psql -c "CREATE DATABASE $DB_NAME"
    fi

    # Create the user if it doesn't exist
    if ! sudo -u postgres psql -t -c "SELECT 1 FROM pg_user WHERE usename='$PG_USER'" | grep -q 1; then
        sudo -u postgres psql -c "CREATE USER $PG_USER WITH PASSWORD '$PG_PASSWORD'"
    fi

    # Set permissions for the user
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $PG_USER"
fi

sudo usermod -aG $(whoami) postgres

