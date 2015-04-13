#!/bin/bash

echo "[run.sh] Running CBECC-Com CLI interface"
echo "[run.sh] Arguments are: $@"

export WINE_PYTHON=/root/.wine/drive_c/Python27/python.exe

# python RunCbeccCom.py $@

cd /var/cbecc-com-files/ && xvfb-run -a wine $WINE_PYTHON RunCbeccCom.py $@
