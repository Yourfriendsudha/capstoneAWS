
## Project Overview

In this project, you will apply the skills you have acquired throughout in this Nanodegree

### Project Scope : Proposal

Your project goal is to operationalize this working, machine learning microservice using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project you will:
* use circle-ci for continuous integration
* Test your project code using linting
* Create Dockerfile to containerize this application
* Push the docker image to Dokcer Hub
* Deploy your containerized application using Docker and test using circleci
* Configure and create a AWS EKS cluster
* Deploy the container using Kubernetes
* Test rolling strategy by updating the flask app and deploying again


---
## Clone the Source code

git clone https://github.com/Yourfriendsudha/capstoneAWS.git
cd capstoneAWS/

## Setup the Environment

* Create a virtualenv and activate it
python3 -m venv ~/.devops
source ~/.devops/bin/activate

* Run `make install` to install the necessary dependencies


### Running `app.py`

Standalone:  `python app.py`

## folder setup
1. .circleci folder contains the config file to run the automated CI-CD tasks
2. we will operationalize a Python flask app—in a provided file, `app.py` 
3. deployment.yml - Configuration of the actual objects that make up the pod using metadata, port and label  
4. urls.txt - contains the project submission urls
5. DockerFile - A file used to instruct to build the image for the python app
6. Makefile - A file used to execute goals during application compilation that contains things like  install, all, uninstall, lint, setup, etc,.
7. requirements.txt -  to help install the dependencies easily



