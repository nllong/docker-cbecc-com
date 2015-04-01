# CBECC-Com using Docker & Wine

This container runs [CBECC-com](http://bees.archenergy.com/software.html) using
Docker and Wine. This is the base image for other images such as the VNC based image.

## Pulling from Docker Hub

```
docker pull nllong/cbecc-com:3
```

## Building from Docker File

```
docker build -t nllong/cbecc-com .
```

## Running Container

* Inspecting Container

```
docker run -it --rm nllong/cbecc-com /bin/bash
```

* Running a CBECC COM file for testing

```
docker run -it --rm -v $(pwd)/cbecc-test-inputs:/var/cbecc-com-files/run/  nllong/cbecc-com /bin/bash /var/cbecc-com-files/daemon/run.sh -i /var/cbecc-com-files/run

/var/cbecc-com-files/run.sh -i /var/cbecc-com-files/run


* Running CBECC Com Daemon

Not yet implemented


## Running test files
