from mixer.backend.django import mixer
from django.utils import timezone
from jobs.models import JobPost, UserManager, User, UserMembership
import uuid
import pytest
 
# JobPost Test Suite
@pytest.mark.django_db
class TestJobPost:
    def test_jobpost_model(self):
        self.company_name = 'Google MERN'
        self.title = 'Software Engineer'
        self.description = 'Program in MERN stack'
        self.job_location = 'Las Vegas'
        self.requirements = 'Must work in MERN stack for at least a year'
        self.min_salary = 60000
        self.max_salary = 80000
        self.is_active = True
        self.tags = 'javascript, mongodb, sql, express.js'
        self.created_date = timezone.now()
        self.published_date = timezone.now()

        self.test_jobpost = JobPost.objects.create(
            title = self.title,
            description = self.description,
            job_location = self.job_location,
            requirements = self.requirements,
            min_salary = self.min_salary,
            max_salary = self.max_salary,
            is_active = self.is_active,
            tags = self.tags,
            created_date = self.created_date,
            published_date = self.published_date,
        )

        def test_publish_jobpost(self):
            assert isinstance(self.publish, JobPost)
        
        def test_str(self):
            assert self.__str__ == self.title


# UserManager Test Suite
class TestUserManager:
    try: 
        UserManager()
    except NameError:
        print('Does not exist')
    else:
        print('It may exist but we have a little error going on.')

    try:
        getattr(UserManager, '_create_user')
    except AttributeError:
        print("_create_user doesn't exist")
    else:
        print("Exists")

    try:
        getattr(UserManager, 'create_user')
    except AttributeError:
        print("create_user doesn't exist")
    else:
        print("Exists")

    try:
        getattr(UserManager, 'create_superuser')
    except AttributeError:
        print("create_superuser doesn't exist")
    else:
        print("Exists")


# User Test Suite
@pytest.mark.django_db
class TestUser:
    def test_user_model(self):
        self.is_employer = True
        self.email = 'example_email@gmail.com'
        self.password = 'example_password'
        self.is_active = True
        self.is_staff = True
        self.company_name = 'Example Company'
        self.company_logo = '<img src=\'#\' alt=\'example\'>'
        self.company_summary = 'An example company description for the company'
        self.application_inbox = []
        self.first_name = 'Firstname'
        self.last_name = 'Lastname'
        self.profile_photo = '<img src=\'#\' alt=\'example\'>'
        self.created_date = timezone.now()
        self.jwt_secret = uuid.uuid4()

        self.test_user = User.objects.create(
            is_employer = self.is_employer,
            email = self.email,
            password = self.password,
            is_active = self.is_active,
            is_staff = self.is_staff,
            company_name = self.company_name,
            company_logo = self.company_logo,
            company_summary = self.company_summary,
            application_inbox = self.application_inbox,
            first_name = self.first_name,
            last_name = self.last_name,
            profile_photo = self.profile_photo,
            created_date = self.created_date,
            jwt_secret = self.jwt_secret
        )

        # test_user = mixer.blend(User) 
        def test_create_user(self):
            assert isinstance(self.test_user, User)
            
        def test_str(self):
            assert self.__str__ == self.email

# Membership Test Suite
@pytest.mark.django_db
class TestUserMembership:
    try:
        UserMembership()
    except NameError:
        print('Does not exist')
    else:
        print('It may exist but we have a little error going on.')

    try:
        getattr(UserMembership, '__str__')
    except AttributeError:
        print("__str__ doesn't exist")
    else:
        print("Exists")


    # def test_usermembership_model(self):
    #     user_membership = mixer.blend(UserMembership)
        
    #     def test_create_user_membership(self):
    #         assert isinstance(self.test_usermembership, UserMembership)

    #     def test_str(self):
    #         assert self.__str__ == self.user.email

# class UserMembership(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     stripe_customer_id = models.CharField(max_length=40)
#     membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
#     # stripe_product_id = models.CharField(max_length=40)

#     def __str__(self):
#         return self.user.email
