## Example 1 - Containerizing a simple webscraper app.

1 - Create movie scraper `main.py` for best 250 movies.

2 - Create `Dockerfile`.

3 - Build Docker image.

```bash
docker build -t python-imdb .
```

4 - Create and run the image.

```bash
docker run python-imdb
```

5 - After modifying file, the program is able to take in user input. Therefore, rebuild the docker image.

6 - To allow interactive mode, we need run the new image using following command.

```bash
docker run -i -t python-imdb
```

`-i` - interactive mode and `-t` - terminal mode.

## Example 2 - Containerizing an API app

1 - As this is just for demo purpose, we took an example from official documentation of FastAPI and copied it in `main.py`

2 - Spin up the fastapi server on local machine before dockerizing it.

```bash
uvicorn main:app --reload
```

3 - Create `Dockerfile`.

4 - Build Docker image.

```bash
docker build -t fastapi-image .
```

5 - Run the image.

```bash
docker run -p 80:80 fastapi-image
```

6 - Name the container and run in the background.

```bash
docker run -d --name myfastapicontainer -p 80:80 fastapi-image
```

`-p` 80:80: Map the port from outside to the port from the container

Host in Dockerfile must be:

`host: 0.0.0.0`: "placeholder", it tells a server to listen for and accept connections from any IP address ("all IPv4 addresses on the local machine").

7 - Whenever we run the image, a new container is created. This consumes a lot of space in the hard drive. Therefore, we can also run its container by first going to the desktop app and click on play button.

8 - To check if the docker container is running.

```bash
docker ps
```

9 - To browse inside the container via command line. We can also directly access it via the Docker Desktop app.

```bash
docker exec -it myfastapicontainer </bin/sh or bash>
```
