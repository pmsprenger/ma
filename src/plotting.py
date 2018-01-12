import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'serif','sans-serif':['Computer Modern Roman']})
rc('text', usetex=True)

# Add list of lists with data.
data = []

df = pd.DataFrame(data)
df = df.transpose()
df.columns = ['Bible 50', 'Bible 100', 'Bible 200', 'UN 50', 'UN 100', 'UN 200', 'TED 50', 'TED 100', 'TED 200']

df = pd.DataFrame(df, columns=['Bible 50', 'Bible 100', 'Bible 200', 'UN 50', 'UN 100', 'UN 200', 'TED 50', 'TED 100', 'TED 200'])

fig = plt.figure()

#ax = fig.add_subplot(111)

df.boxplot()#, showbox=False, showcaps=False)

ax = fig.add_subplot(111)
ax.grid(False)

ax.set_xticklabels(['Bible\nk=50', 'Bible\nk=100', 'Bible\nk=200', 'UN\nk=50', 'UN\nk=100', 'UN\nk=200', 'TED\nk=50', 'TED\nk=100', 'TED\nk=200'])

ax.set_ylabel("Amount of root repetitions per topic", rotation='vertical')

#ax.set_yscale('log')
#ax.set_xlabel("k = topics")
#ax.set_title("The three Data Sets")

fig.savefig('plot.png')#, bbox_inches='tight')
#plt.show()
