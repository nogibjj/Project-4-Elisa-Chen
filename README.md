[![CI](https://github.com/nogibjj/Project-4-Elisa-Chen/actions/workflows/makefile.yml/badge.svg)](https://github.com/nogibjj/Project-4-Elisa-Chen/actions/workflows/makefile.yml)
# Project-4-Elisa-Chen - Activity Generator

This repository contains the source code, config files and a short video demo of my activity generator program using continuous integration and continuous delivery methods. 

<insert diagram>

## Key Objectives and Project Description
This project was created as part of the IDS 706 Data Engineering Class at Duke. The goal of the project was to create a Microservice that returns a JSON payload and performs a Data Engineering related task. We are expected to perform Continuous Integration with Github Actions and configure build server to deploy changes on build (Continuous Delivery) using FastAPI.

I wanted to create a program that will recommend an activity for you to do randomly. The data is pulled using [Bored API](https://www.boredapi.com/) to suggest an activity for a user. The JSON payload returned will contain information about the activity, type of activity, number of participants needed for the activity, price of activity, and other useful information. 

## Demo Video

## Methodology
1. The activity was obtained from BoredAPI using `requests` package in Python and stored in a JSON object
2. FastAPI was leveraged to display the randomly generated activity
3. The program was containerized in AWS ECR and pushed to production using AppRunner
4. Continuous Delivery was enabled using AWS CodeBuild.

## Example Output
```
{
  "activity": "Sit in the dark and listen to your favorite music with no distractions",
  "type": "relaxation",
  "participants": 1,
  "price": 0,
  "link": "",
  "key": "9908721",
  "accessibility": 1
}
```


