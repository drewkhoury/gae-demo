# I'm in the fast lane

*Oh you're in a hurry? This should only take 10 minutes or less!*

1) Authenticate to GoogleCloud with your Google Account:
```
docker volume create gcloud-config-volume

docker run --rm -ti -v gcloud-config-volume:/root/.config \
google/cloud-sdk:alpine gcloud auth login
```

**Note: Make sure you run the following commands from this folder `gae-demo/`...**

2) Create a local development environment for this app:
```
~/code/gae-demo $  docker-compose up local
```

- Web Server = http://localhost:8080/
- Admin Console = http://localhost:8000/

3) Create a new Google Cloud Project and deploy this app:
```
~/code/gae-demo $  docker-compose up new-deploy
```

Browse to your production-ready application (replace xxx with your project id from step 3):
- https://devops-demo-xxx.appspot.com

4) Make any changes you like to the application, then deploy the latest code to an existing project (replace xxx with your project id from step 3):
```
~/code/gae-demo $  export CLOUDSDK_CORE_PROJECT=devops-demo-xxx
~/code/gae-demo $  docker-compose up re-deploy
```

# More Info

Detailed instructions can be found here:

- https://github.com/drewkhoury/gae-demo/wiki/Requirements
- https://github.com/drewkhoury/gae-demo/wiki/Local-Environment
- https://github.com/drewkhoury/gae-demo/wiki/Deployments
