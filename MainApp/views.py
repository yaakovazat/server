from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {

        })


class TextManagerView(View):
    def post(self, request):
        content = request.POST.get("content", "")
        print(content)
        if len(content):
            old_content = content
            '''
               Qazkaz Text Manager functions
            '''
            content = content + "QazKaz"
            return render(
                request,
                "index.html",
                {
                    "content": content,
                    "old_content": old_content,
                }
            )
        else:
            return render(
                request,
                "index.html",
            )


class FileManagerView(View):
    def post(self, request):
        file_form = UploadFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_obj = FileUpload()
            file = file_form.cleaned_data['file']
            file_obj.name = file.name
            file_obj.file = file
            file_obj.save()
            # '''
            #     Qazkaz File Manager functions
            #  '''
            return render(request, 'index.html', {
                "type": "file",
                "content": "This is test File"
            })
        else:
            return render(request, 'index.html', {
                "error": file_form
            })


class ImageManagerView(View):
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            file_obj = ImageUpload()
            file = image_form.cleaned_data['image']
            file_obj.name = file.name
            file_obj.image = file
            file_obj.save()
            # '''
            #     Qazkaz Image Manager functions
            #  '''
            return render(request, 'index.html', {
                "image": file_obj,
                "type": "file",
                "content": "This is test Image"
            })
        else:
            return render(request, 'index.html', {
                "error": image_form
            })

