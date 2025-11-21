from modeltranslation.translator import register, TranslationOptions
from .models import Category,SubCategory,Product

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('sub_category_name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name','description', )