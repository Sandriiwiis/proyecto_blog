from django.db import models

# Autores
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    genero_favorito = models.CharField(max_length=50, default="Fantasía")

    def __str__(self):
        return f"✨ {self.nombre} {self.apellido}"

#Artículos (Entradas del blog)
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    # Conexión: Un artículo pertenece a un Autor
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"📖 {self.titulo}"