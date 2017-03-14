from django import template

from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def isFollower(requestUserId, userId):
    followers = User.objects.get(id=userId).following.values_list("user_from", flat=True)
    if requestUserId in followers:
        return 1
    else:
        return 0 
    
#     In template
#     {% isFollower request.user.id  user.id  as isfollower %}