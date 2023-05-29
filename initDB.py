def init():
    """
    Функция для инициализации базы данных

    В shell:
    from initDB import init
    init()
    """

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

    print(f'   Posts = {Post.objects.count()}')
    print(f'  Posts created.')
    print(f' Data initialization complete.')

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

    print(f'   Comments = {Comment.objects.count()}')
    print(f'  Comments created.')

    print(f'DB initialization complete')
