## Implementation

### Creating h5 files
The implementation for the converter had me start at the Pandas library.
I looked at the to_hdf function, which given the API would be perfect for what I needed.
After getting the to_hdf function to work, I was able to create h5 files.

### Reading h5 files

After looking at several ways to read h5 files, I went to Chat-GPT.
From Chat-GPT I was able to ask it a question on how to create a python program that would
let me view h5 files in my terminal and as a GUI.
The GUI worked immediately, but contained an archaic tree format that display every variable in the h5 format.
The terminal was the better way to go because it allowed me to change what the user could see which could let me filter out some of the blank variables.

<br />

Taking the Chat-GPT code segment, I quickly modified it to display the filename of what data the user was looking at. 
After that I was able to filter out the blank variables and only include the given table that I made from the converter before.
I added two cases for the code to handle the table format of H5 files, and the block format that Dataset 2 (RWR_historical_data.h5) is in. 
