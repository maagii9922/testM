from django.http import HttpResponse
from .models import Category, Family, Group, Person



def home(request):
    # p = Person(name='bat')
    # p.save()
    # p1 = Person.objects.get(pk=1)
    # p = Person.objects.get(name='bat')
    # p = Person.objects.get(name__contains='o')
    # p = Person.objects.get(name__startswith='a')
    # p = Person.objects.filter(pk=1,name='bat')
    # p = Person.objects.filter(name='bat')[0:5]
    # p1 = Person.objects.filter(name='bat')[5:10]
    # p2 = Person.objects.filter(name='bat')[10:16]
    # p = Person.objects.filter(nas__gt=20,nas__lt = 50)

    #//insert
    # p = Person.objects.get(pk=1)  
    # f = Family(fToo=3)
    # f.save()
    # p.famToo=f
    # p.save()
    # p = Person.objects.get(pk=1)
    # print(p.famToo)

    # f = Family(fToo=2)
    # f.save()

    # p = Person(name='dddf',nas=23,famToo = f)
    # p.save()
    # print(p.famToo)
    # p = Person.objects.get(famToo__fToo=84)
    # f = Family.objects.get(person__name = 'oi.lk,')
    # print(f.fToo)

    # p = Person.objects.get(pk=3)
    # f = Family(fToo = 333,fOvog = 'jjj')
    # f.save()
    # p.famToo = f
    # p.save()
    # c = Category(catName = 'uilanhai')
    # c.save()
    # c = Category(catName = 'huurhun')
    # c = Category(catName = 'aashtai')
    # f1 = Family(fToo = 2,fOvog = 'nn')
    # f1.save()
    # f = Person(name = 'sk',nas = 38,famToo = f1, cName= c)


    #//update
    # p = Person.objects.get(pk=1)      
    # c = Category.objects.get(catName = 'huurhun')
    # p.cName=c
    # p.save()
    # print(p)

    #//person=>category
    # p = Person.objects.get(cName_id =5)    
    # print(p)
    
    g = Group(groupName = 'prog')
    g.save()
    g1 = Group(groupName = 'prog1')
    g1.save()
    g2 = Group(groupName = 'prog2')
    g2.save()
    c = Category(catName = 'nnn')
    c.save()
    f = Family(fToo = 1,fOvog = 'z')
    f.save()
    p = Person(name = 'nomuka',nas =1, famToo = f,cName = c)
    p.save()
    p.gName.add(g)
    p.gName.add(g1)
    p.gName.add(g2)
    print(p)

    # c = Category.objects.get(person =1)
    # print(c)



    # print(p1)
    # print(p2)
    return HttpResponse("okok")





