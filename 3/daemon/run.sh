#!/bin/bash

echo "Running CBECC-Com CLI interface"
echo $@

export WINE_PYTHON=/root/.wine/drive_c/Python27/python.exe

cd /var/cbecc-com-files/ && xvfb-run -a wine $WINE_PYTHON RunCbeccCom.py $@
