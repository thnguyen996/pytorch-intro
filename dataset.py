import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import matplotlib.pyplot as plt, mpld3
from torch.utils.data import DataLoader

train_dataset = datasets.FashionMNIST(
   root="./",
   download=True,
   transform=ToTensor(),
   train=True
   )
test_dataset = datasets.FashionMNIST(
   root="./",
   download=True,
   transform=ToTensor(),
   train=False
   )

## Plot the dataset
## We can index dataset just like using normal tensor training_data[0]
img, label = train_dataset[0]



labels_map = {
       0: "T-Shirt",
       1: "Trouser",
       2: "Pullover",
       3: "Dress",
       4: "Coat",
       5: "Sandal",
       6: "Shirt",
       7: "Sneaker",
       8: "Bag",
       9: "Ankle Boot",
   }

plt.imshow(img.squeeze(), cmap="gray")
plt.title(labels_map[label])
mpld3.show(port=6019, open_browser=False)
