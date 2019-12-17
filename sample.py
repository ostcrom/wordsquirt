import rumps
import time

rumps.debug_mode(True)  # turn on command line logging information for development - default is off


@rumps.clicked("About")
def about(sender):
    sender.title = 'NOM' if sender.title == 'About' else 'About'  # can adjust titles of menu items dynamically
    rumps.alert("This is a cool app!")


@rumps.clicked("Arbitrary", "Depth", "It's pretty easy")  # very simple to access nested menu items
def does_something(sender):
    my_data = {'poop': 88}
    rumps.notification(title='Hi', subtitle='There.', message='Friend!', sound=does_something.sound, data=my_data)
does_something.sound = True


@rumps.clicked("Preferences")
def not_actually_prefs(sender):
    if not sender.icon:
        sender.icon = 'level_4.png'
    sender.state = not sender.state
    does_something.sound = not does_something.sound


@rumps.timer(4)  # create a new thread that calls the decorated function every 4 seconds
def write_unix_time(sender):
    with app.open('times', 'a') as f:  # this opens files in your app's Application Support folder
        f.write('The unix time now: {}\n'.format(time.time()))


@rumps.clicked("Arbitrary")
def change_statusbar_title(sender):
    app.title = 'Hello World' if app.title != 'Hello World' else 'World, Hello'


@rumps.notifications
def notifications(notification):  # function that reacts to incoming notification dicts
    print(notification)


def onebitcallback(sender):  # functions don't have to be decorated to serve as callbacks for buttons
    print(4848484)           # this function is specified as a callback when creating a MenuItem below

def test_func(sender):
    print(sender)

app = rumps.App("My Toolbar App", title='World, Hello')
menu_list = []

other_list = ['a','b','c']
print(app.menu)
for i in other_list:
    menu_list.append(rumps.MenuItem("One bit", callback=lambda: test_func(i)))

app.menu = [
    rumps.MenuItem('A', callback=test_func, key='F'),
    ('B', ['1', 2, '3', [4, [5, (6, range(7, 14))]]]),
    'C',
    [rumps.MenuItem('D', callback=test_func), (1, 11, 111)],
    rumps.MenuItem('E', callback=test_func, key='e'),
    "a",
    None,
    {
        'x': {'hello', 'hey'},
        'y': ['what is up']
    },
    [1, [2]],
    ('update method', ['walking', 'back', 'to', 'you']),
    'stuff',
    None
]
app.run()
