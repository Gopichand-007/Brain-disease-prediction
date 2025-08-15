import torch
import torch.nn as nn
import torch.optim as optim

# Dummy model for demonstration
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(224*224, 2)  # 2 classes: Disease / No Disease

    def forward(self, x):
        return self.fc(x)

if __name__ == "__main__":
    model = SimpleNet()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    print("Model Ready for Training")
