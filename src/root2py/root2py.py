######Required libraries########
import uproot
import pickle5 as pickle
import pandas as pd
import awkward as ak


kwargs = dict(filename=str,tree=str,branches=list)  ###dict object kwargs common between different definitions
#print(kwargs)

###############Def opens any root file by using uproot###################
def open(**kwargs)->ak:
    return uproot.open(kwargs['filename'])[kwargs['tree']].arrays(kwargs['branches'], library='ak')

###############Def saves any root file to a hdf format##################
def savehdf(outfile: str,**kwargs):
    df =  open(**kwargs)
    #
    store = ak.to_dataframe(df)  
        #print(df[i])
    store.to_hdf(outfile,'key',mode='w')         
                   # store[branches[i]] = open(filename,tree=tree,branches=branches)
            #print(store)
    return store

pkloption = {'compression': str,'protocol': int, 'storage_option': dict}
###############Def saves any root file to a pkl format##################
def savepkl(outfile: str,*pkloption,**kwargs):
    df =  open(**kwargs)
    #
    store = ak.to_dataframe(df)  
        #print(df[i])
    store.to_pickle(outfile,*pkloption)         
                   # store[branches[i]] = open(filename,tree=tree,branches=branches)
            #print(store)
    return store