# %% [markdown]
# ###  Exploration du dataset :

# %% [markdown]
#  l'importation des bibliotèque :

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# - numpy --> pour le calcul scientifique .
# - pandas --> pour les structures de données et les outils d'analyse de données.
# - matplotlib --> pour outils de visualisation de données.

# %% [markdown]
#  Afficher des dataset /chargement :

# %%
data = pd.read_csv('./adult.csv')
print(data)


# %%
# le nomber des lignes et colones :
data.shape

# %% [markdown]
# le dataset contient 15 attribut , 32560 individus .

# %%
# le type des données et valeurs possibles :

data.columns = ['age', 'workclass' , 'fnlwgt', 'education',
'education_num', 'marital-status', 'occupation', 'relationship', 'race',
'sex', 'capital_gai', 'capital_loss', 'hours_per_week', 'country',
'income']

data.info()

# %%
# les attributs numerique

data.describe()

# %% [markdown]
#  _la question 1 :_    
#    
# 
# le dataset :   
#   
# ensemble de données sur des observations concernant des différents paramètres financiers pour des adultes : âge, sexe, état civil ,pays, revenu , éducation , profession, gain en capital, et d'autres paramètres defini par suites ( attributs) .  
# 
#       
#       
# les attributs sont :
#  - age : l'age de l'individu , valeur continue positive .
#  - workclass : la classe d'oeuvre , les valeurs possibles : Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
#  - fnlwgt : le poids final, qui est le nombre d'unités dans la population cible que l'unité répondante représente , valeur continue positive .
#  - education : le niveau d’études atteint par l’individu, les valeurs possibles: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
#  - education_num : le nombre total d'années d'études, qui est une représentation continue de la variable discrète éducation.
#  - marital-status : l'état civil ,les valeurs possibles : Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
#  - occupation : la profession ,les valeurs possibles : Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
#  - relationship : le rôle de l'unité répondante dans la famille ,les valeurs possibles : Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
#  - race : la race de l'individu, les valeurs possibles: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
#  - sex : Female, Male.
#  - capital_gai / capital_loss : le revenus provenant de sources d'investissement autres que les salaires/salaires (gain /perte) , valeur continue .
#  - hours_per_week : nombres des heures de travaille  par semain ,valeur continue positive .
#  - country : le pays , les valeurs possibles:  United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
#  - income : le revenu , les valeurs possibles: >50K , <=50K .
# 
# 

# %% [markdown]
# _la question 2 :_  maximum, minimum, moyenne et l'écart type des attributs numériques. 

# %% [markdown]
# le max , min , moyenne , l’écart-type de l’âge :

# %%
max_age = data['age'].max()
min_age = data['age'].min() 
mean_age = data['age'].mean()
std_age = data['age'].std()

print("le max de l'age : " , max_age)
print("le min de l'age : " , min_age)
print("la moyenne de l'age : " , mean_age)
print("l’écart-type de l'age : " , std_age)

# %% [markdown]
# le max , min , moyenne , l’écart-type de capital_gai :

# %%
max_capital_gai = data['capital_gai'].max()
min_capital_gai = data['capital_gai'].min()
mean_capital_gai = data['capital_gai'].mean()
std_capital_gai = data['capital_gai'].std()

print("le max de capital_gai: " , max_capital_gai)
print("le min de capital_gai : " , min_capital_gai)
print("la moyenne de capital_gai : " , mean_capital_gai)
print("l’écart-type de capital_gai : " , std_capital_gai)

# %% [markdown]
# le max , min , moyenne , l’écart-type de capital_loss : 

# %%
max_capital_loss = data['capital_loss'].max()
min_capital_loss = data['capital_loss'].min()
mean_capital_loss = data['capital_loss'].mean()
std_capital_loss = data['capital_loss'].std()

print("le max de capital_loss : " , max_capital_loss)
print("le min de capital_loss : " , min_capital_loss)
print("la moyenne de capital_loss : " , mean_capital_loss)
print("l’écart-type de capital_loss : " , std_capital_loss)

# %% [markdown]
# le max , min , moyenne , l’écart-type de hours_per_week :

# %%
max_hours_per_week = data['hours_per_week'].max()
min_hours_per_week = data['hours_per_week'].min()
mean_hours_per_week = data['hours_per_week'].mean()
std_hours_per_week = data['hours_per_week'].std()

print("le max de hours_per_week : " , max_hours_per_week)
print("le min de hours_per_week : " , min_hours_per_week)
print("la moyenne de hours_per_week : " , mean_hours_per_week)
print("l’écart-type de hours_per_week : " , std_hours_per_week)

# %% [markdown]
# _la question 3 :_ le nombre d’individus qui gagnent plus de 50.000$ et ceux qui gagnent moins ainsi que leurs
# pourcentages.

# %%
nbr_over = len(data[(data.income == '>50K')])
pourcentage_over = (nbr_over *100) / len(data)
nbr_less = len(data[(data.income == '<=50K')])
pourcentage_less = (nbr_less*100) / len(data)

print("le nombre d’individus qui gagnent plus de 50.000$ : " , nbr_over)
print("le pourcentages d’individus qui gagnent plus de 50.000$ : " , pourcentage_over , "%")
print("le nombre d’individus qui gagnent moin de 50.000$ : " , nbr_less)
print("le pourcentages d’individus qui gagnent moin de 50.000$ : " , pourcentage_less , "%")

# %% [markdown]
# _la question 4 :_  le nombre d’hommes et de femmes.

# %%
femme = len(data[(data.sex == 'Female')])
homme = len(data[(data.sex == 'Male')])


print("le nombre des femmes : " ,femme )
print("le nombre des hommes : " ,homme  )

# %% [markdown]
# _la question 5 :_ le nombre d’hommes qui gagnent plus de 50.000$ et ceux qui gagnent moins ainsi que leurs
# pourcentages. 

# %%
nbr_homme_over = len(data[(data.sex == 'Male') & (data.income == '>50K')])
pourcentage_homme_over = (nbr_homme_over*100) / homme
pourcentage_homme_over_total = (nbr_homme_over*100) / len(data)
nbr_homme_less = len(data[(data.sex == 'Male') & (data.income == '<=50K')])
pourcentage_homme_less = ( nbr_homme_less*100) / homme
pourcentage_homme_less_total = (nbr_homme_less*100) / len(data)

print("le nombre d’hommes qui gagnent plus de 50.000$ : " , nbr_homme_over)
print("le pourcentage d’hommes qui gagnent plus de 50.000$ (par rapport le nombre des hommes ) : " , pourcentage_homme_over , "%")
print("le pourcentage d’hommes qui gagnent plus de 50.000$ (par rapport le nombre des individus ) : " , pourcentage_homme_over_total , "%")
print("le nombre d’hommes qui gagnent moin de 50.000$ : " , nbr_homme_less)
print("le pourcentage d’hommes qui gagnent moin de 50.000$ (par rapport le nombre des hommes ) : " , pourcentage_homme_less , "%")
print("le pourcentage d’hommes qui gagnent moin de 50.000$ (par rapport le nombre des individus ) : " , pourcentage_homme_less_total , "%")

# %% [markdown]
# _la question 6 :_  Donner le nombre de femmes qui gagnent plus de 50.000$ et ceux qui gagnent moins ainsi que leurs
# pourcentages. 

# %%
nbr_femme_over = len(data[(data.sex == 'Female') & (data.income == '>50K')])
pourcentage_femme_over = (nbr_femme_over*100) / femme
pourcentage_femme_over_total = (nbr_femme_over*100) / len(data)
nbr_femme_less = len(data[(data.sex == 'Female') & (data.income == '<=50K')])
pourcentage_femme_less = ( nbr_femme_less*100) / femme
pourcentage_femme_less_total = (nbr_femme_less*100) / len(data)

print("le nombre des femmes qui gagnent plus de 50.000$ : " , nbr_femme_over)
print("le pourcentage des femmes qui gagnent plus de 50.000$ (par rapport le nombre des femmes ) : " , pourcentage_femme_over , "%")
print("le pourcentage des femmes qui gagnent plus de 50.000$ (par rapport le nombre des individus ) : " , pourcentage_femme_over_total , "%")
print("le nombre des femmes qui gagnent moin de 50.000$ : " , nbr_femme_less)
print("le pourcentage des femmes qui gagnent moin de 50.000$ (par rapport le nombre des femmes ) : " , pourcentage_femme_less , "%")
print("le pourcentage des femmes qui gagnent moin de 50.000$ (par rapport le nombre des individus ) : " , pourcentage_femme_less_total , "%")

# %% [markdown]
# _la question 7 :_ le nuage de points montrant la distribution de l’âge des enregistrements (âge vs nombre
# d’entrées).

# %%
plt.xlabel('l\'age')
plt.ylabel('le nombres d\'individu')
plt.title('le nuage de points')
plt.scatter(x=data.age, y=data.index[0:len(data)], color="green")
plt.show

# %% [markdown]
# _la question 8 :_

# %%
data.groupby('income').age.mean().plot(kind='bar')
plt.show() 

# %% [markdown]
# _la question 9 :_   les questions 6 et 7(le niveau d’études au lieu de l’âge ) .

# %% [markdown]
# extraire le groupe des femme

# %%
G_F=data[(data.sex == 'Female')]

# >5oK
G_F_over=data[(data.sex == 'Female') & (data.income == '>50K')]

# <=50K
G_F_Less=data[(data.sex == 'Female') & (data.income =='<=50K')]

# %% [markdown]
# la moyenne , la médiane , la variance et l’écart-type 

# %%
 

# le groupr des femmes 'moyenne'
G_F_moy = G_F['education_num'].mean()

# le groupr des femmes 'median'
G_F_med = G_F['education_num'].median()

#le groupr des femmes ' variance'
G_F_var = G_F['education_num'].var()

#le groupr des femmes 'l’écart-type '
G_F_et = G_F['education_num'].std()

 

print("la moyenne de education_num (pour les femme ): " , G_F_moy) 
print("la médiane de education_num (pour les femme ) : " , G_F_med) 
print("la variance de education_num (pour les femme ): " , G_F_var) 
print("l’écart-type de education_num (pour les femme ) : " , G_F_et) 
 

#  femmes qui gagnent plus de 50.000$ 'moyenne' selent niveau d'etude
G_F_O_moy = G_F_over['education_num'].mean()

#  femmes qui gagnent plus de 50.000$ 'median' selent niveau d'etude
G_F_O_med = G_F_over['education_num'].median()

#  femmes qui gagnent plus de 50.000$ 'variance' selent niveau d'etude
G_F_O_var = G_F_over['education_num'].var()

#  femmes qui gagnent plus de 50.000$ 'l’écart-type' selent niveau d'etude
G_F_O_et = G_F_over['education_num'].std()


print("la moyenne de education_num (pour les femme qui gagnent plus de 50.000$ ): " , G_F_O_moy) 
print("la médiane de education_num (pour les femme qui gagnent plus de 50.000$) : " , G_F_O_med) 
print("la variance de education_num (pour les femme qui gagnent plus de 50.000$): " , G_F_O_var) 
print("l’écart-type de education_num (pour les femme qui gagnent plus de 50.000$ ) : " , G_F_O_et) 

# femmes qui gagnent moins de 50.000$ 'moyenne' selent niveau d'etude
G_F_L_moy = G_F_Less['education_num'].mean()

# e femmes qui gagnent moins de 50.000$ 'median' selent niveau d'etude
G_F_L_med = G_F_Less['education_num'].median()
 
# e femmes qui gagnent moins de 50.000$ 'variance' selent niveau d'etude
G_F_L_var = G_F_Less['education_num'].var()

# e femmes qui gagnent moins de 50.000$ 'l’écart-type' selent niveau d'etude
G_F_L_et = G_F_Less['education_num'].std()


print("la moyenne de education_num (pour les femme qui gagnent plus de 50.000$ ): " , G_F_L_moy) 
print("la médiane de education_num (pour les femme qui gagnent plus de 50.000$) : " , G_F_L_med) 
print("la variance de education_num (pour les femme qui gagnent plus de 50.000$): " , G_F_L_var) 
print("l’écart-type de education_num (pour les femme qui gagnent plus de 50.000$ ) : " , G_F_L_et)



# %% [markdown]
#  Représenter la distribution de education_num par un histogramme pour tout les femmes 
# 

# %%
G_F_eduction=G_F['education_num']

plt.hist(G_F_eduction)
plt.show()

# %% [markdown]
# Représenter la distribution de education_num par un histogramme pour  les femmes  gagnent plus de 50.000$ 
# 

# %%
G_F_eduction_over=G_F_over['education_num']
plt.hist(G_F_eduction_over)
plt.show()

# %% [markdown]
# Représenter la distribution de education_num par un histogramme pour  les femmes  gagnent moins de 50.000$ 
# 

# %%
G_F_eduction_Less=G_F_Less['education_num']
plt.hist(G_F_eduction_Less)
plt.show()

# %% [markdown]
# le nuage de points montrant la distribution de niveau d'etude des enregistrements 

# %%
plt.xlabel('l\'niveau')
plt.ylabel('le nombres d\'individu')
plt.title('le nuage de points')
plt.scatter(x=data.education_num, y=data.index[0:len(data)], color="red")
plt.show

# %% [markdown]
# _la question 10 :_   les questions 6 et 7(le statut de l’employé (self-employed, private, federalgov, …) au lieu de l’âge)

# %%
data['workclass']

CD = data.groupby('workclass').size()
print(CD)


# %% [markdown]
# convert-categorical-variable-to-numeric statut de l’employé

# %%
data_workclass = pd.read_csv('./adult.csv')
data_workclass.columns = ['age', 'workclass' , 'fnlwgt', 'education',
'education_num', 'marital-status', 'occupation', 'relationship', 'race',
'sex', 'capital_gai', 'capital_loss', 'hours_per_week', 'country',
'income'] 

# %%

data_workclass['workclass'].replace(['?', 'Federal-gov','Local-gov','Never-worked','Private','Self-emp-inc','Self-emp-not-inc','State-gov','Without-pay'],[0, 1,2,3,4,5,6,7,8], inplace=True)
print(data_workclass)
print(data)

# %%
CD2 = data_workclass.groupby('workclass').size()
print(CD2)

# %% [markdown]
# extraire le groupe des femme

# %%

G_F=data_workclass[(data_workclass.sex == 'Female')]
# >5oK
G_F_over=data_workclass[(data_workclass.sex == 'Female') & (data_workclass.income == '>50K')]

# <=50K
G_F_Less=data_workclass[(data_workclass.sex == 'Female') & (data_workclass.income =='<=50K')]

# %% [markdown]
# la moyenne et la médiane de workclass

# %%
# le groupr des femmes 'moyenne'
G_F_moy = G_F['workclass'].mean() 
print("la moyenne de workclass (pour les femme ): " , G_F_moy)   

# on ne peut pas prendre cette valeur en considération car apres la coversion de categorical-variable-to-numeric workclass , les valeur devienne : {0,1,2,3,4,5,6,7,8,}

# le groupr des femmes 'median'
G_F_med = G_F['workclass'].median()
print("la médiane de workclass (pour les femme ): " , G_F_med) 

# femmes qui gagnent moins de 50.000$ 'median' selon workclass
G_F_med_les = G_F_Less['workclass'].median()
print("la médiane de workclass (pour les femme qui gagnent moins de 50.000$): " , G_F_med_les)

# %% [markdown]
# Représenter la distribution de workclass par un histogramme pour tout les femmes 

# %%
G_F_workclass=G_F['workclass']
plt.hist(G_F_workclass)
plt.show()

# %% [markdown]
# Représenter la distribution de workclass par un histogramme pour  les femmes  gagnent plus de 50.000$ 
# 

# %%
G_F_workclass_over=G_F_over['workclass']

plt.hist(G_F_workclass_over)
plt.show()

# %% [markdown]
#  Représenter la distribution de workclass par un histogramme pour  les femmes  gagnent moins de 50.000$ 

# %%
G_F_workclass_Less=G_F_Less['workclass']
plt.hist(G_F_workclass_Less)
plt.show()

# %% [markdown]
# le nuage de points montrant la distribution de workclass des enregistrements 
# 

# %%
plt.xlabel('l\'workclass')
plt.ylabel('le nombres d\'individu')
plt.title('le nuage de points')
plt.scatter(x=data_workclass.workclass, y=data_workclass.index[0:len(data_workclass)], color="grey")
plt.show

# %% [markdown]
# _la question 11 :_   les questions 6 et 7( le poste occupé (adm-clerical, sales, craft-repair, …) au lieu de l’âge)

# %%
data['occupation']

OCD = data.groupby('occupation').size()
print(OCD)

# %% [markdown]
# convert-categorical-variable-to-numeric statut de l’employé

# %%
data_occupation = pd.read_csv('./adult.csv')
data_occupation.columns = ['age', 'workclass' , 'fnlwgt', 'education',
'education_num', 'marital-status', 'occupation', 'relationship', 'race',
'sex', 'capital_gai', 'capital_loss', 'hours_per_week', 'country',
'income']

# %%
data_occupation['occupation'].replace(['?', 'Adm-clerical','Armed-Forces','Craft-repair','Exec-managerial','Farming-fishing','Handlers-cleaners','Machine-op-inspct','Other-service','Priv-house-serv','Prof-specialty','Protective-serv','Sales','Tech-support','Transport-moving'],[0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14], inplace=True)

# %%
OCD2 = data_occupation.groupby('occupation').size()
print(OCD2)

# %% [markdown]
# extraire le groupe des femme

# %%

G_F=data_occupation[(data_occupation.sex == 'Female')]
# >5oK
G_F_over=data_occupation[(data_occupation.sex == 'Female') & (data_occupation.income == '>50K')]

# <=50K
G_F_Less=data_occupation[(data_occupation.sex == 'Female') & (data_occupation.income =='<=50K')]
 
# on ne peut pas prendre cette valeur en considération car apres la coversion de categorical-variable-to-numeric occupation , les valeur devienne : {0,1,2,3,4,5,6,7,8,}


# %% [markdown]
# la moyenne et la médiane d occupation

# %%
# le groupr des femmes 'median'
G_F_med = G_F['occupation'].median()
# femmes qui gagnent moins de 50.000$ 'median' selon  l'occupation
G_F_med_l = G_F_Less['occupation'].median()

print("la médiane d occupation (pour les femme ): " , G_F_med) 
print("la médiane de workclass (pour les femmes qui gagnent moins de 50.000$  ): " , G_F_med_l) 

# %% [markdown]
# Représenter la distribution de occupation par un histogramme pour tout les femmes 

# %%

G_F_occupation=G_F['occupation']
plt.hist(G_F_occupation, color="orange")
plt.show()

# %% [markdown]
# Représenter la distribution de occupation par un histogramme pour  les femmes  gagnent plus de 50.000$ 

# %%

G_F_occupation_over=G_F_over['occupation']
plt.hist(G_F_occupation_over, color="orange")
plt.show()

# %% [markdown]
# Représenter la distribution de occupation par un histogramme pour  les femmes  gagnent moins de 50.000$ 

