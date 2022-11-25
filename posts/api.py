from ninja import Router

router = Router()

@router.get('healthcheck')
def healtcheck(request):
    return {
        'status':'ok'
    }    