# Imtihon Backend (Django + DRF)

## Ishga tushirish

```bash
python -m venv .muhit
# Windows:
.muhit\Scripts\Activate.ps1
# Linux/Mac:
source .muhit/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # admin panelga kirish uchun
python manage.py runserver
```

Server manzili: http://127.0.0.1:8000/

- Admin panel: http://127.0.0.1:8000/admin/
- API (mahsulotlar ro'yxati): http://127.0.0.1:8000/api/products/

Ichida tayyor 2 ta test mahsulot bor (Telefon, Noutbuk) — db.sqlite3 fayli
bilan birga keladi, shuning uchun darhol API javob beradi.

## Yangi model qo'shish tartibi (eslab qolish uchun)

1. `base/models.py` — model yozish
2. `python manage.py makemigrations && python manage.py migrate`
3. `base/admin.py` — admin panelda ko'rsatish
4. `base/serializers.py` — serializer yozish
5. `base/views.py` — ViewSet yozish
6. `base/urls.py` — routerga ro'yxatdan o'tkazish (bu fayl allaqachon `config/urls.py`
   ga ulangan, `api/` prefiksi bilan)

## Muhim eslatma

`INSTALLED_APPS` ichida albatta `'base'` bo'lishi shart — aks holda
"doesn't declare an explicit app_label" xatosi chiqadi.
