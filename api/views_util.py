def obj_to_post(obj):
    post = dict(vars(obj))

    # convert to string
    if obj.modify_dt:
        post['modify_dt'] = obj.modify_dt.strftime('%y-%m-%d %H:%M')
    else:
        post['modify_dt'] = ''

    if obj.tags:
        post['tags'] = [tag.name for tag in obj.tags.all()]
    else:
        post['tags'] = []

    if obj.owner:
        post['owner'] = obj.owner.username
    else:
        post['owner'] = 'Anomymous'

    del post['_state']


    return post

def prev_next_post(obj):
    try:
        prevObj = obj.get_prev()   # model 에 메소드 정의되어 있음
        prevDict = {'id': prevObj.id, 'title': prevObj.title}
    except obj.DoesNotExist as e:
        prevDict = {}

    try:
        nextObj = obj.get_next()
        nextDict = {'id': nextObj.id, 'title': nextObj.title}
    except obj.DoesNotExist as e:
        nextDict = {}

    return prevDict, nextDict
