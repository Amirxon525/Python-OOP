### ✅ 1. **Car klassini yozing**

🚗 `Car` nomli class yozing. Quyidagi atributlarni o‘z ichiga olishi kerak:

* `brand` — mashina brendi (masalan, “BMW”)
* `model` — model nomi (masalan, “X5”)
* `year` — ishlab chiqarilgan yili (masalan, 2022)

📝 **Talab:**

* `__init__()` konstruktor orqali atributlarni qabul qilsin.
* Hech qanday metod yozilmaydi, faqat class va atributlar.

---

### ✅ 2. **Student klassini yozing**

🎓 `Student` nomli class yarating. Quyidagi atributlar bo‘lishi kerak:

* `name` — to‘liq ismi
* `age` — yoshi
* `grade` — bahosi yoki o‘qish darajasi (masalan, 9-sinf)

📝 **Talab:**

* Har bir atribut `__init__()` orqali qiymat qabul qilsin.
* Kodni o‘zingiz xohlagan 2-3ta object bilan sinab ko‘ring (shu fayl ichida).

---

### ✅ 3. **User klassini yozing**

👤 `User` klassi yarating. U foydalanuvchi haqida quyidagi atributlarni saqlasin:

* `username` — login nomi
* `email` — elektron pochta manzili
* `is_active` — foydalanuvchi aktivmi (True/False)

📝 **Talab:** 

* Ob’ekt yaratganda, barcha atributlar qiymatini olish kerak.
* `is_active` uchun True yoki False qiymat kiritilsin.

---

### ✅ 4. **Movie klassini yozing**

🎬 `Movie` nomli class yarating. U quyidagilarni o‘z ichiga olsin:

* `title` — kino nomi
* `genre` — janri (masalan, “action”, “comedy”)
* `duration` — davomiyligi (daqiqalarda)
* `rating` — IMDB reytingi (masalan, 8.5)

📝 **Talab:**

* `float` va `int` turidagi atributlardan foydalaning.
* Object yaratib, barcha atributlarni terminalga `print()` bilan chiqarib ko‘rsating.

---

### ✅ 5. **Product klassini yozing**

🛍️ `Product` nomli class yozing. Do‘kon mahsulotlarini ifodalasin:

* `name` — mahsulot nomi
* `price` — mahsulot narxi (masalan, 12999.99)
* `category` — mahsulot turi (masalan, “electronics”)
* `in_stock` — mahsulot omborda bormi (True/False)

📝 **Talab:**

* 2 ta mahsulot uchun object yarating.
* `print()` orqali har bir mahsulotning nomi va narxini chiqarib bering.

---

### ✅ **Task 6 – Student klassi bilan ishlash**

`Student` nomli class yozing.

**Atributlar:**

* `name` – o‘quvchining ismi
* `age` – o‘quvchining yoshi
* `grade` – o‘qiyotgan sinfi

**Metod:**

* `info()`

  * **Nima qiladi:** o‘quvchi haqida matn ko‘rinishida ma’lumotni chiqaradi.
  * **Return:** hech nima qaytarmaydi, faqat `print()` qiladi.
  * **Namuna chiqish:** `"Ali, 15 yoshda, 9-sinf o‘quvchisi."`

---

### ✅ **Task 7 – Movie klassi bilan ishlash**

`Movie` nomli class yozing.

**Atributlar:**

* `title` – film nomi
* `genre` – janri
* `duration` – davomiyligi (daqiqa)
* `rating` – film bahosi (float, masalan, 8.5)

**Metod:**

* `show_summary()`

  * **Nima qiladi:** film nomi, janri va bahosini bir qatorda chiqaradi.
  * **Return:** hech nima qaytarmaydi, `print()` qiladi.
  * **Namuna chiqish:** `"Inception — fantastika janridagi film. Reyting: 8.8/10."`

---

### ✅ **Task 8 – Product klassi bilan ishlash**

`Product` nomli class yozing.

**Atributlar:**

* `name` – mahsulot nomi
* `price` – mahsulot narxi (masalan, 199.99)
* `category` – mahsulot turi
* `in_stock` – boolean (True/False) — omborda bor yoki yo‘qligi

