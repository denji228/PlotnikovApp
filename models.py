from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.get_full_name()

class ConsultationRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('processing', 'В обработке'),
        ('waiting', 'Ожидает подтверждения'),
        ('canceled', 'Отменена'),
        ('solved', 'Решена'),
    ]
    
    CATEGORY_CHOICES = [
        ('software', 'Программное обеспечение'),
        ('hardware', 'Настройка оборудования'),
        ('security', 'Кибербезопасность'),
        ('network', 'Сетевая инфраструктура'),
        ('servers', 'Серверные системы'),
    ]
    
    METHOD_CHOICES = [
        ('online', 'Онлайн'),
        ('offline', 'Офлайн'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date_time = models.DateTimeField()
    contact_phone = models.CharField(max_length=20)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    cancel_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Заявка #{self.id} от {self.user}"