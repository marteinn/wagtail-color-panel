from django.conf.urls import include, url
from wagtail.admin import urls as wagtailadmin_urls

from wagtail import VERSION as WAGTAIL_VERSION
if WAGTAIL_VERSION >= (3, 0):
    from wagtail import urls as wagtail_urls
else:
    from wagtail.core import urls as wagtail_urls

urlpatterns = [
    url(r"^admin/", include(wagtailadmin_urls)),
    url(r"", include(wagtail_urls)),
]
