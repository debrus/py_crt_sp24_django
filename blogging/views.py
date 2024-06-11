from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# syndication imports
from django.contrib.syndication.views import Feed


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class LatestPostsFeed(Feed):
    title = "Recent Blog Posts"
    link = ""
    description = "The five most recent blog posts"

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return f"/posts/{item.pk}/"

    def item_guid(self, item):
        return item.pk

    def item_categories(self, item):
        return item.categories.all()

    def item_author_name(self, item):
        return item.author

    def item_pubdate(self, item):
        return item.published_date

    def item_updateddate(self, item):
        return item.modified_date


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
