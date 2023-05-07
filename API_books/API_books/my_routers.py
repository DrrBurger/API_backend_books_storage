from rest_framework import routers

from book.views import BookViewSet, AuthorViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)


