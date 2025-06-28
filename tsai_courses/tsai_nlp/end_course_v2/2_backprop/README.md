

# Training a neural network in excel

See [here](https://docs.google.com/spreadsheets/d/1TFFpHnyvWdSU_Ql9Et7SKmbfh2FQzmf4aM_nZvxrEHc/edit?usp=sharing) for an implementation of the formulae given below.

Screenshots of the loss function curve for different learning rates given at the end.
Screenshot of the excel file given below:
![Training a neural network in excel](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/2_backprop/images/training_nn_in_excel.png)

---

## Neural Network  
Assuming we have a neural network as given below, we will in later sections give formulae for forward and backward propogation  
  
**Inputs:** i1 and i2  
  
**Layer1 Weights:** w1, w2, w3, w4  
  
**Layer1 Outputs:** h1, h2  
  
**Layer1 Activations:** a\_h1, a\_h2  
  
**Layer2 Weights:** w5, w6, w7, w8  
  
**Layer2 Outputs:** o1, o2  
  
**Layer2 Activations:** a\_o1, a\_o2  
  
**Targets:** t1, t2  

---


## Forward Propogation

The below formulae detail out calculation of outputs, activations and errors would be as follows:

h1 = i1 * w1  +  i2 * w2  
h2 = i1 * w3  +  i2 * w4  
  
a\_h1 = exp(h1)  /  ( exp(h1) + 1 )  
a\_h2 = exp(h2)  /  ( exp(h2) + 1 )  
  
o1 = a\_h1 \* w5  +  a\_h2 \* w6  
o2 = a\_h1 \* w7  +  a\_h2 \* w8  
  
a\_o1 = exp(o1)  /  ( exp(o1) + 1 )  
a\_o2 = exp(o2)  /  ( exp(o2) + 1 )  
  
  
E1 (Error from a\_o1)  =  (1/2) \* ((t1 - a\_o1)^2)  
E2 (Error from a\_o2)  =  (1/2) \* ((t2 - a\_o2)^2)  
E\_T (Total Error)      =  E1 + E2  

---


## Backward Propogation

**Imp Note:** _Please read the "Chain Rule Comonents" column below as the numberator in the first row and enominator in the row right below it!_


| Derivative    | Derivative Formula                                 | Chain Rule Components           |
| --------------|----------------------------------------------------|---------------------------------|
| d-E\_T / d-w1 | = [A+B] * (sig(h1) * (1-sig(h1))) * i1             | d-E\_T   \*  d-a\_h1  \*  d-h1  |
|               | = [A+B] * a\_h1 * (1-a\_h1) * i1                   | d-a\_h1  \*  d-h1     \*  d-w1  |
|               |                                                    |                                 |
| d-E\_T / d-w2 | = [A+B] * (sig(h1) * (1-sig(h1))) * i2             | d-E\_T   \*  d-a\_h1  \*  d-h1  |
|               | = [A+B] * a\_h1 * (1-a\_h1) * i2                   | d-a\_h1  \*  d-h1     \*  d-w2  |
|               |                                                    |                                 |
| d-E\_T / d-w3 | = [C+D] * (sig(h2) * (1-sig(h2))) * i1             | d-E\_T   \*  d-a\_h2  \*  d-h2  |
|               | = [C+D] * a\_h2 * (1-a\_h2) * i1                   | d-a\_h2  \*  d-h2     \*  d-w3  |
|               |                                                    |                                 |
| d-E\_T / d-w4 | = [C+D] * (sig(h2) * (1-sig(h2))) * i2             | d-E\_T   \*  d-a\_h2  \*  d-h2  |
|               | = [C+D] * a\_h2 * (1-a\_h2) * i2                   | d-a\_h2  \*  d-h2     \*  d-w4  |
|               |                                                    |                                 |
| d-E\_T / d-w5 | = (a\_o1 - t1) * (sig(o1) * (1-sig(o1))) * a\_h1   | d-Et     \*  d-a\_o1  \*  d-o1  |
|               | = (a\_o1 - t1) * a\_o1 * (1-a\_o1) * a\_h1         | d-a\_o1  \*  d-o1     \*  d-w5  |
|               |                                                    |                                 |
| d-E\_T / d-w6 | = (a\_o1 - t1) * (sig(o1) * (1-sig(o1))) * a\_h2   | d-Et     \*  d-a\_o1  \*  d-o1  |
|               | = (a\_o1 - t1) * a\_o1 * (1-a\_o1) * a\_h2         | d-a\_o1  \*  d-o1     \*  d-w6  |
|               |                                                    |                                 |
| d-E\_T / d-w7 | = (a\_o2 - t2) * (sig(o2) * (1-sig(o2))) * a\_h1   | d-Et     \*  d-a\_o2  \*  d-o2  |
|               | = (a\_o2 - t2) * a\_o2 * (1-a\_o2) * a\_h1         | d-a\_o2  \*  d-o2     \*  d-w7  |
|               |                                                    |                                 |
| d-E\_T / d-w8 | = (a\_o2 - t2) * (sig(o2) * (1-sig(o2))) * a\_h2   | d-Et     \*  d-a\_o2  \*  d-o2  |
|               | = (a\_o2 - t2/ * a\_o2 * (1-a\_o2) * a\_h2         | d-a\_o2  \*  d-o2     \*  d-w8  |
|               |                                                    |                                 |


---

## TOTAL LOSS BY EPOCH CHARTS FOR DIFFERENT LEARNING RATES:

### Learning Rate = 0.1
![Total Loss by Epochs (LR = 0.1)](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/2_backprop/images/Total%20Loss%20by%20Epochs%20%28LR%20%3D%200.1%29.png)

### Learning Rate = 0.2
![Total Loss by Epochs (LR = 0.2)](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/2_backprop/images/Total%20Loss%20by%20Epochs%20%28LR%20%3D%200.2%29.png)

### Learning Rate = 0.5
![Total Loss by Epochs (LR = 0.5)](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/2_backprop/images/Total%20Loss%20by%20Epochs%20%28LR%20%3D%200.5%29.png)

### Learning Rate = 0.8
![Total Loss by Epochs (LR = 0.8)](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/2_backprop/images/Total%20Loss%20by%20Epochs%20%28LR%20%3D%200.8%29.png)

### Learning Rate = 1.0
![Total Loss by Epochs (LR = 1.0)](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/2_backprop/images/Total%20Loss%20by%20Epochs%20%28LR%20%3D%201.0%29.png)

### Learning Rate = 2.0
![Total Loss by Epochs (LR = 2.0)](https://github.com/sairamsubramaniam/tsai_nlp/blob/master/end_course_v2/2_backprop/images/Total%20Loss%20by%20Epochs%20%28LR%20%3D%202.0%29.png)


