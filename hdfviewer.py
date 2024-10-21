import h5py
import os as os

hdf_dir = 'HDF_Output/'
for filename in os.listdir(hdf_dir):
    hdf_file = os.path.join(hdf_dir, filename)
    with h5py.File(hdf_file, 'r') as f:

        print("Keys: %s" % f.keys())
        a_group_key = list(f.keys())[0]

        print(type(f[a_group_key]))

        data = list(f[a_group_key])

        data = list(f[a_group_key])

        ds_obj = f[a_group_key]
        ds_arr = f[a_group_key]['table']
        print(ds_obj)