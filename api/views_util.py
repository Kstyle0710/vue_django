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

def make_tag_cloud(qsTag):
    minCount = min(tag.count for tag in qsTag)
    maxCount = max(tag.count for tag in qsTag)

    # minweight, maxweight = 1, 3

    def get_weight_func(minweight, maxweight):
        if minCount == maxCount:
            factor = 1.0
        else:
            factor = (maxweight - minweight) / (maxCount - minCount)

        def func(count):
            weight = round(minweight + (factor * (count - minCount)))
            return weight

        return func

    weight_func = get_weight_func(1, 3)
    tagList = []
    for tag in qsTag:
        weight = weight_func(tag.count)
        tagList.append({
            'name': tag.name,
            'count': tag.count,
            'weight': weight,
        })
    return tagList




