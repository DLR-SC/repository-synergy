#  Espcap

__Espcap__ is a program that uses __tshark__ to capture packets live from a network interface or from PCAP files and index them in Elasticsearch.  __Espcap__ runs only on Python 3.x.  For those of you who used **Espcap** previously, note  I deleted that repo and replaced it with this one when I decided to move away from Pyshark for packet capture. This version of __Espcap__ is lighter weight since it has far fewer module dependencies. 

## Requirements

**Espcap** relies on the Elasticsearch Python Client module to index packets in Elasticsearch. The version of the client module must match the version of Elasticsearch you want to use.  The two most recent **major** versions of Elasticsearch are 6.x and 7.x, so **Espcap** has two different sets of requirements for each version.

Although not required, you can run **Espcap** in a virtual environment if you want to keep its dependencies local instead of global.  If you decide that's how you want to go, I recommend using **pipenv**, which makes virtual environment easy to manage.  To get **pipenv**, just run `pip install pipenv`.

### Support for *Elasticsearch 7.x* requires:

1. Python 3.7 (Python 2.7.x not supported)
2. TShark 3.0.1 (included in Wireshark)
3. *Click* module for Python
4. Elasticsearch Python Client module 7.x
5. Elasticsearch 7.x

### Support for  *Elasticsearch 6.x* requires:

1. Requirements 1 - 3 listed above
2. Elasticsearch Python Client module 6.x
3. Elasticsearch 6.x

## Installation

1. Install Wireshark for your OS.

2. Clone the __Espcap__ repo then cd into the *espcap* directory.

3. Optionally, activate your *pipenv* virtual environment:
   ```
   pipenv shell
   ```

4. Install the required Python modules for Elasticsearch 7.x:
   ```
   pip install -r requirements-7.x.txt
   ```
   If you have Elasticsearch 6.x, use the *requirements-6.x.txt* file instead. 
   
5. Create the packet index template by running *scripts/templates.sh* as follows specifying the node IP address and TCP port of your Elasticsearch instance (localhost:9200 in this example):
   ```
   scripts/packet_template-7.x.sh localhost:9200
   ```
   If you are using Elasticsearch 6.x, run *packet_template-6.x.sh* instead.

6. Set the `tshark_path` variable in the *config/espcap.yml* file.  You can locate *espcap.yml* in one of 3 places:
   - Use the file directly from the *config* directory.
   - Copy it to the same directory where *espcap.py* and its related Python files reside.
   - Create the */etc/espcap* directory and copy it there.
   - Any other directory you want.  However, if you don't use one of the previous options, you'll need to add the directory path to the list of config directories contained in the *tshark.py* file.

7. cd into the *src* directory.

8. Run *espcap.py* to index some packet data in Elasticsearch:
    ```
    espcap.py --file=test_pcaps/test_http.pcap --node=localhost:9200
    ```

9. Run *packet_query.sh* as follows to check that the packet data resides in your Elasticsearch instance:
    ```
    scripts/packet_query.sh localhost:9200
    ```

## Running Examples

+ Display the following help message:
  ```
  espcap.py --help
  Usage: espcap.py [OPTIONS]

  Options:
    --node  TEXT     Elasticsearch IP and port (default=None, dump packets to
                     stdout)
    --nic   TEXT     Network interface for live capture (default=None, if file
                     or dir specified)
    --file  TEXT     PCAP file for file capture (default=None, if nic specified)
    --dir   TEXT     PCAP directory for multiple file capture (default=None, if
                     nic specified)
    --bpf   TEXT     Packet filter for live capture (default=all packets)
    --chunk INTEGER  Number of packets to bulk index (default=1000)
    --count INTEGER  Number of packets to capture during live capture
                     (default=0, capture indefinitely)
    --list           List the network interfaces
    --help           Show this message and exit.
  ```

+ Load the test packet capture files and index the packets in the Elasticsearch cluster running at 10.0.0.1:9200, assuming your present working directory is *espcap/src*:
  ```
  espcap.py --dir=../test_pcaps --node=10.0.0.1:9200
  ```

+ Same as the previous except load the *test_pcaps/test_http.pcap* file:
  ```
  espcap.py --file=../test_pcaps/test_http.pcap --node=10.0.0.1:9200
  ```

+ Do a live capture from the network interface `eth0`, get all packets and index them in the Elasticsearch cluster running at 10.0.0.1:9200:
  ```
  espcap.py --nic=eth0 --node=10.0.0.1:9200
  ```

+ Same as the previous except dump the packets to `stdout`:
  ```
  espcap.py --nic=eth0
  ```

