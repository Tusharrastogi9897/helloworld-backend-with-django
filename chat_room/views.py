from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token


def index(request):
    return render(request, "index.html")

class TokenAPI(APIView):

    def put(self, request):
        
        if "email" in request.data and "password" in request.data:
            user_ = User.objects.filter(email=request.data["email"])
            if user_:
                user_ = user_[0]
                pCheck = user_.check_password(request.data["password"])
                if pCheck:
                    token_, _ = Token.objects.get_or_create(user=user_)
                    return Response(dict(token=token_.key), status=status.HTTP_200_OK)
                else:
                    return Response({"error": "User credentials are incorrect!"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"error": "User credentials are incorrect!"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "User credentials are not given!"}, status=status.HTTP_403_FORBIDDEN)

class GetListAPI(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_ = None
    model_ = None

    def get(self, request, page):
        list_ = self.model_.objects.all()
        serializer = self.serializer_(list_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)