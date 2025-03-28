# https://hub.docker.com/r/nvidia/cuda
FROM nvidia/cuda:12.0.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

ARG PYTHON_VERSION=3.12
ARG USER=dockeruser
ARG UID=1001 # Set this to your user ID: id -u
ARG GID=1001 # Set this to your group ID: id -g 

RUN apt update && apt install -y software-properties-common wget\
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


# Set correct HOME environment variable for the non-root user
ENV HOME=/home/$USER

# Install Miniconda as the non-root user
RUN wget -O $HOME/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash $HOME/miniconda.sh -b -p $HOME/miniconda \
    && rm $HOME/miniconda.sh \
    && echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> $HOME/.bashrc \
    && echo 'source $HOME/miniconda/etc/profile.d/conda.sh' >> $HOME/.bashrc

# Install Jupyter using pip from the miniconda environment
ENV PATH=$HOME/miniconda/bin:$PATH


# Install Jupyter
RUN pip install Jupyter

WORKDIR /workspace

CMD [ "bash" ]