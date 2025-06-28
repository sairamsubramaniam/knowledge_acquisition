
## BASICS OF NEURAL NETWORKS

--------------------

1. What is a neural network neuron?

A neural network consists of:
a) Input
2) Weights
3) Activation Function
4) Output

Usually a neural network processes inputs in this order:
- Inputs are multiplied with weights
- Results of above step are passed through Activation Function
- OUTPUT OF THE ABOVE STEP IS CALLED A NEURON
- These (neuron) outputs are multiplied with more weights and 
  passed through Activation Functions leading to more neurons as outputs
- At some point, a final layer of neurons are processed to give the final outputs of the model

Why are they called neurons?
- Because they behave like the neurons in our brain - deciding whether to OR how much to "pass on a signal" to the next layer.
- The activation function does one of the following things:
  - Outputs a number between 0 and 1 (if the function used in Sigmoid)
  - Outputs a number between 0 and inf (if the function used in ReLU)
  - Outputs a number between -1 and 1 (if the function used in tanh)
- The above point tells us that the input to "Neuron Activation" is either supressed to 0 or the signal is passed further (1, inf or -1)
- This behaviour is similar to neuron in the brain, where too a neuron either ignore or passes the signal input it receives



--------------------

2. What is the use of the learning rate?

"Backpropogation" in a neural network adjusts weights based on the derivative of the loss function with respect to the concerned weight.
The magnitude of the derivative however is an issue and makes the weight changes too large, making the training process unstable.

The reason why this unstability occurs is because we are supposed to make weight updates using partial derivatives.
Partial derivatives ignore the iter-relationships between weights and assumes that the update to this particular weight is "so small" that the inter-relationships shouldn't matter!
When we break this rule of "very small updates", instability occurs.

Learning rate is used to make the magnitude of the update (the derivative) very small! Thats the use of learning rate in neural networks



--------------------

3. How are weights initialized?

Weights are initialized randomly. The key point is to NOT initialize them as zeroes as then the network wouldn't start training.
Initialization can be random based on of the following strategies:
- Normal Distribution
  Randomly choosing numbers from a normal distribution
- Xavier Initialization
  Numbers from a uniform distribution but bounded by +/- (  sqrt(6) / sqrt(number\_of\_inputs + number\_of\_output\_neurons)  )
- Kaiming Initialization
  Randomly choosing numbers from a normal distribution and then multiplying the numbers with sqrt(2) / sqrt(number\_input\_parameters)

[source](https://towardsdatascience.com/weight-initialization-in-neural-networks-a-journey-from-the-basics-to-kaiming-954fb9b47c79)



--------------------

4. What is "loss" in a neural network?

Loss is the comparison between the model's output and the desired output. 
An ideal loss function should output a huge number when the gap between model's output and desired output is large
and a small number if it is small, becoming zero when there is no gap at all!

This number guides the training of a neural network. 
The network would update its weights with the objective of reducing this number



--------------------

5. What is the "chain rule" in gradient flow?

The chain rule states that:
if z == func2( func1(x) ), then:
    dz / dx  ==  A * B, where:
        A == d_func2( func1(x) ) / d_func1(x)    AND
        B == d_func1(x) / dx
meaning, consider the whole complicated (internal) function as "x" and find its derivative. Then multiply it the derivative of the (internal) function itself!



