# Wound-Analysis-Auxiliary
Repository for additional code not required for live server deployment but necessary for preprocessing.

Mainly this repo is made for preprocessing the images given to train the Siamese network in Wound-Analysis-ML.

This is because Wound-Analysis-ML is directly deployed on Heroku, which has a maximum size limit that it's currently barely under. As a result, anything unncessary, such as processing with OpenCV, will not be present on that repo, and will instead be here.