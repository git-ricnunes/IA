# -*- coding: utf-8 -*-


import numpy as np
import random as rand
import copy as cp
import math


######## AUX FUNCTIONS ########
def CountOutput(examples):
    trueCount=0
    falseCount=0
    for example in examples:
        if example[1]==1 :
            trueCount=trueCount+1
        else:
            falseCount=falseCount+1
    return trueCount,falseCount
            
def PluralityValue(examples):
    # Function : PluralityValue
    # desc: 
    # args:
    # return :
    trueCount,falseCount=CountOutput(examples)

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

def Importance(attributes,examples):
    # Function : Importance
    # desc: 
    # args:
    # return :
    argmaxArray=[]
    p,n=CountOutput(examples)
    totalEntropy=Entropy(p,n)
    for att in range(attributes.shape[0]):
        argmaxArray.append(Gain(examples,att,totalEntropy))
    return attributes[np.argmax(argmaxArray)]

def Entropy(p,n):
    # Function : Entropy
    # desc: 
    # args:
    # return :
        
    q = p/(p+n)
    if q==0 or q==1:
        return 0
    else:
        B = -1*( ( q * (math.log(q,2)) ) + ( (1-q ) * math.log( (1-q) ,2))) 
    
    return B

def Remainder(examples,attribute):
    # Function : Remainder
    # desc: 
    # args:
    # return :
        
    p,n=CountOutput(examples)
    remainderSum=0
    
    attribureValue= []
    attribureValueAux= []
    for example in examples:
        if example[0][attribute] in attribureValueAux:
            i=attribureValueAux.index(example[0][attribute])
            if example[1] == 0:
                attribureValue[i]=((attribureValue[i][0],attribureValue[i][1]+1,attribureValue[i][2]))
            else:
                attribureValue[i]=((attribureValue[i][0],attribureValue[i][1],attribureValue[i][2]+1))
        else:
            if example[1] == 0:
                attribureValueAux.append(example[0][attribute])
                attribureValue.append((example[0][attribute],1,0))
            else:
                attribureValueAux.append(example[0][attribute])
                attribureValue.append((example[0][attribute],0,1))
   
    for atv in attribureValue:
       remainderSum=remainderSum + ((atv[2]+atv[1])/(p+n) * Entropy(atv[2],atv[1]))      
         
  
    return remainderSum

def Gain(examples,attribute,entropy):
    # Function : Gain
    # desc: 
    # args:
    # return :
    
    return entropy - Remainder(examples,attribute)


def DTL(examples,attributes,parentExamples):
    # Function : DTL
    # desc: 
    # args:
    # return :
        
    tree = np.empty((3,), dtype=object)
    if examples.size == 0:
        return PluralityValue(parentExamples)
    elif CheckExamplesClassification(examples):
        return examples[0][1]
    elif attributes.size == 0:
        return PluralityValue(examples)
    else:
        A = Importance(attributes,examples)
        AIndex = np.where(attributes == A)
        
        tree=[A]
        vksArr=[]
        
        pExamples=cp.deepcopy(examples)
        pAttributes=cp.deepcopy(attributes)
        for example in examples:
            vksArr.append((example[0][A],example[1]))
        
        for vks in np.unique(vksArr):
            exsAux=[]
            exsAuxY=[]
            exs=[]
            for example in examples:
                if example[0][A] == vks:
                    exsAux.append(example[0])
                    exsAuxY.append(example[1])
            exs=CreateExamples(np.array(exsAux),np.array(exsAuxY))
            
            tree.append(DTL(exs,np.delete(pAttributes,AIndex),np.array(pExamples)))     
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
    tree=DTL(examples,attributes,[])
    return tree