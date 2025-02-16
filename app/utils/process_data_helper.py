from app.services.insight_service import InsightService


class ProcessDataHelper:

    @staticmethod
    def process_data(platform: str, accounts: list, fields: str, resume: bool = False) -> list:

        data = {"header": [], "body": []}

        for account in accounts:

            insights = InsightService.get_insights(platform, account, fields)

            if not insights:
                return False

            account_data = ProcessDataHelper.process_account(
                platform, account, insights
            )
            header = account_data[0]
            account_data.pop(0)
            data["body"].extend(account_data)

        if resume:
            data["body"] = ProcessDataHelper.process_resume(data["body"], platform)

        header.insert(0, "Plataform")
        header.insert(1, "Account Name")

        data["header"] = header

        return data
    
    @staticmethod
    def process_account(platform: str, account: list, insights: list) -> list:

        processed = ProcessDataHelper.process_insights(insights)

        for row in processed[1:]:
            row.insert(0, platform)
            row.insert(1, account["name"])

        return processed

    @staticmethod
    def process_insights(insights: list) -> list:

        keys = [key for key in insights[0].keys() if key != "id"]
        rows = [keys]

        for insight in insights:
            row = [insight.get(key, "") for key in keys]
            rows.append(row)

        return rows

    @staticmethod
    def process_resume(data: dict, platform: str) -> dict:

        total_row = [None if isinstance(value, str) else 0 for value in data[0]]

        for row in data:
            for i, value in enumerate(row):
                if isinstance(value, (int, float)):
                    total_row[i] += value
                elif value == platform and total_row[i] is None:
                    total_row[i] = platform

        return [total_row]
