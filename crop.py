### for each set of coordinates generated in the res_[filename].txt, crop and output to crop folder - dylan-roussin

# example line: '1706,20,1784,20,1784,38,1706,38'
# read as: bottom-left, bottom-right, top-right, top-left
# bottomleft(1706,20) 
# bottomright (1784,20) 
# topright (1784,38) 
# topleft (1706,38)

import numpy as np

coor_file = "result/res_csgo.txt"

# open craft result txt
with open(coor_file) as f:
    lines = f.read().split("\n") # new lines char are their own entry in resulting array
    bounding_coor = np.array([line for line in lines if line.strip() != ""]) # remove new line char from array
    
for i in bounding_coor:
  print("test")

# crop with numpy slicing to create a pointer to crop points rather than creating new images https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python