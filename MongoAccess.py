# _*_ coding:utf-8 _*_

# MongoAcc                                              #
# Este script utiliza o driver PyMongo para acessar a   #
# base de dados do MongoDB criada previamente com o     #
# script TwitterSimpleCapt. Note que, todas as funções  # 
# estão entre uma condição de loop para possibilitar o  #
# acompanhamento dos resultados em tempo real.          #

# @author Robert Carlos                                 #
# email robert.n.roll@gmail.com                         #
# 2016-12-23 (CC BY 3.0 BR)                             #

from pymongo import MongoClient

def mongo_menu():
    '''
    Menu principal para funções que acessam
    a base de dados no MongoDB
    '''
    print 'MongoMenu'
    print '1 - popularidade por país'
    print '2 - popularidade por idioma'
    print '3 - tweets por usuário'
    print '0 - sair'
    escolha = raw_input('')
    if escolha == '1':
        twitter_popular_pais()
    elif escolha == '2':
        twitter_popular_idioma()
    elif escolha == '3':
        twitter_por_data_criacao()
    else:
        print 'Saindo...'
        quit()

        
def twitter_popular_pais():
    '''
    Agrupa os tweets por país de origem e soma o total
    de tweets enviados por cada conjunto   
    '''
    client = MongoClient()
    db = client.Twitter
    escolha = 's'
    print 'PAÍS | TOTAL'
    
    while escolha == 's':
        for doc in db.tweets.aggregate([
            {'$group': {'_id': '$country', 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}},
            {'$limit': 10}]):
            print doc['_id'],'->',doc['count']
            
        client.close()
        print '\n'
        escolha = raw_input('Deseja atualizar a lista? s/n ')
    mongo_menu()
    

def twitter_popular_idioma():
    '''
    Agrupa os tweets por idioma e soma o total
    de tweets para cada conjunto
    '''
    client = MongoClient()
    db = client.Twitter
    escolha = 's'
    print 'LANG | TOTAL'
    while escolha == 's':
        for doc in db.tweets.aggregate([
            {'$group': {'_id': '$lang', 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}},
            {'$limit': 5}]):
            print doc['_id'],'->',doc['count']
        client.close()
        print '\n'
        escolha = raw_input('Deseja atualizar a lista? s/n ')
    mongo_menu()

    
def twitter_por_data_criacao():
    '''
    Agrupa os tweets por data de criação e soma o total
    de tweets enviados por cada conjunto de ano
    '''
    client = MongoClient()
    db = client.Twitter
    escolha = 's'
    print 'ANO | TOTAL'
    while escolha == 's':
        for doc in db.tweets.aggregate([
            {'$group': { '_id' :{'$year' : '$us_created_at'},
                        'count' : {'$sum': 1}}},
            {'$sort' : {'count' : 1}}
        ]):
            print doc['_id'],'->',doc['count']
        client.close()
        print '\n'
        escolha = raw_input('Deseja atualizar a lista? s/n ')

    
if __name__ == '__main__':
    mongo_menu()
    
