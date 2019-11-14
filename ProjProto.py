import io

import torch
import PIL
import torchvision
import torchvision.transforms as transforms

from PIL import Image
import imghdr
import numpy
import zipfile
from PIL import Image
import imghdr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import array as arr

X_data = []
z = zipfile.ZipFile('by_class.zip')
for i in range(500):

    file_in_zip = z.namelist()[i]
    if ".png" in file_in_zip or ".JPG" in file_in_zip:
        data = z.read(file_in_zip)
        dataEnc = io.BytesIO(data)
        img = Image.open(dataEnc)
        X_data.append(img)

plt.imshow(X_data[300])
plt.show()
plt.imshow(X_data[200])
plt.show()
plt.imshow(X_data[100])
plt.show()


