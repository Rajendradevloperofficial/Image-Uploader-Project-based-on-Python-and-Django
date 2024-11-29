from django.db import models

# create your  modles here.

class Image(models.Model):
	photo=models.ImageField(upload_to='myimage')
	date =models.DateTimeField(auto_now_add=True)

	