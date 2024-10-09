import requests
import argparse
import concurrent.futures
import os

def is_wordpress_site(url):
    try:
        print(f"Checking: {url}")  # Debugging output
        response = requests.get(url, timeout=5)  # Let requests handle SSL verification
        if 'wp-content' in response.text or 'wp-includes' in response.text:
            return url, True
    except requests.ConnectionError:
        print(f"Connection error accessing {url}. It might be down or inaccessible.")
    except requests.Timeout:
        print(f"Timeout error accessing {url}. The request took too long.")
    except requests.SSLError:
        print(f"SSL error accessing {url}. This domain may not support HTTPS.")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")  # General request error
    return url, False

def grep_wordpress_domains(domain_list):
    wordpress_domains = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_domain = {executor.submit(is_wordpress_site, domain): domain for domain in domain_list}
        for future in concurrent.futures.as_completed(future_to_domain):
            domain, is_wp = future.result()
            if is_wp:
                wordpress_domains.append(domain)

    return wordpress_domains

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Check for WordPress domains.")
    parser.add_argument('-l', '--list', required=True, help='Filename containing list of domains to check')
    parser.add_argument('-o', '--output', help='Output file to save WordPress domains')
    
    args = parser.parse_args()
    
    # Read domains from the specified file
    if not os.path.exists(args.list):
        print(f"Error: The file '{args.list}' does not exist.")
        return

    with open(args.list, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]

    # Normalize domains
    normalized_domains = []
    for domain in domains:
        if not domain.startswith(('http://', 'https://')):
            domain = 'https://' + domain
        elif domain.startswith('http://'):
            domain = domain.replace('http://', 'https://')
        normalized_domains.append(domain)

    wordpress_domains = grep_wordpress_domains(normalized_domains)

    print("\nWordPress Domains:")
    for domain in wordpress_domains:
        print(domain)

    # Save results to output file if specified
    if args.output:
        with open(args.output, 'w') as outfile:
            for domain in wordpress_domains:
                outfile.write(domain + '\n')
        print(f"\nResults saved to '{args.output}'.")

if __name__ == "__main__":
    main()
