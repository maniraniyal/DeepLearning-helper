#!/bin/bash
echo "Checking for gcsfuse and installing."
if ! dpkg-query -W gcsfuse; then
  export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
  echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
  sudo apt-get update
  sudo apt-get install gcsfuse -y
  mkdir SETUP_BUCKET
  mkdir WEIGHTS_BUCKET
  mkdir DATASET_BUCKET

fi
echo "Checking for CUDA and installing."
# Check for CUDA and try to install.
if ! dpkg-query -W cuda-9-0; then
  # The 16.04 installer works with 16.10.
  curl -O http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
  sudo dpkg -i ./cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
  sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
  sudo apt-get update
  sudo apt-get install cuda-9-0 -y
  cd $HOME
  tar xzvf SETUP_BUCKET/cudnn-9.0-linux-x64-v7.1.tgz
  sudo cp cuda/lib64/* /usr/local/cuda/lib64/
  sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
  rm -rf cuda
fi
# Enable persistence mode
nvidia-smi -pm 1

# Note that user should create $USER-dl-setup bucket in advance. and this bucket should have cuDNN
gcsfuse "$USER-dl-setup" SETUP_BUCKET
gcsfuse "$USER-dl-weights" WEIGHTS_BUCKET
gcsfuse "$USER-dl-dataset" DATASET_BUCKET


