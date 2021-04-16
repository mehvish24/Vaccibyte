# Vaccibyte
Done by: Mehvish Hafiz, Nallani Mounika, Shruti Laya.
This is a vaccine repository using csv files.
In this we have used Flask, Rest-APIs. The language used is Python.
In this project we have used three csv files that are used to store vaccine, userand patient information. On those csv files we can perform three API operations i.e; GET, POST, DELETE.

Our code is on the file named app.py.

Our project is divided into three modules:
a) Vaccine inventory: We have created a vaccine.csv file to store vaccine information. We can perform GET, POST and DELETE operations on that.
b) Patient inventory: We have created a patient.csv file to store patient information. We can perform GET, POST operations on that.
c) User inventory: We have created a user.csv file to store user information. We can perform POST, DELETE operations on that. Note: We were planning to only keep 1 user for the project.

We used different inventories for all three because it's easier to manage smaller database rather than one single large database. It makes the information easier to read without any confusions.

For the same application we created a DOCKER IMAGE on the local machine, the docker image was created using code that is present in Dockerfile, requirements.txt and docker-compose.yml files.

This github code is to be pulled from amazon ec2 server. Done for that.
