# Если человеку нужно поработать над нашим сервисом, нужно последовательно выполнить команды:
# 1. Установка виртуальной среды с библиотеками
# pipenv install
#
# # 2. Активация виртуальной среды
# pipenv shell
#
# # 3. Обеспечиваем доступ к сервису
# python churn_serving.py
# # Альтернативный вар:
# pipenv run python churn_serving.py



# Должны увидеть результат:
#  * Serving Flask app 'churn'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:9696
#  * Running on http://192.168.0.11:9696
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 572-002-360