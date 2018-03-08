from django.test import TestCase

# Create your tests here.
# from amara.models import Collection
from amara.views import analyzeOSChina


class CollectionTestCase(TestCase):
    def test001(self):

        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')
        uri = 'https://www.oschina.net/p/hiriver?from=20170528'
        os_china_collection = analyzeOSChina(uri)
        print('origin: ', repr(os_china_collection))
        # Collection.objects.create(**os_china_collection)
        # objects_all = Collection.objects.all()
        # print('all001: ', repr(objects_all))
        # if objects_all:
        #     all__id = objects_all[0].id
        #     print('id: ', repr(all__id))
        #     get = Collection.objects.get(id=all__id)
        #     print('select001: ', repr(get))
        #     get.name = 'TEST000'
        #     get.save()
        #     get = Collection.objects.get(id=all__id)
        #     print('select002: ', repr(get))
        #     Collection.objects.filter(id=all__id).delete()
        # objects_all = Collection.objects.all()
        # print('all002: ', repr(objects_all))

