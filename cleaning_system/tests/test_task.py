from    car.models  import Car
import  time

@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': 'amqp://localhost:6379',
        'result_backend': 'redis://localhost:6379'
    }

def test_create_task(celery_app, celery_worker):
    @celery_app.task
    def create_car():
        assert  1==1
        
   
