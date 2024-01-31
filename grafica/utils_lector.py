import matplotlib.pyplot as plt
def get_population_by_country(data,country):
   result = list(filter(lambda item:item['Country/Territory']==country,data))
   return result

def get_poulation_keys(data):
    objecto = data[0]
    try:
        values = objecto.values()
        labels = objecto.keys()
    except  Exception as e:
         print(f"Error personalizado capturado: {e}")         

    return labels, values

def generate_bar_char(labels, values):
    try:
        fig, ax = plt.subplots()
        ax.bar(labels,values)
        plt.savefig ('grafico.png')
    except  Exception as e:
         print(f"Error personalizado capturado: {e}")         
        

def generate_pie_char(labels, values):
    try:
        fig, ax = plt.subplots()
        ax.pie(labels,values)
        ax.axis('equal')    
        plt.savefig ('grafico.png')
    except  Exception as e:
         print(f"Error personalizado capturado: {e}")         
            

def imprime():
    print('***')
