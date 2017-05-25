import graphene


class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_fullname(self, args, context, info):
        return '{} {}'.format(self.first_name, self.last_name)


schema = graphene.Schema(query=Person)
result = schema.execute('{ first_name }')

if isinstance(result.data, (dict,)):
    print(result.data.get('first_name'))
