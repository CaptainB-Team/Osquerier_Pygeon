import osquery

def sendQuery(inQuery):
    osqClient = osquery.ExtensionClient()
    osqClient.open()
    queryResult = osqClient.extension_client().query(inQuery)
    if(queryResult.status.code != 0):
        return ('ERROR: Problem running query: ' + str(queryResult.status.message))
    else:
        result = ''
        for row in queryResult.response:
            rowResult = '{'
            for key, val in row.items():
                rowResult += '\'' + str(key) + '\' : ' + str(val) + ', '
            rowResult = rowResult[:-2]
            result += rowResult + '}, '
    return result
