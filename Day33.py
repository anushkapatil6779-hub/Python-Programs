#count plot
import seaborn as sns
import matplotlib.pyplot as plt

#build in data sets avaible already
data=sns.get_dataset_names()
print(data)

#load the dataset of pengunis from this list
penguins=sns.load_dataset("penguins")
print(penguins)

sns.countplot(data=penguins,x="species",hue="island")
plt.show()

'''
#boxplot
sns.boxplot(data=penguins,x="species",y="body_mass_g",hue="island")
plt.show()

#violen plot
sns.violinplot(data=penguins,x="species",y="body_mass_g",hue="island")
plt.show()

#violen plot by using swarm plot
sns.violinplot(data=penguins,x="species",y="body_mass_g",hue="island",palette="pastel")
sns.swarmplot(data=penguins,x="species",y="body_mass_g",hue="island",size=2)
plt.show()

#KDE plot (to use similar density representation)
sns.kdeplot(data=penguins,x="body_mass_g",hue="species",palette="pastel")
plt.show()

sns.kdeplot(data=penguins,x="body_mass_g",hue="species",palette="pastel",fill=True)
sns.despine()
plt.show()


#find corelation between 2 coloumns
columns=["bill_length_mm","flipper_length_mm","body_mass_g"]
corelation=penguins[columns].corr()
print(corelation)

#heatmap
sns.heatmap(data=penguins[columns].corr())
plt.show()

#heatmap add functions annot and cmap
sns.heatmap(data=penguins[columns].corr(),annot=True,cmap="Blues")
plt.show()

#rug plot
sns.rugplot(data=penguins,x="body_mass_g",y="species",palette="Set2")
plt.show()

#rug plot adding 3rd element like hue
sns.rugplot(data=penguins,y="body_mass_g",hue="species",palette="Set2")
plt.show()

#rug plot by adding height function
sns.rugplot(data=penguins,y="body_mass_g",hue="species",palette="Set2",height=0.2)
plt.show()
'''
#pair plot
sns.pairplot(data=penguins)
plt.show()

sns.pairplot(data=penguins,hue="species",palette="Set2",diag_kind="hist")
plt.show()

graph=sns.pairplot(data=penguins,hue="species",palette="Set2")
graph.map_upper(sns.scatterplot)
graph.map_lower(sns.kdeplot)
graph.map_diag(sns.histplot)
graph.add_legend()
plt.show()

































