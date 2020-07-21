from django.db import models

class authorDetails(models.Model):
    email = models.CharField(max_length=254)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class blogDetails(models.Model):
    authorEmail = models.ForeignKey(authorDetails,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    blog = models.TextField()
    posted_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)




