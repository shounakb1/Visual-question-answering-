import matplotlib
matplotlib.use('Agg')
import os
import argparse
import tensorflow as tf
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


from cnn import CNN
model_file='model_large0.010.90.5(lr,deacy,dropout)0.010.990.2(lr,deacy,dropout)/legendbox_cnn'

num_classes = 4
input_size = 864
model = CNN(input_size = input_size, num_classes = num_classes, optimizer = 'Adam')
model.load(filepath = model_file)
np.random.seed(0)
global shuffled_idx
shuffled_idx = np.arange(20000)
np.random.shuffle(shuffled_idx)    
x_test=[]
y_test=[]
mini_batch_idx = [shuffled_idx[k] for k in range(1200, 1400)]
print(mini_batch_idx)
n=0
for i in mini_batch_idx:
    j=0

    with open('linechart_csv_15001_20000.csv','r') as c:
        cr=csv.reader(c)
        for line in cr:
            if(line[5]=="Legendbbox" and (j==i)):
                img=np.array(mpimg.imread(str(line[0])))
                img=img[:,:,0:-1]
                x_test.append(img)
                y_test.append(list(map(float, line[1:5])))
                print('loading image '+str(n))
                j+=1
                n+=1
            elif(line[5]=="Legendbbox"):
                j+=1
print(model.gradients(np.array(x_test),np.array(y_test)))