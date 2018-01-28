from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from .models import Comment, BlogPost
from users.models import User

class BlogPostModelTest(TestCase):
    """Testing BlogPost model"""
    def test_blogpost_creation(self):
        """Testing blogpost creation"""
        blogpost = BlogPost.objects.create(
            title='My first post',
            content='This is just some random content for my test',
            category='Testing',
            is_live=True
        )
        now = timezone.now()
        self.assertLessEqual(blogpost.pub_date, now)
        self.assertIs(blogpost.is_live, True)
        self.assertEqual(blogpost.slug, 'my-first-post')


class BlogPostViewTest(TestCase):
    """Testing BlogPost views, urls and templates"""
    def setUp(self):
        self.blogpost = BlogPost.objects.create(
            title='My first post',
            content='Some random content for my test post',
            category='Testing',
            is_live=True
        )
        self.blogpost2 = BlogPost.objects.create(
            title='My second post',
            content='Content for my second test post',
            category='More Testing',
            is_live=True
        )
        self.comment = Comment.objects.create(
            post=self.blogpost,
            comment='A comment for my first test post',
            author='Henrik Christensen',
            is_deleted=False
        )

    def test_blogpost_list_view(self):
        """Testing BlogPost listview, url and template"""
        resp = self.client.get(reverse('blog:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.blogpost, resp.context['object_list'])
        self.assertIn(self.blogpost2, resp.context['object_list'])
        self.assertTemplateUsed(resp, 'blogposts/blogpost_list.html')
        self.assertTemplateUsed(resp, 'blogposts/blogpost_list.html')
        self.assertContains(resp, self.blogpost.title)
        self.assertContains(resp, self.blogpost2.title)

    def test_blogpost_detail_view(self):
        """Testing BlogPost detailview, url and template"""
        resp = self.client.get(reverse('blog:detail', kwargs={'slug': self.blogpost.slug}))
        resp2 = self.client.get(reverse('blog:detail', kwargs={'slug': self.blogpost2.slug}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.blogpost, resp.context['object'])
        self.assertTemplateUsed(resp, 'blogposts/blogpost_detail.html')
        self.assertContains(resp, self.blogpost.title)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(self.blogpost2, resp2.context['object'])
        self.assertTemplateUsed(resp2, 'blogposts/blogpost_detail.html')
        self.assertContains(resp2, self.blogpost2.title)


class CommentModelTest(TestCase):
    """Testing Comment model"""
    def setUp(self):
        self.blogpost = BlogPost.objects.create(
            title='Test title',
            content='Some random content',
            category='Testing',
            is_live=True
        )

    def test_comment_creation(self):
        """Testing comment creation"""
        comment = Comment.objects.create(
            post=self.blogpost,
            comment='My super awesome test comment',
            author='Henrik Christensen',
            is_deleted=False
        )
        now = timezone.now()
        self.assertLessEqual(comment.pub_date, now)
        self.assertIs(comment.is_deleted, False)


class CommentViewTest(TestCase):
    """Testing Comment views, urls and templates"""
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='henrik',
            email='henrik@henrik.com',
            password='testpassword',
        )
        self.user2 = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword'
        )
        self.blogpost = BlogPost.objects.create(
            title='Testing title',
            content='Some random content',
            category='Testing',
            is_live=True
        )
        self.comment = Comment.objects.create(
            post=self.blogpost,
            comment='A super awesome comment',
            author=self.user.username,
            is_deleted=False
        )
        self.comment2 = Comment.objects.create(
            post=self.blogpost,
            comment='Random stuff',
            author=self.user2.username,
            is_deleted=True
        )

    def test_comment_in_blogpost_detail_view(self):
        """Testing comments in blogposts detailview"""
        resp = self.client.get(reverse('blog:detail', kwargs={'slug': self.blogpost.slug}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.comment, resp.context['comments'])
        self.assertIn(self.comment2, resp.context['comments'])
        self.assertTemplateUsed(resp, 'blogposts/blogpost_detail.html')
        self.assertContains(resp, self.comment.comment)
        self.assertNotContains(resp, self.comment2.comment)

    def test_comment_delete_view_anonymous_request(self):
        """Testing if comments deleteview will redirect anonymous users to login"""
        resp = self.client.get(reverse('blog:comment_delete', kwargs={'pk': self.comment.pk}), follow=True)
        self.assertRedirects(resp, '{}?next={}'.format(
            reverse('users:login'), reverse('blog:comment_delete', kwargs={'pk': self.comment.pk})
        ))
        resp = self.client.post(reverse('blog:comment_delete', kwargs={'pk': self.comment.pk}), follow=True)
        self.assertRedirects(resp, '{}?next={}'.format(
            reverse('users:login'), reverse('blog:comment_delete', kwargs={'pk': self.comment.pk})
        ))

    def test_comment_delete_view_valid_request(self):
        """Testing comments deleteview accepts requests from logged in users
        that are superusers or is comment.author"""
        pass
