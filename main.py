import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# MANIPULACION Y ANALISIS DE DATOS /// DATA MANIPULATION AND ANALYSIS

# Usaremos los siguientes cuatro archivos csv para nuestro analisis por lo que los convertimos en dataframe y los
# asignamos a una variable

# We'll use the following four files for our analysis so we'll convert them into a pandas dataframe and assign them to a
# variable

daily_activity = pd.read_csv("dailyActivity_merged.csv")
hourly_calories = pd.read_csv("hourlyCalories_merged.csv")
daily_sleep = pd.read_csv("sleepDay_merged.csv")
weight = pd.read_csv("weightLogInfo_merged.csv")

# Esta funcion da informacion basica acerca del dataframe
# This function gives basic info about a dataframe

def basic_info (dataframe):
    print(dataframe.head(5))
    print(dataframe.columns)
    print(dataframe.describe())
    dataframe.info()

# La siguiente funcion agrupa todos los datos de un dataframe en base a una columna especifica
# The following function groups all data of a dataframe by a specific column

def Group_Fast (dataframe, column_to_group, columns_to_show, operation):
    if columns_to_show == False:
        if operation == "count":
            finalname = dataframe.groupby(str(column_to_group)).count()
        elif operation == "sum":
            finalname = dataframe.groupby(str(column_to_group)).sum()
        elif operation == "mean":
            finalname = dataframe.groupby(str(column_to_group)).mean()
        else:
            print("Operation not supported")
            return
        return finalname
    else:
        if operation == "count":
            finalname = dataframe.groupby(str(column_to_group))[columns_to_show].count()
        elif operation == "sum":
            finalname = dataframe.groupby(str(column_to_group))[columns_to_show].sum()
        elif operation == "mean":
            finalname = dataframe.groupby(str(column_to_group))[columns_to_show].mean()
        else:
            print("Operation not supported")
            return
        finalname = finalname.to_frame(name="Normal_Count")
        finalname["Percentage"] = finalname["Normal_Count"] / finalname["Normal_Count"].sum() * 100
        return finalname

# La siguiente funcion crea una nueva columna condicional que en base a un BMI dice el estado fisico del usuario
# es decir si tiene sobrepeso, peso normal, etc.

# The following function creates new conditional column that depending on a BMI column
# tells the users physical status (Overweight, normal weight, etc.)

def BMI (dataframe, column, name_columns_int, name_columns_string):
    i = 0
    dataframe[str(name_columns_string)] = ""
    dataframe[str(name_columns_int)] = np.nan
    for x in dataframe[str(column)]:
        if x == 0 or np.isnan(x):
            dataframe.at[i, str(name_columns_int)] = np.nan
            dataframe.at[i, str(name_columns_string)] = np.nan
        elif x <= 18.5 and x > 0:
            dataframe.at[i, str(name_columns_int)] = 1
            dataframe.at[i, str(name_columns_string)] = "Underweight"
        elif x <= 24.9 and x >= 18.5:
            dataframe.at[i, str(name_columns_int)] = 2
            dataframe.at[i, str(name_columns_string)] = "Normal Weight"
        elif x <= 29.9 and x >= 25:
            dataframe.at[i, str(name_columns_int)] = 3
            dataframe.at[i, str(name_columns_string)] = "Overweight"
        elif x >= 30:
            dataframe.at[i, str(name_columns_int)] = 4
            dataframe.at[i, str(name_columns_string)] = "Obese"
        i = i + 1
    return dataframe

# Esta funcion crea una columna clasificando las horas de sueno que tiene el usuario
# This function creates a new column classifying the number of hours used by each user to sleep

def hours_sleep (dataframe, column, name_columns_string):
    i = 0
    dataframe[str(name_columns_string)] = ""
    for x in dataframe[str(column)]:
        if x == 0 or np.isnan(x):
            dataframe.at[i, str(name_columns_string)] = np.nan
        elif x <= 300 and x > 0:
            dataframe.at[i, str(name_columns_string)] = "1-5"
        elif x <= 480 and x >= 300.1:
            dataframe.at[i, str(name_columns_string)] = "5.1-8"
        elif x >= 480.1:
            dataframe.at[i, str(name_columns_string)] = "8- "
        i = i + 1
    return dataframe

# Para facilidad de uso renombramos la columna "SleepDay" de el archivo de habitos de sueno
# For easiness of use we rename the "SleepDay" column of the sleep habits file

daily_sleep = daily_sleep.rename(columns={"SleepDay":"ActivityDate"})

# Las columnas de las fechas que deberian ser de tiempo y fecha no son detectadas como tal por lo que las cambiamos
# The date columns are detected like objects when they should be datetime so we change those columns

daily_activity["ActivityDate"] = pd.to_datetime(daily_activity["ActivityDate"])
daily_sleep["ActivityDate"] = pd.to_datetime(daily_sleep["ActivityDate"])

# Ahora unimos dos archivos para tener toda la data en un solo archivo
# Now we join two files to have all data in only one file

daily_activity = pd.merge(daily_activity, daily_sleep, how="outer", on=["Id", "ActivityDate"])

# Creamos una columna nueva que indica el dia de la semana en letras
# We create a new column that indicates the day of the week in letters

daily_activity["day_of_week"] = daily_activity["ActivityDate"].dt.day_name()

