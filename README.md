# DS18B20 Temperature Sensor

## Pre-setup

`direnv` should be installed, the generic method for doing that is

```shell
curl -sfL https://direnv.net/install.sh | bash
```

## Setup

```shell
PYTHON_VERSION=$(cat .python-version)
direnv allow
pyenv install $PYTHON_VERSION
pyenv virtualenv $PYTHON_VERSION $VENV
pyenv activate $VENV
pip install poetry
poetry install
```
