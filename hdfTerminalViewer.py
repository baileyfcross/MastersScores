import os
import h5py
import sys
import numpy as np


def display_hdf5_structure(file_path):
    try:
        for filename in os.listdir(file_path):
            hdf5_file_path = os.path.join(file_path, filename)
            with h5py.File(hdf5_file_path, 'r') as f:
                print(f"Structure and data of the HDF5 file: {filename}")
                print_hdf5_group(f, "")
    except Exception as e:
        print(f"Error reading HDF5 file: {e}")


def print_hdf5_group(group, indent):
    """
    Recursively prints the structure of a HDF5 group or dataset,
    and displays actual data values for datasets formatted as a table.
    """
    for key in group:
        item = group[key]
        if isinstance(item, h5py.Group):
            print_hdf5_group(item, indent + "  ")  # Recursively print group contents
        elif isinstance(item, h5py.Dataset) and key == "table":
            print(f"{indent}Dataset: {key}, Shape: {item.shape}, Dtype: {item.dtype}")
            # If dataset is a structured table, display it in table format
            data = item[()]
            if isinstance(data, np.ndarray):
                if data.dtype.names:  # Check if it's a structured array (table format)
                    print_table_as_table(data, indent)
                else:
                    print(f"{indent}  Data: {data[:10]}...")  # Display first 10 elements for large datasets
            else:
                print(f"{indent}  Data: {data}")


def print_table_as_table(structured_array, indent):
    """
    Print a structured array (HDF5 table) in a table format with headers.
    """
    # Get the field names (column headers)
    headers = structured_array.dtype.names

    # Calculate the maximum width for each column to format it neatly
    column_widths = [max(len(str(item)) for item in structured_array[col]) for col in headers]

    # Print the header row
    header_row = " | ".join([f"{header:{width}}" for header, width in zip(headers, column_widths)])
    print(f"{indent}{header_row}")

    # Print a separator line
    print(f"{indent}{'-' * len(header_row)}")

    # Print the data rows
    for row in structured_array:
        row_str = " | ".join([f"{str(value):{width}}" for value, width in zip(row, column_widths)])
        new_row_str = row_str.replace("b'","")
        print(f"{indent}{new_row_str}")

    print(f"{indent}{'-' * len(header_row)}")

def main():

    file_path = "HDF_Output/"
    display_hdf5_structure(file_path)


if __name__ == "__main__":
    main()