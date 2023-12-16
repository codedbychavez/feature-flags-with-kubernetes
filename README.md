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

## Running the backend

```bash
docker build -t backend .

docker run -p 3000:3000 backend
```

## Notes

Use this command to run the backend in a container

```bash
docker compose up --build -d
```

```bash
docker compose down
```


