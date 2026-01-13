from django.db import models

class SearchLog(models.Model):
    # This stores the SMILES string
    smiles = models.CharField(max_length=255)
    
    # This stores the date and time automatically when the record is created
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.smiles} - {self.timestamp}"
