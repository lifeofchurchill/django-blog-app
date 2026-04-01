from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)

    class meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.name


class Post(models.Model): #status choices for the blog with repitition of the same ord twice.
    STATUS_CHOICES = [    #first one is stored in the DB and the second one is the UI.
        ('draft', 'Draft'), 
        ('published', 'Published'),
    ]

    title = models.CharField(max_length = 200,)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', blank=True)
    bio = models.TextField()
    twitter_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null = True)
    linkedin_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")

    def __str__(self):
        return f"{self.user.username}'s comment"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
    
    def __str__(self):
        return f"{self.user.username} liked a post"
    

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
    
    def __str__(self):
        return f"{self.user.username} bookmarked a post"

