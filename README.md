## Vaccibyte
### Done by: Mehvish Hafiz, Nallani Mounika, Shruthi Laya.
This is a vaccine repository using csv files.
In this we have used Flask, Rest-APIs. The language used is Python.
In this project we have used three csv files that are used to store vaccine, userand patient information. On those csv files we can perform three API operations i.e; GET, POST, DELETE.
Our code is on the file named **app.py**.
#### Our project is divided into three modules:
1. **Vaccine inventory**: We have created a vaccine.csv file to store vaccine information. We can perform GET, POST and DELETE operations on that.
2. **Patient inventory**: We have created a patient.csv file to store patient information. We can perform GET, POST operations on that.
3. **User inventory**: We have created a user.csv file to store user information. We can perform POST, DELETE operations on that. Note: We were planning to only keep 1 user for the project.
We used different inventories for all three because it's easier to manage smaller database rather than one single large database. It makes the information easier to read without any confusions.
For the same application we created a DOCKER IMAGE on the local machine, the docker image was created using code that is present in Dockerfile, requirements.txt and docker-compose.yml files.

#### Steps of the work:
**STEP 1:** _Importing the required packages in the python IDE_

<p align="center">
  <img width="650" height="250" src="https://user-images.githubusercontent.com/82588312/115039573-3562bb00-9eee-11eb-81f0-a17ddc07389f.png">
</p>


**STEP 2:** _Creating the rest endpoints._ We have three endpoints in the application we are creating & we will also write the code blocks for all three which we are going to fill with methods later.These methods will be used to implement GET, POST & DELETE operations on the csv files later.

<p align="center">
  <img width="650" height="250" src="https://user-images.githubusercontent.com/82588312/115040072-adc97c00-9eee-11eb-9031-1c00c2500a2c.png">
</p>


**STEP 3:** _Write the code to read-write data into csv files & also delete data for some endpoints._

Check the code [here!!](https://github.com/mehvish24/Vaccibyte/blob/main/app.py)

**STEP 4:** _Running the web server on local machine._

<p align="center">
  <img width="650" height="300" src="https://user-images.githubusercontent.com/82588312/115042224-e8341880-9ef0-11eb-90ae-72cc480859ba.png">
</p>


Click on the link http://127.0.0.1:5000/ that will be available to check your code on the local machine.

**STEP 5:** _Check in POSTMAN all the endpoints, for GET, POST & DELETE._

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115044601-49f58200-9ef3-11eb-8139-e408a8d9d5a3.png">
</p>

<h5 align="center">The original csv file.</h5>

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115042977-9e97fd80-9ef1-11eb-9107-0abdb7ef3bc3.png">
</p>

<h5 align="center">GET request on POSTMAN.</h5>

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115045644-53331e80-9ef4-11eb-8bd8-e99239378686.png">
</p>

<h5 align="center">Csv file after Performing two POST operations.</h5>

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115043335-0a7a6600-9ef2-11eb-9271-6c15c11ccdcd.png">
</p>

<h5 align="center">The POST request on POSTMAN.</h5>

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115045936-97262380-9ef4-11eb-90ca-702da0352f0a.png">
</p>

<h5 align="center">Csv file after one DELETE operation.</h5>

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115043604-4e6d6b00-9ef2-11eb-9625-6baeb3534d9e.png">
</p>

<h5 align="center">The DELETE request on POSTMAN.</h5>

It can be done in the same way for other endpoints.

#### Creating Docker Image for same code: 
**STEP 1:** _Creating a Dockerfile._
You can check the code [here!!](https://github.com/mehvish24/Vaccibyte/blob/main/Dockerfile)

**STEP 2:** _Creating a requirements.txt file._
You can check the code [here!!](https://github.com/mehvish24/Vaccibyte/blob/main/requirements.txt)

**STEP 3:** _Creating a docker-compose.yml file._
You can check the code [here!!](https://github.com/mehvish24/Vaccibyte/blob/main/docker-compose.yml)

**STEP 4:** _Using Command docker-compose build in terminal to build the image, I used it in Python IDE terminal._

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115117641-3f9fba80-9fbd-11eb-88b2-abfafe7753c4.png">
</p>



**STEP 4:** _Using Command docker-compose up in terminal to run the image on container._

<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/82588312/115117727-af15aa00-9fbd-11eb-9a9f-77fc461966a9.png">
</p>



#### Conclusion: 
By following the steps above we can create a REST API easily with Flask & Python and can also test it on POSTMAN on the local machine. We can also create an image for the same code by following steps mentioned above.




