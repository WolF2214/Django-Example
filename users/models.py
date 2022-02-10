from datetime import datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.
# Los modelos se definen con clases
# Django crea los ID o primary keys por nosotros

class User(models.Model): # herencia de la clase de models
    # campos de mi modelo, los character fields son campos de texto
    first_name = models.CharField("el Nombre de la Persona", max_length=30) 
    last_name = models.CharField("el Apellido de la Persona", max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="los carros del usuario")

class Website(models.Model):
    STATUS_CHOICES = (
        ('R', 'Reviewd'),
        ('N', 'Not Reviewed'),
        ('E', 'Error'),
        ('A', 'Accepted')
        )
            
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True) # campo URL, unique para q solo haya una URL
    release_date = models.DateField() # fechas
    rating = models.IntegerField() # numeros enteros
    status = models.CharField(choices=STATUS_CHOICES,max_length=1) # opciones 
    ownwer = models.ForeignKey(User, on_delete=models.CASCADE) 
    """ owner: propietarios asociado con los user(se une el modelo a traves de la ForeinKey y el User), 
    cuando borramos un usuario se puede completar con diferentes acciones:
        Cascade: cuando borramos un usuario tambien 
                 borramos el modelo de Website
        SET_NULL: cuando borramos un usuario el campo se pone nulo(sigue existiendo pero queda vacio) """

    """ class Meta:
        ordering = ['rating'] # para cualquier cosa q no sea un campo
        db_table = 'website_custom_table_name'
        verbose_name = 'La Pagina Web'
        verbose_name_plural = 'Las Paginas' """

    def was_releasedd_last_week(self): # incorporacion de un post 
        if self.release_date < datetime.date(2022,10,2):
            return "Released before last week"
        else:
            return "Released this week"

    @property # podemos llamar una propiedad sin necesidad de definir los parentesis
    def get_full_name(self):
        return f"Este es el nombre completo del sitio web: {self.name}"

class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True) 
""" primary_key sirve para solo leer y no poder actualizar, si intentamos modificar crea una nueva instancia """
    