+ Do a live capture of TCP packets with source port or destination port == 80 and index in Elasticsearch running at 10.0.0.1:9200:
  ```
  espcap.py --nic=eth0 --bpf="tcp port 443" --node=10.0.0.1:9200
  ```

+ List the network interfaces
  ```
  espcap.py --list
  ```

## Packet Indexing

### Time Series Indexing

When indexing packets in Elasticsearch, a new index is created for each day. The index naming format is _packets-yyyy-mm-dd_. The index type is `_doc` for both live and file capture. Index `_id` is automatically assigned by Elasticsearch.

### Packet Index Structure

Packets from *tshark* are indexed just as they are received.  Packet payloads are contained in `layers` objects with each protocol, `frame`, `eth`, `ip`, `tcp`, etc., contained in a sub-object with the corresponding protocol fields.   Here is an example of a DNS packet:


```
      {
        "_index" : "packets-2015-08-14",
        "_type" : "_doc",
        "_id" : "yjgVamoBqD8GDhvGePoE",
        "_score" : 0.004597709,
        "_source" : {
          "timestamp" : "1439587239879",
          "layers" : {
            "frame" : {
              "frame_frame_interface_id" : "0",
              "frame_interface_id_frame_interface_name" : "en0",
              "frame_frame_encap_type" : "1",
              "frame_frame_time" : "Aug 14, 2015 14:20:39.879373000 PDT",
              "frame_frame_offset_shift" : "0.000000000",
              "frame_frame_time_epoch" : "1439587239.879373000",
              "frame_frame_time_delta" : "0.000217000",
              "frame_frame_time_delta_displayed" : "0.000217000",
              "frame_frame_time_relative" : "0.963427000",
              "frame_frame_number" : "9",
              "frame_frame_len" : "71",
              "frame_frame_cap_len" : "71",
              "frame_frame_marked" : "0",
              "frame_frame_ignored" : "0",
              "frame_frame_protocols" : "eth:ethertype:ip:udp:dns"
            },
            "eth" : {
              "eth_eth_dst" : "58:23:8c:b4:42:56",
              "eth_dst_eth_dst_resolved" : "Technico_b4:42:56",
              "eth_dst_eth_addr" : "58:23:8c:b4:42:56",
              "eth_dst_eth_addr_resolved" : "Technico_b4:42:56",
              "eth_dst_eth_lg" : "0",
              "eth_dst_eth_ig" : "0",
              "eth_eth_src" : "60:f8:1d:cb:43:84",
              "eth_src_eth_src_resolved" : "Apple_cb:43:84",
              "eth_src_eth_addr" : "60:f8:1d:cb:43:84",
              "eth_src_eth_addr_resolved" : "Apple_cb:43:84",
              "eth_src_eth_lg" : "0",
              "eth_src_eth_ig" : "0",
              "eth_eth_type" : "0x00000800"
            },
            "ip" : {
              "ip_ip_version" : "4",
              "ip_ip_hdr_len" : "20",
              "ip_ip_dsfield" : "0x00000000",
              "ip_dsfield_ip_dsfield_dscp" : "0",
              "ip_dsfield_ip_dsfield_ecn" : "0",
              "ip_ip_len" : "57",
              "ip_ip_id" : "0x0000a7f9",
              "ip_ip_flags" : "0x00000000",
              "ip_flags_ip_flags_rb" : "0",
              "ip_flags_ip_flags_df" : "0",
              "ip_flags_ip_flags_mf" : "0",
              "ip_flags_ip_frag_offset" : "0",
              "ip_ip_ttl" : "64",
              "ip_ip_proto" : "17",
              "ip_ip_checksum" : "0x00003122",
              "ip_ip_checksum_status" : "2",
              "ip_ip_src" : "10.0.0.2",
              "ip_ip_addr" : [
                "10.0.0.2",
                "75.75.76.76"
              ],
              "ip_ip_src_host" : "10.0.0.2",
              "ip_ip_host" : [
                "10.0.0.2",
                "75.75.76.76"
              ],
              "ip_ip_dst" : "75.75.76.76",
              "ip_ip_dst_host" : "75.75.76.76"
            },
            "udp" : {
              "udp_udp_srcport" : "33967",
              "udp_udp_dstport" : "53",
              "udp_udp_port" : [
                "33967",
                "53"
              ],
              "udp_udp_length" : "37",
              "udp_udp_checksum" : "0x0000aab3",
              "udp_udp_checksum_status" : "2",
              "udp_udp_stream" : "6",
              "udp_text" : "Timestamps",
              "text_udp_time_relative" : "0.000000000",
              "text_udp_time_delta" : "0.000000000"
            },
            "dns" : {
              "dns_dns_id" : "0x0000cfe4",
              "dns_dns_flags" : "0x00000100",
              "dns_flags_dns_flags_response" : "0",
              "dns_flags_dns_flags_opcode" : "0",
              "dns_flags_dns_flags_truncated" : "0",
              "dns_flags_dns_flags_recdesired" : "1",
              "dns_flags_dns_flags_z" : "0",
              "dns_flags_dns_flags_checkdisable" : "0",
              "dns_dns_count_queries" : "1",
              "dns_dns_count_answers" : "0",
              "dns_dns_count_auth_rr" : "0",
              "dns_dns_count_add_rr" : "0",
              "dns_text" : "Queries",
              "text_text" : "s.ytimg.com: type A, class IN",
              "text_dns_qry_name" : "s.ytimg.com",
              "text_dns_qry_name_len" : "11",
              "text_dns_count_labels" : "3",
              "text_dns_qry_type" : "1",
              "text_dns_qry_class" : "0x00000001"
            }
          }
        }
      }
```