**Metod:**

* `check_stock()`

  * **Nima qiladi:** mahsulot omborda bormi yoki yo‘qligini ekranga chiqaradi.
  * **Return:** hech nima qaytarmaydi, faqat `print()` qiladi.
  * **Namuna chiqish:**

    * `"AirPods omborda mavjud ✅"`
    * `"iPhone 13 hozirda tugagan ❌"`

---

### ✅ **Task 9 – User klassi bilan ishlash**

`User` nomli class yozing.

**Atributlar:**

* `username` – login nomi
* `email` – foydalanuvchi emaili
* `is_active` – foydalanuvchi aktivmi (True/False)

**Metodlar:**

* `activate()`

  * **Nima qiladi:** `is_active` ni `True` ga o‘zgartiradi va foydalanuvchi faollashtirilgani haqida xabar beradi.
  * **Return:** hech nima qaytarmaydi, faqat `print()` qiladi.

* `deactivate()`

  * **Nima qiladi:** `is_active` ni `False` ga o‘zgartiradi va foydalanuvchi bloklangani haqida xabar beradi.
  * **Return:** hech nima qaytarmaydi, faqat `print()` qiladi.

---

### ✅ **Task 10 – BankAccount klassi bilan ishlash**

`BankAccount` nomli class yozing.

**Atributlar:**

* `owner` – hisob egasining ismi
* `balance` – hisobdagi pul miqdori

**Metodlar:**

* `deposit(amount)`

  * **Nima qiladi:** berilgan summani balansga qo‘shadi.
  * **Return:** yangi balansni `print()` qiladi.

* `withdraw(amount)`

  * **Nima qiladi:** agar balans yetarli bo‘lsa, pul yechib beradi; aks holda ogohlantiradi.
  * **Return:** yangi balans yoki xato xabarni `print()` qiladi.

📌 Maqsad: Obyekt holatini method orqali o‘zgartirishni o‘rganish.

---

### ✅ **Task 11 – Book klassi bilan ishlash**

`Book` nomli class yozing.

**Atributlar:**

* `title` – kitob nomi
* `author` – muallif
* `is_read` – True/False (kitob o‘qilganmi)

**Metod:**

* `mark_as_read()`

  * **Nima qiladi:** `is_read` ni `True` ga o‘zgartiradi
  * **Return:** `"Kitob o‘qilgan deb belgilandi"` degan `print()` chiqaradi

* `status()`

  * **Nima qiladi:** o‘qilganmi yoki yo‘qmi — shuni bildiradi
  * **Return:** `"O‘qilgan"` yoki `"O‘qilmagan"` deb `print()` qiladi

📌 Maqsad: Boolean atributlar bilan ishlash, method orqali holatni o‘zgartirish

---
Juda yaxshi ketayapsan, Diyorbek!
Endi sening talabing bo‘yicha `12-task`dan boshlab **obyektlar bilan ishlashga qaratilgan** mustaqil uyga vazifalarni yozaman. Bu bosqichda o‘quvchilar:

* bir nechta object yaratishni,
* ular ustida amallar bajarishni,
* obyektlar orasida farq qilishni,
* methodlarni obyektga nisbatan qo‘llashni o‘rganadi.

---

### ✅ **Task 12 – Multiple Bank Accounts**

`BankAccount` nomli class yozing.

**Atributlar:**

* `owner`
* `balance`

**Metodlar:**

* `deposit(amount)`
* `withdraw(amount)`
* `show_balance()` – hisobdagi mablag‘ni `print()` qiladi

📝 **Topshiriq:**

* 3 ta hisob egasi (obyekt) yarating.
* Har biriga turli summalarda `deposit()` va `withdraw()` amallarini bajaring.
* Yakuniy balansni `show_balance()` orqali ko‘rsating.

📌 Maqsad: Obyektlar orasidagi mustaqil holatlarni tushunish.

---

### ✅ **Task 13 – Library kitoblari ro‘yxati**

`Book` nomli class yozing.

