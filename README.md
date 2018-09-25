*Oh you're in a hurry? This should only take 10 minutes (or less!)*

### 1) Authenticate to Google Cloud with your Google Account
```
# create a volume where we will store authentication credentials
docker volume create gcloud-config-volume

# generate the authenetication credentials
# note: this command will give you a google-link that you can use to generate a token
docker run --rm -ti -v gcloud-config-volume:/root/.config google/cloud-sdk:alpine gcloud auth login
```

Note: Run the following commands from this repo's root folder. i.e `gae-demo/`...

### 2) Create a local development environment for this app
```
~/code/gae-demo $  docker-compose up local
```

- Web Server = http://localhost:8080/
- Admin Console = http://localhost:8000/

### 3) Create a new Google Cloud Project and deploy this app
```
~/code/gae-demo $  docker-compose up new-deploy
```

Browse to your production-ready application (replace xxx with your project id):
- https://devops-demo-xxx.appspot.com

### 4) Deploy the latest code to an existing project

Make any changes you like to the application, then deploy the latest code (replace xxx with your project id from step 3).

```
~/code/gae-demo $  export CLOUDSDK_CORE_PROJECT=devops-demo-xxx
~/code/gae-demo $  docker-compose up re-deploy
```

# More Info

Detailed instructions can be found here:

- https://github.com/drewkhoury/gae-demo/wiki/Requirements
- https://github.com/drewkhoury/gae-demo/wiki/Local-Environment
- https://github.com/drewkhoury/gae-demo/wiki/Deployments
