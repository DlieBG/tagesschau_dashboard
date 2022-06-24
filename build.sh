#!/bin/bash

sudo rm -rf ./data/postgres
docker-compose -f docker-compose-visualize.yml up --build --force-recreate -d

sleep 10

cd migrator || exit
docker-compose up --build --force-recreate
cd ../cleaner  || exit
docker-compose up --build --force-recreate
cd ../regionMatcher  || exit
docker-compose up --build --force-recreate
