from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


posts = [
    {'id':0,
     'title': 'Let\'s explore python',
     'content': 'Python is interpreted, high level, general purpose programming language. USed in web, data and ML.'},
    {'id': 1,
     'title': 'dont know',
     'content': 'Example content'},
    {'id': 2,
     'title': 'i know',
     'content': 'too lazy to come up with an example'},
]

categories = [
    'Programming',
    'Food',
    "ML/AI"
]
# Create your views here.
def home(request):
    html = ""
    for post in posts:
        html += f'''
            <div>
            <a href="/post/{post['id']}/">
                <h1>{post['id']} - {post['title']}</h1></a>
                <p>{post['content']}</p>
            </div>
        '''
    name = 'Jeff Bezos'
    return render(request, 'posts/index.html', {'posts': posts, 'categories': categories})




def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request, "posts/post.html", {'post_dict':post_dict})
    else:
        return HttpResponseNotFound('Post not avaliable')

def google(request, id):
    url = reverse("posts", args=[id])
    return HttpResponseRedirect(url)

