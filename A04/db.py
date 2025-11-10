#!/usr/bin/env python3
import sys
import os
import csv
import sqlite3
from pathlib import Path

class WorldDB:
    def __init__(self, argv):
        # Allowed only one "global": the class instance
        self.args = argv[1:]
        self.db_path = "db.sqlite"
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON;")

    # ---------- utilities ----------
    def table_exists(self, table_name):
        cur = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (table_name,)
        )
        return cur.fetchone() is not None

    def quoted(self, name):
        return '"' + name.replace('"', '""') + '"'

    # ---------- CSV import ----------
    def import_csv(self, csv_path):
        table = Path(csv_path).stem  # filename without extension
        if self.table_exists(table):
            return  # do not recreate table if exists

        with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f, delimiter=';')  # <<< FIXED: semicolon CSV files
            try:
                headers = next(reader)
            except StopIteration:
                return

            # Create table (all TEXT columns)
            cols_sql = ", ".join(f"{self.quoted(h)} TEXT" for h in headers)
            self.conn.execute(f"CREATE TABLE {self.quoted(table)} ({cols_sql});")

            # Prepare insert
            placeholders = ", ".join(["?"] * len(headers))
            insert_sql = f"INSERT INTO {self.quoted(table)} VALUES ({placeholders});"

            # Insert rows
            rows = [row for row in reader]
            self.conn.executemany(insert_sql, rows)
            self.conn.commit()

    def import_from_args(self):
        for p in self.args:
            if not os.path.isfile(p):
                print(f"CSV file not found: {p}")
                continue
            self.import_csv(p)

    # ---------- Answer Question #2 ----------
    def get_column(self, table, want):
        cur = self.conn.execute(f'PRAGMA table_info({self.quoted(table)});')
        for row in cur.fetchall():
            if row["name"].lower() == want.lower():
                return row["name"]
        return None

    def answer_q2(self):
        """
        Q2: What is the total population of Southern Europe?
        """
        question = "What is the total population of Southern Europe?"

        if not self.table_exists("country"):
            print(question)
            print("Answer: (cannot compute – table 'country' missing)")
            return

        region_col = self.get_column("country", "Region")
        pop_col = self.get_column("country", "Population")

        if not region_col or not pop_col:
            print(question)
            print("Answer: (cannot compute – 'Region' or 'Population' column missing)")
            return

        sql = f"""
        SELECT SUM(CAST({self.quoted(pop_col)} AS INTEGER)) AS total
        FROM {self.quoted("country")}
        WHERE {self.quoted(region_col)} = 'Southern Europe';
        """

        cur = self.conn.execute(sql)
        row = cur.fetchone()
        total = row["total"] if row and row["total"] is not None else 0

        print(question)
        print(f"Answer: {total}")

    # ---------- main ----------
    def run(self):
        if self.args:  # if CSVs were provided: import them
            self.import_from_args()
        self.answer_q2()
        self.conn.close()


def main():
    app = WorldDB(sys.argv)
    app.run()

if __name__ == "__main__":
    main()
