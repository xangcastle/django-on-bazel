import json
import sys

import django
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from notes.models import Note


def health(request):
    return JsonResponse(
        {
            "status": "ok",
            "python": sys.version.split()[0],
            "django": django.get_version(),
            "executable": sys.executable,
        }
    )


@csrf_exempt
@require_http_methods(["GET", "POST"])
def notes(request):
    if request.method == "GET":
        return JsonResponse({"notes": [note.as_dict() for note in Note.objects.order_by("id")]})

    try:
        title = json.loads(request.body)["title"]
    except (ValueError, KeyError, TypeError):
        return HttpResponseBadRequest('expected JSON body {"title": "..."}')
    note = Note.objects.create(title=title)
    return JsonResponse(note.as_dict(), status=201)
