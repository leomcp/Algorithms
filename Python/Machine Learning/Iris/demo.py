'''
Hellow World of Machine Learning : Python implemenation of clasification of iris flower 
'''
''' 
1. Load the data
Iris flowers dataset is used, it contains 150 observations of iris flowers. There are four columns
of measurments of the flower in centimeters. We are going to load the iris data from CSV file URL.
'''
# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

'''
2. Summarize the Datset
Look at the data in some different ways 
'''
#Shape : Dimensions of Data 
print(dataset.shape)

#Head : Peek at the Data 
print(dataset.head(20))

#Desciptiptions : Statistical Summary 
print(dataset.describe)

#class distribution : No of instances (rows) that belong to each class
print(dataset.groupby('class').size())


'''
3. Data Visualizations 
Two types od plots :
1. Univariate plots to better understand each attributes.
2. Multivariate plots to better understand the relationships between attributes 
'''
# Univariate Plots: box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

#Univariate Plots : histograms 
dataset.hist()
plt.show()

#Multivariate Plots : scatter plot matrix
scatter_matrix(dataset)
plt.show()

'''
4. Evaluate some algorithms 
Create some models of the data and estimate their accuracy on unseen data.
'''
#create a validation dataset 
#split-out validation dataset 
array=dataset.values 
X=array[:,0:4]
Y=array[:,4]
validation_size=0.20
seed =7
X_train,X_validation,Y_train,Y_validation=model_selection.train_test_split(X,Y,test_size=validation_size,random_state=seed)

#test options and evaluationn metric
seed=7
scoring='accuracy'
'''
We use metric of 'accuracy' to evaluate models. This is a ratio of the number of correctly predicted instances
in divided by the total number of instances in the dataset multiplied by 100 to give percentage. 
'''
#Bulid models
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
#Selecting the best model : KNN has the largest estimated accuracy score 
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

# Compare Algorithms : Plot of the model evaluation results and compare the spread and the mean accuracy of each
# There is a population of accuracy measures for each algorithm because each algorithm was evaluated 10 times
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

'''
5. Make Predictions 
The KNN algorithm was the most accurate model that was tested. Now we want to get an idea of the accuracy of the 
model on our validation set. We can run the KNN model directly on the validation set and summarize the results as 
a final accuracy score, a confusion matrix and a classification report.
'''
# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
'''
We can see that the accuracy is 0.9or 90%. The confusion matrix provides an indication of three errors made.
Finally, the classification report provides a breakdown of each class by precision, recall, f1-score and 
support showing excellent results (granted the validation dataset was small)
'''
