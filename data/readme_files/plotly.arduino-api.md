## Real-time Graphing and Data Logging

#### The easiest and fastest way to plot and share data on the Arduino.
[![Real-time Plotting with Arduino and Plotly](http://new.tinygrab.com/c751bc2ee22cd3db5a6d3fccb22458d570efc9ac84.png)](http://vimeo.com/89003132)

Plotly's Arduino libraries connects Arduinos to plotly's beautiful online graphing tool for real-time, interactive data logging and graphing. It's free, open source, and your graphs and data are entirely online.

Here is an example of a real-time graph: [http://plot.ly/~streaming-demos/6/](http://plot.ly/~streaming-demos/6/)

## Super easy

```C
#include <WiFi.h>
#include "plotly_streaming_wifi.h"

#define num_traces 2
// Sign up to plotly here: https://plot.ly
// View your API key and stream tokens in your settings: https://plot.ly/settings
char *tokens[num_traces] = {"your_plotly_stream_token", "another_plotly_stream_token"};
plotly graph = plotly("your_plotly_username", "your_plotly_api_key", tokens, "your_filename", num_traces);

int status = WL_IDLE_STATUS;     // the Wifi radio's status
char ssid[] = "wifi_network_name"; //  your network SSID (name)
char pass[] = "wifi_network_password"; // // your network password

void wifi_connect(){
    // attempt to connect using WPA2 encryption:
    Serial.println("... Attempting to connect to WPA network...");
    status = WiFi.begin(ssid, pass);
    // if you're not connected, stop here:
    if ( status != WL_CONNECTED) {
      Serial.println("... Couldn't get a WiFi connection, trying again");
      wifi_connect();
    }
    // if you are connected, print out info about the connection:
    else {
      Serial.println("... Connected to network");
    }
}

void setup() {

  Serial.begin(9600);

  wifi_connect();

  // Initialize a streaming graph in your plotly account
  graph.init();
  // Initialize plotly's streaming service
  graph.openStream();
}

void loop() {
  // now let's stream data to plotly, giddyup!
  graph.plot(millis(), analogRead(A0), tokens[0]);
  graph.plot(millis(), analogRead(A1), tokens[1]);
}
```

## 5 Minute Quickstart

**Note: this library doesn't work with the latest Arduino IDE. Use 1.0.3 (for WiFi) or 1.0.5 for other shields. See https://github.com/plotly/arduino-api/issues/38 for more details**

If you're working on the Yún, click on the [`plotly_yun`](/plotly_yun) folder for separate instructions.

If you're device isn't internet connected, you can still connect to plotly over serial. Click on the [`plotly_streaming_serial`](/plotly_streaming_serial) folder for separate instructions.

1. Sign up to plotly: [https://plot.ly](https://plot.ly).
2. Download and uncompress the latest plotly release: [https://github.com/plotly/arduino-api/releases](https://github.com/plotly/arduino-api/releases).
3. Place the appropriate library your Arduino libraries folder. On a Mac, this is in `~/Documents/Arduino/libraries/`:
    ![](http://new.tinygrab.com/c751bc2ee29f2d309e4fd8985685df0a1d83cf115a.png)
4. Open up the Arduino IDE. If your using WiFi and haven't upgraded your firmware, use the [IDE version 1.0.3](http://arduino.cc/en/Main/OldSoftwareReleases).
5. Load up one of the [examples](/examples) from this repository. Fill in your plotly username, API key, stream tokens, and filename. You can find your API key and stream tokens here: [https://plot.ly/settings](https://plot.ly/settings). It'll look something like:

    ```cpp
    char *tokens[] = {"ab4kf5nfdn","kdf5bn4dbn"};
    plotly graph("anna.lyst","ab4kftunvd", tokens, "arduino graph");
    ```
    (those are fake keys and tokens)

6. Upload the program.
7. Open up your Serial Monitor. You'll see an output like:

    ```
    ... Attempting to connect to WPA network...
    ... Connected to network
    ... Attempting to connect to plotly's REST servers
    ... Connected to plotly's REST servers
    ... Sending HTTP Post to plotly
    ... Sent message, plotly's response:
    ... A-ok from plotly, All Streams Go!
    ... View your streaming plot here: https://plot.ly/~streaming-demos/6
    ... Connecting to plotly's streaming servers...
    ... Connected to plotly's streaming servers
    ... Initializing stream
    ... Done initializing, ready to stream!
    ```
8. Grab the URL that was printed out, view your graph in your browser, and celebrate! The graph and data is saved in your plotly account, so you can view it in your plotly file list here: [https://plot.ly/plot](https://plot.ly/plot). You can view, edit, and share your graphs while data is streaming to them in real-time. Everybody that views the graph will see the exact same data at the same time (try it out yourself: open your graph in two different browser windows).

## Usage and Docs

### Usage, Your Data Rights, and Private Graphs
When you make a graph on plotly, you retain the rights to your content (see our terms [here](https://plot.ly/tou)). You also control whether your graphs are public or private. Public plotting is free; for a lot of private use, you can get a Premium or Organizational plan (see http://plot.ly/plans). It's just like GitHub.

By default, anyone can view the graphs at the unique URL. To make the graphs private, so that only you can see them when your logged in, set `world_readable` to `false`:

```Cpp
  plotly graph = plotly("your_plotly_username", "your_plotly_api_key", streaming_tokens, "your_plotly_filename", num_traces);
  graph.world_readable = false;
```

### Time stamping
By default, plotly assumes that `x` is `millis()` and automatically converts the `x` to a real-time timestamp with the timezone `"America/Montreal"` on the server. To disable this, set `convertTimestamp` to `false`, e.g.

```Cpp
  plotly graph = plotly("your_plotly_username", "your_plotly_api_key", streaming_tokens, "your_plotly_filename", num_traces);
  void setup(){
    graph.convertTimestamp = false;
  }
```

To change the timezone, set `timezone` to one of the strings in here: [Accepted Timezone Strings.txt](https://github.com/plotly/arduino-api/blob/master/Accepted%20Timezone%20Strings.txt), e.g.

```Cpp
  plotly graph = plotly("your_plotly_username", "your_plotly_api_key", streaming_tokens, "your_plotly_filename", num_traces);
  void setup(){
    graph.timezone = "Africa/Abidjan";
  }
```

### Adjusting the number of points plotted at a time
By default, your real-time graph will graph the `30` most recent points at a time. To adjust this, set the member variable `maxpoints` to something else, e.g.

```Cpp
  plotly graph = plotly("your_plotly_username", "your_plotly_api_key", streaming_tokens, "your_plotly_filename", num_traces);
  void setup(){
    graph.maxpoints = 200;
  }
```

### Editing the live  graph
Plotly graphs can be edited while data is streaming to them. Every aspect of the graph is configurable: you can add a second y-axis, turn the graphs into subplots, change the colors, update the title, change the chart type, etc. To get started, just open up the graph in your list of files here: [https://plot.ly/plot](https://plot.ly/plot) or click `Save and Edit` on the public view of your graph that the serial monitor printed out (e.g. [http://plot.ly/~streaming-demos/6/](http://plot.ly/~streaming-demos/6/)).

### Multiple Viewers
Everybody who looks at your streaming graph sees the exact same data, at the exact same time. Give it a try yourself: open up a graph in two different browser windows.

### Overwriting or Appending Data
By default, the initialization of your graph (`graph.init();`) overwrites the existing graph with your new data. This is the perfect option for development: when you re-run your script, a fresh new graph is created. However, when you run your Arduino for an extended period of time, the Arduino may reset itself, which would in turn reset the graph and remove the existing data. To prevent this from happening, you can use the `fileopt` `"extend"`, which will append your new data to the existing data in the graph.


So, for running your Arduino for a very long time, you should add
```Cpp
graph.fileopt = "extend"; // Remove this if you want the graph to be overwritten on initialization
```
to your `setup()` loop, i.e.

```Cpp
void setup() {
  Serial.begin(9600);

  startEthernet();

  bool success;
  graph.maxpoints = 500;
  graph.fileopt = "extend"; // Remove this if you want the graph to be overwritten
  success = graph.init();
  while(!success){
    Serial.println(F("Error initializing graph, trying again."));
    delay(5000);
    success = graph.init();
  }
  graph.openStream();
}
```

### Streaming Multiple Traces to Multiple Plots
Example code is here: [Streaming Multiple Traces to Multiple Plots](https://gist.github.com/chriddyp/11222798). View the comment at the bottom of the example for an explanation of the code.

### Logging and Debugging
The parameter `log_level` sets how debugging information is printed out over serial. For troubleshooting, set `log_level` to `0`, i.e.

```Cpp
void setup(){
  Serial.begin(9600);
  startEthernet();

  graph.log_level = 0;

  success = graph.init();
  if(!success){while(true){}}
  graph.openStream();
}

```
Set `log_level` to `4` if you want nothing to be printed out on serial.

### Docs

```Cpp
class plotly(char *username, char *api_key, char* stream_tokens[], char *filename, int nTraces);
```

**Public Member Functions**

- `bool plotly.init()`

  Creates an empty graph in your plotly account that will get streamed to. This is done by making an API call to plotly's REST service. Returns `true` if initialization was successful, `false` otherwise.
- `void plotly.openStream()`

  Opens a TCP connection to plotly's streaming service. The stream is uniquely identified by the `stream_tokens`.
- `void plotly.closeStream()`

  Closes the TCP connection to plotly's streaming service.
- `void plotly.reconnectStream()`

  Reopens the connection to plotly's streaming service if not connected.
- `void plot(unsigned long x, int y, char *token)`

  Plots `(x, y)` to the streaming graph.
- `void plot(unsigned long x, float y, char *token)`

  Plots `(x, y)` to the streaming graph.

**Public Member Parameters**
- `int plotly.log_level` (Default `2`)

  Determines which messages are printed over serial. Levels are:
  - `0`: Debugging
  - `1`: Informational
  - `2`: Status
  - `3`: Errors
  - `4`: Quiet
- `bool plotly.dry_run`

  If `True`, then no calls are made to Plotly's servers.
- `int plotly.maxpoints` (Default `30`)

  Determines the number of points to plot at a time. Valid from `1` to `200000`.
- `bool plotly.convertTimestamp` (Default `true`)

  If `true`, the Plotly assumes that `x` is milliseconds since program start (`millis()`) and automatically converts these values into a timestamp.
- `char *plotly.timeZone` (Default: `"America/Montreal"`)

  The timezone to convert the timestamps if `plotly.convertTimestamp=true`. A list of the accepted timezones are in this repo: [Accepted Timezone Strings.txt](https://github.com/plotly/arduino-api/blob/master/Accepted%20Timezone%20Strings.txt)

- `bool plotly.world_readable` (Default: true)

  If `true`, then your graph is publicly viewable and discoverable by unique url. If `false`, then only you can view the graph.

- `char *plotly.fileopt` (Default `"overwrite"`)

  Either `"extend"` or `"overwrite"`.

  If `"overwrite"`, then when the graph is initialized (during `plotly.init()`), the existing graph is overwritten with a new one. This means that the existing data in the graph will be removed. This option is good for development, when you want a fresh graph to appear everytime you run your script.

  If `"extend"`, then the existing data is kept when the graph is initialized (during `plotly.init()`), and the new data is appended onto the existing data. This option is good for when you are running your device for an extended period of time, for if the Arduino resets (which may happen every few hours) then the existing data in the graph is not removed.

## Projects

- A video of our real-time heart rate monitor (click to view):
[![Real-time Heart Rate Monitor with Plotly and an Arduino Yun](http://new.tinygrab.com/c751bc2ee2533bf46bba1b0b65720764edcfb06c6b.png)](https://vine.co/v/Mq2LQexrbl7)

- A video of an Arduino streaming-data from a mountain edge, in Peachland, BC
[![Arduino streaming-data data to plotly from a mountain edge, in Peachland, BC](http://new.tinygrab.com/c751bc2ee28fbde72ce2f6b8904f1efd034210827d.png)](http://vimeo.com/87362390)

- DHT22 Temperature and Humidity sensor: [http://plot.ly/workshop/arduino-dht22/](http://plot.ly/workshop/arduino-dht22/)

- Analog Light Sensor: [http://plot.ly/workshop/arduino-analoglight/](http://plot.ly/workshop/arduino-analoglight/)

- ML8511 UV Sensor: [http://plot.ly/workshop/arduino-uvsensor/](http://plot.ly/workshop/arduino-uvsensor/)

- Air Quality Sensor: [http://plot.ly/workshop/arduino-airquality/](http://plot.ly/workshop/arduino-airquality/)

- Water Flow Sensor: [http://plot.ly/workshop/arduino-waterflow/](http://plot.ly/workshop/arduino-waterflow/)

- TMP36 Temperature Sensor: [http://plot.ly/workshop/arduino-tmp36/](http://plot.ly/workshop/arduino-tmp36/)


## Contributing Notes
The `wifi`, `ethernet`, `gsm`, and `cc3000` libraries and examples are 95% identical and so are automatically generated from template files in the `plotly_dev` folder. We use Mako, one of Python's templating libraries to generate these files. To run, do:

```bash
$ python render.py
```

## Get in touch
- [@plotlygraphs](https://twitter.com/plotlygraphs)
- <chris@plot.ly>
