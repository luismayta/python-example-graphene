import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(
        name=graphene.Argument(
            graphene.String,
            default_value='stranger')
    )

    def resolve_hello(self, args, context, info):
        return 'Hello {}'.format(
            args.get('name')
        )


schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data.get('hello'))
