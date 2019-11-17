from blup.user import user

@user.route("/")
def index():
    return "user 'index hello word'"