https://github.com/Chocapikk/wpprobe

## 🕵️ Usage

[](https://github.com/Chocapikk/wpprobe#️-usage)

### **🔄 Update WPProbe**

[](https://github.com/Chocapikk/wpprobe#-update-wpprobe)

Update WPProbe to the latest version:

```shell
wpprobe update
```

### **Update the Wordfence database**

[](https://github.com/Chocapikk/wpprobe#update-the-wordfence-database)

Update the local Wordfence vulnerability database:

```shell
wpprobe update-db
```

### **Basic scan for a single website (Stealthy mode - default)**

[](https://github.com/Chocapikk/wpprobe#basic-scan-for-a-single-website-stealthy-mode---default)

Scan a single WordPress site using the default stealthy mode:

```shell
wpprobe scan -u https://example.com
```

### **Use brute-force mode for comprehensive scanning**

[](https://github.com/Chocapikk/wpprobe#use-brute-force-mode-for-comprehensive-scanning)

Scan a WordPress site using brute-force detection:

```shell
wpprobe scan -u https://example.com --mode bruteforce
```

### **Use hybrid mode for optimal balance of stealth and thoroughness**

[](https://github.com/Chocapikk/wpprobe#use-hybrid-mode-for-optimal-balance-of-stealth-and-thoroughness)

Scan a WordPress site using hybrid mode (stealthy first, then brute-force for remaining plugins):

```shell
wpprobe scan -u https://example.com --mode hybrid
```

### **Provide a custom plugin list for brute-force scanning**

[](https://github.com/Chocapikk/wpprobe#provide-a-custom-plugin-list-for-brute-force-scanning)

Use a custom list of plugins for brute-force or hybrid scanning:

```shell
wpprobe scan -u https://example.com --mode bruteforce --plugin-list my-plugins.txt
```

### **Scan multiple targets from a file with 20 concurrent threads**

[](https://github.com/Chocapikk/wpprobe#scan-multiple-targets-from-a-file-with-20-concurrent-threads)

Scan multiple sites from a `targets.txt` file using 20 threads:

```shell
wpprobe scan -f targets.txt -t 20
```

### **Save results to a CSV file**

[](https://github.com/Chocapikk/wpprobe#save-results-to-a-csv-file)

Save scan results to a CSV file:

```shell
wpprobe scan -f targets.txt -t 20 -o results.csv
```

### **Save results to a JSON File**

[](https://github.com/Chocapikk/wpprobe#save-results-to-a-json-file)

Save scan results to a JSON file:

```shell
wpprobe scan -f targets.txt -t 20 -o results.json
```

### Use a custom HTTP/HTTPS proxy

[](https://github.com/Chocapikk/wpprobe#use-a-custom-httphttps-proxy)

Route all requests through a specific proxy using `--proxy` argument. If `--proxy` is not specified, `WPProbe` will automatically check for the following environment variables (in priority order):

- `HTTPS_PROXY` / `https_proxy`
- `HTTP_PROXY` / `http_proxy`
- `ALL_PROXY` / `all_proxy`

Will also respect `NO_PROXY` / `no_proxy` for bypass rules.