import graphene


class Person(graphene.ObjectType):
    first_name = graphene.String(
        name=graphene.Argument(
            graphene.String,
            default_value='name'
        )
    )
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, args, context, info):
        return '{} {}'.format(self.first_name, self.last_name)


schema = graphene.Schema(query=Person)
result = schema.execute('{ full_name }')

if isinstance(result.data, (dict,)):
    print(result.data)
