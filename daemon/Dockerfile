FROM nllong/cbecc-com:vnc
MAINTAINER Nicholas Long <nicholas.long@nrel.gov>

# Install 32-bit ruby to talk to the DLLs
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -yq ruby2.0 build-essential ruby2.0-dev && \
    rm -rf /var/lib/apt/lists/*

# Symlink Ruby 2.0
RUN ln -s /usr/bin/ruby2.0 /usr/local/bin/ruby \
    && ln -s /usr/bin/gem2.0 /usr/local/bin/gem \
    && ln -s /usr/bin/irb2.0 /usr/local/bin/irb

# Add bundler gem
RUN gem install bundler


# install Ruby for wine - there seems to be major problems with getting this to work

#RUN curl -SL http://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.0.0-p594.exe -o ruby2.0.exe
#RUN xvfb-run -a wine ruby2.0.exe /silent

# Install Python 2.7
RUN curl -SLO https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi
# RUN curl -SLO http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20214/pywin32-214.win32-py2.6.exe
RUN wine msiexec /i python-2.7.8.msi ALLUSERS=1



# VNC server setup
RUN mkdir -p ~/.vnc && x11vnc -storepasswd password ~/.vnc/passwd
RUN bash -c 'echo "firefox" >> /.bashrc'

EXPOSE 5900
