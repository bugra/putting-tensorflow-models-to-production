# putting-tensorflow-models-to-production
Tutorial Materials for Putting Tensorflow Models To Production 

## A bit about me
**Bugra Akyildiz**

### What I do
- Tech Lead for Jet Search&Recommendations
- Worked on Visual Search, Recommendations, Query Suggestions

### What I did
- Lead for recommender system @Hinge
- Worked for a number of startups that did not quite make it :) 

### Background
- MS in machine learning&signal processing(CS) [NYU]
- BS in signal processing(EE) [Bilkent]


### Tutorial Material
- Tutorial: https://github.com/bugra/putting-tensorflow-models-to-production 
- http://bit.ly/bugra-tf
- `git clone https://github.com/bugra/putting-tensorflow-models-to-production.git` to your local machine


### How to reach me
- Twitter @bugraa => You can ask questions if you want after tutorial
- You can also reach to me: bugra@nyu.edu (I may not be responsive until 14th Jan)


### How many
- people are students
- hit a /GET or /POST endpoint
- people have used Docker
    - operating-system-level virtualization, also known as "containerization" 
- people have used `pip`
    - Pip Installs Packages
- people have used Tensorflow in some capacity


### General Setup
0. Install Python3: https://www.python.org/downloads/ (Are you in the right conference ;) ?
1. Install docker: https://www.docker.com/get-started
2. Install pip3: https://pip.pypa.io/en/stable/installing/
3. Install all of the dependencies through `pip3 install -r requirements.txt` (Not sure what this is; ask ;)


### Prepare Environment
- `git clone https://github.com/bugra/putting-tensorflow-models-to-production.git`
- `pip3 install -r requirements.txt`


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