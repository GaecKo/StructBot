# StructBot
*****
### Présentation

**StructBot** est un **bot discord** ayant pour but de *simplifier* et d'*automatiser* la vie des différents membres d'un staff e-sport.
****

## Status
Avancée:
   ▰▰▰▰▰▰▰▰▱▱ 80%

Le bot s'oppère autour de différents points:
* [X] Fonction annexes inutiles :)

* [X] Création facile de **statistique** 
    * [X] Ratio Win / Loose 
    * [X] Ration Mort / Kill

* [ ] L'ajout **d'évènements éffectués**
    * retour chaque semaine des activités

* [ ] L'ajout **d'évènements à venir**
    * [X] Ajout de rappels, avec des tags 
    * [X] Tout cela peut se configurer
    * [ ] Ajout d'un choix de channel où envoyer le message

* [X] Quelques citations :)
* [ ] Autres idées à venir
****

## Choix
* Les stats personnalisées seront ajoutées en fonction de chaque structure
* Le retour imagé ne sera sans doute pas fait dans un premier temps
* Une grosse partie du travail doit être adapté aux besoins de chaques structures.
* Certaines commandes seront améliorées afin de mieux remplir le besoin 
****

## Fonctionnement général
* Le bot utilise discord.ext pour fonctionner. Celui ci est utile grâce à ses fonctions du genre:
```py
@bot.command(name='nom_commande')
async def nom_commande(ctx, *, msg):
    # ctx étant le context (channel, id, user, ...)
    # msg est le message en tant que tel à partir de la commande
    # ....
    # ....
```
* Le bot se base aussi sur des bot.event:
```py
@bot.event
async def on_ready():
    # s'active quand le bot est prêt
    # ...
    # ...

# ou encore:

@bot.event
async def on_message(msg):
    # s'active quand un message est envoyé sur discord
    # ...
    # ...
```
* Ensuite, en fonction des commandes, contenu du message, ... certaines actions sont éffectués, pour comprendre ces fonctions, il faut se référer dans le code directement. 
* Les fichiers JSON sont utilisés comme première approche, mais sera remplacé par la suite par sécurité
****

## Hébergement
* Afin d'héberger le bot, et pour des raisons financières, repl.it est utilisé avec un keep_alive afin que le bot ne s'arrête jamais. Ceci est une solution temporaire
****
