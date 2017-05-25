import graphene


class UserFields(graphene.AbstractType):
    name = graphene.String()


class User(graphene.ObjectType, UserFields):
    pass


class UserInput(graphene.InputObjectType, UserFields):
    pass
