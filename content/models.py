from django.db import models

class Feed(models.Model):
    content       = models.TextField()
    image         = models.TextField()
    profile_image = models.TextField()
    user_id       = models.TextField()
    like_count    = models.IntegerField()

class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()