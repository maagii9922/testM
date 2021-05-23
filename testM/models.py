from django.db import models
# from django.db.models.deletion import CASCADE
# from django.db.models.fields.related import OneToOneField

class Family(models.Model):
    fToo = models.IntegerField()
    fOvog = models.CharField(max_length=50)


    def __str__(self):
         return str(self.fToo)+"-"+self.fOvog

class Category(models.Model):
    catName = models.CharField(max_length=50)

    def __str__(self):
         return self.catName

class Group(models.Model):
    groupName = models.CharField(max_length=50)

    def __str__(self):
         return self.gName


class Person(models.Model):
    name = models.CharField(max_length=50)
    nas = models.IntegerField()
    famToo = models.OneToOneField(Family,on_delete=models.CASCADE)
    cName = models.ForeignKey(Category, on_delete=models.CASCADE)
    gName = models.ManyToManyField(Group)

    def __str__(self):
        return str(self.id)+". "+self.name+ " "+str(self.famToo)+" "+str(self.cName.catName)





