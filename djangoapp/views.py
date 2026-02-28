from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    if request.method=="GET":
        info_people={
            "name":'Anjana',
            "age": 24,
            "place":"Thrissur"

        }
        return Response(info_people)
    elif request.method=="PUT":
        return Response("This is PUT method")
   
    elif request.method=="POST":
        return Response("This is POST method")


# python to json convert using serializer
@api_view(['POST','GET','PUT','PATCH','DELETE'])
def person(request):
    if request.method=="GET":
        persons=Person.objects.all()
        serializer=PersonSerializer(persons,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        dataval=request.data
        serializer=PersonSerializer(data=dataval)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method=="PUT":
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer=PersonSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
  
    elif request.method=="PATCH":
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer=PersonSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    else:
        data=request.data
        obj=Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"message":"invalid account"})

    