import root2py
import importlib.resources
def get_data():
    with importlib.resources.path("root2py.data", "sample.root") as filepath:
        in_file_path = filepath
    return in_file_path

#def save_data(a: str)->str:
#    with importlib.resources.path("root2py.data", "") as filepath:
#        out_file_path = filepath,a
#    return out_file_path
#data = save_data("output.hdf5")
#print(data)