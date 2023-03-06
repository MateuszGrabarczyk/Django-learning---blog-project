from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField( max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    excerpt = models.CharField(max_length=300)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name + " " + self.text[:50]

