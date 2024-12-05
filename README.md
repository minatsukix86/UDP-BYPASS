# UDP Flood Bypass Script
![Img](https://media.discordapp.net/attachments/1299118707305484389/1314345055150149762/d0979b26cec609049b3d1a3dee5b89b3.gif?ex=67536eb8&is=67521d38&hm=3b8ea2e95bb84368d2500ba0e854cc776d2d8f701acf8fd161e27d4695478a88&=)

A high-performance UDP flood script for testing and research purposes. This Python-based tool is designed with flexibility and efficiency in mind, featuring customizable options for payloads, target configurations, and attack parameters.

---

## Features

- **Random Payload Generation**: Supports dynamically generated payloads for increased testing variability.
- **IP Randomization**: Generates random IP addresses within a given subnet to simulate distributed sources.
- **Multi-Target Support**: Simultaneously attack multiple targets using threading.
- **TCP Handshake Simulation**: Includes optional TCP handshake simulation for broader testing.
- **Customizable Parameters**: Configure payload size, repeat counts, delays, and more via command-line arguments.

---

## Requirements

- Python 3.6 or higher
- Modules: `socket`, `random`, `struct`, `time`, `threading`, `argparse`

---

## Installation

1. Clone the repository or download the script:

   ```bash
   git clone https://github.com/yourusername/udp-flood-bypass.git
   cd udp-flood-bypass
   ```

2. Ensure Python is installed on your system:

   ```bash
   python3 --version
   ```

3. Install any missing dependencies (if necessary).

---

## Usage

The script is designed to be run from the command line with flexible arguments:

```bash
python3 udp_b.py --targets <TARGETS> --dest_port <PORT> [OPTIONS]
```

### Example:

```bash
python3 udp_b.py --targets 192.168.1.10:80 192.168.1.20:443 --dest_port 80 --payload_size 1024 --random_payload --repeat 20 --csleep 50 --netmask 24
```

### Arguments:

- **`--targets`**: List of target IPs and ports in the format `IP:PORT` (required).
- **`--source_port`**: Source port for sending packets (optional, random by default).
- **`--dest_port`**: Destination port for targets (required).
- **`--payload_size`**: Size of the payload in bytes (default: 512).
- **`--random_payload`**: Enables random payload generation.
- **`--repeat`**: Number of packets to send per target (default: 10).
- **`--csleep`**: Delay in milliseconds between packets (default: 100ms).
- **`--netmask`**: Subnet mask for random IP generation (default: 24).

---

## Notes

- This script is for educational and testing purposes only. Unauthorized usage against systems is strictly prohibited.
- Ensure you have appropriate permissions to test on the specified targets.

---


## Disclaimer

This tool is designed for educational and security research purposes. Misuse of this tool can lead to severe legal consequences. The author is not responsible for any misuse or damage caused by this software.

---

