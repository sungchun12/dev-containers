#-----------------------------------------------------------------------------------------
# This docker file is primarily used for building python-based data analytic pipelines
# Add other packages as needed to explore data interactively(ex: Jupyter Lab)
# This image is pretty heavy at >1.5 GB, so keep in mind rebuilds will take time
# I install the gcloud sdk as that's where I prefer to deploy pipelines
#-----------------------------------------------------------------------------------------

FROM python:3

# Configure apt
# Only install necessary debian packages, not suggested ones
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release, nano, unzip (common in install instructions for CLIs)
RUN apt-get -y install git procps lsb-release nano unzip wget

###### Install google cloud SDK ######
# Downloading gcloud package
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# Installing the package without manual inputs
RUN mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh --quiet

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin
######################################

###### Install Terraform #############
RUN wget --quiet https://releases.hashicorp.com/terraform/0.12.1/terraform_0.12.1_linux_amd64.zip \
  && unzip terraform_0.12.1_linux_amd64.zip \
  && mv terraform /usr/bin \
  && rm terraform_0.12.1_linux_amd64.zip
######################################

# Install any missing dependencies for enhanced language service
RUN apt-get install -y libicu[0-9][0-9]

RUN mkdir /workspace
WORKDIR /workspace

# Install Python dependencies from requirements.txt if it exists
COPY .devcontainer/requirements.txt requirements.txt* /workspace/
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt && rm requirements.txt*; fi

# Clean up
RUN apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash
