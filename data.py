import pandas as pd
import numpy as np


# Données
data1 = pd.read_csv('2021-01-22_deces_parsexe_age_jour_France.csv', sep=';')
# Transformation des dates de type string en type date
data1["Date_evenement"] = pd.to_datetime(data1["Date_evenement"], format="%d/%m/%Y")
data_eve = data1["Date_evenement"]


# Données des femmes selon les âges
f_m_24 = data1["Femmes_0_24ans_Deces2020"]
f_25_49 = data1["Femmes_25_49ans_Deces2020"]
f_50_64 = data1["Femmes_50_64ans_Deces2020"]
f_65_74 = data1["Femmes_65_74ans_Deces2020"]
f_75_84 = data1["Femmes_75_84ans_Deces2020"]
f_85 = data1["Femmes_85ans_plus_Deces2020"]

# Données de la mortalité totale des femmes selon âge
f_m_24_M = f_m_24.max()
f_25_49_M = f_25_49.max()
f_50_64_M = f_50_64.max()
f_65_74_M = f_65_74.max()
f_75_84_M = f_75_84.max()
f_85_M = f_85.max()


# Données des hommes selon les âges
h_m_24 = data1["Hommes_0_24ans_Deces2020"]
h_25_49 = data1["Hommes_25_49ans_Deces2020"]
h_50_64 = data1["Hommes_50_64ans_Deces2020"]
h_65_74 = data1["Hommes_65_74ans_Deces2018"]
h_75_84 = data1["Hommes_75_84ans_Deces2018"]
h_85 = data1["Hommes_85ans_plus_Deces2018"]

# Données de la mortalité des hommes selon les âges
h_m_24_M = h_m_24.max()
h_25_49_M = h_25_49.max()
h_50_64_M = h_50_64.max()
h_65_74_M = h_65_74.max()
h_75_84_M = h_75_84.max()
h_85_M = h_85.max()



# Données préparés pour la figure bar
df = pd.DataFrame({
    "Age": ["0-24", "0-24", "25-49", "25-49", "50-64", "50-64", "65-74", "65-74", "75-84", "75-84", "85-plus",
            "85-plus"],
    "Nombre de morts": [h_m_24_M, f_m_24_M, h_25_49_M, f_25_49_M, h_50_64_M, f_50_64_M, h_65_74_M, f_65_74_M, h_75_84_M,
                        f_75_84_M, h_85_M, f_85_M],
    "Genre": ["Hommes", "Femmes", "Hommes", "Femmes", "Hommes", "Femmes", "Hommes", "Femmes", "Hommes", "Femmes",
              "Hommes", "Femmes", ]
})

# Données du total de décès selon les âges pour la fiugre Pie
T_m_24 = h_m_24_M + f_m_24_M
T_25_49 = h_25_49_M + f_25_49_M
T_50_64 = h_50_64_M + f_50_64_M
T_65_74 = h_65_74_M + f_65_74_M
T_75_84 = h_75_84_M + f_75_84_M
T_85 = f_85_M + h_85_M
list2 = ["0-24-ans", "25-49-ans", "50-64-ans", "65-74-ans", "75-84-ans", "85-plus"]
list1 = [list2, [T_m_24, T_25_49, T_50_64, T_65_74, T_75_84, T_85]]
# Redimensionnement de la liste : 2 colomnes et 6 features
list1 = np.reshape(list1, (2, 6)).T
df2 = pd.DataFrame(list1, columns=["Age", "Total"])