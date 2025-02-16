from app.services.platform_service import PlatformService
from app.services.account_service import AccountService
from app.services.insight_service import InsightService
from app.utils.process_data_helper import ProcessDataHelper
import pandas as pd

class GeneralService:
    
    def get_general_data(resume = False):

        platforms = PlatformService.get_platforms()

        if not platforms:
            return False

        all_data = []

        for platform in platforms:
            
            accounts = AccountService.get_accounts(platform["value"])
            if not accounts:
                return False
            
            fields = InsightService.get_fields(platform["value"])
            if not fields:
                return False

            data = ProcessDataHelper.process_data(platform["value"], accounts, fields, resume)
            
            df = pd.DataFrame(data["body"], columns=data["header"])
            df = GeneralService.standardize_headers(df)
            all_data.append(df)

        df_combined = pd.concat(all_data, ignore_index=True)
        csv = df_combined.to_csv(index=False)

        return csv
    
    def standardize_headers(df):

        column_map = {
            "region": "country", 
            "adName": "ad_name",
            "cost_per_click": "cpc",
            "cost": "spend",
            "effective_status": "status"
        }

        df.rename(columns=column_map, inplace=True)
    
        df = df.loc[:, ~df.columns.duplicated()]
        
        return df
