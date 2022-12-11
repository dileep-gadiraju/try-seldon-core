# Try Seldon Core 
#### Repository to bring up [Seldon core](https://www.seldon.io/solutions/open-source-projects/core) locally with minimal effort. This repo also lists the know issues and work around/fixes needed for installation, run Seldon Core out of the box sample notebooks  with ease.

## References
[Install Locally](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html)

[Notebooks](https://docs.seldon.io/projects/seldon-core/en/latest/examples/notebooks.html)

[Seldon Core](https://docs.seldon.io/projects/seldon-core/en/latest/index.html)

[Seldon Core Setup](https://docs.seldon.io/projects/seldon-core/en/latest/examples/seldon_core_setup.html)

## Setup Seldon Core locally
[Setup Seldon Core with Kind](./setup_seldon_core_using_kind.ipynb)

<!-- 3) `pip install seldon-core`
1) `pip install mlflow`
2)  `kind delete cluster --name seldon`
3) Note: K8S >=1.25 has HPA(HorizontalPodAutoscaler) issues. So creating cluster with  kindest/node:v1.24.7 image.
   `kind create cluster --name seldon --image kindest/node:v1.24.7`
   For apiextensions.k8s.io/v1beta1 CRD issue , use `kind create cluster --name seldon --image=kindest/node:v1.21.2`
   Refer: https://stackoverflow.com/questions/69054622/unable-to-install-crds-in-kubernetes-kind
4)  `kubectl cluster-info --context kind-seldon`
5)  `istioctl install --set profile=default -y`
6)  `kubectl label namespace default istio-injection=enabled`
7)  Follow instructions [Create Istio Gateway](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html) , [install-seldon-core](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html#install-seldon-core) , [local-port-forwarding](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html#local-port-forwarding) -->

<!-- 11) Istio : Plugin certificates and key into cluster
    1) follow below steps to plugin certs for istio
     References: https://istio.io/latest/docs/tasks/security/cert-management/plugin-ca-cert/
12) Istio: Create Ingress resource
    ```
kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: istio
  name: ingress
spec:
  rules:
  - host: httpbin.example.com
    http:
      paths:
      - path: /status
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 8000
EOF
    ```
1)  Istio Ingress setup:
    kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml
    kubectl wait --namespace metallb-system \
                --for=condition=ready pod \
                --selector=app=metallb \
                --timeout=90s
    docker network inspect -f '{{.IPAM.Config}}' kind
    export INGRESS_NAME=istio-ingressgateway
    export INGRESS_NS=istio-system
    kubectl get svc "$INGRESS_NAME" -n "$INGRESS_NS"
    echo http://$INGRESS_HOST:$INGRESS_PORT/headers
    export INGRESS_HOST=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    export INGRESS_PORT=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
    export SECURE_INGRESS_PORT=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
    export TCP_INGRESS_PORT=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.spec.ports[?(@.name=="tcp")].port}')


    References:
    https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports
    https://kind.sigs.k8s.io/docs/user/loadbalancer/
14) Ensure the istio ingress gatewaty is port-forwarded to localhost:8004
    kubectl port-forward $(kubectl get pods -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].metadata.name}') -n istio-system 8004:8080
    References: https://docs.seldon.io/projects/seldon-core/en/latest/examples/istio_examples.html
15)  -->
    


## [Setup MINIO](https://docs.seldon.io/projects/seldon-core/en/latest/examples/minio_setup.html)

## [Kubernetes-based Event Driven Autoscaler(KEDA) Setup](https://docs.seldon.io/projects/seldon-core/en/latest/examples/keda.html)

## [Seldon Deploy](https://deploy.seldon.io/_/downloads/en/v1.3/pdf/)

## [istioctl](https://istio.io/latest/docs/ops/diagnostic-tools/istioctl/)

