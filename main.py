from programas import metodos
from grafica import lector_csv as lc


def lectura():
    path= './grafica/data.csv'
    lc.readCsv(path)
    

if __name__ == '__main__':
    lectura()
    

