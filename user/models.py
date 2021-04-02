from django.db import models

class City(models.Model):
    x_coordinate = models.DecimalField(max_digits=6,decimal_places=3)
    y_coordinate = models.DecimalField(max_digits=6,decimal_places=3)
    store=models.BooleanField()
    warehouse=models.BooleanField()
    # City_Choices=[
    #     (1,'Mumbai'),
    #     (2,'Pune'),
    #     (3,'Nashik'),
    #     (4,'Nagpur'),
    #     (5,'Thane'),
    #     (6,'Alibaugh'),
    # ]
    # class city_choice= models.CharField(
    #     max_length=7,
    #     choices=City_Choices,
    #     default=Mum,
    # )
# class City_Dist(models.Model):
#     Adj_matrix={
#         {0,5,4,15,1,3},
#         {5,0,8,7,5,6},
#         {4,8,0,17,4,9},
#         {15,7,17,0,16,8},
#         {1,5,4,16,0,4},
#         {3,6,9,8,4,0}
#     }



