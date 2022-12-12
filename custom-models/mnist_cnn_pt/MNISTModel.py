import torch
import torch.nn as nn
import torch.nn.functional as F

input_size = 784
hidden_sizes = [128, 64]
output_size = 10
# Build a feed-forward network

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.liner1=nn.Linear(input_size, hidden_sizes[0])
        self.liner2=nn.Linear(hidden_sizes[0], hidden_sizes[1])
        self.liner3=nn.Linear(hidden_sizes[1], output_size)

    def forward(self, x):
        model = nn.Sequential(self.liner1,
                      nn.ReLU(),
                      self.liner2,
                      nn.ReLU(),
                      self.liner3,
                      nn.LogSoftmax(dim=1))
        return model

class MNISTModel:
    def __init__(self):
        self._model = Net()
        self._model.load_state_dict(torch.load("mnist_cnn.pt"))
        self._model.eval()

    def predict(self, x, names):
        output = self._model(torch.from_numpy(x).float())
        return {"probability": output.tolist()}