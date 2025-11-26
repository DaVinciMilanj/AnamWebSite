from django.core.cache import cache
from django.db.models import F
from .models import SiteStat


def increase_views_cached(step=1, flush_threshold=100):
    key = "site_views_buffer"
    buffer = cache.get(key, 0) + step
    cache.set(key, buffer, 60 * 10)

    if buffer >= flush_threshold:
        SiteStat.objects.update_or_create(
            pk=1,
            defaults={}
        )
        SiteStat.objects.filter(pk=1).update(
            total_views=F("total_views") + buffer
        )

        cache.set(key, 0, 60 * 10)
