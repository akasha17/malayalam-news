from django.db import models

# Define the Category model for news
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Define the News model
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # category can be optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_headline = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Define the Advertisement model
class Advertisement(models.Model):
    image = models.ImageField(upload_to='advertisements/')
    link = models.URLField()

    def __str__(self):
        return f"Advertisement: {self.link}"
