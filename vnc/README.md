# CBECC-Com using Docker & Wine - with VNC

Uses CBECC-Com base image with a VNC server for GUI access. This is used for testing when upgrading to new versions of CBECC-Com

## Building from Docker File

```
docker build -t cbecc-vnc .
```

## Running Containter

* Inspecting Container

```
docker run -it --rm cbecc-vnc /bin/bash
```

* Running VNC Server

```
docker run -it --rm -p 5900:5900 -v $(pwd)/test:/var/cbecc-com-files cbecc-desktop bash
x11vnc -forever -usepw -create

# Connect to VNC via the boot2docker IP address

# In container you can start CBECC-Com by calling
wine /root/.wine/drive_c/Program\ Files/CBECC-Com\ 2013/CBECC-Com13.exe
```
