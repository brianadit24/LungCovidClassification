from torch import nn
from torchvision.models import resnet34

class LungCovNet(nn.Module):
    def __init__(self, output_size=2):
        super().__init__()
        self.basemodel = resnet34(pretrained=False)
        self.freeze()
        self.basemodel.fc = nn.Sequential(
            nn.Linear(512, output_size),
            nn.LogSoftmax(dim=1)
        )
    
    def forward(self, x):
        x = self.basemodel(x)
        return x

    def freeze(self):
        for param in self.basemodel.parameters():
            param.requires_grad = False # Freezing Weight
    
    def unfreeze(self):
        for param in self.basemodel.parameters():
            param.requires_grad = True # Unfreezing Weight