from django.http import JsonResponse

def send_json(request):
 
 data =[{'name': 'Tugba', 'email': 'tugba@example.org'},
            {'name': 'Can', 'email': 'can@example.org'}]
 return JsonResponse(data,safe = False )
