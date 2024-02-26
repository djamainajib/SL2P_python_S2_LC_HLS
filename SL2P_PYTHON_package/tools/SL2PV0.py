import pickle
    
 # --------------------
 # Sentinel2 Functions: 
 # --------------------
def s2_createFeatureCollection_estimates():
    with open('./SL2P_PYTHON_package/nets/SL2P-S2-20m.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_errors():
    with open('./SL2P_PYTHON_package/nets/SL2P-S2-20m-errors.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_domains():
    with open('./SL2P_PYTHON_package/nets/SL2P-S2-domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_createFeatureCollection_Network_Ind():
    with open('./SL2P_PYTHON_package/nets/SL2P-parameter-file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file


 # Same functions as above using 10 m bands:   
def s2_10m_createFeatureCollection_estimates():
    with open('./SL2P_PYTHON_package/nets/SL2P-S2-10m.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_10m_createFeatureCollection_errors():
    with open('./SL2P_PYTHON_package/nets/SL2P-S2-10m-errors.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def  s2_10m_createFeatureCollection_domains():
    with open('./SL2P_PYTHON_package/nets/SL2P-S2-10m-domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def s2_10m_createFeatureCollection_Network_Ind():
    with open('./SL2P_PYTHON_package/nets/SL2P-parameter-file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file    
    
 # -------------------
 # Landsat8 Functions:
 # -------------------
def l8_createFeatureCollection_estimates():
    with open('./SL2P_PYTHON_package/nets/SL2P-LC08.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file


def l8_createFeatureCollection_errors():
    with open('./SL2P_PYTHON_package/nets/SL2P-LC08-errors.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l8_createFeatureCollection_domains():
    with open('./SL2P_PYTHON_package/nets/SL2P-LC08-domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l8_createFeatureCollection_ranges():
    with open('./SL2P_PYTHON_package/nets/SL2P-LC08-range.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l8_createFeatureCollection_Network_Ind():
    with open('./SL2P_PYTHON_package/nets/SL2P-parameter-file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file


 # -------------------
 # Landsat9 Functions:
 # -------------------
def l9_createFeatureCollection_estimates():
    with open('./SL2P_PYTHON_package/nets/SL2P-LC08.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_errors():
    with open('./SL2P_PYTHON_package/nets//SL2P-LC08-errors.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_domains():
    with open('./SL2P_PYTHON_package/nets/SL2P-LC08-domain.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_ranges():
    with open('./SL2P_PYTHON_package/nets/SL2P-LC08-range.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file

def l9_createFeatureCollection_Network_Ind():
    with open('./SL2P_PYTHON_package/nets/SL2P-parameter-file.pkl', "rb") as fp:   #Pickling
        file = pickle.load(fp)
    fp.close()    
    return file