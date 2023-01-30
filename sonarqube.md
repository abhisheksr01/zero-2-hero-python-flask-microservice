# Setting SonarQube locally using Docker

## Pre requisite

We will be using docker to spin up a local instance of sonarqube and scan the code.

1. Execute below command to spin up a local instance.

```
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```

2. Access the app at http://localhost:9000/projects and use the default credentials of `admin/admin`. You will be prompted to reset the password.

3. 

3. [Click here to Install ngrok](https://ngrok.com/download), you will need to sign up for free ngrok account. This is required for integrating Sonarqube with GitHub.

4. 


https://docs.sonarqube.org/latest/setup/get-started-2-minutes/