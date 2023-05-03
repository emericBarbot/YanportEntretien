import pandas


dataImmo = pandas.read_csv('Dataset - Ads _ Levallois-Perret - 2019-08 - export-ads-levallois-perret-2019-08-27.csv')
dataImmoV2 = pandas.DataFrame(columns=dataImmo.columns)



# j'itere chaque annonce
for index, row in dataImmo.iterrows():
    # Regarder si l'annonce porte sur le même bien immobilier qu'une annonce déjà enregistrée dans dataImmoV2
    NumColonneSimilaire = dataImmoV2.loc[(dataImmoV2['SURFACE'] == row['SURFACE']) &
                             (dataImmoV2['PRICE'] == row['PRICE']) &
                             (dataImmoV2['PROPERTY_TYPE'] == row['PROPERTY_TYPE'])   ]
    

    if not NumColonneSimilaire.empty:
        # Le bien existe déjà dans dataImmoV2 => On ajoute le lien de l'annonce et le nom du site dans le bien déjà existant dans dataImmoV2
        dataImmoV2.loc[NumColonneSimilaire.index, 'URL'] += '; ' + row['URL']
        dataImmoV2.loc[NumColonneSimilaire.index, 'CRAWL_SOURCE'] += '; ' + row['CRAWL_SOURCE']


    else:
        # Le bien n'existe pas déjà dans dataImmoV2 => On ajoute la colonne du bien à dataImmoV2
        dataImmoV2 = pandas.concat([dataImmoV2, row.to_frame().T], ignore_index=True)


dataImmoV2.to_csv('DatasetModifié.csv', index=False)

