
def user_has_c_c_and_is_recolector(user):    
    return user.groups.filter(name='recolector').exists() and hasattr(user , 'collection_center')