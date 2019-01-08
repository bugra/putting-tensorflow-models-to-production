# putting-tensorflow-models-to-production
Tutorial Materials for Putting Tensorflow Models To Production 

The main directory is reserved for a fully productionized model which is resnet model. 

### Pointers
- `Dockerfile`: Resnet model dockerfile which can be used as `docker build .` and then `docker run -p 8501:8501 -it {{SHA}}`
- `/models`: This has various models file as well as model configuration file.
- `/client` directory has the client code that interacts with Tensorflow serving API.
- `/tf_serving_scripts`: it has starting script for an example of how Tensorflow model can be used in the production.
- `/notebooks`: directory that has many more examples which I will go through in the tutorial



#### Resnet Client
```
{'model_version_status': [{'version': '1538687457', 'state': 'AVAILABLE', 'status': {'error_code': 'OK', 'error_message': ''}}]}
Prediction class: 286, avg latency: 145.65750800000015 ms
```

