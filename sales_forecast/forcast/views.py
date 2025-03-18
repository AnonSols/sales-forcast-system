
import csv
from django.http import HttpResponse
from django.utils import timezone  # Changed from datetime
from .utils import forcast_sales  # NEW IMPORT
from .models import HistoricalData
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class SalesListView(LoginRequiredMixin,ListView):
   
    template_name = 'sales_list.html'
    context_object_name = 'sales_records'
    ordering = ['-date']
    login_url = '/login/'

    FORECAST_DAYS = 7

    # def get_queryset(self):
    #     return HistoricalData.objects.all().order_by('-date')
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return HistoricalData.objects.filter(
                Q(product_category__icontains=query) | Q(sales__icontains=query)
            ).order_by('-date')
        return HistoricalData.objects.all().order_by('-date')
    
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sales_records = self.get_queryset()

        total_sales = sum(r.sales for r in sales_records)
        avg_sales = total_sales / len(sales_records) if sales_records else 0

        # Get historical sales data
        historical_values = list(sales_records.values_list('sales', flat=True))
        historical_dates = [record.date.strftime("%b %d") for record in sales_records]
        

        # Update context
        context.update({
            'total_sales': total_sales,
            'average_sales': avg_sales,
            'current_date': timezone.now().strftime("%B %d, %Y"),
            'forcast_dates': [
                (timezone.now() + timezone.timedelta(days=i)).strftime("%b %d")
                for i in range(1, self.FORECAST_DAYS + 1)
            ],
            'forcast_values': forcast_sales(historical_values, steps=self.FORECAST_DAYS),
            'historical_dates': historical_dates,  # Add historical dates
            'historical_values': historical_values,  # Add historical values
            'forecast_days':self.FORECAST_DAYS
        })
        return context

def export_sales_csv(request):
    """Export sales records to a CSV file."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_records.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Category', 'Sales'])

    sales_records = HistoricalData.objects.all()
    for record in sales_records:
        writer.writerow([record.date, record.product_category, record.sales])

    return response