# %%
G_F_occupation_Less=G_F_Less['occupation']
plt.hist(G_F_occupation_Less, color="orange")
plt.show()

# %% [markdown]
# le nuage de points montrant la distribution de occupation des enregistrements 

# %%
plt.xlabel('l\'occupation')
plt.ylabel('le nombres d\'individu')
plt.title('le nuage de points')
plt.scatter(x=data_occupation.occupation, y=data_occupation.index[0:len(data_occupation)], color="yellow")
plt.show

# %% [markdown]
# _la question 12 :_ un graphique de barres empilées présentant la relation entre le nombre d’heures travaillées et le
# revenu.

# %%
data.groupby('income').hours_per_week.mean().plot(kind='bar')
 

# %% [markdown]
# _la question 13 :_  un graphique de barres empilées présentant la relation entre la race et le revenu

# %%
data.groupby(['income','race']).size().unstack().plot(kind='bar',stacked=True)
plt.show()

# %% [markdown]
# _la question 14 :_ un graphique de barres empilées présentant la relation entre le sexe et le revenu

# %%
data.groupby(['income','sex']).size().unstack().plot(kind='bar',stacked=True)
plt.show()

# %% [markdown]
# ###  Prétraitement du dataset :

# %% [markdown]
# _la question 1 :_  Sélection d’attributs 

# %%
for i in data.columns:
    print ("---- %s ---" % i)
    print (data[i].value_counts())

# %% [markdown]
# on a exécuté une boucle for sur toutes les colonnes en utilisant la fonction value_counts de la bibliotèque Pandas qui retourne le nombre des valeurs uniques , d'apres ca on selectionne les colonnes qui ont beaucoup de valeurs distinctes comme l'attribut fnlgwt qui a environ 2000+ valeurs. ( les attributs qui ont beaucoup de valeurs distinctes considéré comme attribut noisy , doit etre supprimer )

# %%
data.drop(['education_num','age', 'hours_per_week', 'fnlwgt', 'capital_gai','capital_loss', 'country'], axis=1, inplace=True)
data.info()

# %% [markdown]
# La fonction Pandas.drop est utilisée pour supprimer des colonnes ou des lignes spécifiées. axis=1 représente que nous avons l'intention de supprimer la colonne elle-même, inplace=True est de mentionner que nous remplaçons la trame de données d'origine.

# %% [markdown]
# _la question 2 :_ Réduction de dimension , trouver la corrélation entre les attributs 

# %%
data.corr()

# %% [markdown]
# les attribut qui sont une coorrélation qui tend vers le 1 indique que ces deux attributs sont pareille , on peut soit les fusionner ou les éliminer , dans notre cas les attributs sont distinct

# %% [markdown]
# _la question 3 :_ Données manquantes/erronées 

# %%
for i in data.columns:
    print ("---- %s ---" % i)
    print (data[i].value_counts())

# %%
print(data)
#income
index_income=data.loc[(data['income']!=('<=50K'))&(data['income']!=('>50K'))]
print("les index des lignes irone pour l'attribut income : " ,index_income)
#race
index_race=data.loc[(data['race']!=('Black'))&(data['race']!=('Asian-Pac-Islander'))&(data['race']!=('Other'))&(data['race']!=('White'))&(data['race']!=('Amer-Indian-Eskimo'))]
print("les index des lignes irone pour l'attribut race : " ,index_race)
#sex
index_sex=data.loc[(data['sex']!=('Male'))&(data['sex']!=('Female'))]
print("les index des lignes irone pour l'attribut sex : " ,index_sex)
#marital-status
index_marital=data.loc[(data['marital-status']!=('Married-spouse-absent'))&(data['marital-status']!=('Widowed'))&(data['marital-status']!=('Married-civ-spouse'))&(data['marital-status']!=('Divorced'))&(data['marital-status']!=('Never-married'))&(data['marital-status']!=('Married-AF-spouse'))&(data['marital-status']!=('Separated'))]
print("les index des lignes irone pour l'attribut marital-status : " ,index_marital)

#workclass
index_workclass=data.loc[(data['workclass']!=('Self-emp-inc'))&(data['workclass']!=('State-gov'))&(data['workclass']!=('Federal-gov'))&(data['workclass']!=('Without-pay'))&(data['workclass']!=('Local-gov'))&(data['workclass']!=('Private'))&(data['workclass']!=('Self-emp-not-inc'))]
print("les index des lignes irone pour l'attribut workclass : " ,index_workclass)


#education
index_education=data.loc[(data['education']!=('Some-college'))&(data['education']!=('Preschool'))&(data['education']!=('5th-6th'))&(data['education']!=('HS-grad'))&(data['education']!=('Masters'))&(data['education']!=('12th'))&(data['education']!=('7th-8th'))&(data['education']!=('Prof-school'))&(data['education']!=('1st-4th'))&(data['education']!=('Assoc-acdm'))&(data['education']!=('Doctorate'))&(data['education']!=('11th'))&(data['education']!=('Bachelors'))&(data['education']!=('10th'))&(data['education']!=('Assoc-voc'))&(data['education']!=('9th'))]
print("les index des lignes irone pour l'attribut education : " ,index_education)


