import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import pickle

shuffled_idx = np.arange(20000)
np.random.shuffle(shuffled_idx)
        
mini_batch_idx = [shuffled_idx[k: k + 100] for k in range(0, 8000, 100)]
for i, idx in enumerate(mini_batch_idx):
            j=0
            x_train=[]
            y_train=[]
            with open('linechart_csv_15001_20000.csv','r') as c:
                cr=csv.reader(c)
                for line in cr:
#                     print(idx)
#                     print(j)
                    if(line[5]=="Legendbbox" and j in idx):
                        print('got image')
                        img=np.array(mpimg.imread(str(line[0])))
                        img=img[:,:,0:-1]

                        x_train.append(img)
                        y_train.append(list(map(float, line[1:5])))
                        print('loading image '+str(j)+'of batch '+str(i))
                        j+=1
                    elif(line[5]=="Legendbbox"):
                        j+=1
print(np.arra)        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                