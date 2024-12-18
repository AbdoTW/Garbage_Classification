# Use an official Ubuntu as the base image
FROM ubuntu:20.04

# Set working directory in the container
WORKDIR /usr/app/src

# Install required dependencies for pyenv and Python installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    git \
    && apt-get clean

# Install pyenv
RUN curl https://pyenv.run | bash

# Initialize pyenv and add it to the bash profile
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Install Python 3.10.0 using pyenv
RUN bash -c "source ~/.bashrc && pyenv install -s 3.10.0 && pyenv global 3.10.0"

# Install required Python packages
RUN bash -c "source ~/.bashrc && pip install --upgrade pip && pip install numpy streamlit pillow keras tensorflow"

# Copy the entire current directory into the container
COPY . /usr/app/src/

# Expose the port Streamlit will run on
EXPOSE 8501

# Set the default command to run Streamlit
CMD ["streamlit", "run", "main.py"]
