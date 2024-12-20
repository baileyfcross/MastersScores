import pandas as pd
import os as os

'''
Converts the given input directory from CSV to HDF5
'''

input_dir = 'Data/'
output_dir = 'HDF_Output/'

for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        csv_file = os.path.join(input_dir, filename)
        hdf_file = os.path.join(output_dir, filename.replace('.csv', '.h5'))

        df = pd.read_csv(csv_file)

        if "Trends" in filename:
            df.to_hdf(hdf_file, key='data', mode='w', format='table', data_columns=["Round_Year","Average","Standard_Deviation"])
        elif "Masters" in filename:
            df.to_hdf(hdf_file, key='data', mode='w', format='table', data_columns=["Year","Place","Player","Score","Notes"])
        else:
            df.to_hdf(hdf_file, key='data', mode='w')