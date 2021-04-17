from PIL import Image
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.forms import ModelChoiceField, ModelForm, ValidationError
from .models import *
from .abstracts import Categories, Product


# Register your models here.


class ProductAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:13px;">Upload image with a min resolution of {}x{}px and a max of {}x{'
            '}px and size of max 3MB</span>'.format(
                *Product.MIN_RESOLUTION, *Product.MAX_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Image size should not exceed 3MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Image resolution less than the minimum!')
        elif img.height > max_height or img.width > max_width:
            raise ValidationError('Image resolution is greater than maximum!')
        return image


class NotebookAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return ModelChoiceField(Categories.objects.filter(slug = 'notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return ModelChoiceField(Categories.objects.filter(slug = 'smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Categories)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Notebook, NotebookAdmin)
