import graphene


class Character(graphene.ObjectType):
    name = graphene.String(required=True)


# Human is a Character Implementation
class Human(graphene.ObjectType):

    born_in = graphene.String()

    class Meta:
        interfaces = (Character, )


class Droid(graphene.ObjectType):

    function = graphene.String()

    class Meta:
        interfaces = (Character, )
