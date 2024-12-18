#!/bin/bash

# Install pyenv
echo "Installing pyenv..."
curl https://pyenv.run | bash

# Update PATH and initialize pyenv for the current shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Install Python 3.10.0 using pyenv
echo "Installing Python 3.10.0 with pyenv..."
pyenv install -s 3.10.0  # '-s' skips installation if already installed
pyenv global 3.10.0

# Verify Python version
echo "Python version:"
python --version

# Install required Python packages
echo "Installing required Python packages..."
pip install --upgrade pip
pip install numpy streamlit pillow keras tensorflow

echo "Environment setup complete!"
echo "To run your project: streamlit run main.py"