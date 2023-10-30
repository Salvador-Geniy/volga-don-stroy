from django.core.cache import cache


def get_data_from_cache_or_queryset(object, object_cache_name):
    """Function for get data from cache or from queryset
    and return serialized data"""
    object_cache = cache.get(object_cache_name)

    if object.cache:
        queryset = object_cache
    else:
        queryset = object.filter_queryset(object.get_queryset())
        cache.set(object_cache_name, queryset, 30)

    page = object.paginate_queryset(queryset)
    if page is not None:
        serializer = object.get_serializer(page, many=True)
        return object.get_paginated_response(serializer.data)
    serializer = object.get_serializer(queryset, many=True)
    return serializer.data

