from urllib.parse import urlencode

from tornado.escape import url_escape, json_encode
from tornado.httpclient import AsyncHTTPClient


class StringDB:
    def __init__(self):
        self.base_url = "https://version-11-5.string-db.org"

    async def get_string_ids(self, gene_names, species):
        params = {
            "identifiers": "\r".join(gene_names),
            "echo_query": 1,
            "species": species
        }

        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}/api/tsv/get_string_ids", method="POST", body=urlencode(params))
        return res.body

    async def get_interaction(self, entry_list, species, network_type):
        params = {
            "identifiers": "\r".join(entry_list),
            "species": species,
            "network_type": network_type
        }
        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}/api/tsv/interaction_partners", method="POST", body=urlencode(params))
        return res.body

    async def get_enrichment(self, study, universe, species):
        params = {
            "identifiers": "\r".join(study),
            "background_string_identifiers": "\r".join(universe),
            "species": species
        }

        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}/api/tsv/enrichment", method="POST", body=urlencode(params))
        return res.body
