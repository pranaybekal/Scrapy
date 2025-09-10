# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import json
from itemadapter import ItemAdapter


class WorkThreePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        for field in ['title', 'location', 'date', 'Category']:
            value = adapter.get(field)

            # If it's a list, join or pick first
            if isinstance(value, list):
                value = ", ".join(v.strip() for v in value if isinstance(v, str))

            # If it's a string, strip it
            if isinstance(value, str):
                value = value.strip()

            adapter[field] = value
        return item


class SaveToJsonPipeline:
    def open_spider(self, spider):
        self.file = open('workthree.json', 'w', encoding='utf-8')
        self.file.write("[")

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item


class SaveToSQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("workthree.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS quotes(
                title TEXT, 
                location TEXT, 
                date TEXT, 
                Category TEXT
            )
        """)

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO quotes (title, location, date, Category) 
            VALUES (?, ?, ?, ?)
        """, (
            item.get('title'),
            item.get('location'),
            item.get('date'),
            item.get('Category')
        ))
        self.conn.commit()
        return item