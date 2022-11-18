[![CI](https://github.com/nogibjj/Project-4-Elisa-Chen/actions/workflows/makefile.yml/badge.svg)](https://github.com/nogibjj/Project-4-Elisa-Chen/actions/workflows/makefile.yml) [![AWS CD](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoidGtTMm5ZSlgrWERrNDljbjB5YkpRVkhHKzlINWpVQUhEY3ZqbVdhcWYxR0ZJV3pkUVBoTENHemM0WC8rdERXQ2lMUDRvWHJCYWxXQzNnekNRQkdVd3VNPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik9IL2RnOHFpRjIwVG1ITUoiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
# Project-4-Elisa-Chen - Activity Generator

This repository contains the source code, config files and a short video demo of my activity generator program using continuous integration and continuous delivery methods. 

![Project_4](https://user-images.githubusercontent.com/25168588/202618952-57517222-0201-4c91-a601-86b5f07c0be9.png)

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

Link to the FastAPI documentation: [https://ps3pduk3yp.us-east-1.awsapprunner.com/docs](https://ps3pduk3yp.us-east-1.awsapprunner.com/docs)

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
