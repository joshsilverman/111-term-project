from queries import queries
from datasource.database_map import map 
from utilities.defs import *
from sql_log import log as sqlLog

from pprint import pprint
import sqlite3

class QueryLib():
    
    def execute(self, queryName):
        
        sql = queries[queryName]['sql']
        tables = queries[queryName]['tables']
        sqlLog.append(sql)
        
        connection = sqlite3.connect(TRANSCRIPT)
        cursor = connection.cursor()
        sqlArray = sql.split(';\n')
        for sqlStatement in sqlArray:
            cursor.execute(sqlStatement)
            connection.commit()
        
        return self._mapResults(cursor.fetchall(), tables)
    
    def customQuery(self, sql, tables):
        
        sqlLog.append(sql)
        
        connection = sqlite3.connect(TRANSCRIPT)
        cursor = connection.cursor()
        sqlArray = sql.split(';\n')
        for sqlStatement in sqlArray:
            cursor.execute(sqlStatement)
            connection.commit()
            
        return self._mapResults(cursor.fetchall(), tables)
    
    def _mapResults(self, results, tables):
        
        resultsList = []
        tableFields = []
        for table in tables:
            tableFieldsTmp = ['%s.%s' % (table, field) for field in map[table]['fields']]
            tableFields.extend(tableFieldsTmp)
            
        for record in results:
            resultsList.append(dict(zip(tableFields, record)))
        
        return resultsList