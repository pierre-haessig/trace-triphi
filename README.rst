==================
Graphique triphasé
==================

Petit script qui trace le graphique d'un système de tensions triphasé sinusoïdal
sur une période réglable.
La dénomination des tensions est réglable (Va, Vb, Vc), (V1, V2, V3), etc...

Option bonus : tracé de la tension redressée triphasée par un pont redresseur
 * redresseur à 6 thyristors, avec angle de retard à l'amorçage ψ
 * redresseur à 6 diode, (en réglant ψ = 0°)

Domaine d'application de ce script : génie électrique
 * réseau triphasé
 * redresseurs en pont
 
Utilisations de ce script :
 1. tel quel
 2. modifier les paramètres à la section "Paramètres réglables"
 3. modifier le script (cf licence)

Prérequis
---------
Testé sous Python 2.6

Modules Python nécessaire :
 * numpy
 * matplotlib


Licence
-------
ce script petit est sous licence BSD (cf. Wikipedia ou autre)
il est librement utilisable et modifiable
Copyright © Pierre Haessig, septembre 2011
