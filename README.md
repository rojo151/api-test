# -testAPI: python-flask-mongo-docker

This is a test RESTful API done with Python and MongoDB using Flask microframework. The project uses Docker to deploy both services.

## Stack

- Python 3
- Flask
- MongoDB
- Docker

## Startup

First of all, [install Docker](https://www.docker.com/products/docker-desktop) to run the containers:

Run 'docker-compose up' to start both the Flask app and the MongoDB in a dev environment

```sh
$ docker-compose up
```

## Structure

Folders and files structure.

```
├── docker-compose.yml
├── README.md
├── api-test
│   ├── app.py 
│   └── requirements.txt 

```

## Documentation

To access the service, send a JSON request to the endpoint: `http://localhost:5000/partium/echoservice`.

Response: 
 - The JSON object is stored in a Mongo database
 - A response is sent back with the original request-payload and, in addition, a
    field containing the server’s unix timestamp at the time of receiving the
    request.

The result of the POST request can be checked in the HTTP response, as well as in the MongoDB, available in the port 27017.
The new entry will be stored inside the 'jsonCollection' collection, found in the 'testClient' database. All the entries of the database are stored in a persistent volume to avoid the loss of the data.

## License

This project is open source, free to use and distribute.