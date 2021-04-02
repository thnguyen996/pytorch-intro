import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

# Hyper-parameters 
input_size = 28 * 28    # 784
num_classes = 10
num_epochs = 100
batch_size = 50
learning_rate = 0.001

# MNIST dataset (images and labels)
train_dataset = torchvision.datasets.FashionMNIST(root='./',
                                           train=True,
                                           transform=transforms.ToTensor(),
                                           download=True)

test_dataset = torchvision.datasets.FashionMNIST(root='./',
                                          train=False,
                                          transform=transforms.ToTensor(),
                                          download=True)

# Data loader (input pipeline)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)


# Logistic regression model

# Loss and optimizer
# nn.CrossEntropyLoss() computes softmax internally

# # Train the model

# Test the model
# In test phase, we don't need to compute gradients (for memory efficiency)

# Save the model checkpoint
