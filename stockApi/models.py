from django.db import models
from django.utils import timezone

# Create your models here.
class item(models.Model):
    title = models.CharField(max_length=10)
    url = models.URLField(primary_key=True)
    stockNum = models.IntegerField()
    stock1Code = models.CharField(max_length=10)
    stock2Code = models.CharField(null=True, max_length=10)
    stock3Code = models.CharField(null=True, max_length=10)
    createDate = models.DateTimeField(default=timezone.now)

    def as_json(self):
        return dict(
            title=self.title,
            url=self.url,
            stockNum=self.stockNum,
            stock1Code=self.stock1Code,
            stock2Code=self.stock2Code,
            stock3Code=self.stock3Code,
            createDate=self.createDate.isoformat())
