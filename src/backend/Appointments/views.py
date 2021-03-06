from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework import generics, mixins
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class AppointmentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
    def put(self,request):
        return self.create(request)

class AppointmentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    #authentication_classes = [TokenAuthentication,BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)


# class ReportList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer
#     # authentication_classes = [TokenAuthentication,BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#
# class ReportDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer
#     # authentication_classes = [TokenAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request):
#         return self.destroy(request, pk)

