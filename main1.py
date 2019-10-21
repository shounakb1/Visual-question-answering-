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
from utils import plot_curve
os.environ["CUDA_VISIBLE_DEVICES"]="1"
train_losses=list()
valid_losses=list()


def train(learning_rate, learning_rate_decay, dropout_rate, mini_batch_size, epochs, optimizer, random_seed, model_directory, model_filename, log_directory,continue_training):

    
    num_classes = 4
    input_size = 864
    training_size=8000
    global train_losses
    global valid_losses
    num_batches=training_size/mini_batch_size
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    if continue_training:
        model_file = os.path.join(model_directory, model_filename)
        tf.reset_default_graph()
        model = CNN(input_size = input_size, num_classes = num_classes, optimizer = 'Adam')
        print('loading saved model...')
        model.load(filepath = model_file)
        validation_idx = [shuffled_idx[k: k + mini_batch_size] for k in range(8000, 10000, mini_batch_size)]
        lowest_loss=0
        for i, idx in enumerate(validation_idx):
            j=0
            n=0
            x_validation=[]
            y_validation=[]
            with open('linechart_csv_15001_20000.csv','r') as c:
                cr=csv.reader(c)
                for line in cr:
                    if(line[5]=="Legendbbox" and j in idx):
                        print('got image')
                        img=np.array(mpimg.imread(str(line[0])))
                        img=img[:,:,0:-1]

                        x_validation.append(img)
                        y_validation.append(list(map(float, line[1:5])))
                        print('loading validation image '+str(n)+'of batch '+str(i))
                        n+=1
                        j+=1
                    elif(line[5]=="Legendbbox"):
                        j+=1
            _, loss=model.validate(np.array(x_validation),np.array(y_validation))
            lowest_loss+=loss
        lowest_loss/=5
        print('initial validation loss:'+str(lowest_loss))    
    else:
        model = CNN(input_size = input_size, num_classes = num_classes, optimizer = optimizer)
        lowest_loss=float("inf")
 
    mini_batch_idx = [shuffled_idx[k: k + mini_batch_size] for k in range(0, training_size, mini_batch_size)]
    
    for epoch in range(epochs):
        print('Epoch: %d' % epoch)

        learning_rate *= learning_rate_decay
        # Prepare mini batches on train set
        
        

        epoch_loss=0
        # Train on train set
        for i, idx in enumerate(mini_batch_idx):
            j=0
            n=0
            x_train=[]
            y_train=[]
            with open('linechart_csv_15001_20000.csv','r') as c:
                cr=csv.reader(c)
                for line in cr:
                    if(line[5]=="Legendbbox" and j in idx):
                        print('got image')
                        img=np.array(mpimg.imread(str(line[0])))
                        img=img[:,:,0:-1]

                        x_train.append(img)
                        y_train.append(list(map(float, line[1:5])))
                        print('loading image '+str(n)+'of batch '+str(i))
                        n+=1
                        j+=1
                    elif(line[5]=="Legendbbox"):
                        j+=1
#             print(np.array(x_train).shape)
            epoch_loss += model.train(data = np.array(x_train), label = np.array(y_train), learning_rate = learning_rate, dropout_rate = dropout_rate)
            
        
        
        print('Training Loss: %f' % (epoch_loss/num_batches))
        train_losses.append(epoch_loss/num_batches)
        validation_idx = [shuffled_idx[k: k + mini_batch_size] for k in range(8000, 10000, mini_batch_size)]
        validation_loss=0
        for i, idx in enumerate(validation_idx):
            j=0
            n=0
            x_validation=[]
            y_validation=[]
            with open('linechart_csv_15001_20000.csv','r') as c:
                cr=csv.reader(c)
                for line in cr:
                    if(line[5]=="Legendbbox" and j in idx):
                        print('got image')
                        img=np.array(mpimg.imread(str(line[0])))
                        img=img[:,:,0:-1]

                        x_validation.append(img)
                        y_validation.append(list(map(float, line[1:5])))
                        print('loading validation image '+str(n)+'of batch '+str(i))
                        n+=1
                        j+=1
                    elif(line[5]=="Legendbbox"):
                        j+=1
            _, loss=model.validate(np.array(x_validation),np.array(y_validation))
            validation_loss+=loss
        validation_loss/=5
        print('validation_loss:'+str(validation_loss))
        valid_losses.append(validation_loss)
        if((validation_loss)<lowest_loss):
            lowest_loss=validation_loss
            model.save(directory = model_directory, filename = model_filename)
            print('Trained model saved successfully with loss:'+str(lowest_loss))
    plot_curve(train_losses = train_losses,valid_losses = valid_losses,filename = os.path.join(log_directory, str(learning_rate)+str(learning_rate_decay)+str(dropout_rate)+'training_curve.png'))        

