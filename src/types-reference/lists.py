import graphene


class Character(graphene.ObjectType):
    name = graphene.String(required=True)
    appears_in = graphene.List(graphene.String())


schema = graphene.Schema(query=Character)
result = schema.execute('{ name, appears_in }')
print(result.data)
