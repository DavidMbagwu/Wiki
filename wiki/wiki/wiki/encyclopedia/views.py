from markdown2 import Markdown
from django.shortcuts import render
import random

from . import util


def converter(request, title):
    markdown = util.get_entry(title)
    if markdown == None:
        return None
    else:
        return Markdown().convert(markdown)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if converter(request, title) == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize(),
            "content": converter(request, title)
        })
    
def randome(request):
    title = random.choice(util.list_entries())
    return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize(),
        "content": converter(request, title )
    })
    
def search(request):
    if request.method == "POST":
        query = request.POST['q']
        entries = converter(request, query)
        if entries is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": query.capitalize(),
                "content": converter(request, query)
            })
        else:
            recommendation = []
            for entry in util.list_entries():
                if query.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "query": query,
                "recommendation": recommendation
            })      

    else:
        return render(request, "encyclopedia/index.html")
    

def new(request):
    return render(request, "encyclopedia/new.html")


def new_title(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title):
            return render(request, "encyclopedia/new_entry_error.html")         
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "title": title.capitalize(),
                "content": converter(request, title)
            })                         
    else:
        return render(request, "encyclopedia/index.html")
    
def edit(request):
    return render(request, "encyclopedia/edit.html",
                  
                 )

def new_content(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if not util.get_entry(title):
            return render(request, "encyclopedia/new_entry_error.html")
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "title": title.capitalize(),
                "content": converter(request, title)
            })                         
    else:
        return render(request, "encyclopedia/index.html")