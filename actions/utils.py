import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action

def create_action(user, verb, target=None):
    # check for any similar action made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id, verb= verb, created__gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)
    if not similar_actions:
        # no existing actions found
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False

def get_actionlist(request_user, user=None):
    actions = Action.objects.all()
    if user:
        # Display all actions given user
        actions = actions.filter(user=user)
    else:
        # Display all actions following users
        actions = actions.exclude(user=request_user)
#         following_ids = request_user.followers.values_list('user_to', flat=True)
        following_ids = request_user.following.values_list('id', flat=True)
        if following_ids:
            
            # If user is following others, retrieve only their actions
            actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]
    return actions