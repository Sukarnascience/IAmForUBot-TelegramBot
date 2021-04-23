import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nlpInput import bagOfWords, tokenize, stemming
from neuralNetwork import NeuralNet

teachingFile = "teachingData.json"
trainingFile = "trainingData.pth"

x_train = []
y_train = []

all_words = []
tags = []
xy = []

ignore = ['!',',','?','.']

batchSize = 8
hidden_size = 8
learning_rate = 0.001
num_epochs = 1000

with open(teachingFile,'r') as dataFile:
    intents = json.load(dataFile)

for i in intents["intents"]:
    tag = i['tag']
    tags.append(tag)
    for j in i["patterns"]:
        words = tokenize(j)
        all_words.extend(words)
        xy.append((words,tag))

all_words = [stemming(i) for i in all_words if i not in ignore]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

for (patternsSent,tag) in xy:
    bag = bagOfWords(patternsSent,all_words)
    x_train.append(bag)
    labelData = tags.index(tag)
    y_train.append(labelData)

x_train = np.array(x_train)
y_tarin = np.array(y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self,idx):
        return self.x_data[idx],self.y_data[idx]

    def __len__(self):
        return self.n_samples

output_size = len(tags)
input_size = len(x_train[0])

dataset = ChatDataset()

device = torch.device('cpu')
train_loader = DataLoader(dataset=dataset,batch_size=batchSize,shuffle=True,num_workers=0) 
model = NeuralNet(input_size,hidden_size,output_size).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)

for epoch in range(num_epochs):
    for (words,labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        output = model(words)
        loss = criterion(output,labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

tranningData = {
    "model_state":model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

torch.save(tranningData,trainingFile)
