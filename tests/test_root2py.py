from root2py.root2py import open
tree="FloatingpointMixedbcstcrealsig4DummyHistomaxxydr015GenmatchGenclustersntuple/HGCalTriggerNtuple"
branches= ["good_cl3d_pt","good_cl3d_eta"]
df = open("skim_small_photons_0PU_bc_stc_hadd.root",tree,branches)
print(df)