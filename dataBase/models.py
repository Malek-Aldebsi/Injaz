from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    name = models.TextField()


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dateOfBarth = models.DateField()
    gender = models.BooleanField()
    height = models.IntegerField()
    weight = models.DecimalField()
    idealWeight = models.DecimalField()
    relationship = models.Choices()
    numOfHousehold = models.IntegerField()
    image = models.ImageField()  # TODO:check
    interest = models.ManyToManyField(Interest, on_delete=models.CASCADE, null=True, blank=True)


class PetKind(models.Model):
    name = models.TextField()


class Pet(models.Model):
    name = models.TextField()
    userID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    petKindID = models.ForeignKey(PetKind, null=True, blank=True, on_delete=models.SET_NULL)


class StepsRecords(models.Model):
    date = models.DateField()
    numOfSteps = models.IntegerField()
    userID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)


class Meal(models.Model):
    dateTime = models.DateTimeField()
    userID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)


class FoodType(models.Model):
    name = models.TextField()


class Food(models.Model):
    name = models.TextField()
    numOfCalories = models.IntegerField()
    foodTypeID = models.ForeignKey(FoodType, null=True, blank=True, on_delete=models.SET_NULL)


class MealFood(models.Model):
    weight = models.IntegerField()
    mealID = models.ForeignKey(Meal, null=True, blank=True, on_delete=models.SET_NULL)
    foodID = models.ForeignKey(Food, null=True, blank=True, on_delete=models.SET_NULL)


class MedicalExaminationsType(models.Model):
    name = models.TextField()


class MedicalExaminationsRecords(models.Model):
    measurement = models.IntegerField()
    dateTime = models.DateTimeField()
    medicalExaminationsType = models.ForeignKey(MedicalExaminationsType, null=True, blank=True, on_delete=models.SET_NULL)
    userID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
