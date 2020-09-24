# Présentation du projet Domopoules

<img src="../hardware/IMG_20200727_080342.jpg" height="250" alt="Poules sortant">

Présentation réalisé avec Remark.js pour le Dev and Test Day 2020 (Orange)
Appuyez sur P pour voir les notes. Puis C pour cloner l'affichage.

---

## Introduction

Les poules, parfait pour occuper les enfants pendant le confinement.

<img src="./enfant_poules.jpg" height="300" alt="Vue écrans Jeedom">

???
Mais pas mal de contraintes, dont ouvrir et fermer la porte matin et soir

---

## Introduction - 2

Le poulailler le lieu parfait pour innover en domotique.
Le WAF est très bon.

__Premier objectif : ouvrir automatiquement la porte du poulailler__

Objectifs suivants : présence des poules en intérieur, nombre d'oeufs.


---

## Des solutions éxistent sur le marché

<img src="./chickenguard.jpg" height="80%" alt="Vue écrans Jeedom">

???
Ici chickenguard
Mais cher(140€), pas domotisé, pas adapté à ma cabane.


---

## Agenda

1. Présentation de Jeedom
1. Présentation du raspberry pi zero WH
2. Le problème de la portée
3. Le problème de l'alimentation
4. ...

---

## Présentation de Jeedom

<img src="./jeedom_overview.jpg" width="100%" alt="Vue écrans Jeedom">

Open source. Français.

???
Système très ouvert : compatible zwave, philips Hue,  ikea...
TODO graphique Jeedom avec ses plugins

---

### Business model

<img src="./logo_jeedom.png" width="10%" alt="Vue écrans Jeedom">

Vente de:

- boxs sur étagère
- plugins
- service de sauvegarde
- noms de domaine

---

## Présentation du raspberry pi zero WH

<img src="./raspberry_family.jpg" width="50%" alt="Vue écrans Jeedom">

Photo de famille : 0 / 1 / 2 / 3 / 4

---

## Présentation du raspberry pi zero WH - 2

<img src="./raspberry-pi-zero-wh-kubii.jpg" height="80%" alt="Vue écrans Jeedom">

<https://www.kubii.fr/cartes-raspberry-pi/2076-raspberry-pi-zero-wh-kubii-3272496009394.html>

???

Pour ceux qui galèrent avec les arduino / ESP TODO
Un vrai linux accessible en SSH, un vrai IDE direct dessus (Vim), Git...
On peut écrire directement en python
Pas cher : 10-15€, mais il faut y ajouter la carte SD

---
## présentation de gpiozero

TODO add screenshots from
https://gpiozero.readthedocs.io/en/stable/recipes.html

---

## Le problème de la portée

<img src="./jardin_vue_helico.png" width="100%" alt="La maison et le poulailler sur la gauche">
Le poulailler est à TODO mètres de la box domotique

zigbee ==> KO
z-wave ==> MOUAIS
Wi-Fi ==> OK

---

### Mais est-ce lié au protocole

Probablement plus au hardware

<img src="./synology_rt2600ac.jpg" width="60%" alt="Un vrai routeur Wi-Fi">

---

### Mais est-ce lié au protocole - 2

<img src="./cle_usb_zwave.jpg" width="60%" alt="clé usb zwave">

???

---

### La solution technique

<img src="../hardware/IMG_20200723_000108.jpg" width="60%" alt="clé usb zwave">

---

## Le problème de l'alimentation

Naivement je pensais que le raspberry pi zero ne consommerait rien et tiendrait qques semaines sur une batterie USB...

Que Neni

---

## Alimentation solution

<img src="../hardware/IMG_20200724_181459.jpg" width="60%" alt="clé usb zwave">

---

## Motion eye OS

---

## Pour aller plus loin


