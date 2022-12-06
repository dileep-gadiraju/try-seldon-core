# try-seldon-core
https://docs.seldon.io/projects/seldon-core/en/latest/index.html

# Setup Seldon Core locally
kind create cluster --name seldon-old --image kindest/node:v1.24.7
https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html
https://docs.seldon.io/projects/seldon-core/en/latest/examples/seldon_core_setup.html


# Setup MINIO
https://docs.seldon.io/projects/seldon-core/en/latest/examples/minio_setup.html

# ISTIO
Port forwarding: kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80

# MINIO
Port forwarding: kubectl port-forward -n minio-system svc/minio 8090:9000

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


# Notebooks with examples
https://docs.seldon.io/projects/seldon-core/en/latest/examples/server_examples.html
https://docs.seldon.io/projects/seldon-core/en/latest/workflow/github-readme.html
kubectl get seldondeployments
kubectl describe seldondeployments iris
kubectl describe seldondeployments sklearn

Known issue with K8S >= 1.25 : 
    https://github.com/SeldonIO/seldon-core/issues/4339
    https://github.com/SeldonIO/seldon-core/issues/2485

kubectl delete  -f ./servers/sklearnserver/samples/iris.yaml
kubectl apply  -f ./servers/sklearnserver/samples/iris.yaml

 kubectl apply -f - << END
apiVersion: machinelearning.seldon.io/v1
kind: SeldonDeployment
metadata:
  name: iris-model
  namespace: seldon
spec:
  name: iris
  predictors:
  - graph:
      implementation: SKLEARN_SERVER
      modelUri: gs://seldon-models/v1.15.0-dev/sklearn/iris
      name: classifier
    name: default
    replicas: 1
END

1) Model with KEDA and Promathieus
   kubectl create -f ./servers/sklearnserver/samples/model_with_keda_prom.yaml
2) 