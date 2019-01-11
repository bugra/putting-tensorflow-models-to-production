# putting-tensorflow-models-to-production
Tutorial Materials for Putting Tensorflow Models To Production 

## A bit about me
**Bugra Akyildiz**

### What I do
- Tech Lead for Jet Search&Recommendations
- Worked on Visual Search, Recommendations, Query Suggestions

### What I did
- Lead for recommender system @Hinge
- Worked a number of startups that quite did not make it :) 

### Background
- MS in machine learning&signal processing(CS) [NYU]
- BS in signal processing(EE) [Bilkent]


### Tutorial Material
- Tutorial: https://github.com/bugra/putting-tensorflow-models-to-production 
- http://bit.ly/bugra-tf
  - (you should at least star it and maybe clone&fork, create an issue, fix things)


### How to reach me
- Twitter @bugraa => You can ask questions you want after tutorial
- You can also reach to me: bugra@nyu.edu (I may not be responsive until 14th Jan)



### General Setup
0. Install Python3: https://www.python.org/downloads/ (Are you in the right conference ;) ?
1. Install docker: https://www.docker.com/get-started
2. Install pip3: https://pip.pypa.io/en/stable/installing/
3. Install all of the dependencies through `pip3 install -r requirements.txt` (Not sure what this is; ask ;)


### Docker Setup
- For any image that you want to build; you can use the following command: `docker build -f {{DOCKER_FILE_PATH}} .`
- After this, we need to "run" the image: `docker run -p 8501:8501 -it {{DOCKER_SHA}}`

> If these do not make a lot of sense, it is great that you are in tutorial and ask ;) They are going to be important


### Pointers
- `Dockerfile`: Resnet model dockerfile which can be used as `docker build .` and then `docker run -p 8501:8501 -it {{SHA}}`
- `/models`: This has various models file as well as model configuration file.
- `/client` directory has the client code that interacts with Tensorflow serving API.
- `/tf_serving_scripts`: it has starting script for an example of how Tensorflow model can be used in the production.
- `/notebooks`: directory that has many more examples which I will go through in the tutorial