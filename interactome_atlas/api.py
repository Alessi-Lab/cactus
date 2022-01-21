from tornado.httpclient import AsyncHTTPClient


class InteractomeAtlas:
    def __init__(self):
        self.base_url = "http://www.interactome-atlas.org/app.php/"

    async def get_interactions(self, proteins):
        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}search_results_interactions?query_interactor=query&page=results&query_id_array={proteins}&search_term_parameter={proteins}&filter_parameter=None&search_term_array%5B%5D={proteins}", method="GET")
        return res.body
