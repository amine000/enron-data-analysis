#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(C = 10000.0, kernel = "rbf")
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print len(pred)
print "predicting time:", round(time()-t1, 3), "s"
accuracy = accuracy_score(labels_test,pred)
print accuracy
print "the 10th item is " + str(pred[10])
print "the 26th item is " + str(pred[26])
print "the 50th item is " + str(pred[50])
counter = 0
for item in pred:
	if(item == 1):
		counter+=1
print "number of emails by chris is " + str(counter)
#########################################################


