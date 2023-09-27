from rest_framework.views import APIView
from officemanager.api.V1.permissions import IsSuperuserOrOfficeManager, IsSuperuserOrOwnOfficeManager
from accounts.models import OfficeManager, User, School, Student
from request.models import Request
from request.serializers import RequestSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from notification.models import Notification
from .serializers import NotificationSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser

class ListRequest(APIView):
    permission_classes = [IsSuperuserOrOfficeManager]

    @swagger_auto_schema(
        operation_description="""This endpoint allows office_manager to see list off request.

            The response will contain a success message including these fields:
                - status
                - sender
                - receiver
                off all request
                """,
        operation_summary="endpoint for list of request",

        responses={
            '200': 'ok',
            '404': 'not found'
        }
    )
    def get(self, request):
        try:
            office_manager = OfficeManager.objects.get(id=request.user.id)
        except OfficeManager.DoesNotExist:
            return Response({'message': 'office_manager does not exist'}, status=status.HTTP_404_NOT_FOUND)
        req = Request.objects.filter(receiver=office_manager)
        ser_data = RequestSerializer(req, many=True)
        if req:
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "شما در حال حاضر درخواستی در سیستم ندارید"}, status=status.HTTP_404_NOT_FOUND)


class GetRequest(APIView):
    permission_classes = [IsSuperuserOrOfficeManager]

    @swagger_auto_schema(
        operation_description="""This endpoint allows office_manager to get information off one request.

            The request should include the id off request.

            The response will contain a success message including these fields:
                - status
                - sender
                - refresh
                - receiver""",
        operation_summary="endpoint for get all of information of one request",
        responses={
            '200': 'ok',
            '404': 'not found'
        }
    )
    def get(self, request, id):
        try:
            office_manager = OfficeManager.objects.get(id=request.user.id)
        except OfficeManager.DoesNotExist:
            return Response({'message': 'office_manager does not exist'}, status=status.HTTP_404_NOT_FOUND)
        req = Request.objects.filter(receiver=office_manager, id=id)
        ser_data = RequestSerializer(req, many=True)
        if req:
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "شما در حال حاضر درخواستی در سیستم ندارید"}, status=status.HTTP_404_NOT_FOUND)


class RejectRequest(APIView):
    permission_classes = {IsSuperuserOrOwnOfficeManager}

    @swagger_auto_schema(
        operation_description="""This endpoint allows office_manager to reject a request.

             The request should include the id of request
             this function check  notification does not accept before
             after reject this function and sent a notification to student
             """,
        operation_summary="endpoint for reject request",
        responses={
            '200': 'ok',
            '400': 'bad request'
        }
    )
    def post(self, request, pk):

        req = Request.objects.filter(id=pk).first()
        if req:
            office_manager = req.receiver
            student = req.sender
            self.check_object_permissions(request, office_manager)
            if req.status != 'a':
                req.status = 'na'
                req.save()
                Notification.objects.create(code=401, sender=request.user, receiver=User.objects.get(id=student.id))
                return Response({'message': 'request is rejected successfully'}, status=status.HTTP_200_OK)
            return Response({'message': 'this request accept before'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'not exist request by this id'})


class AcceptRequest(APIView):
    permission_classes = [IsSuperuserOrOwnOfficeManager]

    @swagger_auto_schema(
        operation_description="""This endpoint allows office_manager to accept a request.

             The request should include the id of request and id of school
             this function first check the school in region of office_manager second 
             check  does not not accept before 
             third check student not join in any school before and school capacity larger than zero  
             after accept this function and assign student to a school 
             and send a notification to student whit content your request accept
             """,
        operation_summary="endpoint for accept request and assign student to one school",
        responses={
            '200': 'ok',
            '400': 'bad request'
        }
    )
    def post(self, request, school_id, request_id):
        try:
            req = Request.objects.get(id=request_id)
        except Request.DoesNotExist:
            return Response({'message': 'request does not exist'}, status=status.HTTP_404_NOT_FOUND)
        office_manager = req.receiver
        student = req.sender
        self.check_object_permissions(request, office_manager)
        try:
            school = School.objects.get(pk=school_id)
        except School.DoesNotExist:
            return Response({'message': 'school does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if school.office_manager == office_manager:
            if req.status != 'na':
                if student.school2 is None and school.capacity > 0:
                    req.status = 'a'
                    req.save()
                    student.school2 = school
                    student.save()
                    capacity = school.capacity
                    capacity -= 1
                    school.capacity = capacity
                    school.save()
                    Notification.objects.create(code=501, sender=request.user, receiver=User.objects.get(id=student.id))
                    return Response({'message': 'this request accept and student assign to one school and sent a '
                                                'notification to student'},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'this school not assign to this student'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'this request reject before'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'this school not in this office_manager region'},
                            status=status.HTTP_400_BAD_REQUEST)


class CancelRequest(APIView):
    @swagger_auto_schema(
        operation_description="""This endpoint allows student to cancel his request

              This view first check a student use this function then get a request from this student with status sent 
              means accept and not accept then get notification of this request and then deleted
              """,
        operation_summary="endpoint for cancel request",
        responses={
            '200': 'ok',
            '400': 'bad request'
        }
    )
    def post(self, request):
        student = Student.objects.filter(id=request.user.id).first()
        if student:
            req = Request.objects.filter(sender=student, status='s').last()
            if req:
                notification = Notification.objects.filter(sender=User.objects.get(id=student.id),
                                                           receiver=User.objects.get(id=req.receiver.id)).last()
                req.delete()
                notification.delete()
                return Response({'message': 'request and notification deleted'})
            else:
                return Response({'message': 'you have not request for canceling'})
        else:
            return Response({'message': 'you are not student'})


class SuperUserListRequest(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        requests = Request.objects.all()
        ser_data = NotificationSerializer(requests, many=True)
        return Response({"data": ser_data.data}, status=status.HTTP_200_OK)
