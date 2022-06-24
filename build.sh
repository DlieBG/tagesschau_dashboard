#!/bin/bash

cd db || exit
sudo docker-compose down
sudo rm -rf ./data/postgres
sudo docker-compose up --build --force-recreate -d
sleep 10

cd ../migrate || exit
sudo docker-compose up --build --force-recreate

cd ../process || exit
cd ./cleaner || exit
sudo docker-compose up --build --force-recreate
cd ../regionMatcher  || exit
sudo docker-compose up --build --force-recreate
