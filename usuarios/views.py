from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Usuario
 
@require_http_methods(["GET"])
def usuarios_list(request):
    qs = Usuario.objects.all()
    data = [u.as_dict() for u in qs]
    return JsonResponse(data, safe=False)
 
@csrf_exempt
@require_http_methods(["POST"])
def insertar(request):
    try:
        data = json.loads(request.body.decode() or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error':'JSON inválido'}, status=400)
    nombre = data.get('nombre','').strip()
    if not nombre:
        return JsonResponse({'error':'Nombre requerido'}, status=400)
    u = Usuario.objects.create(nombre=nombre)
    return JsonResponse({'mensaje':'Usuario insertado','usuario':u.as_dict()}, status=201)
 
@require_http_methods(["GET"])
def buscar(request, codigo):
    try:
        u = Usuario.objects.get(id=codigo)
        return JsonResponse(u.as_dict())
    except Usuario.DoesNotExist:
        return JsonResponse({'error':'Usuario no encontrado'}, status=404)
 
@csrf_exempt
@require_http_methods(["PUT"])
def modificar(request, codigo):
    try:
        data = json.loads(request.body.decode() or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error':'JSON inválido'}, status=400)
    nombre = data.get('nombre','').strip()
    if not nombre:
        return JsonResponse({'error':'Nombre requerido'}, status=400)
    try:
        u = Usuario.objects.get(id=codigo)
        u.nombre = nombre
        u.save()
        return JsonResponse({'mensaje':'Usuario modificado','usuario':u.as_dict()})
    except Usuario.DoesNotExist:
        return JsonResponse({'error':'Usuario no encontrado'}, status=404)
 
@csrf_exempt
@require_http_methods(["DELETE"])
def eliminar(request, codigo):
    try:
        u = Usuario.objects.get(id=codigo)
        u.delete()
        return JsonResponse({'mensaje':'Usuario eliminado'})
    except Usuario.DoesNotExist:
        return JsonResponse({'error':'Usuario no encontrado'}, status=404)
