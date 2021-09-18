from django.db import models

# creare mis clases para los modelos que son la base de datos

class Autor(models.Model):
    id = models.AutoField(primary_key = True) # se pone autofield para que se autoincrementable
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=200, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default=True)
    descripcion = models.TextField(blank=False, null=False)


    class Meta:
        verbose_name ='Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de Publicacion', blank=False, null=False )
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
