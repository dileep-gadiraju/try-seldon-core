# Try Seldon Core - A repo to bring up Seldon core locally with references to known issues

## References
[Install Locally](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html)

[Seldon Core](https://docs.seldon.io/projects/seldon-core/en/latest/index.html)

[Seldon Core Setup](https://docs.seldon.io/projects/seldon-core/en/latest/examples/seldon_core_setup.html)

## Setup Seldon Core locally
1)  `kind delete cluster --name seldon`
2) Note: K8S >=1.25 has HPA issues. So creating cluster with  kindest/node:v1.24.7 image.
   
   `kind create cluster --name seldon --image kindest/node:v1.24.7`
3)  `kubectl cluster-info --context kind-seldon`
4)  `istioctl install --set profile=default -y`
5)  `kubectl label namespace default istio-injection=enabled`
6)  Follow instructions [Create Istio Gateway](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html) , [install-seldon-core](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html#install-seldon-core) , [local-port-forwarding](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html#local-port-forwarding)

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

## Kubernetes-based Event Driven Autoscaler(KEDA) Setup
[Scale Seldon Deployments based on Prometheus Metrics](https://docs.seldon.io/projects/seldon-core/en/latest/examples/keda.html)

## [Seldon Deploy](https://deploy.seldon.io/_/downloads/en/v1.3/pdf/)


## istioctl References
[istioctl](https://istio.io/latest/docs/ops/diagnostic-tools/istioctl/)

## Useful cli commands to troubleshoot 
1)  `kubectl get seldondeployments`
2)  `kubectl describe seldondeployments sklearn`
3)  `kubectl describe svc sklearn`
4)  `kubectl get namespaces`
5)  `kubectl get all -n istio-system`
6)  `kubectl get svc -n istio-system`
7)  `kubectl describe namespace default`
8)  `kubectl describe namespace istio-system`
9)  `kubectl get pods`
10) `kubectl describe pod sklearn-default-0-classifier-6497d676b7-wc28g`
11) `which istioctl`
12) `istioctl version`
13) `istioctl proxy-status`
14) `istioctl proxy-config cluster <pod name>`
15) `istioctl install --set profile=default -y`
16) `istioctl install --set profile=demo -y`
17) `kubectl describe service/istio-ingressgateway -n istio-system`
18) `kubectl get svc istio-ingressgateway -n istio-system -oyaml`
19) `kubectl get ksvc,configuration,revision,route`
20) `kubectl get ingress`
21) `kubectl describe pod <pod name> -n seldon-system`
22) `kubectl describe svc sklearn-default`
23) `kubectl get svc istio-ingressgateway -n istio-system`
24) `kubectl describe svc istio-ingressgateway -n istio-system`
25) `kubectl get pods -n=istio-system`
26) `kubectl logs pods/<pod name> -n=istio-system`
27) `istioctl profile dump demo`
28) `kubectl logs <pod name/container id>`
29) `kubectl get gateway -n istio-system`
30) `kubectl describe gateway/seldon-gateway -n istio-system`
31) `kubectl get gateway --all-namespaces`


## Example Seldon Core Deployments using Helm with Istio
Reference: https://docs.seldon.io/projects/seldon-core/en/latest/examples/istio_examples.html 
1) jupyer notebook
2) open istio_example.ipynb

## Example Model Servers with Seldon
Reference: https://docs.seldon.io/projects/seldon-core/en/latest/examples/server_examples.html
1) jupyer notebook
2) open server_examples.ipynb


## Known issue with K8S >= 1.25 : 
1)  [https://github.com/SeldonIO/seldon-core/issues/4339](https://github.com/SeldonIO/seldon-core/issues/4339)
2)  [https://github.com/SeldonIO/seldon-core/issues/2485](https://github.com/SeldonIO/seldon-core/issues/2485)

## Known issues with Istio configuration
1) [https://github.com/kserve/kserve/issues/1005](https://github.com/kserve/kserve/issues/1005)
2) [https://stackoverflow.com/questions/69826714/fail-to-run-istio-ingressgateway-got-readiness-probe-failed-connection-refused](https://stackoverflow.com/questions/69826714/fail-to-run-istio-ingressgateway-got-readiness-probe-failed-connection-refused)