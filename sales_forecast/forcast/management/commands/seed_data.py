# forcast/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from forcast.models import HistoricalData
from datetime import datetime, timedelta
import random

class Command(BaseCommand):  # Inherits from BaseCommand
    help = "Populates database with sample sales data"

    def handle(self, *args, **options):
        categories = ['Electronics', 'Clothing', 'Groceries']
        
        for i in range(30):  # Create 30 days of data
            HistoricalData.objects.create(
                date=datetime.now() - timedelta(days=30-i),
                product_category=random.choice(categories),
                sales=random.uniform(1000, 5000)
            )
        self.stdout.write(self.style.SUCCESS('✅ Successfully created 30 sales records!'))