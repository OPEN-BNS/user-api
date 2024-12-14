User Directory API 

- GET users API

  URL : /users

- POST users API

  URL : /users

- Build using docker

  docker build -t <IMAGE_NAME> .

- Run using docker

  - Pre requisites : Start MySQL server on port localhost:3306, and create a database name : user_dir_app

  docker create network <NETWORK_NAME>

  docker run -d -p 9090:9090 --name user-dir-api --network <NETWORK_NAME> --restart always --log-opt mode=non-blocking --log-opt max-size=10M --log-opt max-file=10 -e ENCRYPTION_KEY=<PASSWORD_ENCRYPTION_KEY> -e MYSQL_PASSWORD=<MYSQL_PASSWORD> <IMAGE_NAME>

This project is made using FastAPI.
For detail documentation, please vist : http://<SERVER_PATH>/docs
