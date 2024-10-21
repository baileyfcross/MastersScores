import pandas as pd
import os as os

input_dir = 'Data/'
output_dir = 'HDF_Output/'

for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        csv_file = os.path.join(input_dir, filename)
        hdf_file = os.path.join(output_dir, filename.replace('.csv', '.h5'))

        df = pd.read_csv(csv_file)

        df.to_hdf(hdf_file, key='data', mode='w', format='table', data_columns=["Year","Place","Player","Score","Notes"])

        # df = pd.read_hdf(hdf_file, 'data')

        # print(df)