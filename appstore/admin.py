from django.contrib import admin
from .models import Tag,Post,Profile
# Register your models here.


#register tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model=Tag

#register profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model=Profile


#registering posts model with admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model=Post

    list_display=(
        'id',
        'title',
        'subtitle',
        'slug',
        'published_date',
        'published',
    )
    list_filter=(
        'published',
        'published_date',
    )

    list_editable=(
        'title',
        'subtitle',
        'slug',
       # 'published_date',
        'published',
    )

    search_fields=(
        'title',
        'subtitle',
        'slug',
        'body',
    )
    prepopulated_fields={
        'slug':(
            'title',
            'subtitle',
        )
    }
    date_hierarchy='published_date'
    save_on_top=True

