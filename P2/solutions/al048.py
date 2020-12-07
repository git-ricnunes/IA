# -*- coding: utf-8 -*-


import numpy as np
import random as rand
import copy as cp
import math

def classify(T,data):
    
    data = np.array(data)
    out = []
    for el in data:
        #print("el",el,"out",out,"\nT",T)
        wT = T
        for ii in range(len(el)):
            #print(T[0],el[T[0]],T)
            if el[wT[0]]==0:
                if not isinstance(wT[1], list):
                    out += [wT[1]]
                    break
                else:
                    wT = wT[1]
            else:
                if not isinstance(wT[2], list):
                    out += [wT[2]]
                    break
                else:
                    wT = wT[2]
    return np.array(out)

def CountOutput(examples):
    """ Function : CountOutput """

    trueCount=0
    falseCount=0
    for example in examples:
        if example[1]==1 :
            trueCount=trueCount+1
        else:
            falseCount=falseCount+1
    return trueCount,falseCount
            
def PluralityValue(examples):
    """ Function : PluralityValue """
    trueCount,falseCount=CountOutput(examples)
    
    if falseCount > trueCount:
        return 0
    elif falseCount < trueCount:
        return 1
    else: #falseCount == trueCount
        return rand.choice([0,1])

        
def CheckExamplesClassification(examples):
    """ Function : CheckExamplesClassification """
    lastClassification = examples[0][1]
        
    for i in range(1,examples.shape[0]):
        if examples[i][1]!=lastClassification:
            return False
    
    return True        

def Importance(attributes,examples):
    """ Function : Importance """
    argmaxArray=[]
    p,n=CountOutput(examples)
    totalEntropy=Entropy(p,n)
    for att in attributes:
        argmaxArray.append(Gain(examples,att,totalEntropy))
    return attributes[np.argmax(argmaxArray)]


#
def Entropy(p,n):
    """ Function : Entropy """
    q = p/(p+n)
    if q==0 or q==1:
        return 0
    else:
        B = -1*( ( q * (math.log(q,2)) ) + ( (1-q ) * math.log( (1-q) ,2))) 
    
    return B


def Remainder(examples,attribute):
    """ Function : Remainder """
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
       remainderSum=remainderSum + ((atv[2] +atv[1])/(p+n) * Entropy(atv[2],atv[1]))      
         
    return remainderSum

def Gain(examples,attribute,entropy):
    """ Function : Gain """
    
    return entropy - Remainder(examples,attribute)

def DTL(examples,attributes,parentExamples):
    """ Function : DTL """

    if examples.size == 0:
        return PluralityValue(parentExamples)
    elif CheckExamplesClassification(examples):
        if len(parentExamples)==0:
             tree=[0,int(examples[0][1]),int(examples[0][1]) ]
             return tree
        else:
            return int(examples[0][1])
    elif attributes.size == 0:
        return PluralityValue(examples)
    else:
        A = Importance(attributes,examples)
        AIndex = np.where(attributes == A)
        tree=[int(A)]
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
                    exsAux.append( [int(i) for i in example[0]] )    
                    exsAuxY.append(int(example[1]))
            exs=CreateExamples(np.array(exsAux),np.array(exsAuxY))
            
            tree.append(DTL(exs,np.delete(pAttributes,AIndex),np.array(pExamples))) 
            
    return tree

def DecissionTreePostPrunning(tree,D,Y):
    """ Function : DecissionTreePostPrunning """
    workTree= cp.deepcopy(tree)
    Yp = classify(tree,D)

    newTreeError1=0
    newTreeError2=0
    originalErro=np.mean(np.abs(Yp-Y))
        
    isPruned=False
    
    while(not isPruned):
        workTree1=workTree[1]
        print(workTree1)
        if(not isinstance(workTree1,int)):
            Yp = classify(workTree1,D)
            newTreeError1=np.mean(np.abs(Yp-Y))

        workTree2=workTree[2]
        print(workTree2)
        if(not isinstance(workTree2,int)):
            Yp = classify(workTree2,D)
            newTreeError2=np.mean(np.abs(Yp-Y))

        if(originalErro>=newTreeError1):
            if(isinstance(workTree1,int)):
                isPruned=True
            else:
                workTree=workTree1

        elif(originalErro>=newTreeError2):
            if(isinstance(workTree2,int)):
                isPruned=True
            else:
                 workTree=workTree2
        else:
            isPruned=True

    return workTree

def CreateExamples(D,Y):
    """ Function : CreateExamples """

    arrayExamples = np.empty((D.shape[0],), dtype=object)

    for i in  range(0,Y.size):
        arrayExamples[i]= (D[i],Y[i])
        
    return arrayExamples

def createdecisiontree(D,Y, noise = False):
    """ Function : createdecisiontree """

    examples = CreateExamples(D,Y)
    attributes = np.arange(D.shape[1])
    tree=DTL(examples,attributes,[])
    prunnedTree=DecissionTreePostPrunning(tree,D,Y)
    return prunnedTree