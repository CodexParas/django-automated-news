from home.models import Category

def category_items(request):
    categories = list(Category.objects.order_by("name"))
    return {'categories':categories}
