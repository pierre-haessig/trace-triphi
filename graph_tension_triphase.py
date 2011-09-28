#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
==================
Graphique triphasé
==================

Petit script qui trace le graphique d'un système de tensions triphasé sinusoïdal
sur une période réglable.
La dénomination des tensions est réglable (Va, Vb, Vc), (V1, V2, V3), etc...

option bonus : tracé de la tension redressée triphasée par un pont redresseur
 * redresseur à 6 thyristors, avec angle de retard à l'amorçage ψ
 * redresseur à 6 diode, (en réglant ψ = 0°)

Domaine d'application de ce script : génie électrique
 * réseau triphasé
 * redresseurs en pont
 
Utilisations de ce script :
 1. tel quel
 2. modifier les paramètres à la section "Paramètres réglables"
 3. modifier le script (cf licence)

Licence : ce script est sous licence BSD (cf. Wikipedia ou autre)
© Pierre Haessig, septembre 2011
"""

# Import des modules
from __future__ import division
import numpy as np
from numpy import floor, sqrt, pi, sin, cos
import matplotlib.pyplot as plt

################################################
# Paramètres réglables :
# remarque : toutes les phases & angles sont normalisé par 2π (une période a une longueur 1)

theta_min = 0     # phase min sur le graph,
theta_max = 1+1/6 # phase max sur le graph [1 pour une période]
phi0 = 1/4        # phase à l'origine (0 convient très bien, 1/4 pour obtenir des "cosinus")

# Dénomination des tensions :
V_prefix = 'V'
V_labels = ['a', 'b', 'c'] # nom des phases
#V_labels = ['1', '2', '3']

# Bonus : tension redressée triphasée
tension_rectifier = True # activer le tracé, ou non
#tension_rectifier = False
psi_rectifier = 1/12 # angle d'amorçage ψ, à choisir entre 0 et 1/2

### Fin des réglages

################################################
# 2) Calculs :
# vecteur de la phase, en multiple de 2pi
theta = np.linspace(theta_min, theta_max, num=int(500*theta_max))

# 2.1) Tensions simples :
Va = sin(2*pi*(theta + phi0))
Vb = sin(2*pi*(theta + phi0 - 1/3))
Vc = sin(2*pi*(theta + phi0 - 2/3))

# 2.2) Tensions composées :
Vab = Va - Vb
Vbc = Vb - Vc
Vca = Vc - Va

# 2.3) Tension redressées par un pont à thyristor:
indicatrice = floor((theta +phi0 -psi_rectifier)*6 +1/2) % 6
V_rectifier = sqrt(3)*cos(2*pi*(theta+phi0) - pi/3*indicatrice)

# Fonction interne pour la graduation des abscisses :
def smart_frac(phi):
    '''génère une fraction LaTeX de l'angle phi
    Input : angle phi, normalisé par 2pi
    Output: str, contenant la fraction LaTeX correspondante
    
    Exemples :
    >>> smart_frac(0)
    '$0$'
    >>> smart_frac(1/2.)
    '$  \\pi$'
    >>> smart_frac(1)
    '$  2 \\pi$'
    >>> smart_frac(1/6.)
    '$  \\frac{\\pi}{3}$'
    '''
    phi *=2 # phi est maintenant normalisé par pi
    
    ### 1) Extraction de la fraction de phi ###
    # numérateur, dénominateur & signe de la fraction :
    num = None
    den = None
    sgn = None
    
    # helper function
    def is_integer(a, seuil=1e-4):
        '''détermine si le nombre flottant `a` est "à peu près" un entier,
        par rapport à un seuil fixé sur sa partie décimale
        '''
        decimales = abs(a - round(a))
        return decimales <= seuil
    
    for den_test in [1, 2, 3, 6]:
        # on teste différents dénominateurs possibles
        if is_integer(phi*den_test):
            # phi est un multiple de pi
            den = den_test
            num = round(phi*den_test)
            break
    
    # 1.2) Extraction du signe
    if num is not None:
        if num>0:
            sgn = ""
        else:
            sgn = "-"
        num = abs(num)
    
    ### 2) Génération de la chaîne LaTeX ###
    # Cas 0) phi ne se représente par par une fraction en pi :
    if den is None:
        print('Warning, phi=%.2f n\'est pas un multiple de 1/6' % phi)
        return r"$%.2f \pi$" % phi
    
    # Cas phi entier : phi = 0, puis +/-1 puis entier autre
    if den == 1:
        if num == 0:
            return r"$0$"
        elif num == 1: # "π"
            return r"$ %s \pi$" % sgn
        else: # "num π"
            return r"$ %s %d \pi$" % (sgn,num)
    
    else:
        #if num == 1: # "π/den"
        #    return r"$ %s \frac{\pi}{%d}$" % (sgn, den)
        #else: "num/den π"
            return r"$ %s \frac{%d}{%d}\pi$" % (sgn, num, den)
# end smart_frac()

# choix de l'incrément des graduations :
xtick_inc = 1/12 # correspond à π/6
xtick_loc = np.arange(theta_min, theta_max+xtick_inc, xtick_inc)
xtick_lab = [smart_frac(phi) for phi in xtick_loc]

# Étiquettes :
l_simple = [V_prefix + label for label in V_labels]
l_compos  = [V_prefix + label1 + label2
                 for (label1, label2) in zip(V_labels,
                                            V_labels[1:]+[V_labels[0]])
            ]
print(u'Tracé des tensions simples %s' % ', '.join(l_simple))
print(u'et des tensions composées %s ' % ', '.join(l_compos))

if tension_rectifier:
    print(u'et tracé de la tension redressée pour ψ = %.3fπ' % (psi_rectifier*2))

###############################################
# Tracé type 1 : bichromique
# tensions simples et composées
#f = plt.figure(1)
#ax = f.add_subplot(111,
#                   title=u'Système de tensions triphasées sinusoïdales',
#                   xlabel=u'phase θ')
#ax.plot(theta, Va, 'b--', theta, Vb, 'b--', theta, Vc, 'b--')
#ax.plot(theta, Vab,'g:' , theta, Vbc,'g:' , theta, Vca,'g:',  linewidth=2)
#ax.grid(True)
#ax.legend(l_simple + l_compos)
## TODO : ajouter une annotation des tensions par des flèches :
##ax.arrow(0,0, 1,1/2)

#f.show()

###############################################
# Tracé type 2 : quadrichromique
# * tensions simples trichromique (Bleu, Vert, Rouge) + noir
# * tensions composées en pointillé noir
# * tension redressée en noir [optionnel]
f = plt.figure(2)
f.clear()
title = u'Système de tensions triphasées sinusoïdales'
if tension_rectifier:
    title += u', $\psi = ' + smart_frac(psi_rectifier)[1:]
ax = f.add_subplot(111,
                   title=title,
                   xlabel=u'phase θ')
ax.plot(theta, Va, 'b-', theta, Vb, 'g-', theta, Vc, 'r-',  linewidth=2)
ax.plot(theta,  Vab,'k--' , theta,  Vbc,'k--' , theta,  Vca,'k--',
        theta, -Vab,'k--' , theta, -Vbc,'k--' , theta, -Vca,'k--',  linewidth=1)
if tension_rectifier:
    ax.plot(theta, V_rectifier, 'k-', linewidth=2)
ax.grid(True)
ax.legend(l_simple, loc='lower right')
# Légende des  abcisses avec les 'pi' :
ax.set_xticks(xtick_loc)
ax.set_xticklabels(xtick_lab)

# sauvegarde dans un fichier indexé par psi
#f.savefig('redressement_phi_%.2fpi.png' % (psi_rectifier*2))

f.show()

