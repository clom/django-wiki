#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from tomori.models import *


# admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'username',)  # 一覧に出したい項目
    list_display_links = ('id', 'title', 'text', 'username')  # 修正リンクでクリックできる項目



admin.site.register(Article, ArticleAdmin)
admin.site.register(Menu)
admin.site.register(Top)
