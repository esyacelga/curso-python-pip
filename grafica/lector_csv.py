import csv
def readCsv(path):
    with open(path,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            iterable_country= {key:value for (key, value) in iterable}
            data.append(iterable_country)
        return data


            
def imprime():
    print('***')
