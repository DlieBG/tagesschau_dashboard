#!/bin/bash

cd tagesschau || exit
docker build . -t tagesschau_migrator:latest
docker run --env-file ../.env.sample --net="host" tagesschau_migrator:latest

cd ../newsapi || exit
docker build . -t newsapi_migrator:latest
docker run --env-file ../.env.sample --net="host" newsapi_migrator:latest