#occupation
index_occupation=data.loc[(data['occupation']!=('Farming-fishing'))&(data['occupation']!=('Tech-support'))&(data['occupation']!=('Adm-clerical'))&(data['occupation']!=('Handlers-cleaners'))&(data['occupation']!=('Prof-specialty'))&(data['occupation']!=('Machine-op-inspct'))&(data['occupation']!=('Exec-managerial'))&(data['occupation']!=('Priv-house-serv'))&(data['occupation']!=('Craft-repair'))&(data['occupation']!=('Sales'))&(data['occupation']!=('Transport-moving'))&(data['occupation']!=('Armed-Forces'))&(data['occupation']!=('Other-service'))&(data['occupation']!=('Protective-serv'))]
print("les index des lignes irone pour l'attribut occupation : " ,index_occupation) 

#relationship
index_relationship=data.loc[(data['relationship']!=('Not-in-family'))&(data['relationship']!=('Wife'))&(data['relationship']!=('Other-relative'))&(data['relationship']!=('Unmarried'))&(data['relationship']!=('Husband'))&(data['relationship']!=('Own-child'))]
print("les index des lignes irone pour l'attribut marital-status : " ,index_relationship)




# %% [markdown]
# les attributs worclass et occupation contients des valeurs manquantes/erronées , on doit garde seulement les data juste . 

# %%

#workclass
data=data.loc[(data['workclass']==('Self-emp-inc'))|(data['workclass']==('State-gov'))|(data['workclass']==('Federal-gov'))|(data['workclass']==('Without-pay'))|(data['workclass']==('Local-gov'))|(data['workclass']==('Private'))|(data['workclass']==('Self-emp-not-inc'))]
 
#occupation
data=data.loc[(data['occupation']==('Farming-fishing'))|(data['occupation']==('Tech-support'))|(data['occupation']==('Adm-clerical'))|(data['occupation']==('Handlers-cleaners'))|(data['occupation']==('Prof-specialty'))|(data['occupation']==('Machine-op-inspct'))|(data['occupation']==('Exec-managerial'))|(data['occupation']==('Priv-house-serv'))|(data['occupation']==('Craft-repair'))&(data['occupation']==('Sales'))&(data['occupation']==('Transport-moving'))|(data['occupation']==('Armed-Forces'))|(data['occupation']==('Other-service'))|(data['occupation']==('Protective-serv'))]

print(data)


# %% [markdown]
# _la question 4 :_ Transformation des données : convertir les valeurs (attributs) nominales en valeurs numériques utulisant la bibliotèque Pandas 

# %%
data['income'] = data['income'].map({'<=50K': 0, '>50K': 1}).astype(int)
data['sex'] = data['sex'].map({'Male': 0, 'Female': 1}).astype(int)
data['race'] = data['race'].map({'Black': 0, 'Asian-Pac-Islander': 1,'Other': 2, 'White': 3, 'Amer-Indian-Eskimo': 4})
data['marital-status'] = data['marital-status'].map({'Married-spouse-absent': 0, 'Widowed': 1, 'Married-civ-spouse': 2, 'Separated': 3, 'Divorced': 4,'Never-married': 5, 'Married-AF-spouse': 6}) 
data['workclass'] = data['workclass'].map({'Self-emp-inc': 0, 'State-gov': 1,'Federal-gov': 2, 'Without-pay': 3, 'Local-gov': 4,'Private': 5, 'Self-emp-not-inc': 6})
data['education'] = data['education'].map({'Some-college': 0, 'Preschool': 1, '5th-6th': 2, 'HS-grad': 3, 'Masters': 4, '12th': 5, '7th-8th': 6, 'Prof-school': 7,'1st-4th': 8, 'Assoc-acdm': 9, 'Doctorate': 10, '11th': 11,'Bachelors': 12, '10th': 13,'Assoc-voc': 14,'9th': 15}) 
data['occupation'] = data['occupation'].map({ 'Farming-fishing': 1, 'Tech-support': 2, 'Adm-clerical': 3, 'Handlers-cleaners': 4, 'Prof-specialty': 5,'Machine-op-inspct': 6, 'Exec-managerial': 7,'Priv-house-serv': 8,'Craft-repair': 9,'Sales': 10, 'Transport-moving': 11, 'Armed-Forces': 12, 'Other-service': 13,'Protective-serv': 14 }) 
data['relationship'] = data['relationship'].map({'Not-in-family': 0, 'Wife': 1, 'Other-relative': 2, 'Unmarried': 3,'Husband': 4,'Own-child': 5}) 

print(data)

# %% [markdown]
# _la question 4 :_ Normalisation/Standardisation des données

