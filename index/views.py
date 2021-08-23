from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import F

from .models import Collection, Video, Place


class CollectionsView(ListView):
    model = Collection

    def get_queryset(self):
        return Collection.objects.filter(
            date__lte=timezone.now()
        ).order_by("-date", "-id")[:9]

    def get_context_data(self, **kwargs):
        context = super(CollectionsView, self).get_context_data(**kwargs)
        context["video_list"] = Video.objects.all().order_by("-date")
        return context


class CollectionDetailView(DetailView):

    model = Collection
    slug_field = "url"
    
    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        collection_post_slug = self.kwargs['slug']
        if not collection_post_slug in self.request.session:
            Collection.objects.filter(url=collection_post_slug).update(views=F('views') + 1)
            # Insert the slug into the session as the user has seen it
            self.request.session[collection_post_slug] = collection_post_slug
        return context


class AllCollectionsView(View):
    model = Collection

    def get(self, request):
        collection = Collection.objects.order_by("-date")
        dates = Collection.objects.values_list("date", flat=True).order_by("-date").distinct()
        return render(request, "index/all_collections.html", {"collection_list": collection,
                                                              "dates": dates})


class PlaceDetailView(DetailView):

    model = Place
    slug_field = "url"


class VideoDetailView(DetailView):

    model = Video
    slug_field = "url"


class AboutView(View):

    def get(self, request):
        return render(request, "index/about.html",)
