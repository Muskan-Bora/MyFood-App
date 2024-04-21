from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    rest_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
    )
    prod_code = models.IntegerField(default=50)
    added_by = models.CharField(
        max_length=50,
        default='user'
    )
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(
        max_length=500,
        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed ad nisi asperiores amet est pariatur corrupti. Molestias aperiam natus adipisci officiis veniam quo. Hic dicta beatae voluptate accusantium, nostrum maiores."
    )
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://www.shutterstock.com/image-vector/exciting-new-cafe-bar-restaurant-600nw-2145440019.jpg"
    )

    def __str__(self):
        return self.item_name
    
class History(models.Model):
    username = models.CharField(max_length= 100)
    prod_code = models.IntegerField()
    item_name = models.CharField(max_length = 200)
    operation_type = models.CharField(max_length= 100)
    user_type = models.CharField(max_length= 100)

    def __str__(self):
        return str(
            (
                self.prod_code,
                self.item_name,
                self.username,
                self.user_type,
                self.operation_type
            )
        )
    
class NavbarForm(models.Model):
    data = models.CharField(max_length=100)

    def __str__(self):
        return str(
            self.data
        )