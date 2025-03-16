from django.db import models
from django.core.validators import MinValueValidator

class HistoricalData(models.Model):
    """
    Stores historical sales data
    Fields:
    - date: The date of the sales record
    - product_category: Category of the product (e.g. Electronics, Clothing)
    - sales: Dollar amount of sales (must be positive)
    """
    date = models.DateField(help_text="Date of sales entry")
    product_category = models.CharField(
        max_length=100,
        help_text="Product category (e.g. Electronics, Clothing)"
    )
    sales = models.FloatField(
        validators=[MinValueValidator(0.0)],
        help_text="Sales amount in USD"
    )

    def __str__(self):
        return f"{self.date} - {self.product_category}: ${self.sales}"

    class Meta:
        ordering = ['-date']  # Newest entries first by default
        verbose_name_plural = "Historical Sales Data"