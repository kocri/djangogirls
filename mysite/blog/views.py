# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post


def post_list(request):
    post_all_data = Post.objects.all()
    return render(request, 'post_list.html', {'posts': post_all_data})