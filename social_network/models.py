from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  

class Post(models.Model):

    user = models.ForeignKey('User', on_delete='CASCADE', related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    post = RichTextUploadingField(config_name='ckeditor_post')

    class Meta:
        ordering = ['created']