**Atributlar:**

* `title`
* `author`
* `is_read` (False bo‘lib boshlansin)

**Metodlar:**

* `mark_as_read()`
* `status()` – `"O‘qilgan"` yoki `"O‘qilmagan"` deb chiqaradi

📝 **Topshiriq:**

* Kamida 4 ta `Book` obyekti yarating.
* 2 tasini `mark_as_read()` bilan o‘qilgan deb belgilang.
* Barcha kitoblar uchun `status()` metodini chaqiring.

📌 Maqsad: Har bir obyektning `is_read` holati o‘zgarishini ko‘rish.

---

### ✅ **Task 14 – Student ro‘yxatidan eng kattasini topish**

`Student` nomli class yozing.

**Atributlar:**

* `name`
* `age`

**Metod:**

* `show_info()` – ismi va yoshini chiqaradi

📝 **Topshiriq:**

* 5 ta `Student` obyektini yarating (turli yoshda)
* Eng katta yoshdagi talabani aniqlang (Python `max()` yoki oddiy if bilan)
* `show_info()` metodini chaqirib natijani ko‘rsating.

📌 Maqsad: Obyektlar orasida ma’lumot solishtirishni o‘rganish.

---

### ✅ **Task 15 – Productlar narxini umumiy hisoblash**

`Product` nomli class yozing.

**Atributlar:**

* `name`
* `price`
* `in_stock` (True/False)

📝 **Topshiriq:**

* 5 ta mahsulot yarating.
* Faqat `in_stock == True` bo‘lgan mahsulotlar narxini hisoblang.
* Yakuniy natijani `print()` qiling.
  (Masalan: `"Ombordagi mahsulotlar narxi: 274.50"`)

📌 Maqsad: Obyektlar ustida filter, yig‘indi, tahlil qilishni o‘rganish.

---

### ✅ **Task 16 – Kitoblar ro‘yxatini chiqarish va o‘qilganlarini ajratish**

📘 `Book` nomli class yozing.

**Atributlar:**

* `title`
* `author`
* `is_read` – boshlanishida False

**Metodlar:**

* `mark_as_read()` – kitobni o‘qilgan deb belgilaydi
* `status()` – `"O‘qilgan"` yoki `"O‘qilmagan"` deb chiqaradi

📝 **Topshiriq:**

* 5 ta `Book` obyekti yarating va ularni `books` listiga joylang.
* 2 ta kitobni `mark_as_read()` bilan belgilang.
* `for` loop orqali barcha kitoblarning holatini chiqarib bering (`status()` yordamida).
* Faqat o‘qilgan kitoblarning nomlarini alohida chiqarib bering.

📌 **Maqsad:** List ichida obyektlar bilan ishlash, metodlarni kollektiv qo‘llash.

---

### ✅ **Task 17 – Bank hisoblari ro‘yxatidan jami balansni hisoblash**

🏦 `BankAccount` nomli class yozing.

**Atributlar:**

* `owner`
* `balance`

**Metod:**

* `show_balance()` – balansni `print()` qiladi
* `get_balance()` – balansni **qaytaradi (return)**

📝 **Topshiriq:**

* 5 ta `BankAccount` obyektini yarating.
* Ularni `accounts` ro‘yxatiga joylang.
* `for` loop yordamida jami balansni hisoblang.
* Jami balansni `print()` qiling.

📌 **Maqsad:** Obyektlardan qiymat olish (`get_balance()`), yig‘ish, va chiqarish.

---

### ✅ **Task 18 – Mahsulotlar ichidan eng qimmatini topish**

🛍️ `Product` nomli class yozing.

**Atributlar:**

* `name`
* `price`
* `category`

**Metod:**

* `info()` – mahsulot nomi va narxini chiqaradi

📝 **Topshiriq:**

* 6 ta `Product` obyektini yarating, listga joylang.
* List ichidan eng qimmat mahsulotni toping.
* Uning `info()` metodini chaqirib natijani ko‘rsating.

📌 **Maqsad:** Listdagi obyektlarni solishtirish, eng kattasini aniqlash.
