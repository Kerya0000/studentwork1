from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


# создаём фильтр
class NewsFilter(FilterSet):

    class Meta:
        model = Post
        fields = {'dateCreation': ['lt'],
                  'title': ['icontains'],
                  'author':['exact'], }