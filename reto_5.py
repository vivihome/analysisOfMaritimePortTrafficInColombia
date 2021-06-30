import pandas as pd 

def analizar_csv (filePath: str): 
  if filePath.endswith('.csv'): 
    try: 
      archivo = pd.read_csv(filePath, sep=';', header=0, index_col=0, encoding='UTF-8')
    except: 
      return "Ocurrio un error al leer el archivo. Valide la ruta" 
    try: 
      exportar = archivo['EXPORTACION']
      importar = archivo['IMPORTACIÓN']
      transbordo = archivo['TRANSBORDO']

      archivo['Total'] = exportar + importar + transbordo
      archivo = archivo.groupby(['AÑO VIGENCIA','ZONA PORTUARIA'])['Total'].mean()
      archivo = archivo.unstack()
      return archivo.to_dict()
    except Exception as exp:
      print('As ocurred error ',str(exp))
  else:
    return "Extensión inválida"


print(analizar_csv('C:/Users/Administrador/OneDrive/Desktop/vivian/Misión TIC (UTP)/Python/Retos/reto_5/Trafico_Portuario_Mar_timo_En_Colombia.csv'))