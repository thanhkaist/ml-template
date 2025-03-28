# https://hub.docker.com/r/nvidia/cuda
FROM nvidia/cuda:12.0.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

ARG PYTHON_VERSION=3.12
ARG USER=dockeruser
ARG UID=1001 # Set this to your user ID: id -u
ARG GID=1001 # Set this to your group ID: id -g 

RUN apt update && apt install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y && apt update \
    && apt remove -y python3* --purge \
    && apt autoremove -y \
    && apt install -y python${PYTHON_VERSION} python3-distutils git curl \
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

# Install miniconda
RUN wget -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash miniconda.sh -b -p $HOME/miniconda \
    && rm miniconda.sh \ 
    && echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> ~/.bashrc \
    && source ~/.bashrc \
    && source ~/miniconda/etc/profile.d/conda.sh

# Install Jupyter
RUN pip install Jupyter

WORKDIR /workspace

CMD [ "bash" ]