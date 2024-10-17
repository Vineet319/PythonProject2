class Products(models.Model):
    p_name = models.CharField(max_length=100)
    p_brand = models.CharField(max_length=120)