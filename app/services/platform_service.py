from app.services.account_service import AccountService
from app.services.insight_service import InsightService
from app.utils.request_helper import RequestHelper
from app.utils.process_data_helper import ProcessDataHelper
from app.utils.csv_helper import CsvHelper


class PlatformService:

    def get_platform_data(platform, resume=False):

        accounts = AccountService.get_accounts(platform)

        if not accounts:
            return False

        fields = InsightService.get_fields(platform)

        if not fields:
            return False

        data = ProcessDataHelper.process_data(platform, accounts, fields, resume)

        if not data:
            return False

        return CsvHelper.generate_csv(data)

    def get_platforms() -> dict:

        endpoint = "platforms"

        platforms = RequestHelper.fetch_data(endpoint)
        pagination = RequestHelper.verify_pagination(platforms)

        if pagination:
            platforms = RequestHelper.get_outers_pages(platforms, endpoint, False)

        return platforms[endpoint]
