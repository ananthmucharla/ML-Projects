import math
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
## Add more imports if required

##Sample Transformation function
#YOUR CODE HERE for changing the Transformation values.
trnscm = torchvision.transforms.Compose([torchvision.transforms.Resize((100,100)), torchvision.transforms.ToTensor(), torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

##Example Network
class Siamese(torch.nn.Module):
	def __init__(self):
		#YOUR CODE HERE
		
	def forward(self, x):
		#YOUR CODE HERE
		
##Sample classifier Network 
classifier = nn.Sequential(nn.Linear(64, 64), nn.BatchNorm1d(64), nn.ReLU(), nn.Linear(64, 32), nn.BatchNorm1d(32), nn.ReLU(), nn.Linear(32, 16))

##Definition of classes as dictionary
classes = ['person1','person2','person3','person4','person5','person6','person7']
