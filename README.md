# Iris dataset exploration API

## Introduction

This is an exercise to create a production-worthy API for the [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set).
It is meant to be used later as a template for more complex applications and datasets.
Some features suitable for bigger datasets e.g. pagination is already supported.
The API can be used both as a REST-API service and a python package used from other applications.


The key highlights are asynchronous API using [FastAPI](https://fastapi.tiangolo.com/), input validation and type-checking
using [Pydantic](https://pydantic-docs.helpmanual.io/) and ease of deployment and scaling using [Docker Compose](https://docs.docker.com/compose/).

The choice of database is a NoSQL one and more particularly [MongoDB](https://www.mongodb.com/).
Although this dataset is very simple and structured and a relational database would be preferable, the exercise is meant
to be as general as possible and I would like to use it for unstructured or multiple different datasets in the future.

Additionally, the setup is meant to be capable of scaling as much as possible. For example, FastAPI can scale vertically
very well, because we have dockerized the application, it can also be scaled horizontally easily at the level of the API.
Furthermore, at the database level [MongoDB can also scale in multiple ways](https://www.mongodb.com/mongodb-scale).

## Query structure

All queries are REST API POST queries with the following structure:

```
<> below means optional
The general query model:
{
    <species: one or more of 'setosa', 'versicolor' or 'virginica' e.g. "setosa" or ["setosa", "virginica"]>
    <lower: the lower bound by column, default -- no bound, e.g. {"sepal_length": 5, "petal_length": 3}>
    <upper: the upper bound by column, default -- no bound, e.g. {"sepal_length": 5.2}>
    <page: the page number if pagination is used, int >=1 or not provided>
    <per_page: the results per page if pagination is used, int>=1 or not provided>
}
```

## Installation

### With docker -- recommended

1) Make sure [docker is installed](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)
is installed as well.

2) Clone the project and cd into it:
```bash
git clone https://github.com/papapana/iris_api.git
cd iris_api
```

3) Run the build script, *the following commands might require **sudo** rights*
```bash 
docker-compose -f docker-compose.dev.yml up --build iris_api 
```

4) Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) where you can test interactively the API
    - Example `/range/` request body (application/json): 
        ```json 
        {
          "species": "setosa",
          "lower": {
            "sepal_length": 5.0,
            "sepal_width": 3.0
          },
          "upper": {
            "sepal_length": 5.1
          }
        }
        ```
    - Example `/stats/mean` request body (application/json):
        ```json 
        {
          "species": [
            "setosa",
            "versicolor"
          ],
          "lower": {
            "sepal_width": 3.0
          },
          "upper": {
            "sepal_length": 6.1
          }
        }
        ```
---

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

e.g
```python
"""
Example of using the API as an installed package
"""

from iris_api.core.queries import stats as st

st.get_mean(st.IrisQuery(species=['setosa', 'versicolor']))
"""
Result:
"""
[{'mean_sepal_length': 5.006,
  'mean_sepal_width': 3.428,
  'mean_petal_length': 1.462,
  'mean_petal_width': 0.24600000000000002,
  'label': 'setosa'},
 {'mean_sepal_length': 5.936,
  'mean_sepal_width': 2.77,
  'mean_petal_length': 4.26,
  'mean_petal_width': 1.3259999999999998,
  'label': 'versicolor'}]
```


## Structure
```
├── docker-compose.dev.yml     -- settings for development purposes   
├── docker-compose.yml         -- settings for production
├── iris_api
│   ├── app
│   │   ├── api                -- the endpoints
│   │   │   ├── __init__.py
│   │   │   ├── models.py      -- the query models
│   │   │   ├── ranges_api.py
│   │   │   └── stats_api.py
│   │   ├── db.py              -- connection to database
│   │   ├── __init__.py
│   │   └── main.py            -- setting up the endpoint routers
│   ├── core
│   │   ├── __init__.py
│   │   └── queries            -- business logic is here (can be used as a library)
│   │       ├── __init__.py
│   │       ├── ranges.py      
│   │       ├── stats.py
│   │       └── utilities.py
│   ├── __init__.py
│   └── tests                  -- unit tests are here
│       ├── __init__.py
│       └── test_utilities.py
├── notebooks
│   └── iris_demo.ipynb        -- jupyter notebook demo
├── ops                        -- devops scripts are here
│   ├── dev                    -- here for development
│   │   ├── Dockerfile
│   │   └── provisioning       -- here for provisioning the database
│   │       └── Dockerfile
│   └── release                -- here for production
│       └── Dockerfile
├── README.md                  -- current file
├── requirements.txt           -- Python package version requirements
├── scripts
│   └── provision_db.py        -- script that populates the database with the iris dataset
└── setup.py                   -- the installation script for usage as a python library
```

