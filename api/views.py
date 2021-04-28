import uuid
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload(request):
    if request.method == "POST":
        files = request.FILES

        if files:
            for f in files:
                item = request.FILES[f]
                name_enc = str(uuid.uuid4()).replace("-", "")
                fs = FileSystemStorage()
                filename = fs.save(name_enc, item)
                uploaded_file_url = fs.url(filename)

                print("uploaded_file_url:", uploaded_file_url)

        return JsonResponse({"result": "success", "file_url": uploaded_file_url})
    return render(request, "file_upload.html")
