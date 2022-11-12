# Copyright (C) 2022, Kevin J McEntee.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.
#
# I wrote this script as my first exercise on my journey to learn Python and Git

import sys

from pyrovision.models import rexnet1_0x
from torchvision import transforms
import torch
from PIL import Image


# Init
print("Setting up transform...")
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

# original transform from https://github.com/pyronear/pyro-vision/blob/master/README.md
# as of date November 11, 2022
#theTransform = transforms.Compose([transforms.Resize(size=448), transforms.CenterCrop(size=448),
#                                  transforms.ToTensor(), normalize])

# new transform height and width from Mateo email of November 12, 2022
theTransform = transforms.Compose([transforms.Resize([256, 384]),
                                  transforms.ToTensor(), normalize])

print("setting up model...")
model = rexnet1_0x(pretrained=True).eval()

# Predict
numberOfFiles = len(sys.argv)
for index in range(1, numberOfFiles):
    theImage = theTransform(Image.open(sys.argv[index]).convert('RGB'))

    with torch.no_grad():
        prediction = model(theImage.unsqueeze(0))
        is_wildfire = torch.sigmoid(prediction).item() >= 0.5

    print("Predicting", sys.argv[index], is_wildfire)

print("Finished")
