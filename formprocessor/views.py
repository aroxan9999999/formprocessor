from django.http import JsonResponse
from .models import FormTemplate
import json
import re


def validate_field_type(value):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    phone_regex = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
    date_regex = r'^(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$'

    if re.match(email_regex, value):
        return 'email'
    elif re.match(phone_regex, value):
        return 'phone'
    elif re.match(date_regex, value):
        return 'date'
    else:
        return 'text'


def get_form(request):
    if request.method == 'POST':
        data = request.POST.dict()
        field_types = {field: validate_field_type(value) for field, value in data.items()}

        for template in FormTemplate.objects.all():
            template_fields = json.loads(template.fields)
            if all(field in data and field_types[field] == template_fields[field] for field in template_fields):
                return JsonResponse({'matched_template': template.name})

        return JsonResponse(field_types)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)