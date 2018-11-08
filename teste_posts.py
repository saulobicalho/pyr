def consulta_cep(cep):
    import requests
    response = requests.get('https://viacep.com.br/ws/70150900/%s/json/'%cep)
    print cep
    print __name__

    inf __name__ == '__main__':
        consulta_cep('8788')
