# Bienvenue sur la page explicative de Pytact
Pour commencer Pytact est un logiciel python connecté a une base de donnée SQLite visant a gérer vos contacts, un peu comme sur votre téléphone
# 1. L'utilisation en ligne de commande
Cette première partie expliquera comment utiliser certaines commandes sans passer par le menu interactif
## 1.1 Créer de nouveaux contacts
Pour ajouter un nouveau contact il faut taper "**python3 contact.py new**", vous serez ensuite invité a donner les informations concernant votre contact. Attention, vous devez respecter un certain format pour le mail et le numéro de téléphone( mail : test@test.com / téléphone : 0X-XX-XX-XX-XX) sinon cela vous demandera le numéro de téléphone et le mail en boucle.
[Exemple ci-dessous](https://drive.google.com/file/d/1uoLcEpJQY1dE95v4HijWQPdxSeXcSpBO/view?usp=share_link)
## 1.2 Afficher tout les contacts
Afin d'afficher tous vos contacts, vous devez tapez la commande "**python3 contact.py list**"
La liste de contact apparaitra sous [cette forme](https://drive.google.com/file/d/1QdIQDhQUEk3_FLWAIyTD5CfkwIc30ebq/view?usp=share_link)
## 1.3 Rechercher un contact
Afin d'utiliser la fonction search, il faut utiliser cette syntaxe "**python3 contact.py search <méthode> <valeur recherchée>**".
Cette fonction comporte 6 méthodes de recherches :
1)"**--by-name**" permet de faire une recherche grâce au nom du contact
2)"**--by-firstname**" permet de faire une recherche grâce au prénom du contact
3)"**--by-nickname**" permet de faire une recherche grâce au surnom du contact
4)"**--by-email**" permet de faire une recherche grâce a l'adresse Email du contact
5)"**--by-tel**" permet de faire une recherche grâce au numéro de téléphone du contact
6)"**--by-address**" permet de faire une recherche grâce a l'adresse du contact
[Voici un exemple de la fonction recherche](https://drive.google.com/file/d/1qk0bbx1xBtBldkJrCKn4UyP0h3GfNo5O/view?usp=share_link)
## 1.4 Afficher l'aide
Afin d'afficher l'aide en ligne de commande, tapez "**python3 contact.py ?**", l'aide s'affichera sous cette [forme](https://drive.google.com/file/d/1V2M0fD6tPUwBSB_vRgw8REGTGY_YClUd/view?usp=share_link)
## 1.5 Supprimer un contact
Afin de supprimer un contact, tapez la commande "**python3 contact.py delete**", vous serez inviter a taper TOUTES les informations concernant le contact a supprimer
[La fonction suppression ressemble a cela](https://drive.google.com/file/d/1rf2kUsZlBNvwjZ6hfIvpWMJhlTrgImmq/view?usp=share_link)
## 1.6 Modifier les informations d'un contact
Pour modifier les informations concernant un de vos contacts vous devez taper la commande suivante "**pythopn3 contact.py update**"
Vous serez ensuite inviter a taper le type de donnée a modifier concernant votre contact (Nom, Surnom ou autre) puis la nouvelle donnée.
Pour finir vous devrez renseigner toutes les informations concernant votre contact afin de le modifier
[Cela ressemblera a cela](https://drive.google.com/file/d/10ugvg62o1XrUV0GyHfeGA198oudv4i5_/view?usp=share_link)
# 2. L'utilisation en mode interactif
Le mode interactif permet d'utiliser l'application seulement en appelant le script hôte, une fois actif, toutes les options disponibles en lignes de commandes seront disponible en mode interactif. Pour y entrer, je vous invite à taper "**python3 contact.py**"
Pour quitter le mode interactif, il suffit de taper "**bye**" dans le menu des choix.
 [Le mode interactif s'illustre comme ceci](https://drive.google.com/file/d/1pGnHASMGwTX_9GbFl_3qAXruvKcW41tu/view?usp=share_link)
## 2.1 Créer de nouveaux contacts
Comme vous avez pu le constater, afin de créer de nouveaux contacts, il faut taper "1", je vous invite a lire le chapitre 1.1 car ces deux méthodes sont identiques
## 2.2 Afficher tout les contacts
Comme vous avez pu le constater, afin de lister tous vos contacts, il faut taper "2".
L'application vous retourne ensuite une liste [sous le format suivant](https://drive.google.com/file/d/1QdIQDhQUEk3_FLWAIyTD5CfkwIc30ebq/view?usp=share_link)
## 2.3 Rechercher un contact
Afin de rechercher un contact, le programme vous invite a choisir le type de donnée recherchée (Nom, Prénom ou autre). Ensuite vous êtes invité a entrer ce que vous recherchez
Votre résultat sera donc affiché par la suite
La fonction ressemblera a [cela](https://drive.google.com/file/d/150GBVjAaFj4VjyjUMPWMqyJ9rJJhQuyY/view?usp=share_link)
## 2.4 Afficher l'aide
Afin d'afficher l'aide, taper "4 quand vous êtes invité a le faire
Je vous invite a regarder le chapitre 1.4 car ces deux méthodes sont identiques
## 2.5 Supprimer un contact
Pour supprimer un contact, vous devez taper "5".
Je vous invite par la suite a suivre le chapitre 1.5 car la méthode est la même pour le mode interactif et le mode ligne de commande
## 2.6 Modifier les informations d'un contact
Pour supprimer un contact, vous devez taper "6".
Je vous invite par la suite a suivre le chapitre 1.6 car la méthode est la même pour le mode interactif et le mode ligne de commande
