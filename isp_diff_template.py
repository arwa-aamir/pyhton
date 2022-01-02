"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    
    # if both strings are of same length
    if(len(line1)==len(line2)):
        for character in range(len(line1)):
            if line1[character]!=line2[character]:
                return character
        return IDENTICAL
    # if both strings are of different length
    elif(len(line1)!=len(line2)):
        #find larger string
        if(len(line1)>len(line2)):
            
            shorter_string_lenth=len(line2)
        else:
            
            shorter_string_lenth=len(line1)
            
        for character in range(shorter_string_lenth):
            if line1[character]!=line2[character]:
                return character
            ##if the entire shorter line matches the beginning of the longer 
            ##line the first difference is located at the index
            ##that is one past the last character in the shorter line
        return shorter_string_lenth
                
def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if(len(line1)>len(line2)):
        
        shorter_string_lenth=len(line2)
    else:
        
        shorter_string_lenth=len(line1)
    
    #if lines have \n or \r return empty string
    if(line1.count("\n") + line2.count("\n") + line1.count("\r")+ line2.count("\r") != 0):
        return ""
    
    #if lines are operatable find the index of difference
    idx_dif=idx
    
    #If the index is not a valid index the function should also return an empty string
    if(idx_dif==-1 or idx_dif>shorter_string_lenth):
        return ""
    #if index is valid meands a difference does exit between the strings
    else:
        func2_str=line1+"\n"+"="*(idx_dif)+"^"+"\n"+line2+"\n"
        return func2_str
    


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    #if both lists are of same length
    if(len(lines1)==len(lines2)):
        for lists in range(len(lines1)):
            if(singleline_diff(lines1[lists], lines2[lists])!=-1):
                tup=(lists,singleline_diff(lines1[lists], lines2[lists]))
                return tup
        return (IDENTICAL, IDENTICAL)
    
    elif(lines1==[] or lines2==[]):
        return (0,0)
    #if both strings are of different lengths
    elif(len(lines1)!=len(lines2)):
        #find larger list length
        if(len(lines1)>len(lines2)):
            
            shorter_list_length=len(lines2)
        else:
            
            shorter_list_length=len(lines1)

        for lists in range(shorter_list_length):
            if(singleline_diff(lines1[lists], lines2[lists])!=-1):
                tup=(lists,singleline_diff(lines1[lists], lines2[lists]))
                return tup
            
            else:
                return (shorter_list_length,0)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    #create a file object from the given filename
    openfile=open(filename,"rt")
    
    #read data from the file
    file_data=openfile.readlines()
    
    openfile.close()
    data_list=[]
    
    if file_data==[]:
        return []
    
    for line in file_data:
            
        if(line.count("\n")!=0):
            new_string=line.replace("\n","")
        else:
            new_string=line
            
        data_list.append(new_string)
        
    return data_list
        
def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    file1_lines=get_file_lines(filename1)
    file2_lines=get_file_lines(filename2)
    
    
    line_number, index = multiline_diff(file1_lines, file2_lines)
    
    if(line_number==-1 and index==-1):
        #meaning lists are same
        return "No differences\n"
    if(file1_lines==[]):
        file1_string=""
    else:
        file1_string=file1_lines[line_number]
    if(file2_lines==[]):
        file2_string=""
    else:
        file2_string=file2_lines[line_number]
    #otherwise move to singleline_diff_format and return the 3 lines string
    result_string= singleline_diff_format(file1_string,file2_string, index)
    return "Line "+str(line_number)+":\n"+result_string

print(file_diff_format('file1.txt', 'file2.txt'))
