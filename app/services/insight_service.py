from app.utils.request_helper import RequestHelper


class InsightService:

    @staticmethod
    def get_fields(platform: str) -> str:

        endpoint = "fields"
        params = {"platform": platform}

        fields = RequestHelper.fetch_data(endpoint, params)

        pagination = RequestHelper.verify_pagination(fields)

        if pagination:
            fields = RequestHelper.get_outers_pages(fields, endpoint, params)

        return fields[endpoint]

    @staticmethod
    def get_insights(platform: str, account: dict, fields: str) -> dict:

        endpoint = "insights"
        params = {
            "platform": platform,
            "account": account["id"],
            "token": account["token"],
            "fields": ",".join(field["value"] for field in fields),
        }

        insights = RequestHelper.fetch_data(endpoint, params=params)

        pagination = RequestHelper.verify_pagination(insights)

        if pagination:
            insights = RequestHelper.get_outers_pages(insights, endpoint, params)

        return insights[endpoint]
