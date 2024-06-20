# Capstone-C241-PS083: DERMALYZE

## Bangkit Capstone Project 2024
This is the repository that is used for the Machine Learning path

## Project Description
We trained 2 learning models used to classify the potential skin disease/condition of the user along with the skin type. This analysis information is then used to educate and inform the user regarding the potential skin problem, along with possible treatment.

## Schedule During Development
|         Week 1         |       Week 2        |         Week 3          |               Week 4                |
|----------------------- |---------------------|-------------------------|-------------------------------------|
| Explore the literature |   Divide dataset    |   ML model testing #1   |          Data collection #2         |
|   Data collection #1   |   Build ML model    |  ML model evaluation #1 |          Data preparation #2        |
|   Data preparation #1  |                     |  ML model deployment #1 |  Compare new dataset into ML Model  |
|                        |                     |                         |          ML model testing #2        |
|                        |                     |                         |        ML model evaluation #2       |
|                        |                     |                         |        ML model deployment #2       |

## Schedule During Development
|         Week 1         |       Week 2        |         Week 3          |               Week 4                |
|----------------------- |---------------------|-------------------------|-------------------------------------|
| Identification Topics  |
| Explore the literature |   Divide dataset    |   ML model testing #1   |          Data collection #2         |
|   Data collection #1   |   Build ML model    |  ML model evaluation #1 |          Data preparation #2        |
|   Data preparation #1  |  ML model testing #1|  ML model deployment #1 |  Compare new dataset into ML Model  |
| Preprocessing Data #1  |                     |      Build ML model     |          ML model testing #2        |
|                        |                     |  ML model training #1   |        ML model evaluation #2       |
|                        |                     |                         |        ML model deployment #2       |
|                        |                     |                         |            Finishing Model          |
|                        |                     |                         |            ML model training #2     |

## Model
Image classification using a Convolutional Neural Network (CNN) architecture based on MobileNet and Inception.

## Tech Stack
- Python
- Keras
- TensorFlow
- Google Colaboratory
- Jupyter Notebook
- Scikit-Learn

## Datasets
The dataset was created from scratch from open-source data online. The data is stored in this repository
https://github.com/irvanwn/Dermalyze/tree/model/Dataset 

## Models
Due to size constraint of the models, we did not upload the models to this Github repo. The final model is stored in the following links,
[Skin Disease model](https://drive.google.com/drive/folders/19ZNzGaTxYQSUEfvLFn9xtM4t1QQYSfuc?usp=drive_link) and
[Skin Type Model](https://drive.google.com/drive/folders/1TCx6HXcrfljXfB3oloPQUc6XVx1kywtb?usp=sharing)

## Model Deployment 
Deployment is in GCP to ensure that the model runs well and not make the application intensive for the mobile device. This helps with people who don't own newer or more powerful phones.

## Running Training
To aid the training process of the models, we used Google Colaboratory. When trying to replicate our training process, we highly recommend inputting the notebook into Google Colaboratory and running using the GPU runtime. Here is a step-by-step process:

1. Open Google Colaboratory.
2. Import .ipynb (notebook) file into Google Colaboratory.
3. Connecting to GPU runtime (using GPU is crucial for training speed).
4. Running all the cells.
5. Download the model straight from the workspace or copy to the mounted Google Drive.
