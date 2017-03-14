from .models import Action

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

#from django.contrib.auth.models import User
#from mongoengine.errors import DoesNotExist


@ajax_required
@require_POST
@login_required
def delete_action(request):
    action_id = request.POST.get('action_id')
    if action_id:
        try:
            Action.objects.get(id=action_id).delete()
            return JsonResponse({'status': 'ok'})
        except Action.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})

