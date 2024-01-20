import csv
def readCsv(path):
    with open(path,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            print('***'*5)
            print(row)
            
def imprime():
    print('***')
