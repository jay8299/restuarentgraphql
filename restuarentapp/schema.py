from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from restuarentapp.models import Restuarent
import graphene

class Restuarents(DjangoObjectType):
    class Meta:
        model = Restuarent
        filter_fields = ['votes']
        interfaces = (relay.Node, )
class Query(graphene.ObjectType):
    restinfo = relay.Node.Field(Restuarents)
    all_restinfo = DjangoFilterConnectionField(Restuarents)


    def resolve_prodinfo(self,info):
        print(Restuarent.Objects.all())
        return Restuarent.objects.all()

schema = graphene.Schema(query=Query)

