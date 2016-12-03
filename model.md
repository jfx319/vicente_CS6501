

estimating model size in memory:  
http://cs231n.github.io/convolutional-networks/


some keras tutorials:  
http://ml4a.github.io/guides/convolutional_neural_networks/  

fchollet's blog:  
https://blog.keras.io/author/francois-chollet.html  


vgg16 in keras code:  
https://gist.github.com/baraldilorenzo/07d7802847aaad0a35d3  
  this is actually not necessary, since there is now an 'Applications' module with many preloaded models

Viewing json model
```python
from keras.applications.vgg16 import VGG16
model = VGG16(weights='imagenet', include_top=False)

json_string = model.to_json()
open('./VGG16_notop.json', 'w').write(json_string)

import json
import pprint

with open ('VGG16_notop.json', 'r') as handle:
  parsed = json.load(handle)

pprint.pprint(parsed)
```
