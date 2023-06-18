AGENDA = {
    'lf': {
        'phone': '81998365620',
        'email': 'lifas@gmail.com',
        'address': 'rua dom manoel da costa'
    },
    'joner': {
        'phone': '81999999929',
        'email': 'joner@gmail.com',
        'address': 'rua manuel de carvalho'
    },
    'moraes': {
        'phone': '81972371371',
        'email': 'rajninja@gmail.com',
        'address': 'rua caio pereira'
    },
    'squerdinni': {
        'phone': '81993124124',
        'email': 'schettini@gmail.com',
        'address': 'rua clovis bevilaqua',
    }
}


# Mostra os contatos disponíveis na agenda
def showContacts():
    for contact in AGENDA:
        searchContacts(contact)


# Mostra um contato específico
def searchContacts(contact):
    print('Nome: ', contact)
    print('Telefone: ', AGENDA[contact]['phone'])
    print('E-mail: ', AGENDA[contact]['email'])
    print('Endereço: ', AGENDA[contact]['address'])
    print('-----------------------------------------')


# Cria/edita contatos
def createEditContact(contact, phone, email, address):
    AGENDA[contact] = {
        'phone': phone,
        'email': email,
        'address': address
    }


# Deleta um contato
def deleteContact(contact):
    AGENDA.pop(contact)
    print('----------------------------------')
    print('>>>>> Contato "{}" deletado! <<<<<'.format(contact))
    print('----------------------------------')


# Mostra o menu da agenda
def menu():
    print('-----------------------------------------')
    print('Escolha uma opção abaixo:')
    print('1 - Ver contatos')
    print('2 - Buscar contatos')
    print('3 - Criar contato')
    print('4 - Editar contato')
    print('5 - Deletar contato')
    print('0 - Fechar agenda')
    print('-----------------------------------------')

opcao = ''
# Programa em loop
while opcao != 0:
    menu()
    opcao = int(input('Escolha sua opção: '))
    print('-----------------------------------------')

    if opcao == 1:
        print('Agenda:')
        print('-----------------------------------------')
        showContacts()
    elif opcao == 2:
        contact = input('Digite o nome do contato a ser buscado: ')
        searchContacts(contact)
    elif opcao == 3:
        contact = input('Digite o nome do contato: ')
        phone = input('Digite o telefone do contato: ')
        email = input('Digite o e-mail do contato: ')
        address = input('Digite o endereço do contato: ')
        createEditContact(contact,phone, email, address)
        print('-----------------------------------------')
        print('>>>>> Contato "{}" adicionado! <<<<<'.format(contact))
    elif opcao == 4:
        contact = input('Digite o nome do contato: ')
        phone = input('Digite o telefone do contato: ')
        email = input('Digite o e-mail do contato: ')
        address = input('Digite o endereço do contato: ')
        createEditContact(contact, phone, email, address)
        print('-----------------------------------------')
        print('>>>>> Contato "{}" editado! <<<<<'.format(contact))
    elif opcao == 5:
        contact = input('Digite o nome do contato a ser excluído: ')
        deleteContact(contact)
    elif opcao == 0:
        print('Fechando o programa')
        print('-----------------------------------------')
        break
    else:
        print('Opção inválida! Tente novamente.')
