from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from news.models import News
from tastypie import fields
from django.contrib.auth.models import User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        # excludes = ['email', 'username', 'is_active', 'is_staff', 'is_superuser']
        fields = ['firstname', 'lastname', 'username'] # Whitelisting the fields to display
        # allowed_methods = ['get']
        filtering = {
            'username': ALL,
        }


class NewsResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'writer')
    class Meta:
        queryset = News.objects.all()
        resource_name = 'news'
        authorization = Authorization()
        filtering = {
            'writer': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
