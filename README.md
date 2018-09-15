# I'm in the fast lane
`cd gcp-dev && docker build -t gcp-dev . && ../`
`docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login`

For full requirements, see https://github.com/drewkhoury/gae-demo/wiki/Requirements

# Local Environment

Spin up your own Google Cloud locally!

```
docker-compose local
```

- Web Server = http://localhost:8080/
- Admin Console = http://localhost:8000/


See https://github.com/drewkhoury/gae-demo/wiki/Local-Environment for more info,

# Deploy

```
MY_PROJECT=$(mktemp -u devops-demo-XXXXXX| tr '[:upper:]' '[:lower:]')
docker-compose new-deploy
```

See https://github.com/drewkhoury/gae-demo/wiki/Deployments for more info.
