from register.models import User
from register.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserList(APIView):
    """[summary]

    Arguments:
        APIView {[type]} -- [description]
    """

    def get(self, request, format=None):
        """[summary]

        Arguments:
            request {[type]} -- [description]

        Keyword Arguments:
            format {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """[summary]

        Arguments:
            request {[type]} -- [description]

        Keyword Arguments:
            format {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        data = request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                name = User.objects.get(name=request.data["name"])
                return Response({"message": "User already exists"}, status=status.HTTP_409_CONFLICT)
            except User.DoesNotExist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """[summary]

    Arguments:
        APIView {[type]} -- [description]
    """

    def get(self, request, id, format=None):
        """[summary]

        Arguments:
            request {[type]} -- [description]
            id {[type]} -- [description]

        Keyword Arguments:
            format {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "user does not exists"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        """[summary]

        Arguments:
            request {[type]} -- [description]
            id {[type]} -- [description]

        Keyword Arguments:
            format {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        """[summary]

        Arguments:
            request {[type]} -- [description]
            id {[type]} -- [description]

        Keyword Arguments:
            format {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """

        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "user does not exists"}, status=status.HTTP_404_NOT_FOUND)
