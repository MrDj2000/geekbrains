import json
import socket
import .text import routes

sock = socket.socket()
sock.bind(('', 8000))
sock.listen(5)

while True:
    client, address = sock.accept()
    print(f'Client detected {address}')
    data = client.recv(1024)
    request = json.loads(
        data.decode('utf-8')
    )

    client_action = request.get('action')

    resolved_routes = list(
        filter(
            lambda itm: itm.get('action') == client_action,
            get_server_routes()
        )
    )

    resolved_routes[0] if resolved_routes else None

    if routes:
        controller = routes.get('controller')
        controller = controller(request.get('data'))
    else
        response_string = 'Action not supported'

    print(response_string)
    client.send(response_string.encode('utf-8'))
    client.close()
