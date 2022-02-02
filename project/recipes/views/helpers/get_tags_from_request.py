from recipes.models import Tag


def get_tags_from_request(request):
    '''
    Get user's chosen tags from request.POST.
    '''
    if request.method == 'POST':
        tags = Tag.objects.filter(
            slug__in=dict(request.POST).get('tags', [])
        )
        return tags
    return []
