from kubernetes import client, config
from os import path
import yaml

def main():
    # Load the kube config file
    config.load_kube_config()

    file = path.join(path.dirname(__file__), "pod-b.yaml")

    with open(file) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="default")
        print("Pod A deployment created. status='%s'" % str(resp.status))

if __name__ == '__main__':
    main()