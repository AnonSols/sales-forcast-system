

from django.utils import timezone  # Changed from datetime
from .utils import forcast_sales  # NEW IMPORT
from .models import HistoricalData
from django.views.generic import ListView

class SalesListView(ListView):
   
    template_name = 'sales_list.html'
    context_object_name = 'sales_records'
    ordering = ['-date']

    FORECAST_DAYS = 7
    def get_queryset(self):
        return HistoricalData.objects.all().order_by('-date')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     sales_records = self.get_queryset();


    #     total_sales = sum(r.sales for r in sales_records)
    #     avg_sales = total_sales/len(sales_records) if sales_records else 0

    #     historical_values = list(sales_records.values_list('sales', flat=True))
    #     historical_dates = [record.date.strftime("%b %d") for record in sales_records]


    #     # Get last 30 days of sales data (ordered)
    #     sales_data = self.get_queryset().values_list('sales', flat=True)
        
    #     # NEW CONTEXT VARIABLES
    #     # # In your view's get_context_data()
    #     # context['historical_dates'] = [record.date.strftime("%b %d") for record in sales_records]

    #     context.update({
    #         'total_sales': total_sales,
    #         'average_sales': avg_sales, 
    #         'current_date': timezone.now().strftime("%B %d, %Y"),
    #         'forcast_dates': [
    #             (timezone.now() + timezone.timedelta(days=i)).strftime("%b %d") 
    #             for i in range(1,self.FORECAST_DAYS + 1)  # Next 3 days
    #         ],
    #         'forcast_values': forcast_sales(sales_data, steps=self.FORECAST_DAYS),
    #          'historical_dates': historical_dates,  
    #         'historical_values': historical_values 
    #     })
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     sales_records = self.get_queryset()

    #     total_sales = sum(r.sales for r in sales_records)
    #     avg_sales = total_sales / len(sales_records) if sales_records else 0

    #     # Get historical sales data
    #     historical_values = list(sales_records.values_list('sales', flat=True))
    #     historical_dates = [record.date.strftime("%b %d") for record in sales_records]

    #     # Update context
    #     context.update({
    #         'total_sales': total_sales,
    #         'average_sales': avg_sales,
    #         'current_date': timezone.now().strftime("%B %d, %Y"),
    #         'forcast_dates': [
    #             (timezone.now() + timezone.timedelta(days=i)).strftime("%b %d")
    #             for i in range(1, self.FORECAST_DAYS + 1)
    #         ],
    #         'forcast_values': forcast_sales(historical_values, steps=self.FORECAST_DAYS),
    #         'historical_dates': historical_dates,  # Add historical dates
    #         'historical_values': historical_values  # Add historical values
    #     })
    #     return context

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