from django.contrib import auth

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND
)

from account.models import User
from account.forms import SignUpForm
from api.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def sign_up(self, request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is None:
                user = User.objects.create_user(username=username,password=password)
                return Response(status=HTTP_201_CREATED) 
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def sign_in(self, request):
        username = request.GET.get('username','')
        password = request.GET.get('password','')

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user=user)
            return Response(UserSerializer(user).data, status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)  
            
        