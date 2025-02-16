from app.utils.request_helper import RequestHelper


class AccountService:

    @staticmethod
    def get_accounts(platform: str) -> dict:

        endpoint = "accounts"
        params = {"platform": platform}

        accounts = RequestHelper.fetch_data(endpoint, params)
        pagination = RequestHelper.verify_pagination(accounts)

        if pagination:
            accounts = RequestHelper.get_outers_pages(accounts, endpoint, params)

        return accounts[endpoint]
