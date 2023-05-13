from flask import Flask, render_template
import os

app = Flask(__name__)

NEWS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news")

NEWS_FILES = {
    "news1.html"
    "news2.html"
    "news3.html"
}

@app.route("/")
def index():
    news_items = []
    for news_file in NEWS_FILES:
        new_path = os.path.join(NEWS_FOLDER, news_file)
        with open(new_path, "r") as f:
            news_content = f.read()
            news_items.append(news_content)
    return render_template("index.html", news_items=news_items)

if __name__ == "__main__":
    app.run()
