## ---- Import libraries -------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## ---- Read-in data -----------------------------------------------------------
new_df = pd.read_excel(
    io="data/(1.2) dataset_principal.xls",
    sheet_name="Planilha1"
)

### Check column names ----
new_df.columns

### Check the first 5 rows (head) and last 10 rows ----
new_df.head(n=10)
new_df.tail(n=10)

### Get details about the dataset ----
new_df.info()

## ---- Changing variable's name -----------------------------------------------

### Renaming using variables names ----
new_df2 = new_df.rename(
    columns={
        "Estudante": "estudante",
        "Tempo para chegar à escola (minutos)": "tempo",
        "Distância percorrida até a escola (quilômetros)": "distancia",
        "Quantidade de semáforos": "semaforos",
        "Período do dia": "period",
        "Perfil ao volante": "perfil"
    }
)

### Renaming using variables positon in the data frame ----
new_df3 = new_df2.rename(
    columns={
        new_df2.columns[0]: "student",
        new_df2.columns[1]: "time",
        new_df2.columns[2]: "distance",
        new_df2.columns[3]: "traffic-lights"
    }
)

## ---- Selecting variables and values -----------------------------------------

### Subsetting by variable's name ----
new_df3[["distance", "time"]]

### Subsetting by position's name ----
new_df3.iloc[:, [0, 3]]
new_df3.iloc[:, 0:4]

### Selecting variables based on common init ----
new_df3.loc[
    :, new_df3\
        .columns\
            .str\
                .startswith(pat="dis")
]

new_df3.loc[
    :, new_df3\
        .columns\
            .str\
                .endswith("ce")
]

### Selecting rows ----
new_df3.iloc[0:4:,]

### Selecting variables by dropping unwanted ----
new_df3.drop(
    columns=new_df3.iloc[:, 0:2], 
    inplace=True
)

### Changing variable's values ----
conditions = np.where((new_df3.distance) < 10, "near",
    np.where(new_df3["traffic-lights"]) == 2, "do not pass ❌", "OK")

np.where(new_df3.distance < 20, new_df3.distance *2, "😅")
