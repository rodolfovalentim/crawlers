CTLogs crawler
==============

Save certstream tail data.

### How to build:

On the path where the dockerfile exists run:

```
docker build --tag ctlogs-crawler .
```

### How to execute:

In the following, how to start a simple deployment.
You must host your own server running `0rickyy0/certstream-server-go`.
Thus you will start two containers (none of them run as `root`).
Check log path, container user ID and permissions.

Run the server:

```
docker run  --name CTLogs-server \
            -d --restart unless-stopped \
            -p 127.0.0.1:8080:8080 \
            0rickyy0/certstream-server-go
```

Run the crawler, supposing you want to store logs in the `data` folder:

```
docker run --name CTLogs-crawler \
           -d --restart unless-stopped \
           -e CT_URL=ws://127.0.0.1:8080/full-stream \
           -v $(pwd)/data:/usr/src/data \
           --user $(id -u):$(id -g) \
           --network host \
           ctlogs-crawler
```

It uses the following environemntal variable:

- `DATA_PATH`: where to store the logs (inside the container). Default: `/usr/src/data/`
- `CT_URL`: from where to download the feed. Default: `wss://certstream.calidog.io/`
