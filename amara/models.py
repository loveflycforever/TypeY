from django.db import models


class Fashion(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    fashion = models.ForeignKey(Fashion, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    protocol = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, null=True)
    extra = models.CharField(max_length=100, null=True, default=None)
    platform = models.CharField(max_length=100)
    keeper = models.CharField(max_length=100)
    website = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s' % (self.name,
                                            self.title,
                                            self.description,
                                            self.protocol,
                                            self.language,
                                            self.platform,
                                            self.keeper,
                                            self.created_at)
