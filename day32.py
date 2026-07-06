import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#build in data sets avaible already
data=sns.get_dataset_names()
print(data)

#load the dataset of pengunis from this list
penguins=sns.load_dataset("penguins")
print(penguins)


#histogram
sns.set_context("notebook")
sns.set_style("white")
sns.histplot(data=penguins,x="body_mass_g")
plt.show()

             
#istogram but by using 3rd function like hue
sns.histplot(data=penguins,x="body_mass_g",hue="species")
plt.show()

#
sns.histplot(data=penguins,x="body_mass_g",hue="species",multiple="stack")
plt.show()


#regration graph
sns.regplot(data=penguins,x="body_mass_g",y="flipper_length_mm",color="blue")
plt.show()

#line plot
sns.lineplot(data=penguins,x="body_mass_g",y="flipper_length_mm")
plt.show()

#
sns.set_style("whitegrid")
sns.lineplot(data=penguins,x="body_mass_g",y="flipper_length_mm",hue="species")
plt.show()

#
sns.set_style("whitegrid")
sns.lineplot(data=penguins,x="body_mass_g",y="flipper_length_mm",hue="species",style="island")
plt.show()


#joint plot
sns.jointplot(data=penguins,x="body_mass_g",y="flipper_length_mm")
plt.show()

#by adding 3rd function
sns.jointplot(data=penguins,x="body_mass_g",y="flipper_length_mm",hue="species")
plt.show()

#by using kind function
sns.jointplot(data=penguins,x="flipper_length_mm",y="body_mass_g",hue="species",kind="kde")
plt.show()

#hist
sns.jointplot(data=penguins,x="body_mass_g",y="flipper_length_mm",hue="species",kind="hist")
plt.show()

#scatter
sns.jointplot(data=penguins,x="flipper_length_mm",y="body_mass_g",hue="species",kind="scatter")
plt.show()


#bar plot
sns.barplot(data=penguins,x="species",y="body_mass_g",hue="island",palette="Set1")
plt.show()

sns.barplot(data=penguins,x="species",y="body_mass_g",hue="island",palette="Set1",estimator=np.median)
plt.show()


sns.barplot(data=penguins,x="species",y="body_mass_g",hue="island",palette="Set1",estimator=np.std)
plt.show()



