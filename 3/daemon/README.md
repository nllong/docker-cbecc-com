
# Python CbeccComWrapper

## Running Example via Docker

To use the Docker image to run an CIBD or XML model. First, first pull down the docker image `docker pull nllong/cbecc-com:daemon`. Builds are managed via [Docker Hub's Automated Builds](https://registry.hub.docker.com/u/nllong/cbecc-com/)

`cd` into the directory where the file is. (Make sure that you have a recent version of boot2docker running.)

```
docker run -it --rm -v "$(pwd)":/var/cbecc-com-files/run cbecc-com-service /var/cbecc-com-files/run.sh -i /var/cbecc-com-files/run/<filename>
```

## Testing on Docker/Wine

* Start the container and call the python script

Each file should be run in its own directory because the output is at the same level as the input file

```
docker run -it --rm -v $(pwd)/test:/var/cbecc-com-files/test cbecc-com /bin/bash
./run.sh -i test/0200016-OffSml-SG-BaseRun.xml
```

## Testing on Windows

$ python RunCbeccCom.py -s windows -i run/0200016-OffSml-SG-BaseRun.xml

## Known Issues

* Most (if not all) of the paths that are sent to the DLL must have backslashes
* OpenStudio RunManager requires a frame buffer, hence the xvfb-run command in the run.sh file

## Building Docker Image from Command Line

```
docker build -t cbecc-com .
```
