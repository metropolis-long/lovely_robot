from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


def handle_uploaded_file(f):
    print(type(f))
    # with open(r'D:\some\file\name.jpg', 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)