## Questions

### How would you deploy the application?

The application can be deployed wherever Docker is supported. This might be for example a managed container engine like
[AWS Fargate](https://aws.amazon.com/fargate/), virtual hosts like [AWS EC2](https://aws.amazon.com/ec2/) or because
docker-compose is used, it can be more easily deployed on services supporting [Kubernetes](https://kubernetes.io/).

A word of caution, the current version does not have authentication and authorization mechanism at the API level and
therefore should be used either for internal use only or behind a server/load-balancer that would provide 
authentication/authorization. These features can be added easily because the framework used supports them.

It is anyway a good idea to hide the current service behind a production-scale web server such as [Nginx](https://www.nginx.com/)
that could act as a load-balancer also e.g. in cases of increased traffic or for redundancy of the API services

## How would you test your application?

The tests or quality control for this type of application could be of several types like `unit-tests`, `integration tests`, 
`fuzz tests`, `load balancing tests`, `availability tests` and more.

In the current exercise, the most important thing to be tested is the query creation mechanism which implements the main logic.
For this purpose, unit tests have been written under the tests folder.
In the current state, most of the other code written consists of calls to libraries and therefore testing it might be 
redundant, because it would as if we were testing the library. A whole system test would be useful though.

Integration tests can happen using docker e.g. by doing a healthcheck on the database that is up, insert some dummy data
and then perform a query and ensure it gets the appropriate data.

Fuzz tests are very useful if the service is exposed to the general public to ensure that no malicious input can harm
or crash the system. Although, in the current state there is no explicit fuzz test, all the input is strictly-typed and
bounded and checked on each request before it is passed to any logic in the backend. This happens in the `models.py` file
using the `Pydantic` library.

Stress testing can be done using either some online service or some command-line tool like `wrk2`. Improvement of the
situation leads to scaling

### How would you scale your application?

Since the application is deployed using docker, managed services such as `Fargate`, or tools like `Kubernetes` could be
used to scale horizontally the application. 

If the bottleneck is the API, then a load balancer (in practice e.g. an nginx service) could decide to send the requests
to multiple different servers of the API therefore sharing the load. Also, caching results can be very useful to avoid
executing the same query multiple times.

If the bottleneck is the database (in my experience it is more common) then it can also be scaled. The advantage of having
a NoSQL database here is that it can scale horizontally easily and with multiple ways. There could be for example replication
if our app is read-heavy, so copying the same data to multiple databases and sharing the requests between them.
However, NoSQL databases such as MongoDB also support sharding quite easily, so separating the data among servers according
to some key and therefore balancing the load. This is particularly appropriate if the bottleneck is writing to the database.

If the bottleneck is the computation, vertical scaling might be considered, e.g. getting a server with more CPUs, more memory
or attaching and using GPUs


### How would you optimize the implementation of your application?

In terms of performance, I would determine the bottleneck by stress-testing and profiling the execution.
If the bottleneck was related to I/O but not the database, then I would try to have more workers serving the asynchronous requests
or load-balance the service as discussed above.
If it was related to the database, I would scale the database as above
If it were related to computation, first I would try to optimize the bottleneck computations if possible by vectorizing
and compiling to native code and then scale vertically by getting more powerful machines. In certain cases, such as 
deep learning, the solution is most frequently using GPUs or TPUs.

In terms of ease quality control, I would automate the tests by having Continuous Integration set-up and also use metrics
for code-coverage and other quality metrics. For example, currently the Jetbrains PyCharm linter is used throughout and 
there must be no problem before committing. In a production environment, I would add at least one more linter such as
`flake8` and maybe also `black`. If the API was exposed I would add some fuzzy testing too and automated stress-testing
and benchmarking to ensure that a new deployment would not degrade the system.

In terms of deployment, I would set-up continuous deployment and also optimize my docker files, to avoid duplication.

In terms of monitoring, setting up a good logging system would also be necessary for a bigger application. Also, a 
monitoring system such as datadog to monitor metrics and uptime would be necessary.


### How much time did it take for you to implement the task?

The main functionality (having a fully working solution with correct results) took about ~3-4 hours including reading and using FastAPI
for the first time. However, doing the devops for this particular application and the laptop I was using took more than that.
