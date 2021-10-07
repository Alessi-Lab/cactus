from urllib.parse import urlencode

from tornado.escape import url_escape, json_encode
from tornado.httpclient import AsyncHTTPClient


class StringDB:
    def __init__(self):
        self.base_url = "https://version-11-5.string-db.org"

    async def get_string_ids(self, gene_names, species):
        params = {
            "echo_query": 1,
            "species": species
        }
        if not isinstance(gene_names, str):
            params["identifiers"] = "\r".join(gene_names)
        else:
            params["identifiers"] = gene_names

        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}/api/tsv/get_string_ids", method="POST", body=urlencode(params))
        return res.body

    async def get_interaction(self, entry_list, species, network_type):
        params = {
            "species": species,
            "network_type": network_type
        }

        if not isinstance(entry_list, str):
            params["identifiers"] = "\r".join(entry_list)
        else:
            params["identifiers"] = entry_list

        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}/api/tsv/interaction_partners", method="POST", body=urlencode(params))
        return res.body

    async def get_enrichment(self, study, universe, species):
        params = {"species": species}
        if not isinstance(study, str):
            params["identifiers"] = "\r".join(study)
        else:
            params["identifiers"] = study
        if not isinstance(universe, str):
            params["background_string_identifiers"] = "\r".join(universe)
        else:
            params["background_string_identifiers"] = universe
        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}/api/tsv/enrichment", method="POST", body=urlencode(params))
        return res.body
