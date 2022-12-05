# try-seldon-core
try-seldon-core https://docs.seldon.io/projects/seldon-core/en/latest/index.html

# Setup Seldon Core locally
https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html
https://docs.seldon.io/projects/seldon-core/en/latest/examples/seldon_core_setup.html


# Setup MINIO
https://docs.seldon.io/projects/seldon-core/en/latest/examples/minio_setup.html

# ISTIO
Port forwarding: kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80

# MINIO
Port forwarding: kubectl port-forward -n minio-system svc/minio 8090:9000

# Notebooks with examples
https://docs.seldon.io/projects/seldon-core/en/latest/examples/server_examples.html

kubectl rollout status deploy/$(kubectl get deploy -l seldon-deployment-id=sklearn -o jsonpath='{.items[0].metadata.name}')