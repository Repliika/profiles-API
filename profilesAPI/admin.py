from django.contrib import admin
from django.db import models

# Register your models here.

from profilesAPI import models

# registering the model as admin site so we can access via admin interface
# registered user profiles to admin page
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)