#! /usr/bin/python
# -*- coding: utf-8 -*-


def site_title(request):
    title = "Django test"
    return {"SITE_TITLE": title}
