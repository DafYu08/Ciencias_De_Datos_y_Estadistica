#%%
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#import matplotlib.colors as mcolors
#%%
incendios = pd.read_csv('TP2 - Dataset incendios - incendios-cantidad-causas-provincia.csv')
incendios.loc[incendios['provincia'] == 'Santa Fé', 'provincia'] = 'Santa Fe'
provincias = incendios['provincia'].unique()

incendios_año = incendios.groupby('año')['total_incendios', 'incendio_neglgencia',
       'incendio_intencional', 'incendio_natural', 'incendio_desconocida'].sum()
incendios_año=incendios_año.reset_index()
#%%regiones
incendios=incendios.assign(region = 'Litoral')
incendios.loc[incendios['provincia'].isin(['Jujuy', 'Salta', 'Catamarca', 'La Rioja', 'Tucumán', 'Santiago del Estero']), 'region'] = 'Noroeste'
incendios.loc[incendios['provincia'].isin(['San Juan', 'Mendoza', 'San Luis']), 'region'] = 'Cuyo'
incendios.loc[incendios['provincia'].isin(['Córdoba']), 'region'] = 'Sierras'
incendios.loc[incendios['provincia'].isin(['La Pampa', 'Buenos Aires']), 'region'] = 'Pampas'
incendios.loc[incendios['provincia'].isin(['Ciudad Autónoma de Buenos Aires']), 'region'] = 'CABA'
incendios.loc[incendios['provincia'].isin(['Parques Nacionales']), 'region'] = 'Parques Nacionales'
incendios.loc[incendios['provincia'].isin(['Neuquén', 'Río Negro', 'Chubut', 'Santa Cruz']), 'region'] = 'Patagonia'
incendios.loc[incendios['provincia'].isin(['Tierra del Fuego']), 'region'] = 'Extremo austral'

incendios_region = incendios.groupby(['region','año'])['total_incendios', 'incendio_neglgencia','incendio_intencional', 'incendio_natural', 'incendio_desconocida'].sum()
incendios_region=incendios_region.reset_index()
regiones=incendios_region['region'].unique()
#%%
plt.figure(figsize=(16,9))
for p in provincias:
    prov=incendios[incendios['provincia']==p][['año', 'total_incendios']]
    plt.plot(prov['año'],prov['total_incendios'],'o-',label=p)
plt.legend()
plt.title('Total de incendios forestales por año y provincia')
plt.show()

plt.figure(figsize=(16,9))
for p in provincias:
    prov=incendios[incendios['provincia']==p][['año', 'incendio_intencional']]
    plt.plot(prov['año'],prov['incendio_intencional'],'o-',label=p)
plt.legend()
plt.title('Cantidad de incendios forestales intencional por año y provincia')
plt.show()
#%%
plt.figure(figsize=(16,9))
for r in incendios_region.drop_duplicates(['region'])['region']:
    reg=incendios_region[incendios_region['region']==r][['año', 'total_incendios']]
    plt.plot(reg['año'],reg['total_incendios'],'o-',label=r)
plt.legend()
plt.title('Total de incendios forestales por año y region')
plt.show()

plt.figure(figsize=(16,9))
for r in incendios_region.drop_duplicates(['region'])['region']:
    reg=incendios_region[incendios_region['region']==r][['año', 'incendio_intencional']]
    plt.plot(reg['año'],reg['incendio_intencional'],'o-',label=r)
plt.legend()
plt.title('Cantidad de incendios forestales intencional por año y region')
plt.show()
#%%
#plt.plot(incendios_año['año'],incendios_año['total_incendios'],'o-',color='crimson',label='Total')
plt.plot(incendios_año['año'],incendios_año['incendio_neglgencia'],'o-',color='navy',label='Neglgencia')
plt.plot(incendios_año['año'],incendios_año['incendio_intencional'],'o-',color='purple',label='Intencional')
plt.plot(incendios_año['año'],incendios_año['incendio_natural'],'o-',color='plum',label='Natural')
plt.plot(incendios_año['año'],incendios_año['incendio_desconocida'],'o-',color='hotpink',label='Desconocida')
plt.title('Causas de incendios forestales en Argentina')
plt.legend()
plt.xlabel('Año')
plt.ylabel('Catidad de incendios')
plt.show()
#%%
plt.figure(figsize=(12,6))
plt.plot(incendios_año['año'],incendios_año['total_incendios'],'o-',color='crimson',label='Total de incendios')
plt.plot(incendios_año['año'],incendios_año['incendio_neglgencia'],'o-',color='navy',label='Causados por Neglgencia')
plt.plot(incendios_año['año'],incendios_año['incendio_intencional'],'o-',color='purple',label='Causados Intencionalmente')
plt.plot(incendios_año['año'],incendios_año['incendio_natural'],'o-',color='plum',label='Causas Naturales')
plt.plot(incendios_año['año'],incendios_año['incendio_desconocida'],'o-',color='hotpink',label='Causas Desconocidas')
plt.title('Incendios forestales en Argentina',fontsize=20)
plt.legend()
plt.xlabel('Año',fontsize=16)
plt.ylabel('Catidad de incendios',fontsize=16)
plt.show()
#%%
plt.bar(incendios_año['año'],incendios_año['incendio_neglgencia'],color='navy',label='negligencia')
plt.bar(incendios_año['año'],incendios_año['incendio_intencional'],bottom=incendios_año['incendio_neglgencia'],color='blue',label='intencional')
plt.bar(incendios_año['año'],incendios_año['incendio_natural'],bottom=incendios_año['incendio_neglgencia']+incendios_año['incendio_intencional'],color='dodgerblue',label='natural')
plt.bar(incendios_año['año'],incendios_año['incendio_desconocida'],bottom=incendios_año['incendio_neglgencia']+incendios_año['incendio_intencional']+incendios_año['incendio_natural'],color='skyblue',label='desconocida')
plt.title('Causas de incendios forestales en Argentina')
plt.legend()
plt.xlabel('Año')
plt.ylabel('Catidad de incendios')
plt.show()

#%%
plt.figure(figsize=(12,8),dpi=500)
# Crear un colormap
cmap = cm.viridis # Puedes elegir el colormap que prefieras, como 'plasma', 'inferno', etc.
norm = plt.Normalize(0, 4)  # Normalización para que los colores varíen en 4 categorías

# Asignar colores a las barras
colors = [cmap(norm(0)), cmap(norm(1)), cmap(norm(2)), cmap(norm(3))]

# Graficar las barras apiladas con colormap
plt.bar(incendios_año['año'], incendios_año['incendio_intencional'], color=colors[0], label='Intencional')
plt.bar(incendios_año['año'], incendios_año['incendio_neglgencia'], bottom=incendios_año['incendio_intencional'], color=colors[1], label='Negligencia')
plt.bar(incendios_año['año'], incendios_año['incendio_natural'], bottom=incendios_año['incendio_neglgencia']+incendios_año['incendio_intencional'], color=colors[2], label='Natural')
plt.bar(incendios_año['año'], incendios_año['incendio_desconocida'], bottom=incendios_año['incendio_neglgencia']+incendios_año['incendio_intencional']+incendios_año['incendio_natural'], color=colors[3], label='Desconocida')

# Añadir título y etiquetas
plt.title('Causas de incendios forestales en Argentina',fontsize=20)
plt.xlabel('Año',fontsize=16)
plt.ylabel('Cantidad de incendios',fontsize=16)
plt.legend(fontsize=16)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tick_params(axis='both', labelsize=14)
# Mostrar gráfico
plt.show()

