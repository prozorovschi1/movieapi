from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name





class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    category = models.ForeignKey(Category, related_name='movies', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'{self.author} - {self.movie.title} ({self.rating}/10)'


class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Comment by {self.author} on {self.review.movie.title} - {self.created_at.strftime("%Y-%m-%d")}'
