from django.http import HttpResponseRedirect
from django.shortcuts import render

from arden.forms import UpoForm
from common.BilibiliUtils import getInfo


def appendUpo(request):
    form = UpoForm()
    if request.method == 'POST':
        form = UpoForm(request.POST)
        if form.is_valid():
            new_upo = form.save(commit=False)
            new_upo.submitter = '我'
            new_upo.deleted = False
            new_upo.save()
            return HttpResponseRedirect('/gf/logonSuccess')
    return render(request, 'logon.html', {'form': form})


def publishUpo(request):
    getInfo()