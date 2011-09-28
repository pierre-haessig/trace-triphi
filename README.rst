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
 1. tel quel (permet d'obtenir un résultat tel que `graph_tension_triphase_exemple.png`)
 2. modifier les paramètres à la section "Paramètres réglables"
 3. modifier le script (cf licence)

Pour l'utiliser
---------------
Ce script a été testé avec Python 2.6, sous Linux

Modules Python nécessaires :
 * numpy
 * matplotlib

Source : ce script est hébergé sur github : https://github.com/pierre-haessig/trace-triphi

Remarque : ce script a été placé sur github en grande partie pour tester github...

Licence
-------
Ce script petit est sous licence BSD (cf. Wikipedia ou autre).
il est librement utilisable et modifiable

Copyright © Pierre Haessig, septembre 2011
