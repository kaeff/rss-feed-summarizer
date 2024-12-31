# RSS Feed Summarizer

This project is a web application that summarizes RSS feeds. It takes an RSS or Atom feed URL as input and processes the feed to extract full text articles, group them by topic, and generate a summarized RSS feed output.

## Project Structure

```
rss-feed-summarizer
├── src
│   ├── main.py               # Entry point of the application
│   ├── utils
│   │   ├── feed_downloader.py # Downloads and parses the RSS feed
│   │   ├── text_extractor.py  # Extracts full text from articles
│   │   └── summarizer.py      # Summarizes articles by topic
├── requirements.txt           # Project dependencies
├── Dockerfile                  # Docker image configuration
└── cloudbuild.yaml            # Google Cloud Build configuration
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/rss-feed-summarizer.git
   cd rss-feed-summarizer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Build the Docker image:
   ```
   docker build -t rss-feed-summarizer .
   ```

4. Run the application:
   ```
   python src/main.py
   ```

## Usage

To use the application, send a GET request to the server with the `feedUrl` query parameter:

```
http://localhost:5000/summarize?feedUrl=<YOUR_FEED_URL>
```

The server will respond with a summarized RSS feed containing entries grouped by topic.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.