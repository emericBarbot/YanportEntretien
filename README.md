   	 	Explication de la solution  

  

  	  Stratégie choisie  

  

Tout d’abord, j’ai dû déterminer qu’elles étaient les paramètres qui déterminaient si deux annonces provenaient du même bien.  

Le seul paramètre qui puisse relier un bien à son annonce serait l’adresse postale. Cependant, l’adresse exact ne fait pas partie des paramètres contenus dans la base de données. 

 

J’ai donc cherché une liste de paramètre qui puissent ensemble former une clé primaire. 

J’ai d’abord pensé aux 3 paramètre suivant  

-prix du bien  

-nombres de mètres carrés  

-nom du Vendeur (DEALER_NAME) 

Le problème de prendre le nom du vendeur dans la clé primaire est qu’il s’agit d’une variable string qui donc peut être orthographié différemment pour signifier une même variable.  

En effet, dans le cas du bien de 59m² a 839000 euros donnée en exemple dans la consigne, le vendeur est parfois orthographié “IMAX Levallois-Perret" et parfois “IMAX LEVALLOIS”.  

 

J’ai donc ensuite choisi de garder les paramètres : 

-prix du bien  

-nombre de mètres carrés  

Cependant, j’ai pensé que mettre uniquement ces paramètres ne suffiraient pas car nous risquerions de regrouper des annonces qui ne correspondraient pas au même bien. 

 

J’ai donc ajouté les paramètres supplémentaires : 

-type de propriété  

-parking  

Le problème de prendre parking dans la clé primaire est qu’il s’agit d’un paramètre ambiguë. J’ai remarqué que pour le bien de 59m² a 839000 euros donnée en exemple, il est signalé sans parking sur les sites “Logic-Immo”, “se loger” et “le bon coin “ mais signalé sans parking sur les sites “meilleurs agents” et “A VENDRE A LOUER”. J’ai donc jugé ce paramètre ambiguë et j’ai préféré l’enlever. 

Finalement, ma clé primaire se compose des paramètres suivants : 

-type de propriété  

-prix du bien  

-nombre de mètres carrés 

 

Pour regrouper les annonces entre elles, j’ai simplement ajouté tous les liens et tous les noms de site correspondant à un même bien dans une même ligne. 

 

		Critique 

 

Il est possible que mon algorithme ait regrouper des annonces ne correspond pas au même bien. En effet, si deux biens ont le même prix, le même nombre de mètre carré et le même type de propriété alors ils seront regroupés. 

On aurait pu prendre en compte la variable DEALER_NAME. Il aurait alors fallu utiliser un algorithme qui calcule la similarité entre deux variables string.  

Cependant je pense que les critères que j’ai utilisés sont suffisants et produisent un nombre d’erreur négligeable. 
