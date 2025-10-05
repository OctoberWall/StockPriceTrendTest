# coding:utf-8

from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    # ダミーデータ
    ticker = yf.Ticker("GOOGL")
    hist = ticker.history(period='5d', interval='1h' )
    #ラベル
    labels = hist.index.strftime("%Y-%m-%d %H:%M").tolist()
    #終値
    prices = hist['Close'].round(2).tolist()

    #データ
    data = {
        'labels':labels,
        'datasets':[
            {
                'label': 'GOOGLの株価です(GOOGL)',
                'data': prices,
                'borderColor': 'rgba(75, 192, 192, 1)',
                'fill': False
            }
        ]
    }

    return render_template('index.html', data=data)



@app.route('/results', methods=['POST'])
def move_results():
    return render_template("results.html")

if __name__ == '__main__':
    app.debug = True
    app.run()

# デバッグモードTrueにすると変更が即反映される
# ファイルのエンコードはUTF-8で保存すること
# 下記URLをブラウザに打ち込むとページが開く
# http://127.0.0.1:5000/
