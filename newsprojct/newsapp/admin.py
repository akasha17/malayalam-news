# from django.contrib import admin
# from .models import News, Category, Advertisement

# # Admin for the News model
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'created_at', 'is_headline', 'is_latest', 'is_trending')
#     list_filter = ('category', 'is_headline', 'is_latest', 'is_trending')
#     search_fields = ('title', 'content')
#     # Optionally, you can add ordering and editable fields here for better admin management
#     ordering = ('-created_at',)  # Show latest news first

# # Admin for the Category model
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)  # Allow search by category name

# # Admin for the Advertisement model
# class AdvertisementAdmin(admin.ModelAdmin):
#     list_display = ('image_tag', 'link')  # Display an image thumbnail for easier admin experience

#     # Optionally, add a function to show a thumbnail in the admin
#     def image_tag(self, obj):
#         if obj.image:
#             return f'<img src="{obj.image.url}" width="100" />'
#         return ""
    
#     image_tag.allow_tags = True
#     image_tag.short_description = 'Image'

# # Register the models
# admin.site.register(News, NewsAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Advertisement, AdvertisementAdmin)
