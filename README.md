
# Requirements

## 1) Docker
Make sure you can run `docker` commands on your workstation.

https://www.docker.com/products/docker-desktop

## 2) Development Container (For a local env)

Build the development container (based on google/cloud-sdk):

`cd gcp-dev && docker build -t gcp-dev . && ../`

## 3) Authenticate to Google (For Deployments)

Use your Google Account to authenticate to Google Cloud.

Note: *You'll need "an active trial" or "valid payment method" configured before you can create cloud resources).*

This command will create a container that we'll use to make API calls for AutomatedDevOps(tm):

`docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login`


# Hello World

Our hello world app https://devops-gae-demo-1337.appspot.com/ has "Google App Engine" components:

- app.yaml

App Specific components:

- `pages/` jinja2 template files
- `static/` all static files (css/js/img)
- `python/` python scripts (acting as our backend app/web server ... include datamodels)

# Local Environment

Spin up your own Google Cloud locally!


```
docker run \
-it --rm \
-p 8000:8000 \
-p 8080:8080 \
-v "$PWD":/usr/src/myapp \
-w /usr/src/myapp \
gcp-dev bash -c 'dev_appserver.py --host 0.0.0.0 --admin_host 0.0.0.0 --port=8080 app.yaml --enable_sendmail --enable_console'
```

Web Server = http://localhost:8080/

Admin Console = http://localhost:8000/

# Deploy

*Note: Because deployments only require the google sdk, you can use `google/cloud-sdk:alpine` (55mb) instead of building `gcp-dev` ... however if you already have `gcp-dev` that will work just fine too.*


You can create a new project, "google-app-engine" app, and do deployments in a single container:
```
MY_PROJECT=$(mktemp -u devops-demo-XXXXXX| tr '[:upper:]' '[:lower:]')
echo $MY_PROJECT

docker run --rm -ti --volumes-from gcloud-config \
-v "$PWD":/usr/src/myapp -w /usr/src/myapp \
-e CLOUDSDK_CORE_PROJECT=${MY_PROJECT} \
gcp-dev bash -c '/usr/src/myapp/deploy.sh'
```


## More info

deploy.sh will run the following commands:
```
gcloud projects create ${CLOUDSDK_CORE_PROJECT} --name="devops demo project" --labels=type=test
gcloud app create --region=australia-southeast1 --project ${CLOUDSDK_CORE_PROJECT}
gcloud app deploy --quiet
```

You can run one-off commands too:
`gcp-dev bash -c 'gcloud app deploy --quiet'`

Or just shell into the container:
`gcp-dev bash`
