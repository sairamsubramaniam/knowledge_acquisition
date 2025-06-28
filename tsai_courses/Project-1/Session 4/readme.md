## ARCHITECTURAL BASICS - General Approach

0. **Parameters that we wouldn't change for now** - Kernel Size: 3x3;  Activation: ReLU;  Maxpooling: 2x2

1. Decide size of "Convolution Block" From Image resolution 
   A 400x400 resolution requires 5 convoution layers to achieve a receptive field of 11x11
   Therefore, a 28x28 input should be okay having ~2 to 3 layers, receptive field of 5x5 OR 7x7 (we will go with 7x7)

2. Decide the number of kernels in the final layer of each convoluton block 
   A 400x400 image did well with 512 kernels before transition block
   Since, mnist is less complex with lesser expressivity, we will go with 32 kernels

3. Add convolution blocks & transition blocks until receptive field of the network nears object size
4. Meddle with batch size first and then the number of epochs
5. If the training accuracy is higher than validation accuracy, try adding after every layer (except last):
   * Dropout: parameter 0.1 To 0.5
   * Batch Normalization

6. Try learning rate changes to improve accuracy 



### ARCHITECTURAL BASICS - Based on the above approach, the order in which I would think of these concepts are:

1. **Things that are pre-decided**
   - 3x3 Convolutions _(3x3 is supported by hardware better and 3x3 can also be used to achieve receptive field of any size)_

2. **Deciding the Architecture - Convolution Block**
   - Receptive Field & How many layers _(This depends on how big the object is. All layers together must reach the receptive field of the object)_
   - Kernels and how do we decide the number of kernels? _(The layer where edges are detected, will have the highest number of kernels, e.g. 512 kernels for 400x400 img)_

3. **Deciding the Architecture - Transition Block**
   - Position of Transition Layer _(Transition layer awould be employed after every convolution block to decrease parameters & to combine channels in a way tht improves accuracy)_
   - 1x1 Convolutions _(An essential part of a transition block that achieves both the above stated objectives)_
   - MaxPooling & its position _(Max pooling reduces parameters to a great extent  and make computations possible. It could come either before or after  1x1 layer)_

4. **Deciding the Architecture - Final Layers**
   - The distance of MaxPooling / Batch Normalization from Prediction _(No max pooling or batch normalization would be deployed before the final layer as we do not want to distort the data just before the final output)_
   - SoftMax _(Softmax accentuates differences between outputs, however, if accuracy is too critical e.g. disease detection etc. we wouldn't rely on sofmax as the accentuation is not related to the inputs in any way)_

5. **Improving Accuracy**
   - Number of Epochs _(Sometimes, training for a longer time might improve accuracy)_
   - Batch Size _(Training with a lot of samples at one go, might help detecting expressivity / complex features better)_
   - Learning Rate _(Learning rate needs to be optimized in order to reach the right point in accuracy, else the model might keep oscillating without reaching max possible accuracy)_
   - LR schedule _(It has been observed that a step-shaped pattern of learning rates work better to improve accuracy. LR schedule helps us decrease LR slowly as number of epochs increase)_
   - Adam vs SGD _(Apologies, yet to read up on this)_

6. **Improving Accuracy - Reducing Overfitting**
   - DropOut _(Since, dropout over-trains some kernels, while dropping out a few, this helps in reducing over-fitting. We would use dropout, when training accuracy is higher than validation accuracy. Dropout works well between 10% to 50% depending on how simple the images are )_
   - Batch Normalization _(While training, a few kernels may be subdued by back-propogation, leading to lower validation accuracy. Batch normalization provides equal weightage to such kernels too and therefore helps in improving validation accuracy)_
   - Image Normalization _(Apologies, yet to read up on this)_
   
7. **Other things to think about**
   - When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered) _(Apologies, yet to read up on this)_
   - How do we know our network is not going well, comparatively, very early _(By looking at the validation accuracy of the first two epochs, if they are too far away from the target, our network is probably not very good)_
   - When to add validation checks _(With every epoch, so that we can save the best model)_