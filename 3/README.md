# CBECC-Com using Docker & Wine

This container runs [CBECC-com](http://bees.archenergy.com/software.html) using
Docker and Wine. This is the base image for other images such as the VNC based image.

## Pulling from Docker Hub

Not yet published

## Building from Docker File

```
docker build -t nllong/cbecc-com .
```

## Running Containter

* Inspecting Container

```
docker run -it --rm nllong/cbecc-com /bin/bash
```

* Running CBECC Com Daemon

Not yet implemented
