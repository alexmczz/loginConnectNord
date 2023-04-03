# NordVPN CLI Client

This is a command-line interface (CLI) client for the NordVPN service. The client is written in Python and uses the `nordvpn` command-line tool to log in to NordVPN and connect to VPN servers.

## Getting Started

To use the NordVPN CLI client, you'll need to have the `nordvpn` command-line tool installed on your system. You can download the tool from the [official NordVPN website](https://nordvpn.com/download/).

Once you have the tool installed, clone the repository and navigate to the project directory:


## Usage

To use the NordVPN CLI client, run the `connect_nord.py` script with Python:


The script will prompt you to log in to your NordVPN account:


Enter your NordVPN username and password to log in. The script will open the NordVPN login page in your default web browser to complete the authentication process.

Once you're logged in, the script will prompt you to connect to a NordVPN server:


Press Enter to connect to a NordVPN server. The script will execute the `nordvpn connect` command to connect to a server.

If you want to exit the script, type "Quit" and press Enter. The script will print a quitting message and exit after a 5-second delay.

## Contributing

Contributions to the NordVPN CLI client are welcome! If you find a bug or have a feature request, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and submit a pull request.

## License

The NordVPN CLI client is released under the MIT license. See the [LICENSE](LICENSE) file for more details.
