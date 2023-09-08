from typing import Any, Dict
from .models import Words
from django.views import generic

# Create your views here.
class WordsView(generic.TodayArchiveView):
    queryset = Words.objects.all()
    context_object_name = 'words_list'
    date_field = "date"
    template_name = 'words.html'


class WordsListView(generic.ListView):
    model = Words
    context_object_name = 'all_words'
    template_name = 'allwords.html'


class WordsDetailView(generic.DetailView):
    model = Words
    context_object_name = 'words_detail'
    template_name = 'meaning.html'

    def get_context_data(self, **kwargs):
        context = super(WordsDetailView, self).get_context_data(**kwargs)
        context['words_detail'] = Words.objects.filter(pk=self.kwargs['pk'])
        return context