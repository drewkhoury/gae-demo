FROM google/cloud-sdk:latest

# helpful packages
RUN apt-get install git curl vim -y

# python packages
RUN apt-get install python-dev python-pip -y

# set a working directory
WORKDIR /usr/src

# get the "Google Cloud Platform Python Samples"
# https://github.com/GoogleCloudPlatform/python-docs-samples
RUN git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

# satisfy requirements for datastore cloud-client
WORKDIR python-docs-samples/datastore/cloud-client
RUN pip install -r requirements.txt
