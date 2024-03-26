from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Comentario


def home(request):

    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)


def detalhe_post(request, post_id):

    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
    }

    return render(request, 'blog/post_detalhes.html', context)


def blog(request):
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)


def comentar(request, post_id):
    comentario = request.POST.get('comentario')
    perfil = User.objects.all().first().perfil
    post = Post.objects.get(pk=post_id)

    comentario = Comentario(texto=comentario, perfil=perfil, post=post)
    comentario.save()
    response = HttpResponse()
    response["HX-Redirect"] = f"http://127.0.0.1:8000/posts/{post_id}/detalhe_post"
    return response

    # context = {
    #     'post': post,
    # }
    # return render(request, 'blog/post_detalhes.html', context)


def comentar_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comentarios = Comentario.objects.filter(post=post)
    context = {
        'post': post,
        'comentarios': comentarios
    }
    return render(request, "social/htmx_modal_comentario.html", context)


def deletar_comentario(request, comentario_id):
    post = Comentario.objects.get(pk=comentario_id).post
    comentario = Comentario.objects.get(pk=comentario_id)
    comentario.delete()
    comentarios = Comentario.objects.filter(post=post)
    response = HttpResponse()
    # response["HX-Redirect"] = request.path
    response["HX-Redirect"] = f"http://127.0.0.1:8000/posts/{post.id}/detalhe_post"
    return response


def editar_comentario(request, comentario_id):
    post = Comentario.objects.get(pk=comentario_id).post
    comentario = Comentario.objects.get(pk=comentario_id)
    context = {
        'post': post,
        'comentario': comentario
    }

    if request.method == "GET":
        return render(request, "social/modal_comentario_editar.html", context)
    elif request.method == "POST":
        comentario.texto = request.POST.get('comentario')
        comentario.save()
        response = HttpResponse()
        # response["HX-Redirect"] = request.path
        response["HX-Redirect"] = f"http://127.0.0.1:8000/posts/{post.id}/detalhe_post"
        return response
