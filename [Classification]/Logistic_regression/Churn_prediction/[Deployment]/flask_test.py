from flask import Flask

app = Flask('test') # Создаем приложение Flask 'test'

@app.route('/ping', methods=['GET']) # Регистрирует маршрут и назначает его функции ping
def ping():
    return 'PONG'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)