from django import template

from blog.models import Post, Tag

register = template.Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/tags_tpl.html')
def get_tags(cnt=3):
    tags = Tag.objects.all()
    return {'tags': tags}
