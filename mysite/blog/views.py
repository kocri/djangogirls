# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    post_all_data = Post.objects.all()
    posts = Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
    return render(request, 'post_list.html', {'posts': post_all_data})