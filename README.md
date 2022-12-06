# try-seldon-core
https://docs.seldon.io/projects/seldon-core/en/latest/index.html
https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html
https://docs.seldon.io/projects/seldon-core/en/latest/examples/seldon_core_setup.html
# Setup Seldon Core locally
1)  kind delete cluster --name seldon
2)  kind create cluster --name seldon --image kindest/node:v1.24.7
3)  kubectl cluster-info --context kind-seldon
4)  Install ISTIO as per instructions in below link
    istioctl install --set profile=default -y
    istioctl install --set profile=minimal -y
    istioctl install --set profile=demo -y  
5)  kubectl label namespace default istio-injection=enabled
6)  kubectl apply -f - << END
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: seldon-gateway
  namespace: istio-system
spec:
  selector:
    istio: ingressgateway # use istio default controller
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
END
1)  kubectl create namespace seldon-system
2)  helm install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --set istio.enabled=true \
    --namespace seldon-system
3)  kubectl get pods -n seldon-system
4)  Istio : Plugin certificates and key into cluster
    1) follow below steps to plugin certs for istio
     References: https://istio.io/latest/docs/tasks/security/cert-management/plugin-ca-cert/
5)  Istio: Create Ingress resource
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
15) 
    


# Setup MINIO
https://docs.seldon.io/projects/seldon-core/en/latest/examples/minio_setup.html

Port forwarding: 
kubectl port-forward -n minio-system svc/minio 8090:9000

# Kubernetes-based Event Driven Autoscaler(KEDA) Setup
`kubectl config set-context $(kubectl config current-context) --namespace=seldon`
https://docs.seldon.io/projects/seldon-core/en/latest/examples/keda.html
https://keda.sh/docs/2.8/deploy/
https://docs.sysdig.com/en/docs/sysdig-monitor/monitoring-integrations/advanced-configuration/configure-keda/

# Seldon Deploy
https://deploy.seldon.io/_/downloads/en/v1.3/pdf/
https://deploy.seldon.io/en/v1.2/contents/getting-started/production-installation/seldon.html

1) TAG=1.3.0 && \
docker create --name=tmp-sd-container seldonio/seldon-deploy-server:$TAG && \
docker cp tmp-sd-container:/seldon-deploy-dist/seldon-deploy-install.tar.gz . && \
docker rm -v tmp-sd-container
tar -xzf seldon-deploy-install.tar.gz

# Istio references
https://istio.io/latest/docs/ops/diagnostic-tools/istioctl/
### Known issues with Istio configuration
       1) https://github.com/kserve/kserve/issues/1005
       2) https://stackoverflow.com/questions/69826714/fail-to-run-istio-ingressgateway-got-readiness-probe-failed-connection-refused

# Useful commands to check seldon deployments
kubectl get seldondeployments
kubectl describe seldondeployments sklearn
kubectl describe svc sklearn
kubectl describe seldondeployments iris
kubectl get namespaces
kubectl get all -n istio-system
kubectl get svc -n istio-system
kubectl describe namespace default
kubectl describe namespace istio-system
kubectl get pods
kubectl describe pod sklearn-default-0-classifier-6497d676b7-wc28g
which istioctl
istioctl version
istioctl proxy-status
istioctl proxy-config cluster <pod name>
istioctl install --set profile=default -y
istioctl install --set profile=demo -y
kubectl describe service/istio-ingressgateway -n istio-system
kubectl get svc istio-ingressgateway -n istio-system -oyaml
kubectl get ksvc,configuration,revision,route
kubectl get ingress
kubectl describe pod <pod name> -n seldon-system
kubectl describe svc sklearn-default
kubectl get svc istio-ingressgateway -n istio-system 
kubectl describe svc istio-ingressgateway -n istio-system
kubectl get pods -n=istio-system
kubectl logs pods/<pod name> -n=istio-system
istioctl profile dump demo
kubectl logs <pod name/container id>
kubectl get gateway -n istio-system
kubectl describe gateway/seldon-gateway -n istio-system
kubectl get gateway --all-namespaces

# Notebooks with examples
https://docs.seldon.io/projects/seldon-core/en/latest/examples/server_examples.html
https://docs.seldon.io/projects/seldon-core/en/latest/workflow/github-readme.html

### Known issue with K8S >= 1.25 : 
    https://github.com/SeldonIO/seldon-core/issues/4339
    https://github.com/SeldonIO/seldon-core/issues/2485

1)  Try : https://docs.seldon.io/projects/seldon-core/en/latest/examples/istio_examples.html
2)  Serve SKLearn Iris Model
    kubectl delete  -f ./servers/sklearnserver/samples/iris.yaml
    kubectl apply  -f ./servers/sklearnserver/samples/iris.yaml
    kubectl scale --replicas=1 -f ./servers/sklearnserver/samples/iris.yaml
    kubectl rollout status deploy/$(kubectl get deploy -l seldon-deployment-id=sklearn -o jsonpath='{.items[0].metadata.name}')
    kubectl describe seldondeployments sklearn

3)  Serve SKLearn Iris Model with v2 protocol
    kubectl apply  -f ./servers/sklearnserver/samples/iris-sklearn-v2.yaml
    kubectl rollout status deploy/$(kubectl get deploy -l seldon-deployment-id=sklearn-v2 -o jsonpath='{.items[0].metadata.name}')


# Example Seldon Core Deployments using Helm with Istio
Reference: https://docs.seldon.io/projects/seldon-core/en/latest/examples/istio_examples.html 
1) jupyer notebook
2) open istio_example.ipynb

# Example Model Servers with Seldon
Reference: https://docs.seldon.io/projects/seldon-core/en/latest/examples/server_examples.html
1) jupyer notebook
2) open server_examples.ipynb