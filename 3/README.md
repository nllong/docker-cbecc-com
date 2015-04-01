# CBECC-Com using Docker, Wine, and Python

This container runs [CBECC-Com](http://bees.archenergy.com/software.html) using Docker and Wine. There is a wrapper around the CBECC-Com DLLs implemented in python to 'easily' launch the application using a headless server. Builds are managed via [Docker Hub's Automated Builds](https://registry.hub.docker.com/u/nllong/cbecc-com/)

## Running Example

To use the Docker image to run an CIBD or XML model.

* Install and launch [boot2docker](https://github.com/boot2docker/boot2docker)
* Pull the most recent docker image `docker pull nllong/cbecc-com`.
* `cd` into the directory where the XML or CBID CBECC-Com file is. (Make sure that you have a recent version of boot2docker running.)

    ```
    docker run -it --rm -v $(pwd):/var/cbecc-com-files/run nllong/cbecc-com /var/cbecc-com-files/run.sh -i /var/cbecc-com-files/run/<filename>
    ```

* The file should run and all the outputs should be in your local folder

## Building from Docker File

To build the container locally run

```
docker build -t nllong/cbecc-com .
```

You can inspect the container by running

```
docker run -it --rm nllong/cbecc-com /bin/bash
```

# Using the Python CbeccComWrapper

## Testing on Docker/Wine

* Start the container and call the python script

Each file should be run in its own directory because the output is at the same level as the input file

```
docker run -it --rm -v $(pwd)/test:/var/cbecc-com-files/test cbecc-com /bin/bash
./run.sh -i test/0200016-OffSml-SG-BaseRun.xml
```

or

```
docker run -it --rm -v $(pwd)/test:/var/cbecc-com-files/test cbecc-com ./run.sh -i test/0200016-OffSml-SG-BaseRun.xml
```

## Testing on Windows

To test the CbeccComWrapper on windows run

```
$ python RunCbeccCom.py -s windows -i run/0200016-OffSml-SG-BaseRun.xml
```

## Known Issues

* Most (if not all) of the paths that are sent to the DLL must have backslashes
* OpenStudio RunManager requires a frame buffer, hence the xvfb-run command in the run.sh file
