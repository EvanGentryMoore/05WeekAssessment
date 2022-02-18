log_file = open("um-server-01.txt") # Setting a variable called log_file that is the data from um-server-01.txt file. Basically allowing external data to be viewed and analized within this python document.


def sales_reports(log_file): #defining the function sales_report that accepts and expects a variable as a parameter. In this case, the variable should be body of data, like our log_file variable above. 
    for line in log_file: #start of a for-loop within the sales_report function. It basically reads "For each line in the log_file, do..."
        line = line.rstrip() #this is a variable called line that is stripping the trailing characters at the end of a sting. Mainly any extra space characters and/or line-breaks. Since it's in the for-loop, it does this for each line in the document.
        day = line[0:3] #this is a variable called day that is returning the values of characters from each string/line. The [0:3] is indicating that the characters that it'll return will be characters INCLUDING the 0 index and up to but NOT INCLUDING the 3rd index. In short, it returns the values of index 0, 1, and 2 which happen to be the 3 letter abbriviation of the day of the week. 
        if day == "Tue":#This IF statement is checking to see if the values returned in the day varible match the original condition of "Tue". If the values do match, then the IF statment allows whatever code is nested within the IF statement to execute.
            print(line)#This prints each line from the document that meets the IF statement's condition.


sales_reports(log_file)#This is calling the function of sales_report that passes in the variable log_file.

log_file.seek(0)

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)