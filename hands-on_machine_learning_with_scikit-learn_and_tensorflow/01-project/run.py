import os
import tarfile
import pandas as pd
import matplotlib.pyplot as plt
from six.moves import urllib


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("data", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data():
    if os.path.exists(os.path.join(HOUSING_PATH, "housing.csv")):
        return

    if not os.path.isdir(HOUSING_PATH):
        os.makedirs(HOUSING_PATH)

    tgz_path = os.path.join(HOUSING_PATH, "housing.tgz")
    urllib.request.urlretrieve(HOUSING_URL, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=HOUSING_PATH)
    housing_tgz.close()

def load_housing_data():
    csv_path = os.path.join(HOUSING_PATH, "housing.csv")
    return pd.read_csv(csv_path)


fetch_housing_data()
data = load_housing_data()

print("\n ------------- HEAD ------------- \n")
print(str(data.head()))

print("\n ------------- INFO ------------- \n")
print(str(data.info()))

print("\n ------------- OCEAN PROXIMITY VALUES ------------- \n")
print(str(data["ocean_proximity"].value_counts()))

print("\n ------------- DESCRIPTION ------------- \n")
print(str(data.describe()))

print("\n ------------- SHOW HISTOGRAM ------------- \n")
data.hist(bins=50, figsize=(20,15))
plt.show()


