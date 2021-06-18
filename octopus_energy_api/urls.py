


class urls:

    @classmethod
    def build_url(cls, extension, params=None):
        base_url = "https://api.octopus.energy"

        params = '' if params is None else str(params)

        return base_url + extension + params

    @classmethod
    def accounts_url(cls, account_number: str):
        
        url = cls.build_url(f"/v1/accounts/{account_number}")
        
        return url
    
    @classmethod
    def products_url(cls):
        
        url = cls.build_url("/v1/products/?brand=OCTOPUS_ENERGY")

        return url

    @classmethod
    def consumption_url(cls, mpan, serial, start, end, page_size=25000):
        
        setup = f"/v1/electricity-meter-points/{mpan}/meters/{serial}/consumption"
        params = parameters=f"?page_size={page_size}&period_from={start}&period_to={end}&order_by=period"

        url = cls.build_url(setup, params=params)

        return url

    @classmethod
    def meter_point_url(cls, mpan):
        
        setup=f"/v1/electricity-meter-points/{mpan}/"

        url = cls.build_url(setup)

        return url