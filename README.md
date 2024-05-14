# This Vue application is deployed at this ec2 aws address:
http://ec2-51-20-9-64.eu-north-1.compute.amazonaws.com:8080/

![alt text](http://ec2-51-20-9-64.eu-north-1.compute.amazonaws.com:8080/src/images/architecture_project.jpg?t=1715612450630)

# Projet Django pour Backend de Mini-Jeu sur les Noms Celtiques

Ce projet Django est conçu pour fournir un backend permettant d'exposer des endpoints pour récupérer des listes de noms communs et de noms propres, ainsi que des données nécessaires pour un mini-jeu basé sur les noms d'origine celtique.

*******

## L'application expose les endpoints suivants :

GET /wordStems/ : Récupère une liste de noms communs d'origine celtique.
GET /properNouns/ : Récupère une liste de noms propres d'origine celtique.
GET /sessionGameData/ : Endpoint pour le mini-jeu basé sur les noms celtiques.

*******