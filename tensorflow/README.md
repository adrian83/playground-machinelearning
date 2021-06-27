# TENSORFLOW

## Running


### Running with Virtualenv

#### Prerequisites
- Python
- VirtualEnv

#### Steps
1. Create virtual environment: `python -m venv virtenv`
2. Activate virtual environment: `source virtenv/bin/activate`
3. Install required dependencies: `pip install -r requirements.txt`
4. Do stuff...
5. Deactivate virtual environment: `deactivate`



### Running with docker

#### Prerequisites
- Docker

#### Steps
1. `sudo docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./test_installation.py`
