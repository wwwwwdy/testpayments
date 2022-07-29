# Тестовое задание на реализацию клиента к шлюзу Cloudpayments

### Описание проекта:
Клиент описан в client.py, для валидации схем marshmallow описан декоратор SchemaValidator в модуле validator.py.

В проекте реализованы случаи, как без, так и с обработкой 3-D Secure.
Клиент переходит на страницу совершения оплаты, в случае если ему в ответе приходит {"Success": True}, то ему возвращается ответ с успешной оплатой
В случае, если {"Success": Fasle}, то происходит редирект на /checkout/, где клиенту необходимо отправить форму.

Для тестирования тех или иных случаев, необходимо в документации (https://developers.cloudpayments.ru/#skript-checkout) сгенерировать криптограмму и поместить ее в data.json в поле CardCryptogramPacket
Тестовые карты находятся здесь: https://developers.cloudpayments.ru/#testirovanie
Варианты с не валидными данными карт не были реализованы

Для корректного редиректа, в checkout.html необходимо указать свой корректный домен или использовать http://0.0.0.0:8080/
```
<input type="hidden" name="TermUrl" value="https://141c-87-117-53-24.eu.ngrok.io/checkout/">
```

### Как запустить проект:
1. Склонировать репозиторий:
```bash
git clone https://github.com/wwwwwdy/testpayments.git
```
2. Создать виртуальное окружение:
```bash
python -m venv venv
```
или использовать окружение Poetry:
```bash
poetry shell
```
3. Установить зависимости:
- с помощью pip:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
- с помощью poetry:
```bash
poetry install
```
4. Запустить сервер aiohttp:
```bash
python server.py
```
### Warning
При использовании MacOS необходимо установить Install Certificates.command к питону, иначе возникнет проблема с коннектом
