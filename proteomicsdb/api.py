from tornado.httpclient import AsyncHTTPClient


class ProteomicsDB:
    def __init__(self):
        self.base_url = "https://www.proteomicsdb.org"

    async def get_expression(self, proteins):
        client = AsyncHTTPClient()
        res = await client.fetch(f"{self.base_url}/proteomicsdb/logic/api/proteinexpression.xsodata/InputParams(PROTEINFILTER='{proteins}',MS_LEVEL=1,TISSUE_ID_SELECTION='',TISSUE_CATEGORY_SELECTION='tissue;cell line',SCOPE_SELECTION=1,GROUP_BY_TISSUE=1,CALCULATION_METHOD=0,EXP_ID=-1)/Results?$select=UNIQUE_IDENTIFIER,TISSUE_ID,TISSUE_NAME,TISSUE_SAP_SYNONYM,SAMPLE_ID,SAMPLE_NAME,AFFINITY_PURIFICATION,EXPERIMENT_ID,EXPERIMENT_NAME,EXPERIMENT_SCOPE,EXPERIMENT_SCOPE_NAME,PROJECT_ID,PROJECT_NAME,PROJECT_STATUS,UNNORMALIZED_INTENSITY,NORMALIZED_INTENSITY,MIN_NORMALIZED_INTENSITY,MAX_NORMALIZED_INTENSITY,SAMPLES&$format=json", method="GET")
        return res.body
