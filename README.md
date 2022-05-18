# thedwz sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Sandoval97/thedwz.git
$ cd thedwz
```

Run the follow command of docker compose to create APIs container:

```sh
$ docker-compose up --build
```

Once `build` has finished and downloading the dependencies the dev server will be started the command used is:
```sh
$ python manage.py runserver 0.0.0.0:8000
```
So navigate to `http://127.0.0.1:8000/api/v1/`. To see available endpoints

## Joke Endpoint

Returns the list of 15 jokes from chucknorris API: 

```sh
    /api/v1/random-jokes/

    * output
    json
        {
            "length": 0,
            "jokes": []
        }
```

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ ./manage.py test