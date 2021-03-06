from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from track.models import Track, Course, Unit, Lecture, CourseMember, \
			 Category, Article, Practice

from track.api.serializers import (
	TrackSerializer,
	CourseSerializer,
	UnitSerializer,
	LectureSerializer,
	CourseMemberSerializer,
	CategorySerializer,
	ArticleSerializer,
	PracticeSerializer
	)


# get & post manualy
# from rest_framework.views import APIView
# from rest_framework import status

# class TrackList(APIView):
# 	def get(self, request, format=None):
# 		tracks = Track.objects.all()
# 		serializer = TrackSerializer(tracks, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = TrackSerializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)

# track

class TrackList(ListAPIView):
	queryset = Track.published.all()
	serializer_class = TrackSerializer

class TrackDetail(RetrieveAPIView):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer

######################################

# course

class CourseList(ListAPIView):
	queryset = Course.published.all()
	serializer_class = CourseSerializer

class CourseDetail(RetrieveAPIView):
	queryset = Course.published.all()
	serializer_class = CourseSerializer

######################################

# unit

class UnitList(ListAPIView):
	queryset = Unit.published.all()
	serializer_class = UnitSerializer

class UnitDetail(RetrieveAPIView):
	queryset = Unit.published.all()
	serializer_class = UnitSerializer

#######################################

# lecuture

class LectureList(ListAPIView):
	queryset = Lecture.published.all()
	serializer_class = LectureSerializer

class LectureDetail(RetrieveAPIView):
	queryset = Lecture.published.all()
	serializer_class = LectureSerializer

#######################################

# Coursemember

class CourseMemberList(ListAPIView):
	queryset = CourseMember.objects.all()
	serializer_class = CourseMemberSerializer

class CourseMemberDetail(RetrieveAPIView):
	queryset = CourseMember.objects.all()
	serializer_class = CourseMemberSerializer

#######################################

# category

class CategoryList(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryDetail(RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

#######################################

# article

class ArticleList(ListAPIView):
	queryset = Article.published.all()
	serializer_class = ArticleSerializer

class ArticleDetail(RetrieveAPIView):
	queryset = Article.published.all()
	serializer_class = ArticleSerializer

#######################################

# practice

class PracticeList(ListAPIView):
	queryset = Practice.published.all()
	serializer_class = PracticeSerializer

class PracticeDetail(RetrieveAPIView):
	queryset = Practice.published.all()
	serializer_class = PracticeSerializer

# The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions,
# by mixing in the behavior of the various mixin classes.

# The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(),
# .partial_update(), and .destroy().

# Example

# Because ModelViewSet extends GenericAPIView, you'll normally need to provide at least
# the queryset and serializer_class attributes. For example:

# from rest_framework import viewsets

# class TrackViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing accounts.
#     """
#     queryset = Track.published.all()
#     serializer_class = TrackSerializer
