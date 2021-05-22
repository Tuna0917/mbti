from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
INDICATOR = (
        ('E','Extraversion'),
        ('I','Introversion'),
        ('S','Sensing'),
        ('N','iNtuition'),
        ('T','Thinking'),
        ('F', 'Feeling'),
        ('J', 'Judging'),
        ('P', 'Perceiving'),
    )
MBTI = (
        #분석형
        ('INTJ','용의주도한 전략가'),
        ('INTP','논리적인 사색가'),
        ('ENTJ','대담한 통솔자'),
        ('ENTP','뜨거운 논쟁을 즐기는 변론가'),
        #외교형
        ('INFJ','선의의 옹호자'),
        ('INFP','열정적인 중재자'),
        ('ENFJ','정의로운 사회운동가'),
        ('ENFP','재기발랄한 활동가'),
        #관리자형
        ('ISTJ','청렴결백한 논리주의자'),
        ('ISFJ','용감한 수호자'),
        ('ESTJ','엄격한 관리자'),
        ('ESFJ','사교적인 외교관'),
        #탐험가형
        ('ISTP','만능 재주꾼'),
        ('ISFP','호기심 많은 예술가'),
        ('ESTP','모험을 즐기는 사업가'),
        ('ESFP','자유로운 영혼의 연예인'),
    )

class Question(models.Model):
    title = models.CharField('TITLE', max_length=100,blank=True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title

class Select(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=128, blank=True)
    indicator = models.CharField(max_length=1, choices=INDICATOR)

    def __str__(self) -> str:
        return f"{self.indicator}, {self.text}"

class DetailText(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text

class TypeIndicator(models.Model):
    mbti = models.CharField(max_length=4, choices=MBTI)
    image = models.ImageField('IMAGE', upload_to='SorlPhoto/%Y', null=True)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True)
    text = models.TextField(blank=True)
    details = models.ManyToManyField(DetailText)
    like = models.ForeignKey('self', on_delete=models.CASCADE, related_name='like_mbti', null=True)
    hate = models.ForeignKey('self', on_delete=models.CASCADE, related_name='hate_mbti', null=True)

    def get_absolute_url(self):
        return reverse('detail', args=(self.slug,))
    def __str__(self) -> str:
        return f"{self.mbti}, {self.get_mbti_display()}"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.mbti, allow_unicode=True)
        super().save(*args,**kwargs)