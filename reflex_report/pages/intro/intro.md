# Python `Reflex`. Доклад.

## Введение.

### Что?

Доклад посвящён фреймворку `reflex`. 

Это довольно мощный по функционалу 🦍, но немного слабенький по производительности 😅 инструмент, который позволяет делать `web` приложения полностью на python.

С помощью него можно строить `web` приложения не разделяя `backend` и `frontend`.

### Зачем?

На своём сайте они отмечают следующие цели:
- `Pure Python` (не учить что-то другое, а сразу использовать что-то знакомое)
- `Easy to Learn`
- `Full Flexibility` (мало того, что на reflex можно сделать что угодно, так он ещё даёт инструменты для деплоя и бесплатный хостинг)
- `Batteries Included` (работает сразу из коробки с крутыми инструментами)

На мой взгляд подобные библеотеки хороши для новичков, чтобы вкатиться в `web` разработку 😎 Чтобы сделать хоть какое-то web приложения без подобного фреймворка нужно постараться выучить базу `python`, `html`, `css`, `web`. И ещё понять как всё это поженить. А тут всё просто и быстро. 

Создатель этого фреймворка рассказал, как ему пришла идея его создания. Раньше он работал в ИИ стартапе, а затем в бигтехе. Он всегда писал на `python` и `backend`, и анализ данных, и всё что можно. Но, когда дело доходило до создание пользовательских интерфейсов, `python` был очень не выгоден. Приходилось учить `JavaScript` и кучу других инструментов, а это сложно и долго. По итогу создание пользовательского интерфейса было сложнее, чем вся остальная работа.

### Какие вообще существуют аналоги?

Можно использовать `Flask` или `Django` - это мощные инструменты, которые реально используют на промышленном уровне. Но к сожалению они хорошо покрывают `backend`, но не `frontend`. Да, есть крутые шаблонизаторы по типу `jinja`, но обычно они не дают динамики. Есть конечно решения по типу `turbo-flask`, но боюсь их знают единицы, и не просто так 😑 Они довольно костыльны и давно не обновляются.

По этому `reflex` со своей лёгкостью входа и мощным функционалом из коробки занимает своё место в мире разработки.