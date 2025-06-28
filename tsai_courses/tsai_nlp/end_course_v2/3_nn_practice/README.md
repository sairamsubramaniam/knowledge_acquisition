

### Submission by:
1. Sachin Dangayach (sachin.dangayach@gmail.com)
2. Sairam Subramaniam (sairam.subramaniam@gmail.com) 

[Here is the notebook where training was done](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/3_nn_practice/AdditionNet_Sachin_%26_Sai.ipynb)


# Objective

We aim to build a network that would:
1) Recognize handwritten digits when provided as an image input
2) know how to add any number between 0 to 9 to the number predicted from the MNIST image



# Data

- The network would use the MNIST dataset to train images to recognize handwritten digits
- We would also randomly append a number between 0 to 9 to each of the image in MNIST to train the model for addition
- This also means, we would append the sum of the number in the image (data label) and the newly added random number, as the second "label" in the dataset
- The random number would be converted into a one-hot encoded vector while training / prediction



# The Network / Model - Architecture

The network we decided to build is designed as follows:
1. Two convolutions with pooling applied to feature map
2. Dropout layer
3. Six fully connected layers leading to the two outputs - recognized digit & addition result

Design choices we made while building the network:
1. The network would have 2 main components:
  a. For digit recognition
  b. For adding the digit to the random number
2. Once we have the output from component (a), we would concatenate the one-hot encoded random number to the output
3. The final output would contain:
  a. A vector of 10 number giving the probabilities of the image being 0 to 9
  b. A vector of 19 numbers giving the probabilities of the addition being 0 to 18


The summary of the network looks like this:  
![Model Summary](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/3_nn_practice/images/Model%20Parameters.jpg)



# The Network / Model - Loss Function

We went ahead with the Negative Log Likelihood loss as that is known to give good results for comparing outputs for classification problems like this one.

Yes, we set it up as a classification problem mainly because:
  a. Digit recognition is involved
  b. The summations are constrained within the range of 0 to 18, with the input combinations being finite



# The training

Inspired by YOLO, we wanted to train the network for digit recognition for the first few epochs and then 
after it achieves certain level of accuracy, train it for the addition / summation objective

### ACCURACY ACHIEVED - 97.75%
To our surprise, the network does not take more than a few epochs to achieve an ~ 98% accuracy

Here are the loss and accuracy charts from training the network:


Training Logs  
![Training Logs Screenshot](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/3_nn_practice/images/training_logs.png)


Training Loss By Epochs  
![Chart - Training Losses by Epochs](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/3_nn_practice/images/training_loss_by_epochs.png)


Digit Recognition Accuracy By Epochs  
![Chart - Digit Recognition Accuracy by Epochs](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/3_nn_practice/images/test_acc_by_epochs_dra.png)


Addition Accuracy By Epochs  
![Chart - Addition Accuracy by Epochs](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/3_nn_practice/images/test_acc_by_epochs_aa.png)


Training Loss By Batch Iterations  
![Chart - Training Losses by Epochs](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/3_nn_practice/images/training_loss_by_batch_iterations.png)








