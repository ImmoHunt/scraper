from django.contrib import admin
from .models import imggal
from .models import Test, Item, ItemSeries, ItemCategory, Comment, ChatUser
from tinymce.widgets import TinyMCE
from django.db import models


class TestAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["item_title", "item_published"]}),
		("URL", {"fields": ["item_slug"]}),
		("Series", {"fields": ["item_series"]}),
		("Content", {"fields": ["item_content"]})
	]
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
	}

admin.site.register(ItemSeries)
admin.site.register(ItemCategory)
admin.site.register(imggal)
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(ChatUser)