As you can see, there are a considerable number of fields in each packet, not all of should be indexed in Elasticsearch.  Large number of indexed fields can slow down ingestions.  You should index only the fields you plan to use for searching.  

The default fields that are indexed are included in template creation commands in the *packet_template.sh* and *packet_template-6.x.sh* scripts.  To search for UDP packets in the `packets-2019-04-01` index from the most recent to least recently captured, you could use a query like this:

```
GET packets-2019-04-01/_search
{
    "query": {
        "match": {
            "layers.udp.udp_udp_dstport": 53
        }
    },
    "sort": [
      {
          "timestamp": {
              "order": "desc"
          }
      }
    ]
}
```

### Packet Index Mapping

Trying to index all the possible packet fields can slow Elasticsearch down, so a limited number of core fields are mapped. Index mapping is set by two scripts, *packet_template-7.x.sh* and *packet_template-6.x.xh*. These scripts set the mappings for the fields shown in the table below. Dynamic mapping is disabled so only these fields will be mapped.

| Protocol | Field                                   | Mapping                
|----------|-----------------------------------------|------------------------
| frame    | frame_interface_id_frame_interface_name | keyword
| frame    | frame_frame_protocols                   | simple
| ip       | ip_ip_src                               | ip
| ip       | ip_ip_dst                               | ip
| ip       | ip_ip_version                           | integer
| udp      | udp_udp_srcport                         | integer
| udp      | udp_udp_dstport                         | integer
| tcp      | tcp_tcp_srcport                         | integer
| tcp      | tcp_tcp_dstport                         | integer
| tcp      | tcp_flags_tcp_flags_str                 | keyword
| tcp      | tcp_flags_tcp_flags_urg                 | integer
| tcp      | tcp_flags_tcp_flags_ack                 | integer
| tcp      | tcp_flags_tcp_flags_push                | integer
| tcp      | tcp_flags_tcp_flags_syn                 | integer
| tcp      | tcp_flags_tcp_flags_fin                 | integer
| tcp      | tcp_tcp_seq                             | integer
| tcp      | tcp_tcp_ack                             | integer
| tcp      | tcp_tcp_window_size                     | integer

The mapping for `frame_frame_protocols` enables you to search for any protocol within a given packet . For example, if you want to revise the query used before to find DNS, instead of using ports, you could query with the `dns` in the `frame_frame_protocols` field:

```
GET packets-2019-04-01/_search
{
    "query": {
        "match": {
            "layers.frame.frame_frame_protocols": "dns"
        }
    },
    "sort": [
      {
          "timestamp": {
              "order": "desc"
          }
      }
    ]
}
```

Another example is searching for all the TCP packets.  To do that, simply the previous query and substitute `tcp` for `dns`:

```
GET packets-2019-04-01/_search
{
    "query": {
        "match": {
            "layers.frame.frame_frame_protocols": "tcp"
        }
    },
    "sort": [
      {
          "timestamp": {
              "order": "desc"
          }
      }
    ]
}
```

If you want to change the mappings for your packets, just revise the packet template scripts to your liking. Specific application level protocols or additional fields in the other lower level protocols that you want to use for searching are good candidates to add to the mapping template scripts.  You will have to delete your existing packet indexing template, if any, before creating a new one. You should keep dynamic indexing turned off so Elasticsearch does not create new mappings as new packet protocols and fields are encountered.
