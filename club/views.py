from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from . import models

from gym import forms


def index(request):
    num_member = models.Member.objects.all().count()
    num_field = models.Field.objects.all().count()
    num_course_in_progress = models.CoursesInProgress.objects.all().count()
    num_championship = models.Championship.objects.all().count()
    return render(
        request,
        'club/index.html',
        context={'num_member': num_member,
                 'num_field': num_field,
                 'num_course_in_progress': num_course_in_progress,
                 'num_championship': num_championship,
                 }
    )


class AboutListView(generic.ListView):
    model = models.AboutUs
    template_name = 'about_list.html'


def about_detail_def(request, id):
    model = models.AboutUs.objects.filter(pk=id)
    context = {'object_list': model}
    return render(request, 'about_detail.html', context)


#
# def contact(request):
#     var = "hello this is Contact us page"
#     return render(
#         request,
#         'contact.html',
#         context={'var': var}
#     )
#


def tell_me_view(request):
    form = forms.ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            tell_me = form.save(commit=False)
            tell_me.name = form.cleaned_data.get('name')
            tell_me.text = form.cleaned_data.get('text')
            tell_me.save()
            return redirect(reverse('club:index'))
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', {'form': form})


class MemberListView(generic.ListView):
    model = models.Member
    template_name = 'club/member/member_list.html'


def member_detail_def(request, id):
    model = models.Member.objects.filter(pk=id)
    context = {'object_list': model}
    return render(request, 'club/member/member_detail.html', context)


class FieldListView(generic.ListView):
    model = models.Field
    template_name = 'club/field/field_list.html'


def field_detail_def(request, id):
    model = models.Field.objects.filter(pk=id)
    context = {'object_list': model}
    return render(request, 'club/field/field_detail.html', context)
