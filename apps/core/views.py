from django.core.cache import cache
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from apps.partner.models import Partner
from apps.post.models import Post

from apps.stats.models import Fixture, get_top_scorers_summary, Injury
from .models import get_featured


def home(request):
    next_match = Fixture.get_next_match()
    recent_results = Fixture.recent_results()
    standings = cache.get('epl_standings')
    if standings and 'teams' in standings:
        standings_summary = standings['teams'][:6]
    else:
        standings_summary = []
    top_scorers = get_top_scorers_summary()
    injuries = Injury.get_current_injuries()
    recent_posts = Post.recent()
    featured = get_featured()
    context = {
        'next_match': next_match,
        'recent_results': recent_results,
        'standings': standings_summary,
        'players': top_scorers,
        'injuries': injuries,
        'posts': recent_posts,
        'featured': featured,
    }
    return render(request, 'home.html', context)


@user_passes_test(lambda u: u.is_superuser)
def clear_cache(request):
    from django.core.cache import cache
    from django.core.urlresolvers import reverse
    from django.http import HttpResponseRedirect
    from django.contrib import messages

    cache.clear()

    try:
        cache._cache.flush_all()
    except AttributeError:
        pass
    try:
        cache._cache.clear()
    except AttributeError:
        pass
    try:
        cache._expire_info.clear()
    except AttributeError:
        pass

    # django-redis
    try:
        cache.cache.clear()
    except AttributeError:
        pass

    # django-cacheops
    try:
        from cacheops.conf import redis_client

        redis_client.flushdb()
    except ImportError:
        pass

    messages.info(request, "Cache Cleared")
    try:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except KeyError:
        return HttpResponseRedirect(reverse("admin:index"))
    return HttpResponseRedirect(reverse("admin:index"))
