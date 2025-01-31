# https://hub.docker.com/r/nvidia/cuda
FROM nvidia/cuda:11.0.3-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

ARG PYTHON_VERSION=3.12
ARG USER=dockeruser
ARG UID=1001 # Set this to your user ID: id -u
ARG GID=1001 # Set this to your group ID: id -g 

RUN apt update && apt install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y && apt update \
    && apt remove -y python3* --purge \
    && apt autoremove -y \
    && apt install -y python${PYTHON_VERSION} git curl \
    && ln -sf /usr/bin/python${PYTHON_VERSION} /usr/bin/python \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python \
    && rm -rf /var/lib/apt/lists/*


# Create a non-root user
RUN apt update && apt install -y sudo && \
    groupadd -g $GID $USER && \
    useradd -u $UID -g $GID -m -s /bin/bash $USER && \
    usermod -aG sudo $USER && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER
    
USER $USER

# Install Jupyter
RUN pip install Jupyter

WORKDIR /workspace

CMD [ "bash" ]