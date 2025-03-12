import torch
import torch.nn as nn

class SentimentNN(nn.Module):
    def __init__(self, input_size=5000, hidden_size=128):
        super(SentimentNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, 3)  # 3 classes: Negative, Neutral, Positive

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x