# %%
data['workclass'] = data['workclass']/data['workclass'].max()
data['workclass'].astype(int)
data['race'] = data['race']/data['race'].max()
data['race'].astype(int)
data['relationship'] = data['relationship']/data['relationship'].max()
data['relationship'].astype(int)
data['occupation'] = data['occupation']/data['occupation'].max()
data['occupation'].astype(int)
data['education'] = data['education']/data['education'].max()
data['education'].astype(int)
data['marital-status'] = data['marital-status']/data['marital-status'].max() 
data['marital-status'].astype(int)
 


# %%
data.info()

# %% [markdown]
# la formule de normalisation :  
# 
# <p align="center" width="100%">
#     <img src="https://miro.medium.com/max/470/1*renoW28YuTJ7VxU8TfAM6A.png"> 
# </p>

# %% [markdown]
# _la question 6 :_ Séparation des données

# %%
r = 0.7

data_x = pd.DataFrame(np.c_[data['relationship'], data['education'], data['race'],data['occupation'],data['sex'],data['marital-status'],data['workclass']], columns = ['relationship','education','race','occupation','gender','marital','workclass'])
data_y = pd.DataFrame(data.income)

data_train_x = data_x[1 : ((int) (len(data_x)*r))] 
data_test_x = data_x[((int) (len(data_x)*r)) : len(data_x)]

data_train_y = data_y[1 : ((int) (len(data_y)*r))] 
data_test_y = data_y[((int) (len(data_y)*r)) : len(data_y)]


# %% [markdown]
# ### Prédiction et classification  
# 

# %% [markdown]
# #### Régression logistique
# 
# La régression logistique est l'un des algorithmes d'apprentissage automatique supervisé les plus simples et les plus couramment utilisés pour la classification catégorielle. Les concepts fondamentaux de base de la régression logistique sont faciles à comprendre et peuvent être utilisés comme algorithme de base pour tout problème de classification binaire (0 ou 1), pour nous( <50 , =>50)

# %% [markdown]
# Créer un classifieur à base de l’algorithme Régression logistique

# %%
from sklearn.linear_model import LogisticRegression
clf1 = LogisticRegression()

# %% [markdown]
# Appliquer le classifieur sur l’ensemble de données

# %%
clf1.fit(data_train_x, data_train_y)

# %% [markdown]
# appliquer le classifieur résultant sur les data test

# %%
predY = clf1.predict(data_test_x)
summary = pd.concat([pd.DataFrame(data_test_y), pd.Series(predY, name = 'income')], axis=1)

# %% [markdown]
# calculer la Précision

# %%
from sklearn.metrics import accuracy_score
print('Précision = %.2f' % (accuracy_score(data_test_y, predY)))

# %% [markdown]
# la matrice de confusion

# %%
from sklearn.metrics import confusion_matrix
print(confusion_matrix(data_test_y, predY))

# %% [markdown]
# on peut aussi utulise les data train pour le test : 

# %%
predY_train = clf1.predict(data_train_x)
summary = pd.concat([pd.DataFrame(data_train_y), pd.Series(predY_train, name = 'income')], axis=1)
print('Précision (data train)= %.2f' % (accuracy_score(data_train_y, predY_train)))
print(confusion_matrix(data_train_y, predY_train))

# %% [markdown]
# #### Naïve Bayes  
# 
# 
# Naive Bayes est un algorithme de classification pour les problèmes de classification binaire (à deux classes) et multiclasses. On l'appelle Bayes naïf ou Bayes idiot parce que les calculs des probabilités pour chaque classe sont simplifiés pour rendre leurs calculs traitables.

# %% [markdown]
# Créer un classifieur à base de l’algorithme Naïve Bayes.

# %%
from sklearn import naive_bayes
clf2 = naive_bayes.GaussianNB()


# %% [markdown]
# Appliquer le classifieur sur l’ensemble de données

# %%
clf2 = clf2.fit(data_train_x, data_train_y)

# %% [markdown]
# appliquer le classifieur résultant sur les data test

# %%
predY = clf2.predict(data_test_x)
summary = pd.concat([pd.DataFrame(data_test_y), pd.Series(predY, name = 'income')], axis=1)

# %% [markdown]
# calculer la Précision

# %%
from sklearn.metrics import accuracy_score
print('Précision = %.2f' % (accuracy_score(data_test_y, predY)))


# %% [markdown]
# la matrice de confusion

# %%
print(confusion_matrix(data_test_y, predY))

# %% [markdown]
# on peut aussi utulise les data train pour le test : 

# %%
predY_train = clf2.predict(data_train_x)
summary = pd.concat([pd.DataFrame(data_train_y), pd.Series(predY_train, name = 'income')], axis=1)
print('Précision (data train)= %.2f' % (accuracy_score(data_train_y, predY_train)))
print(confusion_matrix(data_train_y, predY_train))

