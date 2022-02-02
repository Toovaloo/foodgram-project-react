from recipes.models import Tag


def get_checked_tags(query):
    '''
    Takes request.GET and returns tags checked by user or all tags existing.
    '''
    checked_tags = Tag.objects.filter(slug__in=query.getlist('tag'))
    return checked_tags or Tag.objects.all()
