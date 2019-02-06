from django.db import models

# Create your models here.

class Search(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class City(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Location (models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class ContactType(models.Model):
    name = models.CharField(max_length=200)

class Contact(models.Model):   
    type  = models.ForeignKey(ContactType,on_delete=models.CASCADE)
    value = models.TextField()
    user = models.ForeignKey("User",on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class User(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Problem(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Service(models.Model):
    name = models.CharField(max_length=200)
    descripcion = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class PropertyType(models.Model):
    name =  models.CharField(max_length=300)

class Property(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()
    type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    required = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data =  models.ManyToManyField(Property,through='CustomerData')
    providers = models.ForeignKey('Provider',on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Provider(models.Model):
    data =  models.ManyToManyField(Property,through="ProviderData")
    service =  models.ForeignKey(Service,on_delete=models.CASCADE)
    problems = models.ManyToManyField(Problem)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customers =  models.ManyToManyField(Customer)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class CustomerData(models.Model):
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE)
    property =  models.ForeignKey(Property,on_delete=models.CASCADE)
    visibility =  models.ForeignKey('VisibilityRule',on_delete=models.CASCADE)
    value =  models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class ProviderData(models.Model):
    provider =  models.ForeignKey(Provider,on_delete=models.CASCADE)
    property =  models.ForeignKey(Property,on_delete=models.CASCADE)
    visibility =  models.ForeignKey('VisibilityRule',on_delete=models.CASCADE)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class RequestState(models.Model):
    name =  models.CharField(max_length=200)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Request(models.Model):
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE)
    provider =  models.ForeignKey(Provider,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)


#el tipo de abstraccion tendra un nombre, que ayudara al usuario a saber que datos se hara publico
# la descripcion explicara el proceso
# cada abstraccion estara ligada una clase especifica de propiedad, para el caso de ejemplo sera el 
#fecha de nacimiento y localizacion 

class Abstraction(models.Model):
    name =  models.CharField(max_length=200)
    description =  models.TextField()
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    level = models.IntegerField()
    process_id = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class VisibilityRule(models.Model):

   
    CONTEXT = (

        ('public', 'Publico'),
        ('onlyme', 'Solo yo'),
        ('contacts', 'Solo mis contactos'),
        ('service', 'Para un servicio'), # debe tener referenciado un request 
        ('custom-list-customers', ' Lista de Clientes'),
        ('custom-list-providers', ' Lista de Proveedores'),
    )
    context_type = models.CharField(
        max_length=100,
        choices=CONTEXT,
        default='onlyme',
    )


    abstraccion =  models.ForeignKey(Abstraction,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)


#Score of service

class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScoreSystem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class ScoreSystemValue(models.Model):
    textual = models.CharField(max_length=200)
    value  = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScoreProvider(models.Model):
    skill =  models.ForeignKey(Skill,on_delete=models.CASCADE)
    score_system = models.ForeignKey(ScoreSystem,on_delete=models.CASCADE)
    score_system_value = models.ForeignKey(ScoreSystemValue,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScoreCustomer(models.Model):
    skill =  models.ForeignKey(Skill,on_delete=models.CASCADE)
    score_system =  models.ForeignKey(ScoreSystem,on_delete=models.CASCADE)
    score_system_value =  models.ForeignKey(ScoreSystemValue,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)



