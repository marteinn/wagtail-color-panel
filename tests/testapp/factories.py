import wagtail_factories

from . import models


class PageWithColorFieldPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.PageWithColorField


class PageWithCharColorFieldPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.PageWithCharColorField


class PageWithDefaultValuePageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.PageWithDefaultValue
