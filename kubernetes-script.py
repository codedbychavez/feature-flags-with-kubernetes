from kubernetes import client, config
from kubernetes.client.rest import ApiException
from os import path
import yaml
import configcatclient

def main():
    # Create a ConfigCatClient instance
    configcat_client = configcatclient.get('gnLbCJ_nhUCGHl1SZNyC5Q/V794nqFnpkWY_7TuhXTaOw')
    
    # Load the kube config file
    config.load_kube_config()

    deployment_file = path.join(path.dirname(__file__), "deployment.yaml")
    service_file = path.join(path.dirname(__file__), "service.yaml")

    # Check if the feature flag is enabled
    is_my_feature_flag_enabled = configcat_client.get_value('myfeatureflag', False)
    
    with open(deployment_file) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        deployment_name = dep['metadata']['name']
        namespace = "default"

        try:
            k8s_apps_v1.read_namespaced_deployment(name=deployment_name, namespace=namespace)
            print("Deployment already exists.")
        except ApiException as e:
            if e.status == 404:
                resp = k8s_apps_v1.create_namespaced_deployment(
                    body=dep, namespace=namespace)
                print("Deployment created. status='%s'" % str(resp.status))
            else:
                print("Error: %s" % e)

        image = "backend-with-node20" if is_my_feature_flag_enabled else "backend-with-node18"
        status = "enabled" if is_my_feature_flag_enabled else "disabled"
        print(f"Feature flag is {status}. Using image: {image}")

        # Define the patch
        patch = {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {
                                "name": "backend-container",
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
        svc = yaml.safe_load(f)
        k8s_core_v1 = client.CoreV1Api()
        service_name = svc['metadata']['name']
        namespace = "default"

        try:
            k8s_core_v1.read_namespaced_service(name=service_name, namespace=namespace)
            print("Service already exists.")
        except ApiException as e:
            if e.status == 404:
                resp = k8s_core_v1.create_namespaced_service(
                    body=svc, namespace=namespace)
                print("Service created. status='%s'" % str(resp.status))
            else:
                print("Error: %s" % e)

if __name__ == '__main__':
    main()