# feature-flags-with-kubernetes

Implementing feature flags with Kubernetes for smoother deployments

## Setup

### Python environment setup

1. Create a virtual environment

```bash
python3 -m venv venv
```

2. Activate the virtual environment

```bash
source venv/bin/activate
```

3. Install the dependencies

```bash
pip3 install -r requirements.txt
```

### Docker setup

1. Build the images for the backend that Kubernetes will use

```bash
docker build -f Dockerfile.with-node18 -t backend-with-node18:latest .
```

```bash
docker build -f Dockerfile.with-node20 -t backend-with-node20:latest .
```

### Kubernetes setup

In this setup, we are using Docker Desktop with Kubernetes enabled.

1. Create the deployments and services

```bash
python3 kubernetes-script.py
```

2. Check the deployments

```bash
kubectl get deployments
```

You should see something like this:

```bash
NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
backend-deployment   1/1     1            1           35m
```

## How it works

In this sample app, we utilize the Python Kubernetes client to create deployments and services. This choice was made to seamlessly integrate Kubernetes with ConfigCat feature flags. It's important to note that the integration of [ConfigCat feature flags](https://configcat.com/#product) with Kubernetes can be approached in various ways. The explanation below details how these components work together:

1. Two Docker images are created for the backend. Each of these are built from a Separate Dockerfile. The Dockerfile.with-node18 uses Node 18 and the Dockerfile.with-node20 uses Node 20.

2. The `kubernetes-script.py` script is run to create the deployments and services. A default deployment logic gets executed to create a Pod with a container that contains the Docker image built from the Dockerfile.with-node18. Afterwards, the feature flag value is checked and if it is true, the Pod's container image is updated/patched to use the Docker image built from the Dockerfile.with-node20.

## Notes

Delete the deployments

```bash
kubectl delete deployments --all
```

Delete the services

```bash
kubectl delete services --all
```
