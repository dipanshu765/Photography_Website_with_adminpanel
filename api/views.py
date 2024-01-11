from rest_framework.decorators import api_view
from rest_framework.response import Response
from pages.models import Content, Team, Gallery
from blog.models import Blog
from contact.models import Contact
from .serializers import ContentSerializer, TeamSerializer, GallerySerializer, BlogSerializer, ContactSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/content',
        'GET /api/blog',
        'GET /api/gallery',
        'GET /api/team',
        'GET /api/contact',
    ]
    return Response(routes)


@api_view(['GET'])
def getContent(request):

    content = Content.objects.all()
    serializer = ContentSerializer(content, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTeam(request):

    team = Team.objects.all()
    serializer = TeamSerializer(team, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getGallery(request):

    gallery = Gallery.objects.all()
    serializer = GallerySerializer(gallery, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getBlog(request):

    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTeam(request):

    team = Team.objects.all()
    serializer = TeamSerializer(team, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getContact(request):

    contact = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)




