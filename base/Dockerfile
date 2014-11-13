FROM ubuntu:14.04
MAINTAINER Nicholas Long <nicholas.long@nrel.gov>

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -yq curl wine:i386 xvfb

# Install Gecko (IE for Linux). Make sure to match the version of wine with gecko.
# http://wiki.winehq.org/Gecko
ENV GECKO_VERSION 2.21
RUN curl -SLO http://downloads.sourceforge.net/wine/wine_gecko-$GECKO_VERSION-x86.msi && \
    mkdir -p /usr/share/wine/gecko && \
    mv wine_gecko-$GECKO_VERSION-x86.msi /usr/share/wine/gecko/

# Install Mono. Make sure to install the right version, not sure how to tell, did this via trial and error (4.5.* do not work).
# List of versions are here: http://sourceforge.net/projects/wine/files/Wine%20Mono/
ENV MONO_VERSION 0.0.8
RUN curl -SLO http://downloads.sourceforge.net/wine/wine-mono-$MONO_VERSION.msi && \
    mkdir -p /usr/share/wine/mono && \
    mv wine-mono-$MONO_VERSION.msi /usr/share/wine/mono/

RUN apt-get autoclean -y

# Install CBECC Com -- Have to call xvfb because the silent install still shows a dialog when it is verifying files
ENV CBECC_DOWNLOAD_URL http://bees.archenergy.com/Documents/Software/CBECC-Com_2013-3_Setup.exe
RUN curl -SLO $CBECC_DOWNLOAD_URL

# have to call xvfb because the silent install still shows a dialog when it is verifying files
RUN xvfb-run -a wine CBECC-Com_2013-3_Setup.exe /S

WORKDIR /var/cbecc-com-files
