Copyright (C) 2022, Kevin J McEntee.

This program is licensed under the Apache License version 2.
See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

Running the script
==================
python3 cliWildFireDetect.py sampleimages/BeverlyHillsFire.jpeg sampleimages/BonnyDoonFire.jpeg sampleimages/LiveOakNurseryFire.jpeg sampleimages/Santa1Fire.jpeg sampleimages/Santa2Fire.jpeg sampleimages/Santa3Fire.jpeg sampleimages/Santa4Fire.jpeg sampleimages/Santa5Fire.jpeg sampleimages/Santa6Fire.jpeg sampleimages/SnowBear.jpeg sampleimages/SnowMakers.jpeg sampleimages/Toro1Fire.jpeg sampleimages/Toro2Fire.jpeg sampleimages/ValleyFog.jpeg 


Introduction
============
I wrote this short script to help teach myself python and git.  I am interested in machine learning and I live in a 
wildfire prone area of California.  I found the https://github.com/pyronear/pyro-vision project on GitHub and
decided to try it out with some images I have captured on my iPhone in the past few years.  Thank you to Mateo
and Francois for being so responsive to my questions.

In the sampleimages directory, there are 11 actual wildfire images and 3 images with no fire.

Images with fire smoke
=======================
BeverlyHillsFire.jpeg was taken on a visit to Beverly Hills, Californian, in July of 2020.  The large fire was
about 65 kilometers (40 miles) north of where I was standing.

BonnyDoonFire.jpeg was taken near my home during the CZU Lightning Fire in August of 2020.  I was 8 kilometers
(5 miles) from the fire.

LiveOakNurseryFire.jpeg was taken from my home and shows a plant nursery on fire in August of 2022.  I was 
12 kilometers (7.5 miles) from the fire.

SantaNFire.jpeg is a time series of images taken from my home of a small fire 5 kilometers (3 miles) away.

ToroNFire.jpeg are 2 images I took of a large fire in Toro Park, far across Monterey Bay from 
my home.  I was 64 kilometers (40 miles) from the fire.

Images without fire smoke
==========================
ValleyFog.jpeg was taken from my home on a cold November 2022 morning and contains valley fog.  Some models
may produce a false positive, mistaking the fog for smoke.

SnowMakers.jpeg was taken in Northstar Village (near Lake Tahoe) in November of 2022.  The snow makers on the right 
side of the images could be seen as blowing smoke.

SnowBear.jpeg, because... Why not?

Results
=======
As of the initial push date of November 12, 2022, the pyrovision model inferred  
Correct positive : 5 of the 11 fire images  
False negatives : 6 of the 11 fire images  
Correct negatives : 3 of 3 non-fire images  






