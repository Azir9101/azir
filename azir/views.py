from django.http import HttpResponse

def test(request):
    return HttpResponse('hellow')


class RiotViews(object):
    pass
