from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

from django.urls import reverse,reverse_lazy
from django.views import generic
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.
class DeleteGroup(generic.DeleteView):
    model=Group
    success_url = reverse_lazy("groups:all")

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model=Group

class ListGroup(generic.ListView):
    print("listed View")
    model=Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    print("IN JOIN")
    def get_redirect_url(self, *args, **kwargs):
        print("IN JOIN11")
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})


    def get(self, request, *args, **kwargs):
        print("IN JOIN2")
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    print("in leave G")
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.GroupMember.DoesNotExist:
                messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)
