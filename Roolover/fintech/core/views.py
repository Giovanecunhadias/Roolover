from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ContaFilha
from .utils import calcular_split

def realizar_deposito(request, conta_filha_id):
    if request.method == 'POST':
        conta_filha = get_object_or_404(ContaFilha, id=conta_filha_id)
        deposito = float(request.POST.get('deposito'))

        splits = calcular_split(deposito, conta_filha)

        # Aqui você pode salvar os splits no banco de dados, se necessário
        # ...

        return JsonResponse(splits, safe=False)
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ContaFilha
from .utils import calcular_split

def realizar_deposito(request, conta_filha_id):
    conta_filha = get_object_or_404(ContaFilha, id=conta_filha_id)
    if request.method == 'POST':
        deposito = float(request.POST.get('deposito'))

        splits = calcular_split(deposito, conta_filha)

        # Aqui você pode salvar os splits no banco de dados, se necessário
        # ...

        return JsonResponse(splits, safe=False)
    else:
        return render(request, 'realizar_deposito.html', {'conta_filha': conta_filha})
