import uproot
import pandas as pd
import awkward as ak
def open(filename: str,tree: str,branches: list)->ak:
    return uproot.open(filename)[tree].arrays(branches, library='ak')
    ak_branches = ak["gen_pt"]
def save(filename: str,branches: list,data: ak):
    store = pd.HDFStore(filename, mode='w')
    for i in list(branches):
        print(branches[i])
        store[branches[i]] = open(filename,tree,branches)
    return store