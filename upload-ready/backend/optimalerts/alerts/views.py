from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from django.shortcuts import get_object_or_404
from .models import Employee, Alert
from .serializers import AlertSerializer

def direct_reports(manager_id):
    return list(Employee.objects.filter(reports_to=manager_id).values_list('id', flat=True))

def subtree_reports_simple(manager_id):
    # simple BFS-style expansion without cycle detection (junior-friendly)
    queue = direct_reports(manager_id)[:]
    idx = 0
    while idx < len(queue):
        emp = queue[idx]
        idx += 1
        children = direct_reports(emp)
        for c in children:
            if c not in queue:
                queue.append(c)
    return queue

class AlertsList(APIView):
    def get(self, request):
        manager_id = request.query_params.get("manager_id")
        if not manager_id:
            return Response({"detail":"manager_id required"}, status=http_status.HTTP_400_BAD_REQUEST)
        if not Employee.objects.filter(id=manager_id).exists():
            return Response({"detail":"manager not found"}, status=http_status.HTTP_404_NOT_FOUND)

        scope = request.query_params.get("scope", "direct")
        q = request.query_params.get("q")
        severity = request.query_params.get("severity")

        if scope not in ("direct","subtree"):
            return Response({"detail":"invalid scope"}, status=http_status.HTTP_400_BAD_REQUEST)

        if scope == "direct":
            emp_ids = direct_reports(manager_id)
        else:
            emp_ids = subtree_reports_simple(manager_id)

        qs = Alert.objects.filter(employee__id__in=emp_ids)
        if severity:
            qs = qs.filter(severity=severity)
        if q:
            qs = qs.filter(employee__name__icontains=q)

        qs = qs.order_by("-created_at")
        serializer = AlertSerializer(qs, many=True)
        return Response(serializer.data)

class AlertDismiss(APIView):
    def post(self, request, pk):
        alert = get_object_or_404(Alert, pk=pk)
        alert.status = "dismissed"
        alert.save()
        serializer = AlertSerializer(alert)
        return Response(serializer.data)
