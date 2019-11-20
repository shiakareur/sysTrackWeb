import os
import pandas as pd
import matplotlib.pyplot as plt

dotacion = pd.read_excel('dotacion.xlsm',sheet_name='BASE DE DATOS', encoding='utf8')

dotacion['Edad']=dotacion['Edad'].fillna(0.0).astype(int)

df=pd.DataFrame(dotacion)

clj=df[(df['Modalidad']=='CAPAC.LAB.JUVENIL') & (df['Estado']=='ACT')]
senati=df[(df['Modalidad']=='APRENDIZ SENATI') & (df['Estado']=='ACT')]
########################
#ROL MF
plt.figure(figsize=(8,8))
cant_clj=clj['Apellidos y Nombres'].count()
cant_senati=senati['Apellidos y Nombres'].count()
cant_total=cant_clj+cant_senati
MF=['CLJ','Aprendiz Senati','Total']
ROL=(cant_clj,cant_senati,cant_total)
barras= plt.bar(MF,ROL,align='center', color='darkred')
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11,
        }
for bar in barras:
      plt.text(bar.xy[0] + 0.35, bar.xy[1]+bar.get_height()+2, bar.get_height(),fontdict=font)
plt.title('ROL EN MODALIDADES FORMATIVAS') #Titulo del grafico
plt.savefig(os.path.join("static", "graficos","rolMF.png"), dpi=300, bbox_inches='tight')
#########################
#CLJXPLANTAS
plt.figure(figsize=(8,8))
grafico_cljxplantas=clj.groupby('Subdivision').size().plot(kind='barh',color='darkgreen')
plt.xlabel('')
plt.ylabel('')
plt.title('CLJ POR PLANTAS')
barras=grafico_cljxplantas.patches
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11,
        }
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width()+0.5, bar.xy[1]+0.25, bar.get_width(),fontdict=font)
plt.savefig(os.path.join("static", "graficos","cljxplantas.png"), dpi=300, bbox_inches='tight')
#########################
#CLJXEDAD
plt.figure(figsize=(8,8))
grafico_cljxedad= clj.groupby('Edad').size().plot(kind='bar',color='darkblue')
plt.xlabel('Edad')
plt.ylabel('')
plt.title('CLJ POR EDAD')
barras=grafico_cljxedad.patches
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11,
        }
for bar in barras:
  plt.text(bar.xy[0] + 0.15, bar.xy[1]+bar.get_height()+0.5, bar.get_height(),fontdict=font)
plt.savefig(os.path.join("static", "graficos","cljxedad.png"), dpi=300, bbox_inches='tight')
#########################
#CLJXGENERO
plt.figure(figsize=(8,8))
impr = ["Mujeres", "Hombres"]
exp=(0.1,0)
grafico_cljxgenero=clj.groupby('Sexo').size().plot.pie(explode=exp,labels=impr, autopct='%1.1f%%')
plt.axis('equal')
plt.ylabel('')
plt.title('CLJ POR GENERO')
plt.savefig(os.path.join("static", "graficos","cljxgenero.png"), dpi=300, bbox_inches='tight')
#########################
#CLJXDISTRITO
plt.figure(figsize=(8,8))
grafico_cljxdistrito=clj.groupby('Distrito').size().plot(kind='barh',color='darkgreen')
plt.xlabel('')
plt.ylabel('')
plt.title('CLJ POR DISTRITO')
barras=grafico_cljxdistrito.patches
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11
        }
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width(), bar.xy[1]+0.05, bar.get_width(),fontdict=font)
plt.savefig(os.path.join("static", "graficos","cljxdistrito.png"), dpi=300, bbox_inches='tight')
#########################
#APRENDIZ SENATI#
#########################
#SENATIXPLANTAS
plt.figure(figsize=(8,8))
grafico_senatixplantas=senati.groupby('Subdivision').size().plot(kind='barh',color='darkblue')
plt.xlabel('')
plt.ylabel('')
plt.title('SENATINOS POR PLANTAS')
barras=grafico_senatixplantas.patches
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11,
        }
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width()+0.5, bar.xy[1]+0.20, bar.get_width(),fontdict=font)
plt.savefig(os.path.join("static", "graficos","senatixplantas.png"), dpi=300, bbox_inches='tight')
#########################
#SENATIXEDAD
plt.figure(figsize=(8,8))
grafico_senatixedad=senati.groupby('Edad').size().plot(kind='bar',color='darkred')
plt.xlabel('Edad')
plt.ylabel('')
plt.title('SENATINOS POR EDAD')
barras=grafico_senatixedad.patches
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11,
        }
for bar in barras:
  plt.text(bar.xy[0] + 0.09, bar.xy[1]+bar.get_height()+0.5, bar.get_height(),fontdict=font)
plt.savefig(os.path.join("static", "graficos","senatixedad.png"), dpi=300, bbox_inches='tight')
#########################
#SENATIXGENERO
plt.figure(figsize=(8,8))
impr = ["Mujeres", "Hombres"]
exp=(0.1,0)
grafico_senatixgenero=senati.groupby('Sexo').size().plot.pie(explode=exp,labels=impr, autopct='%1.1f%%')
plt.axis('equal')
plt.ylabel('')
plt.title('SENATINOS POR GENERO')
plt.savefig(os.path.join("static", "graficos","senatixgenero.png"), dpi=300, bbox_inches='tight')
#########################
#SENATIXDISTRITO
plt.figure(figsize=(8,8))
grafico_senatixdistrito=senati.groupby('Distrito').size().plot(kind='barh',color='darkgreen')
plt.xlabel('')
plt.ylabel('')
plt.title('SENATI POR DISTRITO')
barras=grafico_senatixdistrito.patches
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11
        }
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width()+0.2, bar.xy[1]+0.05, bar.get_width(),fontdict=font)
plt.savefig(os.path.join("static", "graficos","senatixdistrito.png"), dpi=300, bbox_inches='tight')

#########################
#PARA GUARDAR GRÁFICA
#plt.savefig(os.path.join("graficos","rolMF.png"))
