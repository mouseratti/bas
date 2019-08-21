"""
The open Function
Before you can read or write a file,
you have to open it using Python's built-in open() function.
This function creates a file object, which would be utilized to call
other support methods associated with it.

Syntax
file object = open(file_name [, access_mode][, buffering])
file_name − The file_name argument is a string value that contains
the name of the file that you want to access.

access_mode − The access_mode determines the mode in which the file
has to be opened, i.e., read, write, append, etc.
A complete list of possible values is given below in the table.
This is optional parameter and the default file access mode
is read (r).

buffering − If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).

Here is a list of the different modes of opening a file −

Sr.No.	Modes & Description
r - Opens a file for reading only.
The file pointer is placed at the beginning of the file.
This is the default mode.

rb Opens a file for reading only in binary format.
The file pointer is placed at the beginning of the file.
This is the default mode.

r+ Opens a file for both reading and writing.
The file pointer placed at the beginning of the file.

rb+ Opens a file for both reading and writing in binary format.
The file pointer placed at the beginning of the file.

w Opens a file for writing only.
Overwrites the file if the file exists.
If the file does not exist, creates a new file for writing.

wb Opens a file for writing only in binary format.
Overwrites the file if the file exists.
If the file does not exist, creates a new file for writing.

w+ Opens a file for both writing and reading.
Overwrites the existing file if the file exists.
If the file does not exist,
creates a new file for reading and writing.

wb+  Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

a
Opens a file for appending. The file pointer is at the end of the file if the file exists.
That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

ab Opens a file for appending in binary format.
The file pointer is at the end of the file if the file exists.
That is, the file is in the append mode.
If the file does not exist, it creates a new file for writing.

a+

Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

ab+

Opens a file for both appending and reading in binary format.
The file pointer is at the end of the file if the file exists.
The file opens in the append mode.
If the file does not exist, it creates a new file for reading and writing.
"""

# Open a file
fo = open("filename.txt", "a+")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close() # close non-used file
fo.read() # You can't read closed object

# Python automatically closes a file when the reference
# object of a file is reassigned to another file.
# It is a good practice to use the close() method to close a file.
# It is good practice to use the with keyword
# when dealing with file objects.
# The advantage is that the file is properly closed after
# its suite finishes, even if an exception is raised at some point.
with open("foo.txt") as f: # with operator clothes file for you
    f.read()

# To read a file’s contents, call f.read(size),
# which reads some quantity of data and returns it as a string
# (in text mode) or
# bytes object (in binary mode).
# size is an optional numeric argument.
# When size is omitted or negative, the entire contents of the file
# will be read and returned;
# it’s your problem if the file is twice as large as
# your machine’s memory.
# Otherwise, at most size bytes are read and returned.
# If the end of the file has been reached,
# f.read() will return an empty string ('').


# f.write(string) writes the contents of string to the file,
# returning the number of characters written.
f = open("new-file.txt", "a+")
f.write('This is a test\n')
f.tell() # current position of the file
f.seek(0) # go to the 0-th position