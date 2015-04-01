FROM ubuntu:14.04
MAINTAINER Nicholas Long <nicholas.long@nrel.gov>

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -yq curl xvfb software-properties-common python-software-properties && \
    add-apt-repository ppa:ubuntu-wine/ppa && \
    apt-get update && \
    apt-get install -yq wine1.7:i386 --no-install-recommends

# Install Gecko (IE for Linux). Make sure to match the version of wine with gecko.
# http://wiki.winehq.org/Gecko
# 2.21 is for wine-1.5.31 - wine-1.7.2
# 2.36 is for wine-1.7.38 - current
ENV GECKO_VERSION 2.36
RUN curl -SLO http://downloads.sourceforge.net/wine/wine_gecko-$GECKO_VERSION-x86.msi && \
    mkdir -p /usr/share/wine/gecko && \
    mv wine_gecko-$GECKO_VERSION-x86.msi /usr/share/wine/gecko/

# Install Mono. Make sure to install the right version for wine, not sure how to tell, did this via trial and error
# List of versions are here: http://sourceforge.net/projects/wine/files/Wine%20Mono/
ENV MONO_VERSION 4.5.6
RUN curl -SLO http://downloads.sourceforge.net/wine/wine-mono-$MONO_VERSION.msi && \
    mkdir -p /usr/share/wine/mono && \
    mv wine-mono-$MONO_VERSION.msi /usr/share/wine/mono/

RUN apt-get autoclean -y

# Install CBECC Com -- Have to call xvfb because the silent install still shows a dialog when it is verifying files
ENV CBECC_COM_VERSION 3a
ENV CBECC_DOWNLOAD_URL http://bees.archenergy.com/Documents/Software/CBECC-Com_2013-${CBECC_COM_VERSION}_Setup.exe
RUN curl -SLO $CBECC_DOWNLOAD_URL && \
    xvfb-run -a wine CBECC-Com_2013-${CBECC_COM_VERSION}_Setup.exe /S && \
    rm -f CBECC-Com_2013-${CBECC_COM_VERSION}_Setup.exe

WORKDIR /var/cbecc-com-files
