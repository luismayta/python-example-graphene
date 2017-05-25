import graphene


class Person(graphene.ObjectType):
    name = graphene.String(
        name=graphene.Argument(
            graphene.String,
            default_value='L',
        )
    )

    def resolve_name(self, args, context, info):
        return 'Hello {}'.format(
            args.get('name')
        )


schema = graphene.Schema(query=Person)
result = schema.execute('{ name }')
print(result.data.get('name'))
