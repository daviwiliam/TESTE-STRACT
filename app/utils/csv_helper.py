import csv
from io import StringIO


class CsvHelper:

    @staticmethod
    def generate_csv(data: dict) -> str:

        output = StringIO()
        writer = csv.writer(output)

        writer.writerow(data["header"])
        writer.writerows(data["body"])

        output.seek(0)

        return output.getvalue()
