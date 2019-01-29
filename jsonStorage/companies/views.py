from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organisation
from .serializers import OrganisationSerializer

# Create your views here.
class OrganisationList(APIView):
	def get(self, request):
		Organisations = Organisation.object.all()
		serializer = OrganisationSerializer(Organisations, many=True)
		return Response(serializer.data)

	def post(self):
		pass
