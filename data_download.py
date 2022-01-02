import os

# Installs kaggle API
os.system("pip install kaggle")

# Puts the kaggle.json API Token in the ~/.kaggle directory (for kaggle API)
os.system("rm -r ~/.kaggle")
os.system("mkdir ~/.kaggle")
os.system("mv ./creds/kaggle.json ~/.kaggle/")
os.system("chmod 600 ~/.kaggle/kaggle.json")
os.system("kaggle datasets list")

# Downloads the data if not already downloaded
if not os.path.isdir("./data/"):
    os.system("mkdir ./data/")
    os.system("kaggle datasets download -d gpiosenka/100-bird-species -p ./data/")