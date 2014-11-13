
# Python CbeccComWrapper

## Running Example via Docker

```
docker run -it --rm -p 5900:5900 -v $(pwd)/run:/var/cbecc-com-files/run cbecc-com-service /var/cbecc-com-files/run.sh -i /var/cbecc-com-files/run/0200016-OffSml-SG-BaseRun.xml
```

## Running Another File


## Testing on Docker/Wine

* Start the container and call the python script

```
docker run -it --rm -v $(pwd)/run:/var/cbecc-com-files/run cbecc-com-service /bin/bash
# you have to call xvfb because it is still looking for a GUI (runmanager probably)
./run.sh -i run/0200016-OffSml-SG-BaseRun.xml
```

## Testing on Windows

$ python RunCbeccCom.py -i run/0200016-OffSml-SG-BaseRun.xmlpy


