# END2 Session 1 Assignment

## Background & Very Basics

**Assignment**:
### 1. Rewrite the Colab file and:
  - remove the last activation function
  - make sure there are in total 44 parameters
  - run it for 2001 epochs
### 2. You must upload your assignment to a public GitHub Repository and share the link as the submission to this assignment

## Solution:

**[Link to file in git](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/1_intro_to_nn/group_submission/END2_0_Session_1.ipynb)**

### 3. Add a readme file to your project and describe these things:
  - What is a neural network neuron?
  - Ans: Within an artificial neural network, a neuron is a mathematical function that model the functioning of a biological neuron.
    Typically, a neuron compute the weighted average of its input, and this sum is passed through a nonlinear function, often called activation function, such as the sigmoid.

    ![alt](https://i.stack.imgur.com/wXL9A.png)
  - What is the use of the learning rate?
  - Ans: To reduce the training loss while training a neural network, we need to adjust the weights and for this we use SGD. The new value of weight is derived by subtracting the gradient of loss wrt weight multiplied by learning rate from old weight. Right choice of LR needed as if we chose higher values, we might get new weight values oscillating around local minima and if we chose very small value for LR, it will  take long time before we reach the local minima resulting the optimal weight for lesser loss.

  ![alt](https://www.fromthegenesis.com/wp-content/uploads/2020/04/lr_12420_1-1024x384.png)

  - How are weights initialized?
  - Ans: Weights are picked from random normal distribution. If we keep all the weights same, assume all 0 or 1, we will have problem of symmetry as each neuron will get the same value post activation. Also all neurons will get same update in case all of them has got same activation function. Also, lets assume we start with all 0 or 1s, as we start updating the weights, the average iterations we will need to get weights to optimal values will be more than that will choosing them randomly.
    There are approaches for initializing the weights per neuron based on fan in (number of connection to neuron) and fan out values (number of connection from neuron) like Xavier Weight Initialization - The xavier initialization method is calculated as a random number with a uniform probability distribution (U) between the range -(1/sqrt(n)) and 1/sqrt(n) or He Weight Initialization - The he initialization method is calculated as a random number with a Gaussian probability distribution (G) with a mean of 0.0 and a standard deviation of sqrt(2/n)

  - What is "loss" in a neural network?
  - Ans: Loss is nothing but a prediction error of Neural Net. And the method to calculate the loss is called Loss Function. In simple words, the Loss is used to calculate the gradients. And gradients are used to update the weights of the Neural Net.
    ![alt](https://cdn-images-1.medium.com/max/800/1*N1PyOYeog-vyytRbwEwQCQ.png)

  - What is the "chain rule" in gradient flow?
  - Ans: The chain rule is use to calculate the derivative or gradient of a composite function. If a variable z depends on the variable y, which itself depends on the variable x, so that y and z are dependent variables, then z, via the intermediate variable of y, depends on x as well.
    ![alt](https://miro.medium.com/max/1365/1*e6Epzbmngh2a50WUrKleUA.png)
