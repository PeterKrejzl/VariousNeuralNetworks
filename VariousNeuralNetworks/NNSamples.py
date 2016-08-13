'''
based on very nice tutorial
from https://github.com/dennybritz/nn-from-scratch/blob/master/nn-from-scratch.ipynb
'''

import numpy as np
import sklearn
import sklearn.datasets 
import matplotlib.pyplot as plt
import sklearn.linear_model
import matplotlib
from pprint import pprint

def plot_decision_boundary(pred_func):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    
    
    
    
#generate a dataset and plot it
np.random.seed(0)
X,y = sklearn.datasets.make_moons(500, noise=0.2)

#pprint(X.shape)
#(500,2)
#quit()
#plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
#plt.show()


#clf = sklearn.linear_model.LogisticRegression()
#clf.fit(X,y)

#plot_decision_boundary(lambda x: clf.predict(x))
#plt.title('Logistic regression')
#plt.show()



'''
Training a neural network
he number of nodes in the input layer is determined 
by the dimensionality of our data

Similarly, the number of nodes in the output layer 
is determined by the number of classes we have
'''
num_examples = len(X) #training set size
nn_input_dim = 2 #input layer dimensionality
nn_output_dim = 2 #output layer dimensionality

#gradient descent parameters
epsilon = 0.01
reg_lambda = 0.01

def calculate_loss(model):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    #forward propagation
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis = 1, keepdims=True)
    #calculating the loss
    corect_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(corect_logprobs)
    #add regularization
    data_loss += reg_lambda / 2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    
    return 1./num_examples * data_loss

#helper function to predict an output (0 or 1)
def predict(model, x):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    #forward propagation
    z1 = x.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    
    return np.argmax(probs, axis=1)


#this function learms parameters for the neural network
# and returns model
#- nn_hdim: number of nodes in the hidden layer
#- num_passes: number of passes through the training data 
# for gradient descent
#- print_loss: if True, print the loss every 1000 iterations
def build_model(nn_hdim, num_passes=20000,print_loss=False):
    #initialize the parameters to random values
    #we need to learn these
    np.random.seed(0)
    W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1,nn_hdim))
    W2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, nn_output_dim))
    
    #this is what we return at the end
    model = {}
    
    for i in xrange(0, num_passes):
        #forward propagation
        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        
        #backpropagation
        delta3 = probs
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1,2))
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)
        
        #add regularization
        dW2 += reg_lambda * W2
        dW1 += reg_lambda * W1
        
        #gradient descent
        W1 += -epsilon * dW1
        b1 += -epsilon * db1
        W2 += -epsilon * dW2
        b2 += -epsilon * db2
        
        #assign new paramaters to the model
        model = {'W1' : W1, 'b1' : b1, 'W2' : W2, 'b2' : b2}
        
        
        #optionally, print the loss (expensive)
        if print_loss and i % 1000 == 0:
            print('Loss after iteration %i: %f' % (i, calculate_loss(model)))
            
    return(model)
    
    
model = build_model(200, print_loss=False, num_passes=100000)
plot_decision_boundary(lambda x: predict(model,x ))
plt.title('Decision boundary for hidden layer size 3')
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





