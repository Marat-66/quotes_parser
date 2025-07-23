import requests
import json
import pandas as pd
from bs4 import BeautifulSoup


class QuotesParser:
    BASE_URL = "https://quotes.toscrape.com/page/1/"

    def __init__(self):
        self.quotes = []

    def fetch(self):
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        quote_blocks = soup.select("div.quote")

        for block in quote_blocks:
            text = block.find("span", class_="text").get_text()
            author = block.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in block.select(".tags .tag")]

            self.quotes.append({
                "text": text,
                "author": author,
                "tags": tags
            })

    def get_all_quotes(self):
        return self.quotes

    def search_by_author(self, name):
        return [q for q in self.quotes if name.lower() in q['author'].lower()]

    def search_by_tag(self, tag):
        return [q for q in self.quotes if tag.lower() in [t.lower() for t in q['tags']]]

    def search_by_tags(self, tags):
        tags = [t.lower() for t in tags]
        return [q for q in self.quotes if all(tag in [t.lower() for t in q['tags']] for tag in tags)]

    def export_to_json(self, filename="quotes.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.quotes, f, ensure_ascii=False, indent=2)

    def export_to_excel(self, filename="quotes.xlsx"):
        df = pd.DataFrame(self.quotes)
        df.to_excel(filename, index=False)


if __name__ == "__main__":
    parser = QuotesParser()
    parser.fetch()

    print(" Цитаты Альберта Эйнштейна:")
    for q in parser.search_by_author("Einstein"):
        print(f"- {q['text']} ({q['author']})")

    print("Цитаты по тегу 'life':")
    for q in parser.search_by_tag("life"):
        print(f"- {q['text']} ({q['author']})")

    print("Цитаты по тегам 'life' и 'inspirational':")
    for q in parser.search_by_tags(["life", "inspirational"]):
        print(f"- {q['text']} ({q['author']})")

    parser.export_to_json()
    parser.export_to_excel()
    print("\n✅ Экспорт завершён: quotes.json и quotes.xlsx")