# Ahora modificamos y unimos el archivo de peso con el dataframe "daily_activity"
# Now we modify and merger the weight file with the "daily_activity" dataframe

weight = Group_Fast(weight, "Id", "BMI", "mean")
daily_activity = pd.merge(daily_activity, weight, how="outer", on="Id")

# Vamos a agrupar nuestra data para que muestre el promedio de los registros de cada usuario y lo vamos a asignar a una
# nueva varable

# Now we'll group our dataframes by the "Id" column so that it show the average of all data on a particular user

grouped_daily_activity = Group_Fast(daily_activity, "Id", False, "mean")
grouped_hourly_calories = Group_Fast(hourly_calories, "Id", False, "mean")


daily_activity = daily_activity.reset_index()
grouped_daily_activity = grouped_daily_activity.reset_index()

# Ahora usaremos la funcion BMI para crear una columna que indique el estado fisico del usuario
# Now we'll use the BMI function to create a new column that indicates the physical state of the user

daily_activity = BMI(daily_activity, "Normal_Count", "BMI", "BMI_String")
grouped_daily_activity = BMI(grouped_daily_activity, "Normal_Count", "BMI", "BMI_String")

# Creamos una nueva columna que clasifica el numero de horas de sueno del usuario
# We create a new conditional column that classifies the number of hours used by each user to sleep

daily_activity = hours_sleep(daily_activity, "TotalMinutesAsleep", "HoursRange")
grouped_daily_activity = hours_sleep(grouped_daily_activity, "TotalMinutesAsleep", "HoursRange")

# REPRESENTACION GRAFICA DE LOS DATOS /// DATA GRAPHING

# Nuestro primer grafico mostrara el estado fisico de los usuarios
# Our first graph will show the users physical state

sns.color_palette()
sns.countplot(x="BMI_String", data=grouped_daily_activity,
              order=grouped_daily_activity["BMI_String"].value_counts().index)
plt.show()

# En este segundo grafico vamos a mostrar la cantidad de usuarios que entra en cada rango de horas dormidas
# In this second graph we are gonna show the number of user that enters in each hours slept range

sns.countplot(x="HoursRange", data=grouped_daily_activity,
              order=grouped_daily_activity["HoursRange"].value_counts().index)
plt.show()

daily_activity = daily_activity.drop(["index"], axis=1)

# Ahora vamos a modificar la data para luego graficarla mostrando la relacion entre las variables con el metodo de
# correlacion pearson

# Now we are gonna modify the data to then graph it showing the relation between the variable using the pearson method

correlation = daily_activity.drop(["Id", "Percentage"], axis=1)
correlation = correlation.corr()
correlation1 = grouped_daily_activity.drop(["Id", "Percentage"], axis=1)
correlation1 = grouped_daily_activity.corr()


rer = sns.heatmap(data=correlation, annot=True, cmap="Blues")
rer.figure.tight_layout()
plt.show()

rer1 = sns.heatmap(data=correlation1, annot=True, cmap="Blues")
rer1.figure.tight_layout()
plt.show()

# Con el siguiente grafico vamos a mostrar la cantidad de calorias quemadas para cada dia de la semana
# With the following graph we are gonna show the amount of calories burned by each day of the week

sns.barplot(x=daily_activity.day_of_week, y=daily_activity.Calories, ci=None)
plt.show()

# Ahora vamos a modificar la data para luego graficarla mostrando la cantidad de minutos de entrenamiento para cada dia
# de la semana

# Now we are gonna modify and graph the data to show the amount of minutes spent in training by each day of the week

Veryactivesweek = Group_Fast(daily_activity, "day_of_week", "VeryActiveMinutes", "mean")
Fairlyactiveweek = Group_Fast(daily_activity, "day_of_week", "FairlyActiveMinutes", "mean")

veryactiveminutes = sns.barplot(x=daily_activity.day_of_week, y=daily_activity.VeryActiveMinutes, label="veryactiveminutes", color="green", ci=None)
fairlyactiveminutes = sns.barplot(x=daily_activity.day_of_week, y=daily_activity.FairlyActiveMinutes, label="fairlyactiveminutes", color="red", ci=None)
plt.legend(ncol=2, loc="upper right", frameon=True)
plt.show()

veryactiveminutes1 = sns.barplot(x=daily_activity.day_of_week, y=daily_activity.VeryActiveMinutes, label="veryactiveminutes", color="green", ci=None)
plt.show()
fairlyactiveminutes1 = sns.barplot(x=daily_activity.day_of_week, y=daily_activity.FairlyActiveMinutes, label="fairlyactiveminutes", color="red", ci=None)
plt.show()

# Ahora vamos a modificar la data para luego graficarla mostrando la cantidad de calorias quemada por cada hora del dia
# Now we are gonna modify and graph the data to show the amount of calories burned for each hour of the day

hourly_calories["ActivityHour"] = pd.to_datetime(hourly_calories["ActivityHour"])
hourly_calories["Hour"] = hourly_calories["ActivityHour"].dt.hour

hourly_calories = Group_Fast(hourly_calories, "Hour", False, "mean")
plt.plot(hourly_calories.index, hourly_calories.Calories, marker='o', c='b')
plt.xlabel('Hour')
plt.ylabel('Calories')
plt.show()

bmi_help = Group_Fast(grouped_daily_activity, "BMI_String", False, "mean")
bmi_help.to_csv("bmi_grouped.csv")

