from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from .functions import create_random_key
from .models import Keys
from .serializers import KeysSerializer


# Create your views here.
@require_GET
def get_key(request):
    """
    Issue key to user. Require get method. If key issued set it's status to 1 (Issued)
    :param request: HttpRequest.
    :return: JsonResponse
    """
    keys_objects = Keys.objects.filter(status=0)
    # Check if we have not issued keys
    if len(keys_objects) > 0:
        key = keys_objects[0]
    else:
        key = create_random_key()
    serializer = KeysSerializer(key)
    key.status = 1
    key.save()
    return JsonResponse(serializer.data)


@csrf_exempt
@require_POST
def repaid_key(request):
    """
    repaid key. require Post.
    :param request: HttpReques
    :return: Json response
    """
    key = get_object_or_404(Keys, pk=request.POST['pk'])
    if key.status == 1:
        key.status = 2
        key.save()
        serializer = KeysSerializer(key)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'error': 'Key was not issued or was repaid earilier', 'id': key.pk, 'key': key.key, 'status': key.status})


@require_GET
def key_info(request, pk):
    """
    Return key status
    """
    key = get_object_or_404(Keys, pk=pk)
    return JsonResponse({'key_status': key.get_status_display()})


@require_GET
def keys_count(request):
    """
    Return not issued keys count
    """
    keys = Keys.objects.filter(status=0).count()
    return JsonResponse({'Not issued keys': keys})



