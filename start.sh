#!/bin/sh
source env/bin/activate &
cd ./main
python3 flask_server.py &
cd ../knn-frontend
npm start
