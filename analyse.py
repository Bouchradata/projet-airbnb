
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('airbnb-listings.csv',sep=";", low_memory=False)
print(df.shape,"\n")
print(df.head(),"\n")
print(df.columns,"\n")
df['Price']=pd.to_numeric(df['Price'], errors='coerce')


#prix moyen de toutes les annonces mondiales
prix_moyen=df['Price'].mean()
print(f"prix_moyen: {prix_moyen:.2f}€","\n")


#prix moyen par pays
prix_moyens_par_pays=df.groupby('Country')['Price'].mean().sort_values (ascending=True)
print(prix_moyens_par_pays,"\n")


#graphique  prix moyen par pays
prix_moyens_par_pays.plot(kind='barh')
plt.title("PRIX MOYEN PAR PAYS",
          fontsize=15,
          fontweight='bold',
          color= 'green')
plt.xticks(range(0,650,20))
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#top 10 pays avec le plus annonce
top_pays_count=df['Country'].value_counts().head(10)
top_pays = top_pays_count.index.tolist()
print(top_pays_count,"\n")

#prix moyen des 10 villes des 10 pays meilleures annonces

df_top_pays = df[df['Country'].isin(top_pays)]
top_villes=(df_top_pays.groupby(['Country','City'])
            .agg(prix_moyen=('Price','mean'),
            nb_annonce=('Price','count'))
            .sort_values(by='prix_moyen',ascending=False)
            .head(10))

#graphique des top des villes
top_villes=top_villes.sort_values(by='prix_moyen')
top_villes['prix_moyen'].plot(kind='barh',figsize =(10,6))

for index,value in enumerate(top_villes['prix_moyen']):
    nb = top_villes ['nb_annonce'].iloc[index]
    plt.text(value + 0.3, index,
         f'{value :.1f}€ ({nb} annonces)',
         va='center')
plt.xlim(140,160)
plt.title("PRIX MOYEN PAR VILLE",
          fontsize=16,
          fontweight='bold',
          color='purple')
plt.tight_layout()
plt.show()

#prix par type de logement
prix_par_type= df[df['Room Type'] != '9'].groupby('Room Type')['Price'].mean().sort_values(ascending=False)
print(prix_par_type, "\n")


#graphique Top 10 des pays avec le plus d'annonce
top_pays_count.plot(kind='barh')

plt.title("Top 10 des pays avec le plus d'annonces Airbnb",
          fontsize=15,
          fontweight='bold',
          color='purple')
plt.xlabel("Nombre d'annonce")
plt.tight_layout()
plt.show()

#graphique prix par catégorie de logement
prix_par_type.plot(kind='barh')
plt.xlabel("prix")
plt.title("Prix par catégorie de logement",
          fontsize=15,
          fontweight='bold',
          color='red')
plt.show()


