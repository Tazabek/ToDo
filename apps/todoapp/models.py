from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=55, unique=True)
    descriotion = models.TextField()
    is_completed = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='todo/', null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'ToDo list'
