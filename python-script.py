from kubernetes import client, config
from os import path
import yaml

def main():
    # Load the kube config file
    config.load_kube_config()

    kube_deployment = "deployment-a.yaml"
    kube_service = "service.yaml"

    deployment_file = path.join(path.dirname(__file__), kube_deployment)
    service_file = path.join(path.dirname(__file__), kube_service)

    with open(deployment_file) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="default")
        print("Deployment created. status='%s'" % str(resp.status))

    with open(service_file) as f:
        dep = yaml.safe_load(f)
        k8s_core_v1 = client.CoreV1Api()
        resp = k8s_core_v1.create_namespaced_service(
            body=dep, namespace="default")
        print("Service created. status='%s'" % str(resp.status))

if __name__ == '__main__':
    main()