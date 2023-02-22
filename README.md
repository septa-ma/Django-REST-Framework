# Django-rest-framework

# Django REST framework is a powerful and flexible toolkit for building Web APIs.

# Some reasons you might want to use REST framework:
- - It has a web browsable API.
- - Authentication policies including packages for OAuth1a and OAuth2.
- - Serialization that supports both ORM and non-ORM data sources.
- - You can just use regular function-based views if you don't need the more powerful features. 
  For example you can use mixin or generic-class modules for makeing views.
- - Extensive documentation, ( https://www.django-rest-framework.org ) and great community support.

# How to use REST Framework in Django?

- 1- install REST Framework in your project -> pip install djangorestframework
- 2- add it in INSTALLED_APP list -> [..., 'rest_framework', ]
- 3- creating model and serializer 
    serializer is the same as Form class.
- 4- write views and use serializer ( is_valid(), save() )
- 5- view classes can inheretance from APIView or use mixin or generic-class moduke
- 6- use views in urls.py like this:
  from .views import ClassName
  path('routeName', ClassName.as_view(), name='name')

# How to authorize APIs?

- 1- In views.py add this:
- from rest_framework.permissions import IsAuthenticated
- at the top af the view class add this line:
  class className(APIView):
      permission_class = ( IsAuthenticated, ) or [ IsAuthenticated, ]
- 2- enter these commands on terminal:
  - python manage.py migrate
  - python manage.py flush
  - python manage.py createsuperuser
- 3- add it in INSTALLED_APP -> [..., 'rest_framework.authtoken', ]
- 4- add REST_FRAMEWORK = {} dictionary in settings.py file.
    - REST_FRAMEWORK = { 
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication'
         ] 
     } 
- 5- with this command you can make token for a user:
    - python manage.py drf_create_token username
- 6- add these route in urls.py make token accable for client:
   -  from rest_framework.authtoken.views import obtain_auth_token
    - path('token/', obtain_auth_token, name='obtain_token')
