# -*- coding: utf-8 -*-


import numpy as np
import sklearn as skl
import random as rand
import math

def PluralityValue(examples):
    # Function : PluralityValue
    # desc: 
    # args:
    # return :
        
    trueCount=0
    falseCount=0
    
    for example in examples:
        if example[1]==1 :
            trueCount=trueCount+1
        else:
            falseCount=falseCount+1  

    if falseCount > trueCount:
        return 0
    elif falseCount < trueCount:
        return 1
    else: #falseCount == trueCount
        return rand.choice([0,1])
        
def CheckExamplesClassification(examples):
    # Function : CheckExamplesClassification
    # desc: 
    # args:
    # return :
        
    lastClassification = examples[0][1]
    for i in range(1,examples.shape[0]):
        if examples[i][1]!=lastClassification:
            return False
    
    return True        

def Importance(attributes):
    # Function : Importance
    # desc: 
    # args:
    # return :
        
    return np.argmax(attributes)

def Entropy(p,n):
    # Function : Entropy
    # desc: 
    # args:
    # return :
        
    q = p/(p+n)   
    B = -1*( ( q * math.log(q,2) ) + ( (1-q ) * math.log( (1-q) ,2))) 
    
    return B

def Remainder(attributes):
    # Function : Remainder
    # desc: 
    # args:
    # return :
    return np.argmax(attributes)

def Gain(attribute):
    # Function : Gain
    # desc: 
    # args:
    # return :
    return np.argmax(attributes)


def DTL(examples,attributes,parentExamples):
    # Function : DTL
    # desc: 
    # args:
    # return :
        
    tree = np.empty((3,), dtype=object)
    
    if examples.size == 0:
        return PluralityValue(parentExamples)
    elif CheckExamplesClassification(examples):
        return attributes[0]
    elif attributes.size == 0:
        return PluralityValue(examples)
    else:
        A = np.argmax(attributes)
#        np.put(tree,0,A)
       
    return tree

def CreateExamples(D,Y):
    # Function : CreateExamples
    # desc: 
    # args:
    # return :
    arrayExamples = np.empty((D.shape[0],), dtype=object)

    for i in  range(0,Y.size):
        arrayExamples[i]= (D[i],Y[i])
        
    return arrayExamples

def createdecisiontree(D,Y, noise = False):
    # Function : createdecisiontree
    # desc: 
    # args:
    # return :
    
    examples = CreateExamples(D,Y)
    attributes = np.arange(D.shape[1])
    DTL(examples,attributes,[])
    #return tree
    return [0,0,1]