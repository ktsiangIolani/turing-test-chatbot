import pandas as pd
import math
import numpy as np

train = pd.read_csv("pushups_vs_muscle.csv")

import plotly.express as px


fig = px.line(train, x="weekly_hrs_training", y="lean_muscle_pct", title='Pushups vs Muscle')
fig.show()