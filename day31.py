import seaborn as sns
import matplotlib.pyplot as plt

#build in data sets avaible already
data=sns.get_dataset_names()
print(data)

#load the dataset of pengunis from this list
penguins=sns.load_dataset("penguins")
print(penguins)

#perform EDA on penguins dataset
print(penguins.head())
print(penguins.tail())
print(penguins.shape)
print(penguins.size)
print(penguins.ndim)
print(penguins.info)


#display the graph of penguins dataset

sns.set_style("dark") #"ticks","darkgrid","dark","whitegrid","white"
#this both syntaxs used for designs graphs 
sns.set_context("paper")#notebook,poster,talk

#by using palette we can give color for this graph
sns.set_palette("Set1") #Set2,Set3,deep,muted,bright,pastel
sns.scatterplot(data=penguins,x="species",y="body_mass_g",hue="island",style="bill_length_mm",alpha=0.1)

plt.show()

#strip plot

sns.stripplot(data=penguins,x="species",y="body_mass_g",hue="island",dodge=True,jitter=True)
plt.show()


#swarm plot
sns.swarmplot(data=penguins,x="species",y="body_mass_g",hue="island")
plt.show()
