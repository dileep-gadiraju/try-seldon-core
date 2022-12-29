FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
# RUN pip install --upgrade protobuf

# Port for REST
EXPOSE 9001

# Port for GRPC
EXPOSE 5001

# Define environment variable
ENV MODEL_NAME IrisClassifier
# ENV MODEL_NAME MNISTModel
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE --access-log --http-port 9001 --grpc-port 5001