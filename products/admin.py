from django.contrib import admin
from .models import Store, Product, PriceEntry, UserPoints
from django.utils.translation import gettext_lazy as _


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'address')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'barcode', 'created_at', 'updated_at')
    search_fields = ('name', 'barcode')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)


@admin.register(PriceEntry)
class PriceEntryAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'price', 'date_reported', 'reported_by', 'created_at', 'updated_at')
    search_fields = ('product__name', 'store__name', 'price')
    list_filter = ('store', 'product','date_reported')
    ordering = ('-date_reported', 'store', 'product')

class UserPointsListFiler(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("Points")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'total_points'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("0-100", _("0-100")),
            ("100-200", _("100-200")),
            ("200-300", _("200-300")),
            ("300-400", _("300-400")),
            ("400-500", _("400-500")),
            ("500-600", _("500-600")),
            ("600-700", _("600-700")),
            ("700-800", _("700-800")),
            ("800-900", _("800-900")),
            ("900-1000", _("900-1000")),
            ("1000+", _("1000+")),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == "0-100":
            return queryset.filter(
                total_points__gte=0,
                total_points__lte=100,
            )
        if self.value() == "100-200":
            return queryset.filter(
                total_points__gte=100,
                total_points__lte=200,
            )
        if self.value() == "200-300":
            return queryset.filter(
                total_points__gte=200,
                total_points__lte=300,
            )
        if self.value() == "300-400":
            return queryset.filter(
                total_points__gte=300,
                total_points__lte=400,
            )
        if self.value() == "400-500":
            return queryset.filter(
                total_points__gte=400,
                total_points__lte=500,
            )
        if self.value() == "500-600":
            return queryset.filter(
                total_points__gte=500,
                total_points__lte=600,
            )
        if self.value() == "600-700":
            return queryset.filter(
                total_points__gte=600,
                total_points__lte=700,
            )
        if self.value() == "700-800":
            return queryset.filter(
                total_points__gte=700,
                total_points__lte=800,
            )
        if self.value() == "800-900":
            return queryset.filter(
                total_points__gte=800,
                total_points__lte=900,
            )
        if self.value() == "900-1000":
            return queryset.filter(
                total_points__gte=900,
                total_points__lte=1000,
            )
        if self.value() == "1000+":
            return queryset.filter(
                total_points__gt=1000,
            )

@admin.register(UserPoints)
class UserPointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'created_at', 'updated_at')
    search_fields = ('user__username', 'total_points')
  #  list_filter = ('total_points', 'created_at')
    list_filter = [UserPointsListFiler]
    ordering = ('-total_points',)






