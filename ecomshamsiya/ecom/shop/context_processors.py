from . models import Category
def mlink(request):
    link=Category.objects.all()
    return dict(link=link)