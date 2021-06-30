##!/bin/bash

OPTION="$1"
DOWN="down"
CLEAN="clean"
if [ $OPTION = $CLEAN ];
then
    docker-compose down && docker rm -f $(docker ps -a -q) && docker volume rm $(docker volume ls -q)
else
    if [ $OPTION = $DOWN ];
    then
        docker-compose down
    else
        docker-compose -f docker-compose.yml up -d && docker container exec -it -d rasa-bot bash -c "cd rasa && rasa run -m models --enable-api"
    fi
fi