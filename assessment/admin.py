from django.contrib import admin
from .models import Requirement, Recommendation
from django.utils.html import format_html


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('title', 'requirement_class')


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('requirement', 'linked_advice')

    def linked_advice(self, obj):
        keyword = "SBOM"
        if keyword in obj.advice:
            return format_html(
                obj.advice.replace(
                    keyword,
                    f'<a href="https://www.google.com/search?q={keyword}" target="_blank">{keyword}</a>'
                )
            )
        return obj.advice

    linked_advice.short_description = 'Advice with AI Link'
