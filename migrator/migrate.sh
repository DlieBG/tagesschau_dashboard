#!/bin/bash

docker build . -t tagesschau_migrator
docker run --env-file .env.sample --net="host" migrator