AGENDA = {
}


# Mostra os contatos disponíveis na agenda
def showContacts():
    if len(AGENDA) > 0:
        for contact in AGENDA:
            searchContacts(contact)
    else:
        print('A agenda está vazia!')

# Mostra um contato específico
def searchContacts(contact):
    try:
        print('Nome: ', contact)
        print('Telefone: ', AGENDA[contact]['phone'])
        print('E-mail: ', AGENDA[contact]['email'])
        print('Endereço: ', AGENDA[contact]['address'])
        print('-----------------------------------------')
    except KeyValue:
        print('Contato inválido')

# Cria/edita contatos
def createEditContact(contact, phone, email, address):
    AGENDA[contact] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save()


# Deleta um contato
def deleteContact(contact):
    try:
        AGENDA.pop(contact)
        save()
        print('----------------------------------')
        print('>>>>> Contato "{}" deletado! <<<<<'.format(contact))
        print('----------------------------------')
    except KeyError:
        print('----------------------------------')
        print('Contato não encontrado!')


# Mostra o menu da agenda
def menu():
    print('-----------------------------------------')
    print('Escolha uma opção abaixo:')
    print('1 - Ver contatos')
    print('2 - Buscar contatos')
    print('3 - Criar contato')
    print('4 - Editar contato')
    print('5 - Deletar contato')
    print('6 - Exportar contatos (CSV)')
    print('7 - Importar contatos (CSV)')
    print('0 - Fechar agenda')
    print('-----------------------------------------')


# Exporta um arquivo CSV com contatos
def exportContacts(fileName):
    try:
        with open(fileName, 'w') as file:
            for contact in AGENDA:
                phone = AGENDA[contact]['phone']
                email = AGENDA[contact]['email']
                address = AGENDA[contact]['address']
                file.write('{},{},{},{}\n'.format(contact, phone, email, address))
    except:
        print('Erro inesperado, tente novamente.')
        print('-----------------------------------------')


def importContacts(fileName):
    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()
            for line in lines:
                details = line.strip().split(',')
                name = details[0]
                phone = details[1]
                email = details[2]
                address = details[3]

                createEditContact(name,phone,email,address)
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except:
        print('Erro inesperado, tente novamente.')
        print('-----------------------------------------')


def readDetails():
    phone = input('Digite o telefone do contato: ')
    email = input('Digite o e-mail do contato: ')
    address = input('Digite o endereço do contato: ')
    return phone, email, address


def save():
    exportContacts('database.csv')


def load():
    importContacts('database.csv')


option = ''
load()
# Programa em loop
while True:
    menu()
    try:
        option = int(input('Escolha sua opção: '))
    except ValueError:
        print('-----------------------------------------')
        print('O número deve ser inteiro!')
    print('-----------------------------------------')

    if option == 1:
        print('Agenda:')
        print('-----------------------------------------')
        showContacts()
    elif option == 2:
        contact = input('Digite o nome do contato a ser buscado: ')
        searchContacts(contact)
    elif option == 3:
        contact = input('Digite o nome do contato: ')
        try:
            AGENDA[contact]
            print('Contato já existente, tente editar!')
        except KeyError:
            phone, email, address = readDetails()
            createEditContact(contact, phone, email, address)
            print('-----------------------------------------')
            print('>>>>> Contato "{}" adicionado! <<<<<'.format(contact))
    elif option == 4:
        contact = input('Digite o nome do contato: ')
        try:
            AGENDA[contact]
            print('Editando o contato {}'.format(contact))
            phone, email, address = readDetails()
            createEditContact(contact, phone, email, address)
            print('-----------------------------------------')
            print('>>>>> Contato "{}" editado! <<<<<'.format(contact))
        except KeyError:
            print('Este contato não existe, tente criar!')
    elif option == 5:
        contact = input('Digite o nome do contato a ser excluído: ')
        deleteContact(contact)
    elif option == 6:
        file = input('Digite o nome do arquivo para exportação: ')
        exportContacts()
        print('A agenda foi exportada!')
        print('-----------------------------------------')
    elif option == 7:
        file = input('Digite o nome do arquivo para importação: ')
        importContacts(file)
        print('A agenda foi importada!')
        print('-----------------------------------------')
    elif option == 0:
        print('Fechando o programa')
        print('-----------------------------------------')
        break
    else:
        print('Opção inválida! Tente novamente.')