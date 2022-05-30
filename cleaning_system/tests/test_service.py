import  pytest 
from  rest_framework.test   import APIClient
from  service_type.models  import Service
import  json

@pytest.fixture
def  client():
   return APIClient()
@pytest.mark.django_db
def test_service_post(client):
    payload=dict(
      title= "service",
        description= "service  one",
        price= 0.06
    )
    response=client.post('http://127.0.0.1:8000/service/',data=payload,format='json')
    assert  response.status_code==201

@pytest.mark.django_db
def  test_service_list(client):
   Service.objects.create(
      title= "service1",
        description= "service  one",
        price= 0.06
   )
   Service.objects.create(
      title= "service2",
        description= "service  two",
        price= 0.09
   )
   response=client.get('http://127.0.0.1:8000/service/')
   assert  response.status_code==200
   assert    len(response.content)

@pytest.mark.django_db
def test_service_detail_404(client):
    response=client.get('http://127.0.0.1:8000/service/5/')
    assert  response.status_code==404    

@pytest.mark.django_db
def  test_service_update(client):
   service= Service.objects.create(
      title= "service1",
        description= "service  one",
        price= 0.06
   )
   payload=dict(title="serviceeeeeeeeeeeeeee", description= "service  one",price= 0.06)
   response=client.put(f'http://127.0.0.1:8000/service/{service.id}/', payload,  format='json')
   service.refresh_from_db()
   assert  json.loads(response.content)["title"]==payload["title"]


@pytest.mark.django_db
def  test_service_delete(client):
    service= Service.objects.create(
      title= "service1",
        description= "service  one",
        price= 0.06
    )
    response=client.delete(f'http://127.0.0.1:8000/service/{service.id}/')
    assert  response.status_code==204
