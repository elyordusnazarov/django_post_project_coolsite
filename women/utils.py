from .models import Category


menu=[
    {'title':"О сайте",'url_name':'about'},
    {'title':"Добавитъ статъю",'url_name':'add_page'},
    {'title':"Обратная связь",'url_name':'contact'},
 

]

class DataMixin:
    paginate_by = 3
    def get_user_context(self,**kwargs):
        context=kwargs       
        cats=Category.objects.all()

        user_menu =menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu']= user_menu
        
        context['cats']= cats 
        if  'cats_selected' not in context:
            context['cat_selected']=0
        return context
