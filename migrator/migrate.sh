#!/bin/bash

cd tagesschau || exit
docker build . -t tagesschau_migrator
docker run --env-file ../.env.sample --net="host" tagesschau_migrator

cd ../newsapi || exit
docker build . -t newsapi_migrator
docker run --env-file ../.env.sample --net="host" newsapi_migrator