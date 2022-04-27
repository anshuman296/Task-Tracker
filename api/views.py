from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateTeam(request):
    user = request.user
    if user.team_leader == True:
        if request.method == 'POST':
            jsondata = JSONParser().parse(request)
            serializer = TeamSerializer(data=jsondata)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'True', 'msg': 'Team created successfully'})
            else:
                return JsonResponse(serializer.errors, safe=False)
    else:
        return Response({'success': 'False', 'msg': 'Authentication failed'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Check_Availability(request, id):
    user = request.user
    if user.team_leader:
        json = []
        if request.method == 'GET':
            queryset = CustomUser.objects.filter(team_members=id)
            for members in queryset:
                member = CustomUser.objects.get(id=members.id)
                serializer = UserSerializer(member)
                json.append(serializer.data)
        return Response({'success': 'True', 'data': json})
    else:
        return Response({'success': 'False', 'msg': 'Authentication failed'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tas(request):
    user = request.user
    if user.team_leader:
        if request.method == 'POST':
            jsondata = JSONParser().parse(request)
            serializer = TaskSerializer(data=jsondata)
            member_id = jsondata['team_member']
            assigned_status = CustomUser.objects.get(id=member_id)
            assigned = assigned_status.assigned
            if assigned:
                return Response({'success': 'False', 'msg': 'Team member not available'})
            else:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'success': 'True', 'msg': 'Task created successfully'})
                else:
                    return JsonResponse(serializer.errors, safe=False)
    else:
        return Response({'success': 'False', 'msg': 'Authentication failed'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateTask(request, id):
    user = request.user

    if request.method == 'POST':
        task_id = task.objects.get(id=id)
        jsondata = JSONParser().parse(request)
        serializer = TaskSerializer(task_id, data=jsondata, partial=True)
        if user.team_leader:
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'True', 'msg': 'Task updated successfully'})
            else:
                return Response({'failed': 'failed'})
        else:
            allowed = ['assigned', 'in_progress', 'under_review', 'done']
            check_params = (list(jsondata))
            for ele in allowed:
                if ele == check_params[0]:
                    # serializer = TaskSerializer(task_id, data=jsondata, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({'success': 'True', 'msg': 'Task updated successfully'})
                    else:
                        return Response({'failed': 'failed'})
                else:
                    return Response({'success': 'False', 'msg': 'Forbidden'})
    else:
        return Response({'success': 'True', 'msg': 'Task updated successfully'})



