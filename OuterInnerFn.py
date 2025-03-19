def outer(x):
    def inner():
        print(x)
    return inner

fn = outer(10)
fn()


