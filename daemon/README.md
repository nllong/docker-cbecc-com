
# Python CbeccComWrapper

## Testing on Docker/Wine

* Start the container and call the python script

```
docker run -it --rm -v $(pwd):/var/cbecc-com-files/share cbecc-com-service /bin/bash
cd /var/cbec-com-files/share/service
wine /root/.wine/drive_c/Python27/python.exe run.py
```

## Testing on Windows

python service/run.py


