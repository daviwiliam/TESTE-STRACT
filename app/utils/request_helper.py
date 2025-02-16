import requests
from app.config import API_BASE_URL, HEADERS


class RequestHelper:

    def fetch_data(endpoint: str, params: dict = None) -> dict:
        url = f"{API_BASE_URL}{endpoint}"

        try:
            response = requests.get(url, headers=HEADERS, params=params, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar {url}: {e}")
            return {}

    def verify_pagination(response: dict) -> bool:
        if not response or "pagination" not in response:
            return False

        return True

    def get_outers_pages(response: dict, endpoint: str, params: dict) -> dict:
        current = response.get("pagination", {}).get("current", 1)
        total = response.get("pagination", {}).get("total", 1)

        while current < total:

            current += 1
            params["page"] = current

            response_complement = RequestHelper.fetch_data(endpoint, params)

            if not response_complement or endpoint not in response_complement:
                break

            response[endpoint].extend(response_complement[endpoint])

        return response
