#Python implementation of a simple two layer neural network, which computes an XOR of a given input

import numpy as np
import time 

#input variables 
n_hidden=10
n_in=10

#output variables 
n_out=10

#No of Sample data 
n_sample=300

#Hyperparameters 
learning_rate =0.01
momentum=0.9

#Non-Deterministic seeding 
np.random.seed(0)

def sigmoid(x):
	return 1.0/(1.0+np.exp(-x))

def tanh_prime(x):
	return 1-np.tanh(x)**2

def train(x,t,V,W,bV,bW):

	#forward propogation 
	A=np.dot(x,V)+bV
	Z=np.tanh(A)

	B=np.dot(Z,W)+bW
	Y=sigmoid(B)


	#backword propogation 
	Ew=Y-t
	Ev=tanh_prime(A)*np.dot(W,Ew)


	#predict our loss
	dW=np.outer(Z,Ew)
	dV=np.outer(x,Ev)

	#cross entropy 
	loss=np.mean(t*np.log(Y)+(1-t)*np.log(1-Y))

	return loss, (dV,dW,Ev,Ew)


def predict(x,V,W,bV,bW):
	A=np.dot(x,V)+bV
	B=np.dot(np.tanh(A),W)+bW

	return (sigmoid(B)>0.5).astype(int)

#create layers 
V=np.random.normal(scale=0.1,size=(n_in,n_hidden))
W=np.random.normal(scale=0.1,size=(n_hidden,n_out))

bV=np.zeros(n_hidden)
bW=np.zeros(n_out)

params=[V,W,bV,bW]

#generating data .............
x=np.random.binomial(1,0.5,(n_sample,n_in))
T=x^1

#Training NN .........
for epoch in range(100):
	err=[]
	update=[0]*len(params)

	t0=time.clock()

	for i in range(x.shape[0]):

		loss,grad=train(x[i],T[i],*params)

		#update loss 

		for j in range(len(params)):
			params[j]-=update[j]

		for j in range(len(params)):
			update[j]=learning_rate*grad[j]+momentum*update[j]

		err.append(loss)

	print( "Epoch: %d, Loss: %.8f, Time: %.4fs" % (epoch, np.mean( err ), time.clock()-t0 ))

#Try to predict 

x=np.random.binomial(1,0.5,n_in)
print('XOR Prediction')
print(x)
print(predict(x,*params))







