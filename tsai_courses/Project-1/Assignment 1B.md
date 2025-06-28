
**1) What are Channels and Kernels (according to EVA)?**

_ans)_ **Kernels** - A kernel is a matrix (in our case always a 3x3 matrix) that detects. What does it detect? Edges or patterns or shapes in an image. How does it do that? Well a 3x3 matrix is a pattern. For example this is a triangle (approximately if youo consider only the 1s):

![A triangular pattern seen in a kernel](https://res.cloudinary.com/dsmlqb6t9/image/upload/v1556821189/Drawing_plpprz.png)

The above kernel would detect triangles in an image. The method of "detection" is to "convolve" the kernel, i.e. multiply each value of the kernel with with every possible 3x3 sections of the image and the output image would have only (all the) triangles (from the original image) in it. The output image which has all the edges / patterens collected at one place is called a

_ans)_ **Channel** - A channel is therefore layer that consists of ONE feature (e.g. a verticla line, a triangle, all thee red pixels in an image etc.). We can create the image by laying the channels one above the other like say a set "Over-head Projector" sheets.


**2) Why should we only (well mostly) use 3x3 Kernels?**
- Because we can re-create the effect ofo any other odd-numbered kernel (5x5, 7x7 etc.) with a 3x3 kernel. For example a 5x5 kernel's effect can be recreated using a 3x3 kernel over 2 layers
- Nowadays, GPUs have been optimized to run 3x3 kernels the most efficiently as opposed to other sized kernels


**3) How many times do we need to perform 3x3 convolution operation to reach 1x1 from 199x199 (show calculations)**
We will have to perform a 100 such operations to reach 1x1 as shown below:

199 | 197 | 195 | 193 | 191 | 189 | 187 | 
185 | 183 | 181 | 179 | 177 | 175 | 173 | 
171 | 169 | 167 | 165 | 163 | 161 | 159 | 
157 | 155 | 153 | 151 | 149 | 147 | 145 | 
143 | 141 | 139 | 137 | 135 | 133 | 131 | 
129 | 127 | 125 | 123 | 121 | 119 | 117 | 
115 | 113 | 111 | 109 | 107 | 105 | 103 | 
101 | 99 | 97 | 95 | 93 | 91 | 89 | 
87 | 85 | 83 | 81 | 79 | 77 | 75 | 
73 | 71 | 69 | 67 | 65 | 63 | 61 | 
59 | 57 | 55 | 53 | 51 | 49 | 47 | 
45 | 43 | 41 | 39 | 37 | 35 | 33 | 
31 | 29 | 27 | 25 | 23 | 21 | 19 | 
17 | 15 | 13 | 11 | 9 | 7 | 5 | 
3 | 1
