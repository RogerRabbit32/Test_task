from rest_framework import generics
from .serializers import *
from django.http import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from datetime import date, datetime


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.initial_data['phone'] or \
                not serializer.initial_data['login'] or \
                not serializer.initial_data['password'] or \
                not serializer.initial_data['name'] or \
                not serializer.initial_data['birth']:

            return Response({'detail': 'Please enter all required details: '
                                       'phone, login, password, name and date of birth ',
                             'status_code': 400}, status=400)

        try:
            user = User.objects.get(phone=f"{serializer.initial_data['phone']}")
            if user:
                return Response({'detail': 'User with this phone already exists',
                         'status_code': 400}, status=400)

        except:
            pass

        try:
            user = User.objects.get(login=f"{serializer.initial_data['login']}")
            if user:
                return Response({'detail': 'User with this login already exists',
                         'status_code': 400}, status=400)

        except:
            pass

        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        today = date.today()
        born = datetime.strptime(f"{serializer.data['birth']}", "%Y-%m-%d").date()
        if (today.year - born.year - ((today.month, today.day) < (born.month, born.day))) < 18:
            return Response({"detail": "You must be at least 18 years old",
                             "status_code": 400}, status=400, headers=headers)
        user = User.objects.create(**serializer.validated_data)
        user.save()
        pk = user.pk
        return Response({'id': pk}, status=201, headers=headers)


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        if 'id' in self.request.query_params:
            filter_kwargs = {'id': self.request.query_params['id']}
        else:
            raise Http404('Missing required parameters')

        obj = get_object_or_404(queryset, **filter_kwargs)

        return obj


class UserLogin(generics.GenericAPIView):

    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if not serializer.initial_data['login'] or not serializer.initial_data['password']:
            return Response({'detail': 'Please enter both login and password',
                             'status_code': 400}, status=400)
        try:
            user = User.objects.get(login=serializer.initial_data['login'],
                                password=serializer.initial_data['password'])
            pk = user.pk
            return Response({'id': pk}, status=200)

        except:
            raise Http404('User not found')
