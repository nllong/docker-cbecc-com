# CBECC-Com using Docker & Wine - with VNC

Uses CBECC-Com base image with a VNC server for GUI access

## Pulling from Docker Hub

Not yet published

## Building from Docker File

```
docker build -t nllong/cbecc-com:vnc .
```

## Running Containter

* Inspecting Container

```
docker run -it --rm nllong/cbecc-com /bin/bash
```
* Running CBECC Com Daemon

Not yet implemented

* VNC

```
docker run -it --rm -p 5900:5900 cbecc-desktop x11vnc -forever -usepw -create

# In container you can start CBECC-Com by calling
wine /root/.wine/drive_c/Program\ Files/CBECC-Com\ 2013/CBECC-Com13.exe
```
