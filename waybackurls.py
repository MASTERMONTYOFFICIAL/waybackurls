import requests
import argparse

def parse_urls(domain,output):
    url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=text&fl=original&collapse=urlkey"
    res = requests.get(url)
    if res.status_code == 200 and res.text.strip():
        for line in res.text.splitlines():
            print(line)
            results(line,output)
    else:
        print(f"No results found for {domain}")

def results(urls,output):
    with open(output,'a') as f:
        f.write(urls + "\n")

def main():
    try:
        parser = argparse.ArgumentParser(
            prog="Waybackurls updated by zeropwned\nGithub : https://github.com/MASTERMONTYOFFICIAL",
            description="Finding hidden urls via webarchieve"
            )
        parser.add_argument("-d","--domain",help="Pass domain to get wayback urls.")
        parser.add_argument("-dL","--domain_list",help="List of domains to parse wayback urls.")
        parser.add_argument("-o","--output",help="Path to save output result.")
        args = parser.parse_args()
        
        if not args.domain and not args.domain_list:
            parser.print_help()
            return
        
        if not args.output:
            args.output = "results.txt"
        
        if args.domain:
            parse_urls(args.domain,args.output)
        
        if args.domain_list:
            with open(args.domain_list,'r') as domains:
                for domain in domains:
                    parse_urls(domain,args.output)
    except KeyboardInterrupt:
        print("\nExitted by user :)")


if __name__ == '__main__':
    main()