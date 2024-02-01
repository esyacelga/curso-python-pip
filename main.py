from programas import metodos

from grafica import lector_csv as lc
from grafica import utils_lector as ulc


def lectura():
    path= './grafica/data.csv'
    data = lc.readCsv(path)
    data = ulc.get_filter_population_by_continent(data,'South America')
    value_x = ulc.get_values_by_colum(data,'Country/Territory')
    value_y = ulc.get_values_by_colum(data,'World Population Percentage')
    ulc.generate_pie_char(value_x,value_y)
    """ country = input("Ingrese el pais===>")
    pais_filtrado = ulc.get_population_by_country(data,country)
    labels, values = ulc.get_poulation_keys(pais_filtrado)
    ulc.generate_bar_char(labels, values)
    print(labels, values)
     """

if __name__ == '__main__':
    lectura()
    

