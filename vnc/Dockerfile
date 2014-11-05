FROM nllong/cbecc-com
MAINTAINER Nicholas Long <nicholas.long@nrel.gov>

# Install LXDE and VNC server.
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal x11vnc firefox && \
  rm -rf /var/lib/apt/lists/*

# VNC server setup
RUN mkdir -p ~/.vnc && x11vnc -storepasswd password ~/.vnc/passwd
RUN bash -c 'echo "firefox" >> /.bashrc'

WORKDIR /srv
ADD . /srv

EXPOSE 5900
