from django.http import HttpResponseRedirect
from django.shortcuts import render

from arden.forms import UpoForm


def appendUpo(request):
    form = UpoForm()
    if request.method == 'POST':
        mid = request.get['mid']
        form = UpoForm(request.POST)
        if form.is_valid():
            new_upo = form.save(commit=False)
            new_upo.submitter = '我'
            new_upo.deleted = False
            new_upo.save()
            return HttpResponseRedirect('/gf/logonSuccess')
    return render(request, 'logon.html', {'form': form})
