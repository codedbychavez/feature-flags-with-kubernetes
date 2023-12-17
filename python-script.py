from kubernetes import client, config
from os import path
import yaml

def main():
    # Load the kube config file
    config.load_kube_config()

    deployment_file = path.join(path.dirname(__file__), "deployment.yaml")
    service_file = path.join(path.dirname(__file__), "service.yaml")

    # Check if the feature flag is enabled

    is_enabled = True
    
    with open(deployment_file) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
        body=dep, namespace="default")
        print("Deployment created. status='%s'" % str(resp.status))

        if is_enabled:
            # Define the image
            image = "backend-with-node20"

            # Define the patch
            patch = {
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {
                                    "name": "container_name",
                                    "image": image
                                }
                            ]
                        }
                    }
                }
            }
            
            resp = k8s_apps_v1.patch_namespaced_deployment(
                name="backend-deployment",
                namespace="default",
                body=patch,
            )

    with open(service_file) as f:
        dep = yaml.safe_load(f)
        k8s_core_v1 = client.CoreV1Api()
        resp = k8s_core_v1.create_namespaced_service(
            body=dep, namespace="default")
        print("Service created. status='%s'" % str(resp.status))

if __name__ == '__main__':
    main()