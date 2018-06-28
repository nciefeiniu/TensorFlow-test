import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request, 'tranweb/index.html')


@require_POST
def translation(request):
    if request.method == 'POST':
        language_sort = request.POST['languagesotring']
        msg = request.POST['input_text']
        if msg and language_sort:
            print(language_sort)
            msg = {
                "action": "POST",
                "response": msg
            }
    else:
        msg = {
            "action": "get",
            "response": "busy, witeing for a min"
        }
    return HttpResponse(json.dumps(msg))
