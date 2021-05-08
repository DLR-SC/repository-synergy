# Generate config file for [SpechtLite](https://github.com/zhuhaow/SpechtLite)

## List Explaination

- **gfwlist**: proxy list gnerate from [gfwlist](https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt)

- **whitelist**: white list generate from [dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)

- **rejectlist**: reject list from [BurpSuite](https://raw.githubusercontent.com/BurpSuite/CloudGate-RuleList/master/Rule/REJECT)

- **proxyiprange**: Add telegram and Amazon EC2 IPs

##How to use
> 1. Go to `conf` and configure your own adapter in `gfwlist.yaml` or `whitelist.yaml`. If you don't need to generate new config file, just jump to step 4
> 2. `pip3 install -r requirement.txt`
> 3. `python3 spechtlite_conf.py`
> 4. copy or link files which in `conf` to `~/SpechtLiteConf`

##MIT License (MIT)

The MIT License (MIT)

Copyright (c) 2016-2018 geekpi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

