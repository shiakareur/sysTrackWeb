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
for bar in barras:
      plt.text(bar.xy[0] + 0.35, bar.xy[1]+bar.get_height()+2, bar.get_height())
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
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width()+0.5, bar.xy[1]+0.25, bar.get_width())
plt.savefig(os.path.join("static", "graficos","cljxplantas.png"), dpi=300, bbox_inches='tight')
#########################
#CLJXEDAD
plt.figure(figsize=(8,8))
grafico_cljxedad= clj.groupby('Edad').size().plot(kind='bar',color='darkblue')
plt.xlabel('Edad')
plt.ylabel('')
plt.title('CLJ POR EDAD')
barras=grafico_cljxedad.patches
for bar in barras:
  plt.text(bar.xy[0] + 0.15, bar.xy[1]+bar.get_height()+0.5, bar.get_height())
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
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width(), bar.xy[1]+0.05, bar.get_width())
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
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width()+0.5, bar.xy[1]+0.20, bar.get_width())
plt.savefig(os.path.join("static", "graficos","senatixplantas.png"), dpi=300, bbox_inches='tight')
#########################
#SENATIXEDAD
plt.figure(figsize=(8,8))
grafico_senatixedad=senati.groupby('Edad').size().plot(kind='bar',color='darkred')
plt.xlabel('Edad')
plt.ylabel('')
plt.title('SENATINOS POR EDAD')
barras=grafico_senatixedad.patches
for bar in barras:
  plt.text(bar.xy[0] + 0.09, bar.xy[1]+bar.get_height()+0.5, bar.get_height())
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
for bar in barras:
  plt.text(bar.xy[0]+bar.get_width()+0.2, bar.xy[1]+0.05, bar.get_width())
plt.savefig(os.path.join("static", "graficos","senatixdistrito.png"), dpi=300, bbox_inches='tight')

#########################
#PARA GUARDAR GRÁFICA
#plt.savefig(os.path.join("graficos","rolMF.png"))

### SEGUNDA PARTE DE LAS GRAFICAS
DATA = pd.read_excel('DATA.xlsx',sheet_name='ABS 1', encoding='utf8')
DATA2 = pd.read_excel('DATA.xlsx',sheet_name='ABS 2', encoding='utf8')
DATA3 = pd.read_excel('DATA.xlsx',sheet_name='HC', encoding='utf8')
DATA4= pd.read_excel('DATA.xlsx',sheet_name='TIEMPO DE PERMANENCIA', encoding='utf8',header=None, skiprows=1)
DATA5=pd.read_excel('DATA.xlsx',sheet_name='ROTACION', encoding='utf8')
DATA6=pd.read_excel('DATA.xlsx',sheet_name='NOTAS', encoding='utf8')

df=pd.DataFrame(DATA)
df2=pd.DataFrame(DATA2)
df3=pd.DataFrame(DATA3)
df4=pd.DataFrame(DATA4)
df5=pd.DataFrame(DATA5)
df4.columns=['Tiempo (meses)', 'CLJ', 'SENATI', 'CLJ %', 'SENATI %']
df4['CLJ %']=df4['CLJ %']*100
df4['SENATI %']=df4['SENATI %']*100
df5[2017]=df5[2017]*100
df5[2018]=df5[2018]*100
df5[2019]=df5[2019]*100

#ABSENTISMO 1
grafico_Absentismo2 = df.plot(x='Tipos de Absentismos',y='Horas',kind='bar',color='darkblue', figsize=(12,6))
plt.title('Absentismo: Cantidad de Horas')
plt.xticks(None,None,rotation='horizontal')
barras=grafico_Absentismo2.patches
for bar in barras:
  #insertar etiquetas en la barra
  plt.text(bar.get_x()+0.17, bar.get_height()+40, bar.get_height())
#PARA GUARDAR GRÁFICA
plt.savefig(os.path.join("static", "graficos","absentismoHoras.png"),dpi=300, bbox_inches='tight')

# Porcentaje de absentismo
plt.figure(figsize=(10,10))
impr = ["Faltas injustificadas","Descanso médico","Permisos pagados", "Permiso dias no pagados"]
#exp=(0.1,0)
grafico_Absentismo1=df.plot.pie(x='Tipos de Absentismos',y='% MF',labels=impr, autopct='%1.1f%%')
plt.axis('equal')
plt.ylabel('')
plt.title('Absentismo: Porcentaje de MF')
plt.legend(loc='best')
#PARA GUARDAR GRÁFICA
plt.savefig(os.path.join("static", "graficos","absentismoPorcentaje.png"),dpi=300, bbox_inches='tight')

# Horas Capacitacion
plt.figure(figsize=(12,6))
ax = plt.gca()
df3.plot(kind='bar',x='Promoción',y='Horas Programadas',ax=ax)
barras = df3.plot(kind='bar',x='Promoción',y='Horas Ejecutadas', color='red', ax=ax)
# Sacar los valores de los rectangulos
for barra in barras.patches:
  barras.text(barra.get_x(), barra.get_height()+ 30, str(barra.get_height().astype(int)))
plt.xticks(None,None,rotation='horizontal')
plt.savefig(os.path.join("static", "graficos","horasCapacitacion.png"),dpi=300, bbox_inches='tight')

# Tiempo de permanencia
plt.figure(figsize=(10,10))
barras = df4.plot(x='Tiempo (meses)', y=['CLJ %', 'SENATI %'], kind="bar",figsize=(15,6))
# Sacar los valores de los rectangulos
for barra in barras.patches:
  barras.text(barra.get_x()+0.04, barra.get_height()+ 1, str(barra.get_height().astype(int)) + '%')
plt.xticks(None,None,rotation="horizontal")
plt.savefig(os.path.join("static", "graficos","tiempoPermanencia.png"),dpi=300, bbox_inches='tight')

# Rotacion
plt.figure(figsize=(10,10))
barras = df5.plot(x='MODALIDAD', y=[2017,2018,2019], kind="bar",figsize=(15,6))
plt.xticks(None,None,rotation="horizontal")
# Sacar los valores de los rectangulos
for barra in barras.patches:
  barras.text(barra.get_x()+0.04, barra.get_height()+ 1, str(barra.get_height().astype(int)) + '%')
plt.savefig(os.path.join("static", "graficos","rotacion.png"),dpi=300, bbox_inches='tight')

# Notas
DATA6.plot(kind='line',x='Promoción',y='Promedio Notas',figsize=(15,4))
plt.savefig(os.path.join("static", "graficos","notas.png"),dpi=300, bbox_inches='tight')