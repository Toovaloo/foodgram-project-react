from re import sub

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def choose_tag(context, tag):
    '''
    Appends tag=<tag.slug> parameter to a URL if no such tag was already
    passed otherwise deletes such tag parameter from URL.
    '''
    request = context['request']
    if request.GET:
        if tag not in request.GET.getlist('tag'):
            return request.get_full_path() + f'&tag={tag}'
        else:
            result_url = sub(rf'[?&]tag={tag}', '', request.get_full_path())
            if result_url.find('?') != -1:
                return result_url
            return sub('&', '?', result_url, count=1)
    return request.get_full_path() + f'?tag={tag}'


@register.simple_tag(takes_context=True)
def preserve_tags(context, page_number):
    '''
    Given a request like this /?page=1&tags=lunch&tags=dinner returns a URL
    with page number changed preserving other parameters however.
    '''
    request = context['request']
    query_params = request.GET.copy()
    query_params['page'] = page_number
    return '?' + query_params.urlencode()
