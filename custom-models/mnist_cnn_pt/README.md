#### Custom Model built with PyTorch and MNIST dataset to predict handwritten digits. Packaged as docker image with Seldon to expose as microservice model as microservice.

1) Build Image
   
    `docker build . -t mnist-cnn-pt:1.0.0-latest`

2)  Test the Image
    
    `docker run -p 9000:9000 --rm mnist-cnn-pt:1.0.0-latest`

    `curl -X POST http://localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{ "data": { "ndarray": [[5.964,4.006,2.081,1.031]]}}'`

