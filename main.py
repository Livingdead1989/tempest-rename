import os, csv

def main():
    directory_path = os.getcwd() + '/'
    print('My current directory is: ' + directory_path)

    ## import photo directory into listdir
    path = directory_path + 'Photographs to Rename'
    file_extension = '.bmp'
    items = os.listdir(path)


    ## csv handling
    csv_open = open(directory_path+'data.csv','r')
    csv_read = csv.reader(csv_open, delimiter=',')
    next(csv_read) ## skip the first row.

    ## initialise an empty list
    photographs = [] 
    

    ## photograph loop
    for item in items:
        ## clean up file names
        clean_item = (item.strip(file_extension))
        ## add clean file name into photograph list
        photographs.append(clean_item)

    ## nested for loop, reads the records from csv file with photograph list, looking for a match
    for record in csv_read:
        for photograph in photographs:
            ## record[2] is the adno column
            if record[2] == photograph:
                ## rename files if they match
                os.rename(path+'/'+photograph+file_extension,path+'/'+record[0]+' '+record[1]+file_extension)


    csv_open.close() #close csv when finished.
    

if __name__ == '__main__':
    main()