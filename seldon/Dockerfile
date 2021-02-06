FROM python:3.7.8-buster
COPY seldon /app
COPY deploy /deploy
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

# Add parent python path so we can find the deploy module
ENV PYTHONPATH .

# Define environment variable for seldon
ENV MODEL_NAME Iris
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

CMD exec seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE