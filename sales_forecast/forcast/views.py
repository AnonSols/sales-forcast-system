

from django.utils import timezone  # Changed from datetime
from .utils import forecast_sales  # NEW IMPORT
from .models import HistoricalData
from django.views.generic import ListView

class SalesListView(ListView):
   
    template_name = 'sales_list.html'
    context_object_name = 'sales_records'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get last 30 days of sales data (ordered)
        sales_data = HistoricalData.objects.all().order_by('-date')[:30].values_list('sales', flat=True)
        
        # NEW CONTEXT VARIABLES
        context.update({
            'current_date': timezone.now().strftime("%B %d, %Y"),
            'forcast_dates': [
                (timezone.now() + timezone.timedelta(days=i)).strftime("%b %d") 
                for i in range(1,4)  # Next 3 days
            ],
            'forcast_values': forecast_sales(list(sales_data))
        })
        return context