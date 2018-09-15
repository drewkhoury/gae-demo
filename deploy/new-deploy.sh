CLOUDSDK_CORE_PROJECT=$(mktemp -u devops-demo-XXXXXX| tr '[:upper:]' '[:lower:]')

gcloud projects create ${CLOUDSDK_CORE_PROJECT} --name="devops demo project" --labels=type=test
gcloud app create --region=australia-southeast1 --project ${CLOUDSDK_CORE_PROJECT}

cd /usr/src/myapp && gcloud app deploy --project ${CLOUDSDK_CORE_PROJECT} --quiet
