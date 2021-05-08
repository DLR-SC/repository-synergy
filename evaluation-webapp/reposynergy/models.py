from django.db import models

from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

class User(AbstractUser):
    batch =  models.IntegerField( null=True)
    def getUser(email):
        return User.objects.filter(username=email)
    def re_deactivate(self, user_id, activate = True):
        u = User.objects.get(id=user_id)
        u.is_active= activate
        u.save()


class RepositoryPair(models.Model):
    id = models.BigAutoField(primary_key=True)

    repo_url1 = models.CharField(max_length=250,null=False)
    repo_url2 = models.CharField(max_length=250,null=False)

    repo_description1 =models.CharField(max_length=2000,null=False)
    repo_description2 = models.CharField(max_length=2000,null=False)

    score = models.FloatField(default=0.0)
    is_random = models.BooleanField(default=False)

    algorithm = models.CharField(max_length=20, null=True)
    batch = models.IntegerField(null=True)

    def getRepoPairs(self):
        return RepositoryPair.objects.all()

    def getBatchRepoPairs(self, batch):
        return RepositoryPair.objects.filter(batch=batch)

    def getRepoPair(self, pair_id):
        return RepositoryPair.objects.get(pk=pair_id)

class Annotation(models.Model):
    a_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repository_pair = models.ForeignKey(RepositoryPair, on_delete=models.CASCADE)

    annotation_date = models.DateTimeField(default=datetime.now)
    synergy = models.IntegerField( null=False)  # 1-4
    direction = models.IntegerField(null=False)  # good:2 acceptable:1 poor:0
    explanation = models.CharField(max_length=1000,null=False)  # Sufficient:2 Acceptable Insufficient:0

    def getUserAnnotations(user_id):
        return Annotation.objects.filter(user=user_id)

    def get_num_of_annotations_per_user(user_id):
        result = Annotation.objects.values('repository_pair').filter(user=user_id).annotate(
            count=Count('repository_pair'))
        return result['repository_pair']

    def getAnnotation(user_id, pair_id):
        try:
            return Annotation.objects.get(user_id=user_id, repository_pair_id=pair_id)
        except ObjectDoesNotExist as e:
            return None

    def get_batch_annotations(self, batch):
        try:
            return Annotation.objects.filter(repository_pair__batch=batch, user__is_active=True)
        except ObjectDoesNotExist as e:
            return None

