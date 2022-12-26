from .manager import ConnectDB

class ClientDB(object):

    def __init__(self, tb_name) -> None:
        
        self.db = ConnectDB()
        self.tb_name = tb_name
        self.create_tb()

    def close(self):
        self.db.close()

    def create_tb(self):
        try:
            self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS {tb_name} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                end TEXT NOT NULL,
                num INTEGER NOT NULL
            )
            """.format(tb_name=self.tb_name))

        except ImportError as e:
            raise e
    
    def insert(self, **kwargs):
        assert kwargs

        keys_input = ""
        value_input = ""

        for key, value in kwargs.items():
            keys_input += f"{key}, "
            tmp = f"{value}"
            if isinstance(value, str):
                tmp = f"'{value}'"
            
            value_input += f"{tmp}, "
        
        keys_input = keys_input[:-2]
        value_input = value_input[:-2]

        query = f"INSERT INTO {self.tb_name} ({keys_input}) VALUES ({value_input})"
        
        self.db.cursor.execute(query)
        self.db.commit()
    
    def select_all(self):
        query = f"SELECT * FROM {self.tb_name} ORDER BY end"
        r = self.db.cursor.execute(query)
       
        return r.fetchall()
    
    def get_query(self):
        r = self.select_all()
        
        results = {}
        for i in r:
            print(i)
            # new_d = dict(i)
            # new_d.pop("id")
            # print(new_d)
            # results[i[0]] = new_d.copy()

        return results
    # def imprimir_todos_clientes(self):
    #     lista = self.select_all()
    #     print('{:>3s} {:20s}'.format(
    #         'id', 'nome', 'idade', 'cpf', 'email', 'fone', 'cidade', 'uf', 'criado_em'))
    #     for c in lista:
    #         print('{:3d} {:23s}'.format(
    #             c[0], c[1]))