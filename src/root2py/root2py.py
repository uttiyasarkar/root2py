######Required libraries########
import uproot
import pickle5 as pickle
import pandas as pd
import awkward as ak


kwargs = dict(filename=str,tree=str,branches=list)  ###dict object kwargs common between different definitions
#print(kwargs)

###############Def opens any root file by using uproot###################
def open(**kwargs)->ak:
    """Get dataset from the sample.
    
    Parameters
    ----------
    filename: str, inputfilename.
    branches: list, branches present in the root file.
    tree: str, name of the tree present in the root file.

    Returns
    -------
    root file in pandas dataframe format.

    Example
    --------
    >>>from root2py.root2py import open
    >>>df= open(filename=input,branches=branchename,tree=treename)
    >>>print(df)

    """
    return uproot.open(kwargs['filename'])[kwargs['tree']].arrays(kwargs['branches'], library='ak')

###############Def saves any root file to a hdf format##################
def savehdf(outfile: str,**kwargs):
   """Save dataset in HDF5 format.
    
    Parameters
    ----------

    filename: str, input filename with .root extension.
    output: str, output HDF5 filename with extension .hdf5.
    branches: list, branches present in the root file.
    tree: str, name of the tree present in the root file.

    Returns
    -------
    Save root file in HDF5 format.

    Example
    --------
    >>>from root2py.root2py import savehdf
    >>>df2 = savehdf(output,filename=input,branches=branchename,tree=treename)

    """
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
    """Save dataset in pickle format.
    
    Parameters
    ----------

    filename: str, input filename with .root extension.
    output: str, output pickle filename with extension .pkl.
    branches: list, branches present in the root file.
    tree: str, name of the tree present in the root file.

    Returns
    -------
    Save root file in Pickle format.

    Example
    --------
    >>>from root2py.root2py import savepkl
    >>>df2 = savepkl(output2,filename=input,branches=branchename,tree=treename)
    
    """
    df =  open(**kwargs)
    #
    store = ak.to_dataframe(df)  
        #print(df[i])
    store.to_pickle(outfile,*pkloption)         
                   # store[branches[i]] = open(filename,tree=tree,branches=branches)
            #print(store)
    return store