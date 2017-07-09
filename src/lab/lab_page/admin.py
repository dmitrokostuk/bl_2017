from django.contrib import admin
from .models import Post,Travels


class PostAdmin(admin.ModelAdmin):
    models = Post
    list_display =['title', 'timestamp','author']
    list_filter = ['timestamp',]

    search_fields = ['title','timestamp']

    class Meta:
        model = Post
admin.site.register(Post, PostAdmin)

class PostTravels(admin.ModelAdmin):
    models = Travels
    list_display =['title_region', 'region','district']
    list_filter = ['region',]

    search_fields = ['title_region','region']


    class Meta:
        model = Travels

admin.site.register(Travels,PostTravels)
"""
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
"""