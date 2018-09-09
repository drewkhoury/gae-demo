#!/bin/bash

gcloud projects create ${CLOUDSDK_CORE_PROJECT} --name="devops demo project" --labels=type=test
gcloud app create --region=australia-southeast1 --project ${CLOUDSDK_CORE_PROJECT}
gcloud app deploy --quiet
