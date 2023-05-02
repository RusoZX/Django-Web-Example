import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Post, PostLike
@login_required
def api_add_post(request):
    data = json.loads(request.body)
    description = data.get('description')

    post = Post.objects.create(descripcion=description, created_by=request.user)

    return JsonResponse({'success': True})

@login_required
def api_add_like_post(request):
    data =json.loads(request.body)
    post_id = data['post_id']

    if not PostLike.objects.filter(post_id=post_id).filter(created_by=request.user).exists():
        like = PostLike.objects.create(post_id=post_id, created_by=request.user)
    
    return JsonResponse({'success': True})
