Excellent choice. Keeping your 
# Python Multi-threaded Ping Sweeper 🚀

A lightweight and high-speed network discovery tool built with Python. This script scans a local area network (LAN) to identify active hosts by sending ICMP Echo Request packets (pings) concurrently using multi-threading.

## 🌟 Features
- **Concurrent Scanning**: Utilizes `ThreadPoolExecutor` to scan multiple IP addresses simultaneously, significantly reducing total scan time.
- **Cross-Platform**: Automatically detects the operating system (Windows/Linux/macOS) and adjusts ping parameters accordingly.
- **Colorized Output**: Provides clear, color-coded terminal feedback using `colorama` for better readability.
- **Smart IP Handling**: Uses the `ipaddress` library to safely parse and iterate through network subnets.

## 🛠️ Prerequisites
Before running the script, ensure you have:
- **Python 3.x** installed.
- **colorama** library installed.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/batoolhamdan378-bot/Python-Ping-Sweeper.git](https://github.com/batoolhamdan378-bot/Python-Ping-Sweeper.git)

```

2. **Navigate to the project directory:**
```bash
cd ping_sweeper_project

```


3. **Install dependencies:**
```bash
pip install colorama

```



## 💻 Usage

1. Open `main.py` and modify the `network_input` variable to match your local subnet (e.g., `"10.2.0.0/24"`).
2. Run the script:
```bash
python main.py

```



## ⚙️ How It Works

The script splits the network scanning task into 50 concurrent "threads." Each thread picks an IP address from the generated list, executes a system-level ping command, and reports back whether the device is reachable. By running these checks in parallel rather than one-by-one, a scan that would normally take minutes is completed in seconds.

## 📝 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```

---

### **Quick Tips for your GitHub:**
1.  **Replace `YOUR_USERNAME`**: In the "Installation" section of the README, make sure to put your actual GitHub username.
2.  **Add a License**: On GitHub, it's a good habit to add a license file (like MIT). It tells others they are free to use your code.
3.  **The `network_input`**: Since your current IP is `10.2.0.2`, remember to change the line in your `main.py` to `network_input="10.2.0.0/24"` before you do the final push.

**Once you apply the code updates and this README, your project will be a great addition to your GitHub portfolio! Ready to push the final version?**

```