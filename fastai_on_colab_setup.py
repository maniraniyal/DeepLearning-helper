import os
SETUP_CHECK_FILE = "CHECK_IF_SETUP_EXISTS"
KAGGLE_API_credential = '' # please specify your kaggle token here
if os.path.exists(SETUP_CHECK_FILE):
    pass
else:
    with open(SETUP_CHECK_FILE, 'w'):
      pass
    
    !wget https://github.com/fastai/fastai/archive/master.zip
    !unzip -q  -o master.zip
    !pip install bcolz graphviz sklearn_pandas isoweek pandas_summary ipywidgets tqdm torch torchvision torchtext kaggle
    
    #kaggle cli setup
    if len(KAGGLE_API_credential) > 1:
        pass
    else:
        print("""go to https://www.kaggle.com/<myaccountName>/account \n Here myaccountName is your kaggle account name.
              click on 'Create New API Token' which will create new token. Copy and paste the token string into
              KAGGLE_API_credential variable.""")
        import sys
        sys.exit()
    
    !mkdir ~/.kaggle
    !echo '{KAGGLE_API_credential}' > ~/.kaggle/kaggle.json
    !chmod 600 ~/.kaggle/kaggle.json
    
    #to fix PIL issue
    !pip install Pillow==4.0.0
    !pip install PIL
    !pip install image
    
    #download pre-trained models
    !wget http://files.fast.ai/models/weights.tgz
    !tar -xvzf weights.tgz
    !mv weights/ fastai-master/fastai/
    
    #import fastai
    import imp
    fastai = imp.load_source('fastai', '/content/fastai-master/fastai/__init__.py')
    
    #command to download kaggle dataset
    #!kaggle competitions download -c <compitition-dataset-name-here> -w
    
    
