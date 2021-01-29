"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from product.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="home"),
    path("test/", test, name = "test"),
    path("go/", go, name = "go"),
    path("test3/", third, name = "test3"),
    path("add/", addToDo),
    path("remove/", removeToDo),
    path("update/", updateToDo),
    path("books/", bookGetAll),
    path("addtodo", addToDo, name = "add-todo"),
    path("removeToDo/<id>/", removeToDo, name = "delete-todo"),
    path("markToDo/<id>/", markToDo, name = "mark-todo"),
    path("unmarkToDo/<id>/", unmarkToDo, name = "unmark-todo"),
    path("checkedToDo/<id>/", checkedToDo, name = "checked-todo"),
    path("bookIsFarovite/<id>/", bookIsFarovite, name = "bookIsFarovite"),
    path("deleteBook/<id>/", deleteBook, name = "deleteBook"),
    path("bookDetails/<id>/", bookDetails, name = "bookDetails"),

    path("book-add/", bookAdd, name = "book-add"),

    path("book_add/", book_add)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
