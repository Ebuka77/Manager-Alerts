from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import json
from alerts.models import Employee, Alert
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = "Seed db from seed_data.json"

    def handle(self, *args, **kwargs):
        #seed_path = Path(settings.BASE_DIR) / "seed_data.json"
        seed_path = "C:/Users/User/Desktop/assessment/manager-alerts-junior/backend/optimalerts/alerts/seed_data.json"
        with open(seed_path) as f:
            data = json.load(f)
        Employee.objects.all().delete()
        Alert.objects.all().delete()
        for e in data.get("employees", []):
            Employee.objects.create(id=e["id"], name=e["name"], reports_to=e.get("reports_to"))
        for a in data.get("alerts", []):
            emp = Employee.objects.get(id=a["employee_id"])
            Alert.objects.create(
                id=a["id"],
                employee=emp,
                severity=a["severity"],
                category=a["category"],
                created_at=parse_datetime(a["created_at"]),
                status=a["status"]
            )
        self.stdout.write("Seeded")
        [
  {"message": "Server restarted", "created_at": "2025-11-19T00:00:00Z"},
  {"message": "New user signup", "created_at": "2025-11-19T01:00:00Z"}
]
