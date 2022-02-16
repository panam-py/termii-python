<p align="center">
    <img title="Termii" src="https://termii.com/assets/images/logo.png"/>
</p>


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/panam-py/termii-python/releases/tag/v_0.1.0)

## TERMII-PYTHON

Termii SDK for Python to aid in interfacing with the termii API

## Features

- Switch


Termii’s Switch allows you to send messages to any country in the world across SMS and WhatsApp channel through a REST API. Every request made is identified by a unique ID that help our users track the status of their message either by receiving Delivery Reports (DLRs) over their set webhook endpoints or polling the status of the message using a specific endpoint. The Switch is organised around using HTTP verbs and REST. It accepts and returns JSON formatted payload.

- Token

Token allows businesses generate, send and verify one-time-passwords. Token is organised around using HTTP verbs and REST. It accepts and returns JSON formatted payload.

- Insights

Retrieve real-time delivery report of messages sent to customers as well as the status of their contacts.

## Requirements
Before installing this package, ensure Python v3+ is installed and running on your system

## Installation

Termii-Python requires [Pip](https://pypi.org/) to run.

```sh
pip install termii
```

## Usage

After installing termii-python via Pip, start the package with this command:

```sh
from termii.client import Client
Client = Client(api_key)
```

## Contributors
This SDK was created with ❤ by [Hebron Praise](https://github.com/panam-py) and [Eric Alaribe](https://github.com/smith2eric)

## License

This project is under license from MIT. For more details, see the [LICENSE](https://github.com/panam-py/termii-python/blob/main/LICENSE) file.

## **Free Software, Hell Yeah!**

