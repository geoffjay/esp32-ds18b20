import ds18x20
import onewire
import time
import tinyweb

from machine import I2C, Pin

import chirp


# Create web server application
app = tinyweb.webserver()


# Index page
@app.route("/")
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send("<html><body><h1>Hello, world! (<a href='/table'>table</a>)</h1></body></html>\n")


# Another one, more complicated page
@app.route("/table")
async def table(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    await response.send("<html><body><h1>Simple table</h1>"
                        "<table border=1 width=400>"
                        "<tr><td>Name</td><td>Some Value</td></tr>")
    for i in range(10):
        await response.send("<tr><td>Name{}</td><td>Value{}</td></tr>".format(i, i))
    await response.send("</table>"
                        "</html>")


@app.route("/temperature")
async def temperature(request, response):
    ow = onewire.OneWire(Pin(12))
    ds = ds18x20.DS18X20(ow)
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)

    reading = 0
    for rom in roms:
        reading = ds.read_temp(rom)

    await response.start_html()
    await response.send("<html><body><p>Temperature: {}</p></body></html>\n".format(reading))


@app.route("/moisture")
async def moisture(request, response):
    i2c = I2C(scl=Pin(22), sda=Pin(21), freq=300000)
    sensor = chirp.Chirp(bus=i2c, address=0x20)

    await response.start_html()
    await response.send("""
        <html>
            <body>
                <p>Moisture: {}</p>
                <p>Temperature: {}</p>
            </body>
        </html>
    """.format(sensor.moisture, sensor.temperature))


def run():
    app.run(host="0.0.0.0", port=8081)
