#!/bin/bash

echo $@

cd /var/cbecc-com-files/ && xvfb-run -a wine /root/.wine/drive_c/Python27/python.exe RunCbeccCom.py $@

