import requests
import copy
import pandas as pd

url = "https://wabi-brazil-south-api.analysis.windows.net/public/reports/querydata"

querystring = {"synchronous":"true"}

payload = {
    "version": "1.0.0",
    "queries": [
        {
            "Query": {"Commands": [{"SemanticQueryDataShapeCommand": {
                            "Query": {
                                "Version": 2,
                                "From": [
                                    {
                                        "Name": "m",
                                        "Entity": "MEDICAMENTO (2)",
                                        "Type": 0
                                    }
                                ],
                                "Select": [
                                    {
                                        "Column": {
                                            "Expression": {"SourceRef": {"Source": "m"}},
                                            "Property": "Desc. Produto"
                                        },
                                        "Name": "MEDICAMENTO (2).Desc. Produto"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {"SourceRef": {"Source": "m"}},
                                            "Property": "Disp. de  Estoque"
                                        },
                                        "Name": "MEDICAMENTO (2).Disp. de  Estoque"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {"SourceRef": {"Source": "m"}},
                                            "Property": "Abastecimento"
                                        },
                                        "Name": "MEDICAMENTO (2).Abastecimento"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {"SourceRef": {"Source": "m"}},
                                            "Property": "Código"
                                        },
                                        "Name": "MEDICAMENTO (2).Código"
                                    },
                                    {
                                        "Column": {
                                            "Expression": {"SourceRef": {"Source": "m"}},
                                            "Property": "Local"
                                        },
                                        "Name": "MEDICAMENTO (2).Local"
                                    },
                                    {
                                        "Measure": {
                                            "Expression": {"SourceRef": {"Source": "m"}},
                                            "Property": "Status_Estoque"
                                        },
                                        "Name": "MEDICAMENTO (2).Status_Estoque"
                                    }
                                ],
                                "Where": [{"Condition": {"Not": {"Expression": {"In": {
                                                        "Expressions": [{"Column": {
                                                                    "Expression": {"SourceRef": {"Source": "m"}},
                                                                    "Property": "Desc. Produto"
                                                                }}],
                                                        "Values": [[{"Literal": {"Value": "null"}}]]
                                                    }}}}}],
                                "OrderBy": [
                                    {
                                        "Direction": 1,
                                        "Expression": {"Column": {
                                                "Expression": {"SourceRef": {"Source": "m"}},
                                                "Property": "Desc. Produto"
                                            }}
                                    }
                                ]
                            },
                            "Binding": {
                                "Primary": {"Groupings": [{"Projections": [4, 3, 2, 0, 1, 5]}]},
                                "DataReduction": {
                                    "DataVolume": 3,
                                    "Primary": {"Window": {"Count": 1000}}
                                },
                                "SuppressedJoinPredicates": [5],
                                "Version": 1
                            },
                            "ExecutionMetricsKind": 1
                        }}]},
            "CacheKey": "{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"m\",\"Entity\":\"MEDICAMENTO (2)\",\"Type\":0}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Desc. Produto\"},\"Name\":\"MEDICAMENTO (2).Desc. Produto\"},{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Disp. de  Estoque\"},\"Name\":\"MEDICAMENTO (2).Disp. de  Estoque\"},{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Abastecimento\"},\"Name\":\"MEDICAMENTO (2).Abastecimento\"},{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Código\"},\"Name\":\"MEDICAMENTO (2).Código\"},{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Local\"},\"Name\":\"MEDICAMENTO (2).Local\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Status_Estoque\"},\"Name\":\"MEDICAMENTO (2).Status_Estoque\"}],\"Where\":[{\"Condition\":{\"Not\":{\"Expression\":{\"In\":{\"Expressions\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Desc. Produto\"}}],\"Values\":[[{\"Literal\":{\"Value\":\"null\"}}]]}}}}}],\"OrderBy\":[{\"Direction\":1,\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"m\"}},\"Property\":\"Desc. Produto\"}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[4,3,2,0,1,5]}]},\"DataReduction\":{\"DataVolume\":3,\"Primary\":{\"Window\":{\"Count\":500}}},\"SuppressedJoinPredicates\":[5],\"Version\":1},\"ExecutionMetricsKind\":1}}]}",
            "QueryId": "",
            "ApplicationContext": {
                "DatasetId": "e64a28f3-7573-4749-a62b-2a69dbd21bed",
                "Sources": [
                    {
                        "ReportId": "2581c7c6-bf20-473c-8eb3-59b7f017ae02",
                        "VisualId": "d8977c1025b4b21c342b"
                    }
                ]
            }
        }
    ],
    "cancelQueries": [],
    "modelId": 2674899
}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "ActivityId": "4c7b3271-fbe6-bb8f-8bf1-2fefbd4add02",
    "RequestId": "7a86cef9-cf67-b777-a5ff-42fba1cbdf56",
    "X-PowerBI-ResourceKey": "61b565c0-8c8b-4bc4-a68e-083d41c912d2",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://app.powerbi.com",
    "Connection": "keep-alive",
    "Referer": "https://app.powerbi.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

data = response.json()


dim = data["results"][0]["result"]["data"]["dsr"]["DS"][0]["ValueDicts"]

rows = data["results"][0]["result"]["data"]["dsr"]["DS"][0]["PH"][0]["DM0"]

res = []

res.append([dim["D0"][0],dim["D1"][0], dim["D2"][0], dim["D3"][0], dim["D4"][0]])



for idx, row in enumerate(rows[1:]):

    C = row["C"]
    if "R" in row:
        
        # usando idx para copiar a anterior
        aux = copy.deepcopy(res[idx])
        pos = 0

        r = row["R"]

        if "Ø" in row:
            skip = row["Ø"]
        else:
            skip = 0
         
        while r > 0 or pos < 5:
            if skip & 1 == 1:
                aux[pos] = ""

            elif (r & 1)  == 0:
                
                aux[pos] = dim[f"D{pos}"][C[0]] if type(C[0]) == int else C[0]
                C = C[1:]
                

            pos += 1
            r = r >> 1
            skip = skip >> 1
            
        res.append(aux)

    else:
        C = C[:-1]
        res.append([dim[f"D{idx}"][elem] if type(elem) == int else elem for idx,elem in enumerate(C) ])
      

from pprint import pprint
#pprint(res)

df = pd.DataFrame(res, columns = ["loc", "cod", "orgao", "nome", "disp"])
df.to_csv("teste.csv", index=False)