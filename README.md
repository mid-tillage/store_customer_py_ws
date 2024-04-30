# store-customer-py-ws

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Docker](#docker)
  - [Image Resource Usage Metrics](#image-resource-usage-metrics)
- [Kubernetes](#kubernetes)
  - [Pod Resource Usage Metrics](#pod-resource-usage-metrics)

## Description

Store's Customer Web Service example using [Nest](https://github.com/nestjs/nest) framework.

## Installation

```bash
$ pip install -r requirements.txt
```

## Running the app
The following commands allow you to run the application

```bash
# development
$ python app.py
```

## Docker

```bash
# Build Docker image
docker build -t store-customer-py-ws:latest -f Dockerfile .

# Run Docker container (with example port mappings and environment variables)
docker run -p 3020:3020 -p 27017:27017 -e MONGODB_HOST="host.docker.internal" -e MONGODB_PORT="27017" -e MONGODB_NAME="mydb" store-customer-py-ws
```

### Image resource usage metrics

The table below shows resource usage metrics for the `store-customer-py-ws` Docker container.

| REPOSITORY              | TAG    | IMAGE ID      | CREATED        | SIZE  |
|-------------------------|--------|---------------|----------------|-------|
| store-customer-py-ws    | latest | bd8ccd6265f0  | 2 minutes ago  | 155MB |


## Kubernetes

```bash
# Start Minikube to create a local Kubernetes cluster
minikube start

# Configure the shell to use Minikube's Docker daemon
& minikube -p minikube docker-env --shell powershell | Invoke-Expression

# Build Docker image with a specific tag and Dockerfile
docker build -t store-customer-py-ws:latest -f Dockerfile .

# Apply Kubernetes configuration to create a pod
kubectl apply -f kubernetes/pod.yaml

# Port-forward to access the Kubernetes pod locally
kubectl port-forward store-customer-py-ws-pod 3020:3020
```

### Pod resource usage metrics

The table below shows resource usage metrics for the `store-customer-py-ws-pod` pod.

```bash
minikube addons enable metrics-server
kubectl top pods
```

**Note:** If you just enabled the metrics-server addon, remember to wait a couple of seconds before running the `kubectl top pods` command.


| NAME                      | CPU(cores) | MEMORY(bytes) |
|---------------------------|------------|---------------|
| store-customer-py-ws-pod  | 1m         | 26Mi          |
