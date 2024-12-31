def download_feed(feed_url):
    import feedparser

    # Fetch the RSS or Atom feed
    feed = feedparser.parse(feed_url)

    # Check for errors in fetching the feed
    if feed.bozo:
        raise Exception("Failed to parse feed: " + feed.bozo_exception)

    return feed.entries