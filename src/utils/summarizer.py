from langchain import PromptTemplate
from collections import defaultdict
from langchain_community.llms import OpenAI
import os

llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def summarize_articles(articles):
    # Group articles by topic
    topics = defaultdict(list)
    for article in articles:
        topic = article.get('topic')  # Assuming each article has a 'topic' field
        topics[topic].append(article)

    summaries = []
    for topic, articles in topics.items():
        # Create a prompt for summarization
        prompt_text = f"Summarize the following articles on the topic '{topic}':\n"
        for article in articles:
            prompt_text += f"- {article['title']} ({article['link']}): {article['full_text']}\n"

        # Use Langchain to generate a summary
        prompt = PromptTemplate(template=prompt_text).invoke({})
        llm.invoke(prompt)

        # Collect the summary and source links
        source_links = [article['link'] for article in articles]
        summaries.append({
            'topic': topic,
            'summary': summary,
            'source_links': source_links
        })

    return summaries