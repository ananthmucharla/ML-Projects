import torch
import torchvision
import torch.nn as nn
## Add more imports if required

####################################################################################################################
# Define your model and transform and all necessary helper functions here               		           #
# They will be imported to the exp_recognition.py file    							   # 
####################################################################################################################

# Definition of classes as dictionary
classes = {0: 'ANGER', 1: 'DISGUST', 2: 'FEAR', 3: 'HAPPINESS', 4: 'NEUTRAL', 5: 'SADNESS', 6: 'SURPRISE'}

# Example Network
class facExpRec(torch.nn.Module):
	def __init__(self):
		#YOUR CODE HERE
		
	def forward(self, x):
		#YOUR CODE HERE
		
# sample Helper function        
def rgb2gray(image):
	return image.convert('L')
	
# Sample Transformation function
#YOUR CODE HERE for changing the Transformation values.
trnscm = torchvision.transforms.Compose([rgb2gray, torchvision.transforms.Resize((48,48)), torchvision.transforms.ToTensor(), torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