"""
OUTPUT :

Epoch: 0, Loss: -0.45465070, Time: 0.0400s
Epoch: 1, Loss: -0.13697961, Time: 0.0500s
Epoch: 2, Loss: -0.06206941, Time: 0.0500s
Epoch: 3, Loss: -0.04092746, Time: 0.0500s
Epoch: 4, Loss: -0.03159958, Time: 0.0500s
Epoch: 5, Loss: -0.02592744, Time: 0.0400s
Epoch: 6, Loss: -0.02199575, Time: 0.0400s
Epoch: 7, Loss: -0.01907812, Time: 0.0400s
Epoch: 8, Loss: -0.01682099, Time: 0.0400s
Epoch: 9, Loss: -0.01502363, Time: 0.0500s
Epoch: 10, Loss: -0.01356039, Time: 0.0400s
Epoch: 11, Loss: -0.01234775, Time: 0.0500s
Epoch: 12, Loss: -0.01132776, Time: 0.0400s
Epoch: 13, Loss: -0.01045887, Time: 0.0500s
Epoch: 14, Loss: -0.00971052, Time: 0.0500s
Epoch: 15, Loss: -0.00905971, Time: 0.0400s
Epoch: 16, Loss: -0.00848887, Time: 0.0500s
Epoch: 17, Loss: -0.00798436, Time: 0.0500s
Epoch: 18, Loss: -0.00753542, Time: 0.0400s
Epoch: 19, Loss: -0.00713347, Time: 0.0400s
Epoch: 20, Loss: -0.00677160, Time: 0.0400s
Epoch: 21, Loss: -0.00644415, Time: 0.0500s
Epoch: 22, Loss: -0.00614650, Time: 0.0400s
Epoch: 23, Loss: -0.00587477, Time: 0.0500s
Epoch: 24, Loss: -0.00562576, Time: 0.0500s
Epoch: 25, Loss: -0.00539674, Time: 0.0400s
Epoch: 26, Loss: -0.00518541, Time: 0.0500s
Epoch: 27, Loss: -0.00498981, Time: 0.0500s
Epoch: 28, Loss: -0.00480824, Time: 0.0400s
Epoch: 29, Loss: -0.00463926, Time: 0.0500s
Epoch: 30, Loss: -0.00448161, Time: 0.0500s
Epoch: 31, Loss: -0.00433419, Time: 0.0400s
Epoch: 32, Loss: -0.00419603, Time: 0.0500s
Epoch: 33, Loss: -0.00406629, Time: 0.0500s
Epoch: 34, Loss: -0.00394423, Time: 0.0400s
Epoch: 35, Loss: -0.00382919, Time: 0.0500s
Epoch: 36, Loss: -0.00372058, Time: 0.0400s
Epoch: 37, Loss: -0.00361787, Time: 0.0400s
Epoch: 38, Loss: -0.00352061, Time: 0.0400s
Epoch: 39, Loss: -0.00342836, Time: 0.0400s
Epoch: 40, Loss: -0.00334076, Time: 0.0500s
Epoch: 41, Loss: -0.00325746, Time: 0.0400s
Epoch: 42, Loss: -0.00317815, Time: 0.0500s
Epoch: 43, Loss: -0.00310255, Time: 0.0500s
Epoch: 44, Loss: -0.00303042, Time: 0.0400s
Epoch: 45, Loss: -0.00296151, Time: 0.0500s
Epoch: 46, Loss: -0.00289562, Time: 0.0500s
Epoch: 47, Loss: -0.00283255, Time: 0.0400s
Epoch: 48, Loss: -0.00277213, Time: 0.0500s
Epoch: 49, Loss: -0.00271419, Time: 0.0500s
Epoch: 50, Loss: -0.00265858, Time: 0.0400s
Epoch: 51, Loss: -0.00260517, Time: 0.0500s
Epoch: 52, Loss: -0.00255383, Time: 0.0500s
Epoch: 53, Loss: -0.00250444, Time: 0.0400s
Epoch: 54, Loss: -0.00245689, Time: 0.0400s
Epoch: 55, Loss: -0.00241108, Time: 0.0400s
Epoch: 56, Loss: -0.00236692, Time: 0.0400s
Epoch: 57, Loss: -0.00232432, Time: 0.0400s
Epoch: 58, Loss: -0.00228320, Time: 0.0400s
Epoch: 59, Loss: -0.00224348, Time: 0.0400s
Epoch: 60, Loss: -0.00220510, Time: 0.0400s
Epoch: 61, Loss: -0.00216798, Time: 0.0400s
Epoch: 62, Loss: -0.00213207, Time: 0.0400s
Epoch: 63, Loss: -0.00209730, Time: 0.0400s
Epoch: 64, Loss: -0.00206363, Time: 0.0500s
Epoch: 65, Loss: -0.00203101, Time: 0.0400s
Epoch: 66, Loss: -0.00199938, Time: 0.0400s
Epoch: 67, Loss: -0.00196870, Time: 0.0500s
Epoch: 68, Loss: -0.00193892, Time: 0.0400s
Epoch: 69, Loss: -0.00191002, Time: 0.0500s
Epoch: 70, Loss: -0.00188195, Time: 0.0500s
Epoch: 71, Loss: -0.00185467, Time: 0.0400s
Epoch: 72, Loss: -0.00182816, Time: 0.0500s
Epoch: 73, Loss: -0.00180238, Time: 0.0500s
Epoch: 74, Loss: -0.00177730, Time: 0.0400s
Epoch: 75, Loss: -0.00175290, Time: 0.0500s
Epoch: 76, Loss: -0.00172914, Time: 0.0600s
Epoch: 77, Loss: -0.00170600, Time: 0.0500s
Epoch: 78, Loss: -0.00168346, Time: 0.0500s
Epoch: 79, Loss: -0.00166149, Time: 0.0500s
Epoch: 80, Loss: -0.00164008, Time: 0.0500s
Epoch: 81, Loss: -0.00161920, Time: 0.0400s
Epoch: 82, Loss: -0.00159883, Time: 0.0400s
Epoch: 83, Loss: -0.00157896, Time: 0.0500s
Epoch: 84, Loss: -0.00155957, Time: 0.0400s
Epoch: 85, Loss: -0.00154063, Time: 0.0400s
Epoch: 86, Loss: -0.00152214, Time: 0.0500s
Epoch: 87, Loss: -0.00150407, Time: 0.0400s
Epoch: 88, Loss: -0.00148642, Time: 0.0400s
Epoch: 89, Loss: -0.00146917, Time: 0.0400s
Epoch: 90, Loss: -0.00145230, Time: 0.0500s
Epoch: 91, Loss: -0.00143581, Time: 0.0500s
Epoch: 92, Loss: -0.00141968, Time: 0.0400s
Epoch: 93, Loss: -0.00140390, Time: 0.0500s
Epoch: 94, Loss: -0.00138846, Time: 0.0500s
Epoch: 95, Loss: -0.00137334, Time: 0.0400s
Epoch: 96, Loss: -0.00135854, Time: 0.0400s
Epoch: 97, Loss: -0.00134405, Time: 0.0500s
Epoch: 98, Loss: -0.00132986, Time: 0.0400s
Epoch: 99, Loss: -0.00131596, Time: 0.0400s
XOR Prediction
[1 0 1 1 1 1 0 1 0 0]
[0 1 0 0 0 0 1 0 1 1]

"""


