from django.db import models

from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10)
    floor = models.IntegerField()
    capacity = models.IntegerField()
    free_places = models.IntegerField()

    def __str__(self):
        return f"Кімната {self.number} (поверх {self.floor})"

class Resident(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='residents')
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='residents/', blank=True, null=True)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=[
        ('important', 'Важливе'),
        ('event', 'Подія'),
        ('repair', 'Ремонт'),
    ])

    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.position}: {self.name}"

class Request(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('new', 'Нова'),
        ('in_progress', 'В процесі'),
        ('done', 'Виконано'),
    ], default='new')

    def __str__(self):
        return f"Заявка від {self.resident.name} ({self.status})"
