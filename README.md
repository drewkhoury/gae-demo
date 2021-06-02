*Oh you're in a hurry? It should only take 10 minutes (or less!) to deploy to production on your first try*

**Assumptions:** Git, Docker, A Google User Account

Make sure you've cloned this repo, and you're in the root folder:
```
git clone https://github.com/drewkhoury/gae-demo.git && cd gae-demo/
```

### 1) Authenticate to Google Cloud with your Google Account
```
# create a volume where we will store authentication credentials
docker volume create gcloud-config-volume

# generate the authenetication credentials
# note: this command will give you a google-link that you can use to generate a token
docker run --rm -ti -v gcloud-config-volume:/root/.config google/cloud-sdk:alpine gcloud auth login
```

### 2) Create a local development environment for this app
```
docker-compose up local
```

- Web Server = http://localhost:8080/
- Admin Console = http://localhost:8000/

### 3) Create a new Google Cloud Project and deploy this app
```
docker-compose up new-deploy
```

Note: You may see an error message about enabling the API on your first try, follow the link to "enable Cloud Build API". This should prompt you to link to a billing account. Once this is done, you can try a `re-deploy`.

AppEngine costs money but not much, plus there's a free tier: https://cloud.google.com/appengine/pricing

Browse to your production-ready application (replace xxx with your project id):
- https://devops-demo-xxx.appspot.com

### 4) Deploy the latest code to an existing project

Make any changes you like to the application, then deploy the latest code (replace xxx with your project id from step 3).

```
export CLOUDSDK_CORE_PROJECT=devops-demo-xxx
docker-compose up re-deploy
```

# More Info

Detailed instructions can be found here:

- https://github.com/drewkhoury/gae-demo/wiki/Requirements
- https://github.com/drewkhoury/gae-demo/wiki/Local-Environment
- https://github.com/drewkhoury/gae-demo/wiki/Deployments
