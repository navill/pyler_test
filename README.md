# Pyler 과제테스트

## 테이블 구조
![ERD.png](docs_images%2FERD.png)

## 실행 방법
```python
# db migration
python manage.py makemigrations
python manage.py migrate

# create sample data
python manage.py initialize

# runserver
python manage.py runserver  # --settings=config.settings.product
```
- 테스트 admin 계정: admin / test1234
- 테스트 계정: testuser-<0~4> / test1234
- swagger docs: http://127.0.0.1:8000/api/schema/swagger-ui/
  ![swagger.png](docs_images%2Fswagger.png)

