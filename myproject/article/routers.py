from rest_framework import router
from article.viewsets import ArticleViewSet

router = router.DefaultRouter()
router.register(r'article', ArticleViewSet)