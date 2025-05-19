import Dataset

# Classe Books, també hereta de Dataset
class Books(Dataset):
    def __init__(self):
        super().__init__()  # Crida al constructor de la classe pare (Dataset)
    
    # Afegim una valoració per a un llibre
    def afegir_valoracio(self, llibre, usuari, puntuacio):
        if llibre not in self.items:
            self.items[llibre] = {}  # Creem un diccionari per aquest llibre
        self.items[llibre][usuari] = puntuacio  # Guardem la puntuació de l'usuari
    
    # Obtenim els llibres que l'usuari no ha puntuat
    def obtenir_items_no_puntuats(self, usuari):
        items_no_puntuats = []
        for llibre in self.items:
            if usuari not in self.items[llibre]:  # Si l'usuari no ha puntuat aquest llibre
                items_no_puntuats.append(llibre)
        return items_no_puntuats