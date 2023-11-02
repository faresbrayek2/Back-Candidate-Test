from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import LabelSerializer, DocumentSerializer, AnnotationSerializer


labels = []
documents = []
annotations = []

class LabelViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            label = serializer.validated_data  # Create a new label instance
            labels.append(label)  # Add the label to the in-memory list
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            document = serializer.validated_data  # Create a new document instance
            documents.append(document)  # Add the document to the in-memory list
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnnotationViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = AnnotationSerializer(annotations, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AnnotationSerializer(data=request.data)
        if serializer.is_valid():
            annotation = serializer.validated_data  # Create a new annotation instance
            annotations.append(annotation)  # Add the annotation to the in-memory list
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def label_view(request):
    if request.method == 'GET':
        # Your label retrieval logic
        return Response({"message": "Label retrieved successfully"})
    elif request.method == 'POST':
        # Your label creation logic
        return Response({"message": "Label created successfully"})
def document_view(request):
    if request.method == 'GET':
        # Your document retrieval logic
        return Response({"message": "Document retrieved successfully"})
    elif request.method == 'POST':
        # Your document creation logic
        return Response({"message": "Document created successfully"})