## Useful admin and troubleshooting cli commands
1)  `kubectl get seldondeployments`
2)  `kubectl describe seldondeployments <seldondeployment name>`
3)  `kubectl describe svc <svc name>`
4)  `kubectl get namespaces`
5)  `kubectl get all -n istio-system`
6)  `kubectl get svc -n istio-system`
7)  `kubectl describe namespace default`
8)  `kubectl describe namespace istio-system`
9)  `kubectl get pods`
10) `kubectl describe pod <pod name>`
11) `which istioctl`
12) `istioctl version`
13) `istioctl proxy-status`
14) `istioctl proxy-config cluster <pod name>`
15) `istioctl install --set profile=default -y`
16) `istioctl install --set profile=demo -y`
17) `istioctl analyze`
18) `kubectl describe service/istio-ingressgateway -n istio-system`
19) `kubectl get svc istio-ingressgateway -n istio-system -oyaml`
20) `kubectl get ksvc,configuration,revision,route`
21) `kubectl get ingress`
22) `kubectl describe pod <pod name> -n seldon-system`
23) `kubectl describe svc sklearn-default`
24) `kubectl get svc istio-ingressgateway -n istio-system`
25) `kubectl describe svc istio-ingressgateway -n istio-system`
26) `kubectl get pods -n=istio-system`
27) `kubectl logs pods/<pod name> -n=istio-system`
28) `kubectl logs pod/<pod name> --tail=100`
29) `istioctl profile dump demo`
30) `kubectl logs <pod name/container id>`
31) `kubectl get gateway -n istio-system`
32) `kubectl describe gateway/seldon-gateway -n istio-system`
33) `kubectl get gateway --all-namespaces`
34) `kubectl delete all --all`
35) Label a K8s namespace for istio injection `kubectl label namespace seldon istio-injection=enabled`
36) Shows resources available in each node.`kubectl describe nodes`
37) Load docker image to kind cluster/control plane `kind load docker-image nvcr.io/nvidia/tritonserver:21.08-py3 --name kind`
38) `docker exec kind-control-plane crictl images`


## Example Seldon Core Deployments using Helm with Istio
Reference: https://docs.seldon.io/projects/seldon-core/en/latest/examples/istio_examples.html 
1) open [istio_example.ipynb](./istio_example.ipynb)

## Example Model Servers with Seldon
Reference: https://docs.seldon.io/projects/seldon-core/en/latest/examples/server_examples.html
1) open [server_examples.ipynb](./server_examples.ipynb)

## MLFlow Pre-packaged Model Server AB Test Deployment
1) open [mlflow_server_ab_test_ambassador.ipynb](./mlflow_server_ab_test_ambassador.ipynb)

## Triton Examples
1) open [triton_examples.ipynb](./triton_examples.ipynb)
2) git clone https://github.com/azure/azureml-examples

## Example Model Explanations with Seldon
Reference: https://github.com/oegedijk/explainerdashboard/blob/master/notebooks/explainer_examples.ipynb
1)  open [explainer_examples.ipynb](./explainer_examples.ipynb)

## Example IRIS Model loaded from MINIO
1) [iris_deploy_with_minio.ipynb](./iris_deploy_with_minio.ipynb)

## [Custom model packaging and deployment](./custom-models/mnist_cnn_pt/README.md)
Reference: https://docs.seldon.io/projects/seldon-core/en/latest/python/index.html
https://docs.primehub.io/docs/model-deployment-language-wrapper-python#pytorch

## Known issue with K8S >= 1.25 : 
1)  [https://github.com/SeldonIO/seldon-core/issues/4339](https://github.com/SeldonIO/seldon-core/issues/4339)
2)  [https://github.com/SeldonIO/seldon-core/issues/2485](https://github.com/SeldonIO/seldon-core/issues/2485)

## Known issues with Istio configuration
1) [https://github.com/kserve/kserve/issues/1005](https://github.com/kserve/kserve/issues/1005)
2) [https://stackoverflow.com/questions/69826714/fail-to-run-istio-ingressgateway-got-readiness-probe-failed-connection-refused](https://stackoverflow.com/questions/69826714/fail-to-run-istio-ingressgateway-got-readiness-probe-failed-connection-refused)