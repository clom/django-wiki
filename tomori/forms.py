from django.forms import ModelForm
from tomori.models import *


class FormArticle(ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text',)
