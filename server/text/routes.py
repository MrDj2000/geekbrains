from .controllers import ( get_upper_text, get_lower_text )

routes = [
    {
        'action': 'uppet_text',
        'contoller': get_upper_text()
    },
    {
        'action': 'lower_text',
        'contoller': get_lower_text()
    },
]
