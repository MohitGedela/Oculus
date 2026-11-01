import torch
import torch.nn as nn


class BaselineCNN(nn.Module):
    def __init__(self, channels=(32, 64, 128, 256), dropout=0.3):
        super(BaselineCNN, self).__init__()

        self.blocks = nn.ModuleList()
        in_channels = 3
        for out_channels in channels:
            block = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=2),
            )
            self.blocks.append(block)
            in_channels = out_channels

        self.pool = nn.AdaptiveAvgPool2d(1)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(channels[len(channels) - 1], 1)

    def forward(self, x):
        for block in self.blocks:
            x = block(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.dropout(x)
        x = self.fc(x)
        return x


if __name__ == "__main__":
    model = BaselineCNN()
    fake_images = torch.randn(2, 3, 224, 224)
    output = model(fake_images)
    print(output.shape)