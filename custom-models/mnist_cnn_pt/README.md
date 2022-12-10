#### Custom Model built with PyTorch and MNIST dataset to predict handwritten digits. Packaged as docker image with Seldon to expose as microservice model as microservice.

Temp Reference: https://docs.primehub.io/docs/model-deployment-language-wrapper-python#pytorch

#### Style 1 : Package as Docker image with seldon-core-microservice
1) Build Image
   
    `docker build . -t mnist-cnn-pt:latest`

2) Test the Image
    
    `docker run -p 9000:9000 --rm mnist-cnn-pt:latest`

    `curl -X POST http://localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{ "data": { "ndarray": [[5.964,4.006,2.081,1.031]]}}'`

3) 

#### Style 2 : Deploy using SeldonDeploy CRD yaml
