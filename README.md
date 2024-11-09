# LSEG Quiz Application

This is a quiz application built with Flask and containerized with Docker. 
It displays a set of 5 multiple-choice questions. 
Users can submit answers, view their score, and see which answers were correct.
They can restart the quiz if interested.

# Pre-Requisites

- Docker Desktop (For Windows)
- Python 3.8

# Instructions when using Docker from DockerHub

1. **Pull the Image**
   ```
   docker pull vikasgitam/lseg-quiz:3.0

2. **Run the Container after pulling above image**
   ```
   docker run -p 8082:8082 vikasgitam/lseg-quiz:3.0
   
3. Once docker container is up, Quiz can be accessed from -> http://127.0.0.1:8082

# Instructions when using IDE

Run **main.py** which is present under **app** directory. Once in running state, Access quiz from --> http://127.0.0.1:8082

# Instructions when using Docker Locally

1. **Build Docker Image**

   From the path where dockerfile is present, build the Docker image using below command:
   ````
   docker build -t lseg-quiz .

2. **Run the docker container**
    
   Once above build is completed without errors, run the container using below command:
    ```
    docker run -p 8082:8082 lseg-quiz
   
3. Once docker container is up, Quiz can be accessed from -> http://127.0.0.1:8082

