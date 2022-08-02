# Churn-cluster-prediction


#### Deploying a model with Flask, Docker and Heroku

-Implementation of the K-Medoids algorithm to predict segmentation groups.
-Deployment: making the machine learning model available in a production environment, where it can be accessed and utilised by other tools, workflows and software. 

Requirements

To run this code, you'll need the following:
    Heroku account. 
    Heroku CLI. 
    Docker desktop.
    Virtual environment.
    requirements.txt
    
    
 flask
├── build_model.ipynb  # model building code
├── web_api
│   └── model.joblib  # the machine learning model
│   └── app.py  # defines the flask API
│   └── Procfile  # required by Heroku to help start flask app
│   └── requirements.txt  # file containing required packages
│   
└── web_application
    └── model.joblib  # the machine learning model
    └── app.py  # the file that defines our flask API
    └── Procfile  # required by Heroku to help start flask app
    └── requirements.txt  # file containing required packages
    └── templates  # this subdirectory contains HTML templates to help us build the web application
    └── templates  # this subdirectory contains HTML templates to help us build the web application
        └── home.html  # html template to be used in web application
        └── prediction.html  # html template to be used in web application
    └── static  # this subdirectory contains CSS style sheets
        └── style.css  # css style to be used in web application
        └── images.png  # images to be used in web application
        
  

 

