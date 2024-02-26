import os
import dictionariesSL2P, toolsNets
import SL2PV0 as algorithm
import numpy 
from datetime import datetime

def SL2P(sl2p_inp,variableName,imageCollectionName,outPath=None):
    print('Estimating %s from %s data' %(variableName,imageCollectionName, ))
    networkOptions= dictionariesSL2P.make_net_options()
    collectionOptions = (dictionariesSL2P.make_collection_options(algorithm))
    netOptions=networkOptions[variableName][imageCollectionName]
    colOptions=collectionOptions[imageCollectionName]
    
    # prepare SL2P networks
    SL2P,errorsSL2P=makeModel(algorithm,imageCollectionName,variableName) 

    # generate sl2p input data flag
    inputs_flag=invalidInput(sl2p_inp,netOptions,colOptions)
       
    # run SL2P
    print('Run SL2P...\nSL2P start: %s' %(datetime.now()))
    estimate   =toolsNets.wrapperNNets(SL2P      ,netOptions,sl2p_inp)
    uncertainty=toolsNets.wrapperNNets(errorsSL2P,netOptions,sl2p_inp)
    print('SL2P end: %s' %(datetime.now()))
    
     # generate sl2p output product flag
    output_flag=invalidOutput(estimate,netOptions)
    print('Done')
    return {variableName:estimate,variableName+'_uncertainty':uncertainty,'sl2p_inputFlag':inputs_flag,'sl2p_outputFlag':output_flag}

def makeModel(algorithm,imageCollectionName,variableName):
    collectionOptions = (dictionariesSL2P.make_collection_options(algorithm))
    colOptions=collectionOptions[imageCollectionName]
    networkOptions= dictionariesSL2P.make_net_options()
    netOptions=networkOptions[variableName][imageCollectionName]

    ## Compute numNets
    numNets =len({k: v for k, v in (colOptions["Network_Ind"]['features'][0]['properties']).items() if k != 'Feature Index'}) 
    SL2P_nets =[toolsNets.makeNetVars(colOptions["Collection_SL2P"],numNets,netNum) for netNum in range(colOptions['numVariables'])]
    errorsSL2P_nets =[toolsNets.makeNetVars(colOptions["Collection_SL2Perrors"],numNets,netNum) for netNum in range(colOptions['numVariables'])]
    return SL2P_nets,errorsSL2P_nets
        
def invalidInput(image,netOptions,colOptions):
    print('Generating sl2p input data flag')
    [d0,d1,d2]=image.shape
    sl2pDomain=numpy.sort(numpy.array([row['properties']['DomainCode'] for row in colOptions["sl2pDomain"]['features']]))
    bandList={b:netOptions["inputBands"].index(b) for b in netOptions["inputBands"] if b.startswith('B')}
    image=image.reshape(image.shape[0],image.shape[1]*image.shape[2])[list(bandList.values()),:]
    
    #Image formatting
    image_format=numpy.sum((numpy.uint8(numpy.ceil(image*10)%10))* numpy.array([10**value for value in range(len(bandList))])[:,None],axis=0)
    
    # Comparing image to sl2pDomain
    flag=numpy.isin(image_format, sl2pDomain,invert=True)
    return flag.reshape(d1,d2)

def invalidOutput(estimate,netOptions):
    print('Generating sl2p output product flag')
    #var_range=dictionariesSL2P.make_net_options()[variableName][imageCollectionName]
    return numpy.where(estimate<netOptions['outmin'],1,numpy.where(estimate>netOptions['outmax'],2,0))