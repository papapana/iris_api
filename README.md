# Iris dataset exploration API

## Introduction

Sample API for the iris dataset

## Installation

### With docker -- recommended

### Without docker

1) First make sure python 3.8 is available and mongodb is running.

To install python 3.8:

Assuming [Anaconda](https://www.anaconda.com/distribution/) has been installed on the system, create an environment:
```bash
conda create -n py38 python=3.8 numpy pandas pymongo
conda activate py38
```

To install mongodb please follow this [link](https://docs.mongodb.com/manual/administration/install-community/):

Quick way for Ubuntu/Debian-based Linux:

```bash
sudo apt-get install mongodb
sudo service mongodb start
```

Quick way for MacOSX:

```bash
brew tap mongodb/brew
brew install mongodb-community@4.2
brew services start mongodb-community@4.2
```

2) Clone the project and enter in the directory

```bash
git clone https://github.com/papapana/iris_api.git && cd iris_api
```

3) Install the requirements

- To use as a library:
```bash
python setup.py install
``` 

- No intent to use it as a library
```bash
pip install -r requirements.txt
```

4) Run the database provisioning script
```bash
python scripts/provision_db.py
``` 

5) Start the API server

```bash 
uvicorn iris_api.app.main:app --reload  --port 8000
```

## Usage

### As a REST API

- Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) where you can test interactively the API

- See examples in the jupyter notebook in the path `./notebooks/iris_demo.ipynb`
    - to install Jupyter notebook follow this [link](https://jupyter.org/install)

- Endpoints:
    - `POST /range/`
    - `POST /stats/mean/`

### As a library



## Structure
```
├── docker-compose.dev.yml        -- for development purposes
├── docker-compose.yml            -- for production
├── iris_api
│   ├── app              
│   │   ├── api                   -- the endpoints
│   │   │   ├── __init__.py
│   │   │   ├── models.py         
│   │   │   ├── ranges_api.py
│   │   │   └── stats_api.py
│   │   ├── db.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── core                       -- the business logic is here
│   │   ├── __init__.py
│   │   └── queries 
│   │       ├── __init__.py
│   │       ├── ranges.py
│   │       ├── stats.py
│   │       └── utilities.py        -- query generating scripts are here
│   ├── __init__.py
│   └── tests                       -- tests
│       └── __init__.py
├── notebooks
│   └── iris_demo.ipynb             -- demo notebook
├── ops
│   ├── dev
│   │   └── Dockerfile              -- Docker for development
│   └── release
│       └── Dockerfile              -- Docker for production
├── README.md
├── requirements.txt                -- Python package requirements
├── scripts
│   └── provision_db.py             -- script to populate the iris database
└── setup.py

```

## Scaling

## Development

### Extensibility

### Code Quality & Standards

## Security

## Testing