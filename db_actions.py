from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment


def init():

    print(f'DB initialization started...')

    # Очистка объектов
    PostCategory.objects.all().delete()  # Удаление всех объектов PostCategory
    print(f'  PostCategories cleared: {PostCategory.objects.count()}')
    Category.objects.all().delete()  # Удаление всех объектов Category
    print(f'  Categories cleared: {Category.objects.count()}')
    Author.objects.all().delete()  # Удаление всех объектов Author
    print(f'  Authors cleared: {Author.objects.count()}')
    User.objects.all().delete()  # Удаление всех объектов User
    print(f'  Users cleared: {User.objects.count()}')
    print(f' Objects cleared.')

    print(f' Initializing new data...')

    # Создание пользователей и авторов
    User(username="user1").save()
    User(username="user2").save()
    User(username="comment_user1").save()
    User(username="comment_user2").save()
    print(f'   Users created: {User.objects.count()}')

    Author(user=User.objects.get(username="user1"), author_name="author1").save()
    Author(user=User.objects.get(username="user2"), author_name="author2").save()
    print(f'   Authors created: {Author.objects.count()}')
    print(f' Users and authors created.')

    print(f' Creating categories...')
    # Создание категорий
    c1 = Category(name="cat1")
    c1.save()
    c2 = Category(name="cat2")
    c2.save()
    c3 = Category(name="cat3")
    c3.save()
    c4 = Category(name="cat4")
    c4.save()
    print(f'   Categories created: {Category.objects.count()}')
    print(f' Categories created.')

    print(f' Creating posts...')

    # Создание первого поста
    print(f'   Creating Post 1...')
    a = Author.objects.get(author_name='author1')
    p = Post(post_type='0', author=a, post_header='PostHeader1', post_body='post_body1', rating=1)
    p.save()
    print(f'   Post 1 created.')

    # Присвоение категорий первому посту
    print(f'   Assigning categories to Post 1...')
    PostCategory(post=p, category=c1).save()
    PostCategory(post=p, category=c2).save()
    print(f'   Categories assigned to Post 1.')

    # Создание второго поста
    print(f'   Creating Post 2...')
    p = Post(post_type='1', author=a, post_header='PostHeader2', post_body='post_body2', rating=4)
    p.save()
    print(f'   Post 2 created.')

    # Присвоение категории второму посту
    print(f'   Assigning category to Post 2...')
    PostCategory(post=p, category=c3).save()
    print(f'   Category assigned to Post 2.')

    # Создание третьего поста
    print(f'   Creating Post 3...')
    a = Author.objects.get(author_name='author2')
    p = Post(post_type='1', author=a, post_header='NewsHeader3', post_body='news_body1', rating=5)
    p.save()
    PostCategory(post=p, category=c4).save()
    print(f'   Post 3 created.')

    print(f'   Posts created: {Post.objects.count()}')
    print(f' Posts created.')
    print(f' Data initialization complete.')

    # Создание комментариев
    print(f'  Creating comments...')
    p1 = Post.objects.get(post_header='PostHeader1')
    p2 = Post.objects.get(post_header='PostHeader2')
    u1 = User.objects.get(username='comment_user1')
    Comment(post=p1, user=u1, comment_text='Comment #1. Some comment text.', rating=1).save()
    u2 = User.objects.get(username='comment_user2')
    Comment(post=p1, user=u2, comment_text='Comment #2. Well said! Respect!', rating=2).save()

    Comment(post=p2, user=u1, comment_text='Comment #3. Some comment text.', rating=1).save()
    p2 = Post.objects.get(post_header='NewsHeader3')
    Comment(post=p2, user=u1, comment_text='Comment #4. First comment on the news.', rating=1).save()
    Comment(post=p2, user=u2, comment_text='Comment #5. Second comment on the news.', rating=2).save()

    print(f'   Comments created: {Comment.objects.count()}')
    print(f' Comments created.')

    print(f'DB initialization complete')


def acts():
    # Функция для выполнения действий

    init()

    # 1. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
    print('1. Updating likes and dislikes...')
    p1 = Post.objects.get(post_header='PostHeader1')
    p1.like()
    p1.dislike()
    p1.dislike()

    # 2. Обновить рейтинги пользователей.
    print('2. Updating user ratings...')
    print(' Updating user ratings...')
    for a in Author.objects.all():
        a.update_rating()
    # print(Author.objects.all().values('author_name', 'rating'))
    print(' User ratings updated.')

    # 3. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
    a = Author.objects.all().order_by('-rating')[:1][0]
    print(f"3. Best User (according to Forbes):")
    print(f' Username: {a.user.username}')
    print(f' Rating: {a.rating}')

    # 4. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
    #    основываясь на лайках/дислайках к этой статье.
    # лучший пост - аналог SELECT TOP 1 ... ORDER BY rating DESC
    print('4. Best Post:')
    p = Post.objects.all().order_by('-rating')[:1][0]
    print(f' Date added: {p.input_date_time.strftime("%d.%m.%Y %H:%M:%S")}')
    print(f' Author: {p.author.author_name}')
    print(f' Author rating: {p.author.rating}')
    print(f' Post title: "{p.post_header}"')
    print(f' Post preview: "{p.preview()}"')

    # 5. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
    cs = Comment.objects.filter(post=p)
    print(f'5. Comments on the post: {cs.count()}')
    n = 1
    for c in cs:
        print(f' Comment #{n}')
        print(f'  Comment date: {c.input_date_time.strftime("%d.%m.%Y %H:%M:%S")}')
        print(f'  User: {c.user.username}')
        print(f'  Comment rating: {c.rating}')
        print(f'  Comment text: {c.comment_text}')
        n += 1
