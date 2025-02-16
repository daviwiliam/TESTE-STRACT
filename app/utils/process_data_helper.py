from app.services.insight_service import InsightService


class ProcessDataHelper:

    def process_data(platform, accounts, fields, resume=False):

        data = {"header": [], "body": []}

        for account in accounts:

            insights = InsightService.get_insights(platform, account, fields)

            if not insights:
                return False

            account_data = ProcessDataHelper.process_account_data(
                platform, account, insights
            )
            header = account_data[0]
            account_data.pop(0)
            data["body"].extend(account_data)

        if resume:
            data["body"] = ProcessDataHelper.process_resume_data(data["body"], platform)

        header.insert(0, "Plataform")
        header.insert(1, "Account Name")

        data["header"] = header

        return data

    def process_account_data(platform, account, insights):

        processed = ProcessDataHelper.process_insights(insights)

        for row in processed[1:]:
            row.insert(0, platform)
            row.insert(1, account["name"])

        return processed

    def process_insights(insights):

        keys = [key for key in insights[0].keys() if key != "id"]
        rows = [keys]

        for insight in insights:
            row = [insight.get(key, "") for key in keys]
            rows.append(row)

        return rows

    def process_resume_data(data, platform):

        total_row = [None if isinstance(value, str) else 0 for value in data[0]]

        for row in data:
            for i, value in enumerate(row):
                if isinstance(value, (int, float)):
                    total_row[i] += value
                elif value == platform and total_row[i] is None:
                    total_row[i] = platform

        return [total_row]
