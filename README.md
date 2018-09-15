# I'm in the fast lane

Local development environment for this app:
```
docker-compose up local
```

- Web Server = http://localhost:8080/
- Admin Console = http://localhost:8000/

Deploy this app (auth to google for first time, then create new project + deploy code):
```
docker volume create gcloud-config-volume
docker run -ti --name gcloud-config-container -v gcloud-config-volume:/root/.config google/cloud-sdk gcloud auth login

docker-compose up new-deploy
```

Deploy latest code to existing project:
```
# deploy an existing project
export CLOUDSDK_CORE_PROJECT=devops-demo-xxx # (use project id from your first deployment)
docker-compose up re-deploy
```

Browse to: https://${CLOUDSDK_CORE_PROJECT}.appspot.com

# More Info

- https://github.com/drewkhoury/gae-demo/wiki/Requirements
- https://github.com/drewkhoury/gae-demo/wiki/Local-Environment
- https://github.com/drewkhoury/gae-demo/wiki/Deployments
