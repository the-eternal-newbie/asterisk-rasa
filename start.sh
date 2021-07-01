##!/bin/bash
DEEPSPEECH_DIR="./rasa-bot/deepspeech-models/"
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
        if [ -d "$DEEPSPEECH_DIR" ]; then
            echo "Deepspeech already downloaded..."
        else
            cd ./rasa-bot/ && \
                wget https://github.com/mozilla/DeepSpeech/releases/download/v0.5.1/deepspeech-0.5.1-models.tar.gz && \
                tar xvfz deepspeech-0.5.1-models.tar.gz && mv deepspeech-0.5.1-models deepspeech-models && \
                mv ._deepspeech-0.5.1-models ._deepspeech-models && rm deepspeech-0.5.1-models.tar.gz
        fi
    fi
fi