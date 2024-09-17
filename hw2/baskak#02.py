#!/usr/bin/env python
# coding: utf-8

# In[48]:


import matplotlib as plt
import numpy as np
import pandas as pd

bars_length = np.random.randint(-10, 10, 10)
bars_length.sort()



index = ['label num {}'.format(i) for i in range(10)]


df = pd.DataFrame({'bars_length': bars_length}, index=index)
ax = df.plot.barh()


# In[82]:


import matplotlib.pyplot as plt
import numpy as np





plt.rcdefaults()
fig, ax = plt.subplots()


index = ['label num {}'.format(i) for i in range(10)]
bars_length = np.random.randint(-10, 10, 10)
bars_length.sort()
# Example data

y_pos = bars_length
performance = (-10)
error = np.random.rand(len(index))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(index)
ax.invert_yaxis()  #

ax.set_title('smth')

plt.show()


# In[111]:


import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import numpy as np
import pandas as pd

ncols = 10
figsize = (20, 10)
fontsize = 14

dti = pd.date_range('2015-01-01', '2021-3-16', freq='2W')
probabilities_in_time = np.random.random((ncols, len(dti)))
probabilities_in_time = probabilities_in_time /     probabilities_in_time.sum(axis=0)
probabilities_in_time = pd.DataFrame(probabilities_in_time).T
probabilities_in_time.index = dti

cm_subsection = np.linspace(0, 1, ncols)
colors = [cm.coolwarm(x) for x in cm_subsection]


def plot_time_probabilities(probabilities_in_time, figsize):
    plt.figure(figsize=figsize)
    plt.yticks(np.arange(0, 1.2, 0.2), fontsize=fontsize)
    plt.xticks(fontsize=fontsize)

    draw_stack_plot(colors, probabilities_in_time)
    set_grid()
    set_legend()

    plt.show()


def draw_stack_plot(colors, probabilities_in_time):
    for i, color in enumerate(colors):
        if i == 0:
            plt.plot(probabilities_in_time[i], color=color)
            plt.fill_between(probabilities_in_time.index,
                             probabilities_in_time[0], color=color)

        else:
            probabilities_in_time[i] += probabilities_in_time[i-1]
            plt.fill_between(probabilities_in_time.index,
                             probabilities_in_time[i], probabilities_in_time[i-1],
                             color=color)

        plt.plot(probabilities_in_time[i], label=' Probability: {}'.format(
            i), color=color)


def set_grid():
    ax = plt.gca()
    ax.set_axisbelow(False)
    ax.xaxis.grid(True, linestyle='-', lw=1)


def set_legend():
    leg = plt.legend(loc='lower left', fontsize=14, handlelength=1.3)
    for i in leg.legendHandles:
        i.set_linewidth(12)


plot_time_probabilities(probabilities_in_time, figsize)


# In[182]:




import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

index=pd.date_range('2020-02-01', '2020-04-01', freq='D').strftime('%D')
time=pd.date_range('09:00:00', '19:00:001', freq='H').strftime('%H:%M:%S')

defenition=[]
stroka=[]
for i in time:
    for i in time:
        stroka.append(np.random.random((  100, 100)))
    defenition.append(stroka)
    stroka=[]
fig, ax = plt.subplots()
#im = ax.imshow(defenition)

# We want to show all ticks...
ax.set_xticks(np.arange(len(index)))
ax.set_yticks(np.arange(len(time)))
# ... and label them with the respective list entries
ax.set_xticklabels(index)
ax.set_yticklabels(time)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
for i in range(len(time)):
    for j in range(len(index)):
        text = ax.text( defenition[i, j])

fig.tight_layout()
plt.show()

    


# In[185]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
defenition=[]
stroka=[]
for i in time:
    for i in time:
        stroka.append(np.random.random((  100, 100)))
    defenition.append(stroka)
    stroka=[]
print (defenition)