def test(model_file):

    tf.reset_default_graph()

    # Load CIFAR10 dataset
    # cifar10 = CIFAR10()
#     x_test = np.array(x[800:1000])
#     y_test = np.array(y[800:1000])
    x_test=[]
    y_test=[]
    mini_batch_idx = [shuffled_idx[k] for k in range(10000, 10400)]
#     print(mini_batch_idx)
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

    num_classes = 4
    input_size = 864

    model = CNN(input_size = input_size, num_classes = num_classes, optimizer = 'Adam')
    model.load(filepath = model_file)
#     print(len(x_test))
    test_prediction= model.test(data = np.array(x_test))
    print(y_test[0:10])
    print(test_prediction[0:10])
    # print('Test Accuracy: %f' % test_accuracy)


def main():
    # Default settings
    learning_rate_default = 0.01
    learning_rate_decay_default = 0.9
    dropout_rate_default = 0.5
    mini_batch_size_default = 400
    epochs_default = 30
    optimizer_default = 'Adam'
    random_seed_default = 0
    model_directory_default = 'model_valid'+str(learning_rate_default)+str(learning_rate_decay_default)+str(dropout_rate_default)+'(lr,deacy,dropout)'
    model_filename_default = 'legendbox_cnn'
    log_directory_default = 'log'

    # Argparser 
    parser = argparse.ArgumentParser(description = 'Train CNN on CIFAR10 dataset.')

    parser.add_argument('-train', '--train', help = 'train model', action = 'store_true')
    parser.add_argument('-test', '--test', help = 'test model', action = 'store_true')
    parser.add_argument('-continue_training', '--continue_training', help = 'continue training from saved model', action = 'store_true')
    parser.add_argument('--lr', type = float, help = 'initial learning rate', default = learning_rate_default)
    parser.add_argument('--lr_decay', type = float, help = 'learning rate decay', default = learning_rate_decay_default)
    parser.add_argument('--dropout', type = float, help = 'dropout rate', default = dropout_rate_default)
    parser.add_argument('--batch_size', type = int, help = 'mini batch size', default = mini_batch_size_default)
    parser.add_argument('--epochs', type = int, help = 'number of epochs', default = epochs_default)
    parser.add_argument('--optimizer', type = str, help = 'optimizer', default = optimizer_default)
    parser.add_argument('--seed', type = int, help = 'random seed', default = random_seed_default)
    parser.add_argument('--model_dir', type = str, help = 'model directory', default = model_directory_default)
    parser.add_argument('--model_filename', type = str, help = 'model filename', default = model_filename_default)
    parser.add_argument('--log_dir', type = str, help = 'log directory', default = log_directory_default)

    argv = parser.parse_args()

    global learning_rate
    global learning_rate_decay
    global dropout_rate
    global log_directory
    
    # Post-process argparser
    learning_rate = argv.lr
    learning_rate_decay = argv.lr_decay
    dropout_rate = argv.dropout
    mini_batch_size = argv.batch_size
    epochs = argv.epochs
    optimizer = argv.optimizer
    random_seed = argv.seed
    model_directory = argv.model_dir+str(learning_rate_default)+str(learning_rate_decay)+str(dropout_rate)+'(lr,deacy,dropout)'
    model_filename = argv.model_filename
    log_directory = argv.log_dir
    
    np.random.seed(random_seed)
    global shuffled_idx
    shuffled_idx = np.arange(20000)
    np.random.shuffle(shuffled_idx)
    print(shuffled_idx[0:10])
    
    if argv.train:
        print('Training ...')
        train(learning_rate = learning_rate, learning_rate_decay = learning_rate_decay, dropout_rate = dropout_rate, mini_batch_size = mini_batch_size, epochs = epochs, optimizer = optimizer, random_seed = random_seed, model_directory = model_directory, model_filename = model_filename, log_directory = log_directory,continue_training=argv.continue_training)

    if argv.test:
        print('Testing...')
        test(model_file = os.path.join(model_directory, model_filename))


if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        val = input("Save graph?")
        if(val==1):
            plot_curve(train_losses = train_losses,valid_losses = valid_losses,filename = os.path.join(log_directory, str(learning_rate)+str(learning_rate_decay)+str(dropout_rate)+'training_curve.png')) 
#             print('het')