# zero-2-hero-python-flask-microservice

## Introduction

**Instruction on how to use this repo is still a work in progress.**

This repository is developed to demonstrate how a typical business requirement transforms into software code by following the cloud-native practices.

## Pre-requisite

* Python 3.9.5 or higher
* Poetry
* Docker
* FLY CLI (For the CI/CD hands-on)
* Docker Hub Credentials (CI/CD pipeline requires it for pushing the image to docker hub)
* AWS EKS Cluster & credentials(For deploying this application using the CI/CD pipeline)

Note: If you running behind a corporate proxy you or the pipeline may not be able to pull some of the dependencies from the internet.

## Local Execution
You can execute below make commands within this repo to execute operations like unit test, e2e test, vulnerability scanning etc.

If your system doesn't support make commands, look into the [Makefile here](./Makefile) & get the raw commands to execute the task.
![](resources/make-code-instructions.png)

## Local Concourse Pipeline
[Concourse](https://concourse-ci.org/) is an open-source continuous thing-doer.

Built on the simple mechanics of resources, tasks, and jobs, Concourse presents a general approach to automation that makes it great for CI/CD.

Let us quickly spin a concourse pipeline locally and before proceeding make sure you have Docker installed.

From the root of the project change the directory:
```
cd concourse-ci
```
Execute the below command to spin a local concourse tool:
```
make spin-concourse

or 

cd local-concourse

docker compose up -d
```

Access the local concourse using the URL http://127.0.0.1:8080/ and then download the FLY CLI utility from the concourse home page.

---
> **_For Windows:_** 

- Execute the fly.exe as Administrator & then add "C:\Program Files\concourse\fly.exe" to the PATH environment variable.
- You will have to replace the "/" with "\" appropriately and "." from the front of any path references.

---

Update the credentials in the [secrets/vars.yml](./concourse-ci/secrets/vars.yml)

From concourse-ci directory execute the below command to configure the pipeline job.
```
make set-pipeline

or

fly -t main set-pipeline -p zero-2-hero-python-flask-microservice -c pipeline.yml -l ./secrets/vars.yml
```
Authenticate the pipeline by clicking the link highlighted in CLI with **USERNAME/PASSWORD as admin/admin**.

Then approve the pipeline configuration by typing "y" and hit enter.

You might get an error related to the fly version is not sync, if so execute the command recommended in CLI to do so.

By default, all the pipelines in the concourse are paused, execute the below command to unpause the same.

```
fly -t main unpause-pipeline -p zero-2-hero-python-flask-microservice
```
The pipeline can be accessed using the URL http://127.0.0.1:8080/teams/main/pipelines/zero-2-hero-python-flask-microservice

Your pipeline should look something like this:
![](resources/concourse-pipeline.png)

Additionally, you can perform below make commands concerning the concourse CI/CD pipeline.
![](resources/make-pipeline-instructions.png)

Execute the below command to destroy the pipeline:
```
make destroy-pipeline

or 

fly -t main destroy-pipeline -p zero-2-hero-python-flask-microservice
```

Execute the below command to tear off the local concourse:
```
make destroy-concourse

or 

cd local-concourse 

docker compose down
```