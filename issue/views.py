from rest_framework import viewsets, mixins
from common.authentication import AuthenticationMixin
from issue.models import Issue
from issue.serializers import IssueSerializer


class IssueViewSet(
    AuthenticationMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
