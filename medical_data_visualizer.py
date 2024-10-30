import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', sep = ',', header=0, names = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 
                                                                'ap_lo', 'gluc', 'smoke', 'alco', 'active', 'cardio'])

# 2
df['overweight'] = np.where(df['weight']/np.square(df['height']) > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # 6
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    df_cat.columns = ["cardio", "variable", "value", "total"]
    
    # 7
    catplot = sns.catplot(data = df_cat, x = 'variable', y = 'total', hue= 'value', col = 'cardio', kind = 'bar', palette = 'pastel')

    # 8
    fig = catplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
            (df['ap_lo'] <= df['ap_hi']) &
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize = (8, 8))

    # 15

    sns.heatmap(corr, linewidths = 0.5, mask = mask, vmax = 0.4, cmap = 'plasma')

    # 16
    fig.savefig('heatmap.png')
    return fig
