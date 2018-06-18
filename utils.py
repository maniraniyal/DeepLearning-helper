import bcolz

def save_array(rootdir, array):
    c=bcolz.carray(array, rootdir=rootdir, mode='w')
    c.flush()
    
def load_array(rootdir):
    return bcolz.open(rootdir)[:]
