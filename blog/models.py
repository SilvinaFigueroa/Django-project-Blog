from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Data model for blog posts

class Post(models.Model):
    # We have defined the enumeration class Status by subclassing models.TextChoices. 
    # The available choices for the post status are DRAFT and PUBLISHED. 
    # Their respective values are DF and PB, and their labels or readable names are Draft and Published.
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    # post title: This is a CharField field that translates into a VARCHAR column in the SQL database.
    title = models.CharField(max_length=250)
    # This is a SlugField field that translates into a VARCHAR column in the SQL database
    slug = models.SlugField(max_length=250)
    
    # We have imported the User model from the django.contrib.auth.models module and we have added an author field to the Post model. 
    # This field defines a many-to-one relationship, meaning that each post is written by a user, and a user can write any number of posts. 
    # For this field, Django will create a foreign key in the database using the primary key of the related model.  
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='blog_posts',
            default=1
    )
    # This is a TextField field that translates into a TEXT column in the SQL database.
    body = models.TextField()
    
    # This is a DateTimeField field that translates into a DATETIME column in the SQL database
    #  e will use it to store the date and time when the post was published
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.DRAFT)

    # This class defines metadata for the model
    # We use the ordering attribute to tell Django that it should sort results by the publish field.
    class Meta:
    #  We indicate descending order by using a hyphen before the field name, -publish. 
    #  Posts will be returned in reverse chronological order by default.
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
    #  default Python method to return a string with the human-readable representation of the object. 
    #  Django will use this method to display the name of the object in many places, such as the Django administration site.
        return self.title