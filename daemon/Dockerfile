FROM nllong/cbecc-com
MAINTAINER Nicholas Long <nicholas.long@nrel.gov>

# Install Python for Windows
ENV PYTHON_INSTALL_VERSION 2.7.8

RUN curl -SLO https://www.python.org/ftp/python/$PYTHON_INSTALL_VERSION/python-$PYTHON_INSTALL_VERSION.msi && \
    wine msiexec /i python-$PYTHON_INSTALL_VERSION.msi ALLUSERS=1 && \
    rm -f python-$PYTHON_INSTALL_VERSION.msi



# VNC server setup
#RUN mkdir -p ~/.vnc && x11vnc -storepasswd password ~/.vnc/passwd
#RUN bash -c 'echo "firefox" >> /.bashrc'

#EXPOSE 5900
