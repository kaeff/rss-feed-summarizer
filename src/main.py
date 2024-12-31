from flask import Flask, request, jsonify
from utils.feed_downloader import download_feed
from utils.text_extractor import extract_full_text
from utils.summarizer import summarize_articles

app = Flask(__name__)

@app.route('/summarize', methods=['GET'])
def summarize():
    feed_url = request.args.get('feedUrl')
    if not feed_url:
        return jsonify({'error': 'feedUrl query parameter is required'}), 400

    # Download the RSS feed
    feed_data = download_feed(feed_url)
    articles = []

    # Extract full text for each item in the feed
    for item in feed_data:
        # full_text = extract_full_text(item['link'])
        full_text = item['summary']
        articles.append({'title': item['title'], 'full_text': full_text, 'link': item['link']})

    # Summarize articles by topic
    summaries = summarize_articles(articles)

    # Create the summarized RSS feed output
    summarized_feed = {
        'version': '1.0',
        'items': [{'topic': topic, 'summary': summary['summary'], 'links': summary['links']} for topic, summary in summaries.items()]
    }

    return jsonify(summarized_feed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)