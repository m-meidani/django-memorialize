# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseRedirect

from .forms import ImageUploadForm, NewUserForm
from .models import Person, Message
from .gravatar import get_avatar

from django.views.generic import View
from django.shortcuts import render, get_object_or_404, render_to_response
from django.urls import reverse_lazy


# Create your views here.


class WriteMemory(View):
    url = None
    person = None
    type = None

    def dispatch(self, request, *args, **kwargs):
        self.url = kwargs.pop('uuid')
        self.person = get_object_or_404(Person, url=self.url, is_url_valid=True)
        self.type = kwargs.pop('type', None)
        return super(WriteMemory, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        if self.person.email:
            avatar = get_avatar(self.person.email)
        else:
            avatar = None
        return render(request, 'upload.html', {'avatar_url': avatar,
                                               'name': self.person.name})

    def post(self, request):
        if self.type is None or self.type not in ['image', 'text']:
            return HttpResponseBadRequest()

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            if self.type == 'image':
                new_message = Message(person=self.person, image=form.cleaned_data['image'])
            else:
                new_message = Message(person=self.person, text_message=form.cleaned_data['text'])
            new_message.save()
            # These two lines should be commented out to limit number of comments to 1
            # self.person.is_url_valid = False
            # self.person.save()
            return HttpResponseRedirect(reverse_lazy('thanks'))

        return HttpResponse("یک مشکلی وجود داره. احتمالا فرمت عکسی که فرستادی درست نیست. دوباره امتحان کن لطفا :)")


def not_found(request):
    response = render_to_response(
        'Error404.html')
    response.status_code = 404

    return response


def thanks(request):
    return render_to_response('Thanks.html')


class NewUserView(View):

    def get(self, request):
        return render(request, 'anony.html')

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(reverse_lazy('write-memory', kwargs={'uuid': instance.url}))
        return HttpResponse('ایمیل آدرس را درست وارد کنید یا وارد نکنید.')


class IndexView(View):

    def get(self, request):
        messages = Message.objects.all()
        return render(request, 'index.html', context={'messages': messages})
