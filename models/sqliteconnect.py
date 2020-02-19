from flask import *
import sqlite3



class sqliteconnect():
    query = ''
    table = ''
    cur = ''
    constr = ''

    def __init__(self):
        self.constr = sqlite3.connect('blogflask.db')
        cur = self.constr.cursor()
        self.cur = cur

    def fetchall(self):
        result = self.cur.execute(self.query)
        return result.fetchall()
        # return self.query

    def runquery(self):
        try:
            self.cur.execute(self.query)
            return self.constr.commit()
        except Exception as error:
            return {"error": error}

        # return self.query

    def select(self, fields, table):
        self.query = "select {field} from {table}".format(
            field=fields, table=table)
        self.table = table
        return self

    def joinit(self, direction, table, statement):
        self.query += " {dir} JOIN {tb} on {state}".format(
            dir=direction,
            tb=table,
            state=statement)
        return self

    def where(self, statement):
        self.query += " where {state}".format(state=statement)
        return self

    def orderby(self, field, DESCorASC):
        self.query += " ORDER BY {table}.{field} {ASC}".format(
            table=self.table,
            field=field,
            ASC=DESCorASC)
        return self

    def insertinto(self, table, columns, values):
        self.query = "insert into {tbl}  {columns}  values  {values} ".format(
            tbl=table,
            columns=columns,
            values=values
        )
        return self

    def deletefrom(self, table, condition):
        self.query = "DELETE FROM {table_name} WHERE {condition}".format(
            table_name=table,
            condition=condition
        )
        return self

    def updateit(self, table, datadic, condition):
        newdata = " ,  ".join(
            " {key} = '{value}' ".format(key=key, value=value)
            for key, value in datadic.items()
        )
        self.query = "UPDATE {table_name} SET {newdata} WHERE {condition}".format(
            table_name=table,
            newdata=newdata,
            condition=condition
        )
        return self
