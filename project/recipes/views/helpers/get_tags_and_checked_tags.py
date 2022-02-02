from recipes.models import Tag
from recipes.views.helpers import get_checked_tags


def get_tags_and_checked_tags(request):
    '''
    Takes request and returns tuple(tags, checked_tags).
    '''
    tags = Tag.objects.all()
    checked_tags = get_checked_tags(request.GET)
    return (tags, checked_tags)