# %% [markdown]
# #### Arbres de décision    
# 
# L’algorithme d’arbre de décision appartient à la catégorie des algorithmes d’apprentissage supervisé. Cela fonctionne à la fois pour les variables de sortie continues et catégorielles.

# %% [markdown]
# Créer un classifieur à base de l’algorithme Arbres de décision

# %%
from sklearn import tree
clf3 = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3) 

# %% [markdown]
# Appliquer le classifieur sur l’ensemble de données

# %%
clf3 = clf3.fit(data_train_x, data_train_y)

# %% [markdown]
# Afficher l’arbre résultant sous forme textuelle

# %%
txt_tree = tree.export_text(clf3)
print(txt_tree)


# %% [markdown]
# Enregistrer l’arbre résultant dans un fichier

# %%
with open("tree.log", "w") as fout:
    fout.write(txt_tree)

# %% [markdown]
# Produire une représentation graphique de l’arbre résultant

# %%
figure = plt.figure(figsize = (12,10))
reslt = tree.plot_tree(clf3 )
plt.show()


# %% [markdown]
# appliquer le classifieur résultant sur les data test

# %%
predY = clf3.predict(data_test_x) 
summary = pd.concat([pd.DataFrame(data_test_y), pd.Series(predY, name = 'income')], axis=1)

# %% [markdown]
# calculer la Précision

# %%
print('Précision = %.2f' % (accuracy_score(data_test_y, predY)))

# %% [markdown]
# la matrice de confusion

# %%
print(confusion_matrix(data_test_y, predY))

# %% [markdown]
# on peut aussi utulise les data train pour le test : 

# %%
predY_train = clf3.predict(data_train_x)
summary = pd.concat([pd.DataFrame(data_train_y), pd.Series(predY_train, name = 'income')], axis=1)
print('Précision (data train)= %.2f' % (accuracy_score(data_train_y, predY_train)))
print(confusion_matrix(data_train_y, predY_train))

# %% [markdown]
# #### K plus proches voisin  
#   
#   L’algorithme des k plus proches voisins est un algorithme d’apprentissage supervisé ,il sera possible de classer (déterminer le label) d’une nouvelle donnée ,par calcule les distances entre ces donnée

# %% [markdown]
# Créer un classifieur à base de l’algorithme Nearest Neighbors(K plus proches voisin)

# %%
from sklearn import neighbors
clf4 = neighbors. KNeighborsClassifier(n_neighbors=3,
metric='minkowski', p=2)

# %% [markdown]
# Appliquer le classifieur sur l’ensemble de données

# %%
clf4 = clf4.fit(data_train_x, data_train_y)

# %% [markdown]
# appliquer le classifieur résultant sur les data test

# %%
predY = clf4.predict(data_test_x) 
summary = pd.concat([pd.DataFrame(data_test_y), pd.Series(predY, name = 'income')], axis=1)

# %% [markdown]
# calculer la Précision

# %%
print('Précision = %.2f' % (accuracy_score(data_test_y, predY)))

# %% [markdown]
# la matrice de confusion

# %%
print(confusion_matrix(data_test_y, predY))

# %% [markdown]
# on peut aussi utulise les data train pour le test : 

# %%
predY_train = clf4.predict(data_train_x)
summary = pd.concat([pd.DataFrame(data_train_y), pd.Series(predY_train, name = 'income')], axis=1)
print('Précision (data train)= %.2f' % (accuracy_score(data_train_y, predY_train)))
print(confusion_matrix(data_train_y, predY_train))

# %% [markdown]
# faut mieux expérimenter le classifieur sur différents valeurs de k ( 1, 5, 10, 15, 20...) pour avoir la meuilleure valeure.

# %%
#tableau des valeur
nbrNeighbors = [1, 5, 10, 15, 20]

# tableau pour garder les accurancy finale
trainAcc = []
testAcc = []

# on boucle l'algorithme pour les différents valeurs
for k in nbrNeighbors:

    #Créer un classifieur à base de l’algorithme Nearest Neighbors
    clf5 = neighbors.KNeighborsClassifier(n_neighbors=k)
    
    #Appliquer le classifieur sur l’ensemble de données
    clf5.fit(data_train_x, data_train_y)
    
    #appliquer le classifieur résultant sur les data test/train ( on teste aussi sure les meme data utilise pour train)
    predTrainY = clf5.predict(data_train_x)
    predTestY = clf5.predict(data_test_x)

    # calculer la Précision
    trainAcc.append(accuracy_score(data_train_y, predTrainY))
    testAcc.append(accuracy_score(data_test_y, predTestY))

# %% [markdown]
# afficher les resultats(la Précision) sur graph pour mieux compare la resultats de predicition ( pour les data teste et data train)

# %%
plt.plot(nbrNeighbors, trainAcc, 'ro-', nbrNeighbors,
testAcc,'bv--')
plt.legend(['Training Accuracy','Test Accuracy'])
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')
plt.show()


