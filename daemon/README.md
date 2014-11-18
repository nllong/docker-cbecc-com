
# Python CbeccComWrapper

## Running Example via Docker

T o use the Docker image to run an CIBD or XML modelFirst, first pull down the docker image `docker pull nllong/cbecc-com:daemon`

`cd` into the directory where the file is. (Make sure that you have a recent version of boot2docker running.)

```
docker run -it --rm -v "$(pwd)":/var/cbecc-com-files/run cbecc-com-service /var/cbecc-com-files/run.sh -i /var/cbecc-com-files/run/<filename>
```

## Testing on Docker/Wine

* Start the container and call the python script

```
docker run -it --rm -v $(pwd)/run:/var/cbecc-com-files/run cbecc-com-service /bin/bash
# you have to call xvfb because it is still looking for a GUI (runmanager probably)
./run.sh -i run/0200016-OffSml-SG-BaseRun.xml
```

## Testing on Windows

$ python RunCbeccCom.py -s windows -i run/0200016-OffSml-SG-BaseRun.xml

## Known Issues

* Most (if not all) of the paths that are sent to the DLL must have backslashes
* OpenStudio RunManager requires a frame buffer, hence the xvfb-run command

## Building Docker Image from Command Line

```
docker build -t cbecc-com .
```
