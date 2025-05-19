import abc
from abc import ABCMeta, abstractmethod
# Necessitem aquest mòdul per llegir el fitxer CSV
import csv

# Aquesta és una classe "plantilla" que no fem servir directament
# Només és perquè Movies i Books tinguin algunes regles
class Dataset:
    def __init__(self):
        # Aquí guardarem les pel·lícules i les seves puntuacions
        # Exemple: self.items["Titanic"]["Usuari1"] = 5
        self.items = {}
    
    def afegir_puntuacio(self, nom_item, nom_usuari, puntuacio):
        pass
    
    def trobar_items_no_puntuats(self, nom_usuari):
        pass