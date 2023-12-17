# feature-flags-with-kubernetes

Implementing feature flags with Kubernetes for smoother deployments

## Setting up the python environment

1. Create a virtual environment

```bash
python3 -m venv venv
```

2. Activate the virtual environment

```bash
source venv/bin/activate
```

## Installing dependencies

1. Install the kubernetes python client

```bash
pip install kubernetes
```

2. Install the configcat client

```bash
pip install configcat-client
```

## Setup the image

1. Build the images for the backend that Kubernetes will use

```bash
docker build -f Dockerfile.with-node18 -t backend-with-node18:latest .
```

```bash
docker build -f Dockerfile.with-node20 -t backend-with-node20:latest .
```

## Notes

Delete the deployments

```bash
kubectl delete deployments --all
```

Delete the services

```bash
kubectl delete services --all
```
