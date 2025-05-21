from django.db import models

class Jeux(models.Model):
        nom = models.CharField(max_length=100)
        plateforme = models.CharField(max_length = 100)
        date_parution = models.DateField(blank=True, null = True)
        prix = models.IntegerField(blank=False)
        genre = models.TextField(null = True, blank = True)
        resume = models.TextField(null= True, blank = True)

        def __str__(self):
                chaine = f"{self.nom} appartenant aux genres ({self.genre}) disponible sur {self.plateforme} édité le {self.date_parution}"
                return chaine

        def dico(self):
                return {"nom":self.nom, "pateforme":self.plateforme, "date_parution":self.date_parution, "prix":self.prix, "genre":self.genre, "resume":self.resume}

class Studiodev(models.Model):
        nom = models.CharField(max_length=100, blank=False)
        franchise = models.TextField(null = True, blank = True)

        def __str__(self):
           return self.nom

        def dico(self):
            return {"nom": self.nom, "franchise": self.franchise}