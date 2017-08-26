from tastypie.resources import Resource
 
from .models import Produit
 
class AjaxSearchResource(Resource):
 
    class Meta:
        resource_name = 'ajaxsearch'
        allowed_methods = ['post']
 
    def post_listserche(self, request, **kwargs):
        phrase = request.POST.get('q')
        if phrase:
            posts = list(Produit.objects.filter(title__icontains=phrase).values('id', 'title'))
            return self.create_response(request, {'posts': posts})