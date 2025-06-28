Receptive Field Of the Network = 907  (224x224 is incorrect!!)
---
```Formula: Prev RF + (Filter Size - 1) * JumpIn```

Layer Name | Filter Size | JumpIn | RF
--- | ---: | ---: | ---: | 
Input | 1 | NA | 1
convolution | 7 | 1 | 7
max pool | 3 | 2 | 11
convolution | 3 | 4 | 19
max pool | 3 | 4 | 27
inception (3a) | 5 | 8 | 59
inception (3b) | 5 | 8 | 91
max pool | 3 | 8 | 107
inception (4a) | 5 | 16 | 171
inception (4b) | 5 | 16 | 235
inception (4c) | 5 | 16 | 299
inception (4d) | 5 | 16 | 363
inception (4e) | 5 | 16 | 427
max pool | 3 | 16 | 459
inception (5a) | 5 | 32 | 587
inception (5b) | 5 | 32 | 715
avg pool | 7 | 32 | 907