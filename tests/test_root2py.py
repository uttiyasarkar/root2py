import root2py
from root2py.root2py import open
#from root2py.dataimport import get_data
#from root2py.dataimport import save_data
from root2py.root2py import savehdf
from root2py.root2py import savepkl

treename="FloatingpointMixedbcstcrealsig4DummyHistomaxxydr015GenmatchGenclustersntuple/HGCalTriggerNtuple"  ###Name of the tree in the root file
branchename= ["good_cl3d_pt","good_cl3d_eta"] ###Name of the branches that user wants to save as hdf or pkl
input = "tests/sample.root"
print(input)
 ###Input root file path
output = "output.hdf5" ###Output hdf path
output2 = "output.pkl" ###Output pkl path
print(output)
df= open(filename=input,branches=branchename,tree=treename)
#print(df)
df2 = savehdf(output,filename=input,branches=branchename,tree=treename)
df2 = savepkl(output2,filename=input,branches=branchename,tree=treename)