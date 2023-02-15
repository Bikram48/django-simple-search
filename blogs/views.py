from django.shortcuts import render
from blogs.models import Blogs

# Create your views here.
def search_view(request):
    query = request.GET

    try:
        query_obj = int(query.get("q"))
    except:
        query_obj = None

    print( query )
    
    blog_objects = None
    if query_obj is not None:
        blog_objects = Blogs.objects.get(id=query_obj)
        print(blog_objects)
    context = {
        "object": blog_objects
    }
    return render(request, "search.html", context=context)