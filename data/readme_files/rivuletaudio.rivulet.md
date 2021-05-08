# What is rivulet.audio?

rivulet.audio is a new way to acquire and organize music. You create a playlist of songs and it automatically finds "sources" by searching for those songs in torrents. You can share these playlists with anyone and publish them anywhere because the don't contain any copyrighted content or any information about where to get the songs. Once the other user imports your playlist, their client will find torrents to play the songs from.

# Installation

## OS X

### Install

1. Open Terminal.app

2. Install homebrew

  ```
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```

3. Install rivulet from rivuletaudio/tap

  ```
  brew update
  brew install rivuletaudio/tap/rivulet
  ```

4. `rivulet` can be executed from terminal or by running `/Applications/Rivulet.app`

### Upgrade

```
brew update
brew upgrade rivuletaudio/tap/rivulet
```

### Know Issues: 
1. If you see the following error when running the server in terminal:

  ```
  Fatal Python error: PyThreadState_Get: no current thread
  fish: Job 1, 'rivulet' terminated by signal SIGABRT (Abort)
  ```

  Try to re-install boost-python by executing the following commands:

  ```
  brew rm boost-python
  brew install boost-python
  ```

## Debian/Ubuntu/Linux Mint Installation

```
git clone https://github.com/rivuletaudio/rivulet.git
sudo apt-get install -y python-libtorrent python-pip python-lxml flac lame
sudo pip2 install beautifulsoup4 tornado pyyaml
```

## Windows

Use vagrant to set up a virtual machine:

```
vagrant up
```

Then run with:

```
vagrant ssh
python2 /vagrant/server/webserver/webserver.py --host 0.0.0.0
```

## Arch linux installation

```
yaourt rivulet
```

# Running

You can run rivulet.audio on your private server or locally.

```
rivulet
```

or


```
python2 server/webserver/webserver.py
```

then visit `http://localhost:9074` in your browser.

You can change the port and host to bind to with `--port` (or `-p`) and `--host`.

# Config

Copy `server/webserver/config.yaml` to `~/.config/rivulet/config.yaml`. The config file contains documentation about the properties defined in it.
