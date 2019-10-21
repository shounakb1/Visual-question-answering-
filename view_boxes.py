import matplotlib
matplotlib.use('Agg')
import os
import argparse
import tensorflow as tf
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from cnn1 import CNN
model_file='model_valid0.010.90.5(lr,deacy,dropout)0.010.990.2(lr,deacy,dropout)/legendbox_cnn'
# img=mpimg.imread(r'_LineCharts\3_line_0.png')
i = input("enter i:")
x=[]
y=[]
j=0
with open('linechart_csv_15001_20000.csv','r') as c:
                cr=csv.reader(c)
                for line in cr:
                    if(line[5]=="Legendbbox" and (j==i)):
                        img=np.array(mpimg.imread(str(line[0])))
                        image=mpimg.imread(str(line[0]))
                        print('image'+ str(line[0])+'loaded successfully...')
                        img=img[:,:,0:-1]
                        x.append(img)
                        y.append(list(map(float, line[1:5])))
                        j+=1
                        
                    elif(line[5]=="Legendbbox"):
                        j+=1            

num_classes = 4
input_size = 864
model = CNN(input_size = input_size, num_classes = num_classes, optimizer = 'Adam')
model.load(filepath = model_file)        
test_prediction= model.test(data = np.array(x))
print('truth:')
print(y[0])
print('prediction')
print(test_prediction[0])
image=image[int(test_prediction[0][3]):int(test_prediction[0][1]),int(test_prediction[0][0]):int(test_prediction[0][2])]
mpimg.imsave('view.png', image)