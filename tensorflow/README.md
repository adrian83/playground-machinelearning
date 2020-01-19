# TENSORFLOW

## Running

### Running with docker

#### Prerequisites
- Docker

#### Steps
1. `sudo docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./test_installation.py`

### Running locally

#### Prerequisites
1. Python (tested on python 3.6)
2. Virtualenv 
3. Pip

#### Steps
1. `virtualenv --system-site-packages virtenv`
2. `cd virtenv/bin && source activate && cd ../..`
3. `pip install -r requirements.txt`
4. `./test_installation.py`
